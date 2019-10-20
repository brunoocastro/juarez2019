# All things off Juarez for LARC 2019

> On development folder, are all files.


> juarez_vision is a ROS Package, copy that to catkin_ws and run catkin_make

## Code Lines Configuration:

```{r, engine='bash', Config_code_lines}
sudo bash &&
sudo usermod -aG dialout juarez &&
sudo chown juarez /dev/ttyUSB0 &&
sudo chmod 777 /dev/ttyUSB0 && 
source ~/catkin_ws/devel/setup.bash &&
setserial /dev/ttyUSB0 low_latency
```

### On Framework folder, only backup files
