// Copyright 2021 Optiver Asia Pacific Pty. Ltd.
//
// This file is part of Ready Trader Go.
//
//     Ready Trader Go is free software: you can redistribute it and/or
//     modify it under the terms of the GNU Affero General Public License
//     as published by the Free Software Foundation, either version 3 of
//     the License, or (at your option) any later version.
//
//     Ready Trader Go is distributed in the hope that it will be useful,
//     but WITHOUT ANY WARRANTY; without even the implied warranty of
//     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//     GNU Affero General Public License for more details.
//
//     You should have received a copy of the GNU Affero General Public
//     License along with Ready Trader Go.  If not, see
//     <https://www.gnu.org/licenses/>.
#include <array>
#include <iostream>
#include <algorithm>

#include <boost/asio/io_context.hpp>

#include <ready_trader_go/logging.h>

#include "autotrader.h"

using namespace ReadyTraderGo;

RTG_INLINE_GLOBAL_LOGGER_WITH_CHANNEL(LG_AT, "AUTO")

constexpr int LOT_SIZE = 30;
constexpr int POSITION_LIMIT = 100;
constexpr int TICK_SIZE_IN_CENTS = 100;
constexpr int MIN_BID_NEAREST_TICK = (MINIMUM_BID + TICK_SIZE_IN_CENTS) / TICK_SIZE_IN_CENTS * TICK_SIZE_IN_CENTS;
constexpr int MAX_ASK_NEAREST_TICK = MAXIMUM_ASK / TICK_SIZE_IN_CENTS * TICK_SIZE_IN_CENTS;
constexpr float EPSILON = 0.002;
constexpr int EPSILON1 = 0;
constexpr int lot_l = 20, lot_r = 50;
constexpr float ep_l = EPSILON, ep_r = 0.005;


AutoTrader::AutoTrader(boost::asio::io_context& context) : BaseAutoTrader(context)
{
}

void AutoTrader::DisconnectHandler()
{
    BaseAutoTrader::DisconnectHandler();
    // RLOG(LG_AT, LogLevel::LL_INFO) << "execution connection lost";
}

void AutoTrader::ErrorMessageHandler(unsigned long clientOrderId,
                                     const std::string& errorMessage)
{
    // RLOG(LG_AT, LogLevel::LL_INFO) << "error with order " << clientOrderId << ": " << errorMessage;
    if (clientOrderId != 0 && ((mAsks.count(clientOrderId) == 1) || (mBids.count(clientOrderId) == 1)))
    {
        OrderStatusMessageHandler(clientOrderId, 0, 0, 0);
    }
}

void AutoTrader::HedgeFilledMessageHandler(unsigned long clientOrderId,
                                           unsigned long price,
                                           unsigned long volume)
{
    // RLOG(LG_AT, LogLevel::LL_INFO) << "hedge order " << clientOrderId << " filled for " << volume
    //                                << " lots at $" << price << " average price in cents";
}

void AutoTrader::OrderBookMessageHandler(Instrument instrument,
                                         unsigned long sequenceNumber,
                                         const std::array<unsigned long, TOP_LEVEL_COUNT>& askPrices,
                                         const std::array<unsigned long, TOP_LEVEL_COUNT>& askVolumes,
                                         const std::array<unsigned long, TOP_LEVEL_COUNT>& bidPrices,
                                         const std::array<unsigned long, TOP_LEVEL_COUNT>& bidVolumes)
{
    // RLOG(LG_AT, LogLevel::LL_INFO) << "order book received for " << instrument << " instrument";
                                //    << ": ask prices: " << askPrices.front();
                                //    << "; ask volumes: " << askVolumes.at(0)
                                //    << "; bid prices: " << bidPrices.at(0)
                                //    << "; bid volumes: " << bidVolumes.at(0);
    if ((bidPrices[0] + askPrices[0]) == 0) return;
    if (instrument == Instrument::FUTURE)
    {
        preFuture = (bidPrices[0] + askPrices[0]) >> 1;
    }
    if (instrument == Instrument::ETF)
    {
        long newBidPrice = 0;
        long newAskPrice = 0;
        float ask_ep = ((float)-((long)askPrices[0] - preFuture)) / (float)preFuture;
        float bid_ep = ((float)((long)bidPrices[0] - preFuture)) / (float)preFuture;
        long ask_lot = 0;
        long bid_lot = 0;
        if (ask_ep >= EPSILON) 
        {
            newBidPrice = askPrices[0] + (int)((ask_ep - EPSILON) * (float)1000) * TICK_SIZE_IN_CENTS;
            bid_lot = (int)((std::min(ep_r, ask_ep) - ep_l) / (ep_r - ep_l) * (float)(lot_r - lot_l));
            bid_lot += lot_l;
        }
        else if (bid_ep >= EPSILON)
        {
            newAskPrice = bidPrices[0] - (int)((bid_ep - EPSILON) * (float)1000) * TICK_SIZE_IN_CENTS;
            ask_lot = (int)((std::min(ep_r, bid_ep) - ep_l) / (ep_r - ep_l) * (float)(lot_r - lot_l));
            ask_lot += lot_l;
        }
        else
        {
            if (bidPrices[0] != 0) {
                newBidPrice = (preFuture / TICK_SIZE_IN_CENTS) * TICK_SIZE_IN_CENTS - 2 * TICK_SIZE_IN_CENTS;
                newBidPrice = std::min(newBidPrice, (long)((float)(2 * newBidPrice + (bidPrices[0] + TICK_SIZE_IN_CENTS)) / 3.0) / TICK_SIZE_IN_CENTS * TICK_SIZE_IN_CENTS);
                bid_lot = LOT_SIZE - mPosition / 5;
            }
            if (askPrices[0] != 0) {
                newAskPrice =  (preFuture / TICK_SIZE_IN_CENTS) * TICK_SIZE_IN_CENTS + 2 * TICK_SIZE_IN_CENTS;
                newAskPrice = std::max(newAskPrice, (long)((float)(2 * newAskPrice + (askPrices[0] - TICK_SIZE_IN_CENTS)) / 3.0 + TICK_SIZE_IN_CENTS) / TICK_SIZE_IN_CENTS * TICK_SIZE_IN_CENTS);
                ask_lot = LOT_SIZE + mPosition / 5;
            }
            // newBidPrice = (bidPrices[0] != 0) ? (preFuture / TICK_SIZE_IN_CENTS) * TICK_SIZE_IN_CENTS - 2 * TICK_SIZE_IN_CENTS : 0;
            // newAskPrice = (askPrices[0] != 0) ? (preFuture / TICK_SIZE_IN_CENTS) * TICK_SIZE_IN_CENTS + 2 * TICK_SIZE_IN_CENTS : 0;
            // bid_lot = LOT_SIZE - mPosition / 5;
            // ask_lot = LOT_SIZE + mPosition / 5;
        }

        bid_lot = std::min(bid_lot, POSITION_LIMIT - bidding_vol - mPosition);
        ask_lot = std::min(ask_lot, POSITION_LIMIT - asking_vol + mPosition);

        if (mAskId != 0 && newAskPrice != 0 && newAskPrice != mAskPrice || newBidPrice == mAskPrice)
        {
            SendCancelOrder(mAskId);
            mAskId = 0;
        }
        if (mBidId != 0 && newBidPrice != 0 && newBidPrice != mBidPrice || newAskPrice == mBidPrice)
        {
            SendCancelOrder(mBidId);
            mBidId = 0;
        }

        if (mAskId == 0 && newAskPrice != 0 && ask_lot > 0)
        {
            mAskId = mNextMessageId++;
            mAskPrice = newAskPrice;
            SendInsertOrder(mAskId, Side::SELL, newAskPrice, ask_lot, Lifespan::GOOD_FOR_DAY);
            mAsks.insert(mAskId);
            asking_vol = ask_lot;
        }
        if (mBidId == 0 && newBidPrice != 0 && bid_lot > 0)
        {
            mBidId = mNextMessageId++;
            mBidPrice = newBidPrice;
            SendInsertOrder(mBidId, Side::BUY, newBidPrice, bid_lot, Lifespan::GOOD_FOR_DAY);
            mBids.insert(mBidId);
            bidding_vol = bid_lot;
        }
    }
}

void AutoTrader::OrderFilledMessageHandler(unsigned long clientOrderId,
                                           unsigned long price,
                                           unsigned long volume)
{
    // RLOG(LG_AT, LogLevel::LL_INFO) << "order " << clientOrderId << " filled for " << volume
    //                                << " lots at $" << price << " cents";
    if (mAsks.find(clientOrderId) != mAsks.end())
    {
        mPosition -= (long)volume;
        SendHedgeOrder(mNextMessageId++, Side::BUY, MAX_ASK_NEAREST_TICK, volume);
    }
    else if (mBids.find(clientOrderId) != mBids.end())
    {
        mPosition += (long)volume;
        SendHedgeOrder(mNextMessageId++, Side::SELL, MIN_BID_NEAREST_TICK, volume);
    }
}

void AutoTrader::OrderStatusMessageHandler(unsigned long clientOrderId,
                                           unsigned long fillVolume,
                                           unsigned long remainingVolume,
                                           signed long fees)
{

    if (clientOrderId == mAskId)
    {
        asking_vol = remainingVolume;
    }
    else if (clientOrderId == mBidId)
    {
        bidding_vol = remainingVolume;
    }
    if (remainingVolume == 0)
    {
        if (clientOrderId == mAskId)
        {
            mAskId = 0;
        }
        else if (clientOrderId == mBidId)
        {
            mBidId = 0;
        }

        mAsks.erase(clientOrderId);
        mBids.erase(clientOrderId);
    }
}

void AutoTrader::TradeTicksMessageHandler(Instrument instrument,
                                          unsigned long sequenceNumber,
                                          const std::array<unsigned long, TOP_LEVEL_COUNT>& askPrices,
                                          const std::array<unsigned long, TOP_LEVEL_COUNT>& askVolumes,
                                          const std::array<unsigned long, TOP_LEVEL_COUNT>& bidPrices,
                                          const std::array<unsigned long, TOP_LEVEL_COUNT>& bidVolumes)
{
    // RLOG(LG_AT, LogLevel::LL_INFO) << "trade ticks received for " << instrument << " instrument"
    //                                << ": ask prices: " << askPrices[0]
    //                                << "; ask volumes: " << askVolumes[0]
    //                                << "; bid prices: " << bidPrices[0]
    //                                << "; bid volumes: " << bidVolumes[0];
}
