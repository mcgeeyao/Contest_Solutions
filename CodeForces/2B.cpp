#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <assert.h>
#define INT_MAX 2147483647
#define ll long
using namespace std;

// unordered_map<int,int> arr2;
// unordered_map<int,int> arr5;

// int log(int i,int k){
//     if(i==0){return INT_MIN;}
//     if(k==2 and arr2.find(i)!=arr2.end())return arr2[i];
//     if(k==5 and arr5.find(i)!=arr5.end())return arr5[i];
//     if(i%k)return 0;
//     int res=log(i/k,k)+1;
//     if(k==2)arr2[i]=res;
//     if(k==5)arr5[i]=res;
//     return res;
// }

ll log(ll i,int k){
    if(i==0){return INT_MAX/2;}
    ll res=0;
    while (i%k==0){
        i=i/k;
        res+=1;
    }    
    return res;
}

int main(){
    int n;
    ll tmp;
    cin>>n;

    vector<vector<ll>> 
    grid(n,vector<ll> (n,0)),
    dp2(n,vector<ll> (n,0)),
    dp5(n,vector<ll> (n,0));

    vector<vector<int>>
    T2(n,vector<int> (n,-1)),
    T5(n,vector<int> (n,-1));

    bool check=false;
    int x0,y0;

    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cin>>tmp;
            grid[i][j]=tmp;
            if(tmp==0){
                check=true;
                x0=i;
                y0=j;
            }
        }
    }
    dp2[0][0]=log(grid[0][0],2);
    dp5[0][0]=log(grid[0][0],5);

    for(int i=1;i<n;i++){
        dp2[i][0]=dp2[i-1][0]+log(grid[i][0],2);
        dp5[i][0]=dp5[i-1][0]+log(grid[i][0],5);
        T5[i][0]=1;
        T2[i][0]=1;
    }
    for(int j=1;j<n;j++){
        dp2[0][j]=dp2[0][j-1]+log(grid[0][j],2);
        dp5[0][j]=dp5[0][j-1]+log(grid[0][j],5);
        T5[0][j]=0;
        T2[0][j]=0;
    }

    for(int i=1;i<n;i++){
        for(int j=1;j<n;j++){
            dp2[i][j]=min(dp2[i-1][j],dp2[i][j-1])+log(grid[i][j],2);
            if (dp2[i-1][j]<dp2[i][j-1])T2[i][j]=1;
            else T2[i][j]=0;
                    
            dp5[i][j]=min(dp5[i-1][j],dp5[i][j-1])+log(grid[i][j],5);
            if (dp5[i-1][j]<dp5[i][j-1])T5[i][j]=1;
            else T5[i][j]=0;
        }
    }
    assert(dp5[n-1][n-1]>=0 and dp2[n-1][n-1]>=0);
    if (dp5[n-1][n-1]<dp2[n-1][n-1]){
        if(check and dp5[n-1][n-1]>1){
            cout<<1<<endl;
            string res0;
            for(int i=0;i<x0;i++){
                res0+="D";
            }
            for(int i=0;i<y0;i++){
                res0+="R";
            }
            for(int i=x0;i<n-1;i++){
                res0+="D";
            }
            for(int i=y0;i<n-1;i++){
                res0+="R";
            }
            cout<<res0<<endl;
        }
        else{
            string res;
            int x=n-1;
            int y=n-1;
            while (T5[x][y]!=-1){
                if (T5[x][y]==0){
                    res+="R";
                    y-=1;
                }
                else{
                    res+="D";
                    x-=1;
                }
            }
            cout<<dp5[n-1][n-1]<<endl;
            reverse(res.begin(),res.end());
            cout<<res<<endl;
        }
    }else{
        if(check and dp2[n-1][n-1]>1){
            cout<<1<<endl;
            string res0;
            for(int i=0;i<x0;i++){
                res0+="D";
            }
            for(int i=0;i<y0;i++){
                res0+="R";
            }
            for(int i=x0;i<n-1;i++){
                res0+="D";
            }
            for(int i=y0;i<n-1;i++){
                res0+="R";
            }
            cout<<res0<<endl;
        }
        else{
            string res;
            int x=n-1;
            int y=n-1;
            while (T2[x][y]!=-1){
                if (T2[x][y]==0){
                    res+="R";
                    y-=1;
                }
                else{
                    res+="D";
                    x-=1;
                }
            }
            cout<<dp2[n-1][n-1]<<endl;
            reverse(res.begin(),res.end());
            cout<<res<<endl;
        }
    }
}

