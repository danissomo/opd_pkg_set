# Set of submodules for door opening

```bash
mkdir ~/catkin_ws 
cd ~/catkin_ws
mkdir src
catkin_make
cd ~/catkin_ws/src
git clone https://github.com/danissomo/opd_pkg_set.git
cd ~/catkin_ws/src/opd_pkg_set
git submodule update --init --recursive
cd ~/catkin_ws
catkin_make
source ~/catkin_ws/devel/setup.bash
```