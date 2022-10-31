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

```bash
catkin_make --cmake-args \
            -DCMAKE_BUILD_TYPE=Release \
            -DPYTHON_EXECUTABLE=/usr/bin/python3 \
            -DPYTHON_INCLUDE_DIR=/usr/include/python3.6m \
            -DPYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython3.6m.so
```