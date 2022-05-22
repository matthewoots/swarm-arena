# SWARM-ARENA

Forked from `swarm-playground` from ZJU-FAST lab, to test path planning algorithms

## Setup
**Step 1** Setup workspace
```bash
# cd to <your_ws>/src
git clone https://github.com/matthewoots/swarm-arena
catkin build quadrotor_msgs # at <your_ws>
catkin build
```
**Step 2** 
In a terminal
```bash
roscore
```
In another terminal
```bash
source devel/setup.bash
cd src/swarm-arena
sh run.sh
```

## References 
1. Swarm-playground https://github.com/ZJU-FAST-Lab/EGO-Planner-v2
