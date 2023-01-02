#include <Eigen/Eigen>
#include <ros/ros.h>
#include <ros/package.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include "boost/date_time/posix_time/posix_time.hpp"
#include "boost/date_time/local_time_adjustor.hpp"
#include "boost/date_time/c_local_time_adjustor.hpp"


int main(int argc, char **argv)
{
  ros::init(argc, argv, "csv_log");
  ros::NodeHandle nh("~");

  std::string scenario;

  nh.param<std::string>("scenario", scenario, "none");

  std::string package_path = ros::package::getPath("ego_planner");
  std::string file_name = package_path + "/log/summary_" + scenario + ".csv";
  // std::ifstream result_csv_in(file_name);
  std::ofstream result_csv_out;
  result_csv_out.open(file_name, std::ios_base::app);
  boost::posix_time::ptime my_posix_time = ros::Time::now().toBoost();
  boost::posix_time::ptime local_time = boost::date_time::c_local_adjustor<boost::posix_time::ptime>::utc_to_local (my_posix_time);
//   typedef boost::date_time::local_adjustor<my_posix_time, +8, us_dst> us_eastern;
  std::string iso_time_str = boost::posix_time::to_iso_extended_string(local_time);
  result_csv_out << iso_time_str <<"\ndrone_id,min_planning_time,max_planning_time, avg_planning_time,average_init_time,average_opt_time, mission_time, distance, max_vel\n";;
  result_csv_out.close();

//   srand(floor(ros::Time::now().toSec() * 10));

//   ros::Subscriber selected_drones_sub = nh.subscribe<geometry_msgs::PoseStamped>("/rviz_selected_drones", 100, selected_drones_cb);
//   ros::Subscriber user_goal_sub = nh.subscribe<geometry_msgs::PoseStamped>("/goal", 10, user_goal_cb);

//   goals_pub_ = nh.advertise<quadrotor_msgs::GoalSet>("/goal_user2brig", 10);
//   new_goals_arrow_pub_ = nh.advertise<visualization_msgs::MarkerArray>("/new_goals_arrow", 10);

  ROS_INFO("logging csv started");
  while (ros::ok())
  {

    ros::Duration(0.1).sleep();
    ros::spinOnce();
  }

  return 0;
}
