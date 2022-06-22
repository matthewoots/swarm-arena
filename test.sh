# roslaunch ego_planner rviz.launch & sleep 5;

# roslaunch ego_planner swarm.launch & sleep 5;

source ../../devel/setup.bash

i=0
# while test $i -lt 5; do

#     echo "launch code, i is $i"
#     roslaunch ego_planner rviz.launch &

#     sleep 2

#     roslaunch map_generator pcd2cloud.launch pcd_file:=longwall_with_window_y.pcd &

#     sleep 2

#     roslaunch ego_planner 40agent_narrow_passage_travel.launch &

#     sleep 80

#     rosnode kill -a

#     sleep 5

#     i=$(expr $i + 1)

# done

    roslaunch ego_planner rviz.launch &

    sleep 2

    roslaunch map_generator pcd2cloud.launch pcd_file:=longwall_with_window_y.pcd &

    sleep 2

    roslaunch ego_planner 40agent_narrow_passage_travel.launch &

    sleep 80

    rosnode kill -a

    sleep 5

wait
