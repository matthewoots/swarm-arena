import sys
import numpy as np
import os
import math

fname = "opp_side_swap.launch"
def main(argv):
	num = int(argv[1])
	scenario = str(num) + "agent_opposite_side_swap"
	str_begin = "<launch>\n\
	<arg name=\"map_size_x\" value=\"40.0\"/>\n\
	<arg name=\"map_size_y\" value=\"40.0\"/>\n\
    <arg name=\"map_size_z\" value=\" 4.0\"/>\n\
    <arg name=\"odom_topic\" value=\"visual_slam/odom\" />\n\
	<arg name=\"scenario\" value=\"{scenario_}\"/>\n\n\
		\n\
    <!-- swarm topic transmitter bridge-->\n\
    <include file=\"$(find swarm_bridge)/launch/bridge_udp.launch\">\n\
        <arg name=\"drone_id\" value=\"999\"/>\n\
        <arg name=\"broadcast_ip\" value=\"127.0.0.255\"/>\n\
    </include>\n\n".format(scenario_ = scenario)
	str_end = "</launch>\n"
		
	height = 1.5
	initial_spacing = 2
	distance_from_wall = 12
	theta = np.linspace(-3.14159, 3.14159, num+1)
	r = 12
	file_name = "../" + str(num) + "agent_" + fname
	file = open(file_name, "w")
	file.write(str_begin)
	start_position = np.zeros([num,3])
	goal_position = np.zeros([num,3])
	for i in range(num):
		if (i+1)<(num+1)/2+1:
			start_position[i,:] = [distance_from_wall, i*initial_spacing - ((num+1)/2-1) * initial_spacing/2, height]
		else:
			start_position[i,:] = [-distance_from_wall, (i - (num+1)/2)*initial_spacing - ((num+1)/2-1) * initial_spacing/2, height]

	for i in range(num):
		if(i<=num/2-1):
			goal_position[i,:] = start_position[i+num/2,:]
		else:
			goal_position[i,:] = start_position[i-num/2,:]
		
	
	for i in range(num):
		str_for_agent = "    <include file=\"$(find ego_planner)/launch/include/run_in_sim.xml\">\n\
		<arg name=\"drone_id\"   value=\"{drone_id}\"/>\n\
		<arg name=\"scenario\" value=\"$(arg scenario)\"/>\n\
		<arg name=\"init_x\"     value=\"{init_x}\"/>\n\
		<arg name=\"init_y\"     value=\"{init_y}\"/>\n\
		<arg name=\"init_z\"     value=\"{init_z}\"/>\n\
		<arg name=\"target0_x\"   value=\"{target0_x}\"/>\n\
		<arg name=\"target0_y\"   value=\"{target0_y}\"/>\n\
		<arg name=\"target0_z\"   value=\"{target0_z}\"/>\n\
		<arg name=\"map_size_x\" value=\"$(arg map_size_x)\"/>\n\
		<arg name=\"map_size_y\" value=\"$(arg map_size_y)\"/>\n\
		<arg name=\"map_size_z\" value=\"$(arg map_size_z)\"/>\n\
		<arg name=\"odom_topic\" value=\"$(arg odom_topic)\"/>\n\
	</include>\n\n".format(drone_id=i, init_x=start_position[i,0], init_y=start_position[i,1], init_z=start_position[i,2], \
		target0_x=goal_position[i,0], target0_y=goal_position[i,1], target0_z=goal_position[i,2]) 
			#print("({x},{y},{z})".format(init_x, init_y, init_z))
		file.write(str_for_agent)

	file.write(str_end)
	file.close()

if __name__ == '__main__':
	main(sys.argv)
