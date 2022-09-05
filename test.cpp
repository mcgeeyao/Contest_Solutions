
#include <cstdlib>
#include <ctime>
#include <stdio.h>
#include <unistd.h>
#include <sys/time.h>
#include <iostream>
#include <pthread.h>




#define BUF_SIZE 128

struct gps_info
{
   char utc_time[BUF_SIZE];
   char status;
   float latitude_value;
   char latitude;
   float longtitude_value;
   char longtitude;
   float speed;
   float azimuth_angle;
   char utc_data[BUF_SIZE];
} rmc_info;


void subscription_handler(std::string const & payload)
{  
//    gps_info rmc_info = {"asdf", '1', 1, '1', 1, '1', 1, 1,'1'};
   std::cout << payload << std::endl;
   int check = sscanf(payload.c_str(), "$GPRMC,%[^,],%c,%f,%c,%f,%c,%f,%f,%[^,]",
      rmc_info.utc_time,\
      &(rmc_info.status),\
      &(rmc_info.latitude_value),\
      &(rmc_info.latitude),\
      &(rmc_info.longtitude_value),\
      &(rmc_info.longtitude),
      &(rmc_info.speed),\
      &(rmc_info.azimuth_angle),\
      rmc_info.utc_data);
   if (check == 9) 
   {   
        printf("yes, %d\n", check);
        printf("GPRMC {\n");
        printf("utc_time:         %s\n", rmc_info.utc_time);
        printf("status:           %c\n", rmc_info.status);
        printf("latitude_value:   %f\n", rmc_info.latitude_value);
        printf("latitude:         %c\n", rmc_info.latitude);
        printf("longtitude_value: %f\n", rmc_info.longtitude_value);
        printf("longtitude:       %c\n", rmc_info.longtitude);
        printf("speed:            %f\n", rmc_info.speed);
        printf("azimuth_angle:    %f\n", rmc_info.azimuth_angle);
        printf("utc_data:         %s\n", rmc_info.utc_data);
        printf("}\n");
   }
   

}

int main(void) {
    std::string payload = "$GPRMC,000000.00,v,0, , , , , ,010712,,,N*79";
    std::string payload2 = "$GPRMC,000000.00,A,1,1,1,1,1,1,010712,,,N*79";
    subscription_handler(payload2);
    std::cout << payload << std::endl;
    int check = sscanf(payload.c_str(), "$GPRMC,%[^,],%c,%f,%c,%f,%c,%f,%f,%[^,]",
        rmc_info.utc_time,\
        &(rmc_info.status),\
        &(rmc_info.latitude_value),\
        &(rmc_info.latitude),\
        &(rmc_info.longtitude_value),\
        &(rmc_info.longtitude),
        &(rmc_info.speed),\
        &(rmc_info.azimuth_angle),\
        rmc_info.utc_data);
    if (0 < check) 
    {    
            printf("alal");
            printf("yes, %d\n", check);
            printf("GPRMC {\n");
            printf("utc_time:         %s\n", rmc_info.utc_time);
            printf("status:           %c\n", rmc_info.status);
            printf("latitude_value:   %f\n", rmc_info.latitude_value);
            printf("latitude:         %c\n", rmc_info.latitude);
            printf("longtitude_value: %f\n", rmc_info.longtitude_value);
            // printf("longtitude:       %c\n", rmc_info.longtitude);
            // printf("speed:            %f\n", rmc_info.speed);
            // printf("azimuth_angle:    %f\n", rmc_info.azimuth_angle);
            // printf("utc_data:         %s\n", rmc_info.utc_data);
            // printf("}");
            // printf("what");
    }
    check = sscanf(payload2.c_str(), "$GPRMC,%[^,],%c,%f,%c,%f,%c,%f,%f,%[^,]",
        rmc_info.utc_time,\
        &(rmc_info.status),\
        &(rmc_info.latitude_value),\
        &(rmc_info.latitude),\
        &(rmc_info.longtitude_value),\
        &(rmc_info.longtitude),
        &(rmc_info.speed),\
        &(rmc_info.azimuth_angle),\
        rmc_info.utc_data);
    if (0 < check) 
    {    
            printf("alal");
            printf("yes, %d\n", check);
            printf("GPRMC {\n");
            printf("utc_time:         %s\n", rmc_info.utc_time);
            printf("status:           %c\n", rmc_info.status);
            printf("latitude_value:   %f\n", rmc_info.latitude_value);
            printf("latitude:         %c\n", rmc_info.latitude);
            printf("longtitude_value: %f\n", rmc_info.longtitude_value);
            printf("longtitude:       %c\n", rmc_info.longtitude);
            printf("speed:            %f\n", rmc_info.speed);
            printf("azimuth_angle:    %f\n", rmc_info.azimuth_angle);
            printf("utc_data:         %s\n", rmc_info.utc_data);
            printf("}");
    }

    std::cout << "alex391q" << std::endl;





    return 0;
}