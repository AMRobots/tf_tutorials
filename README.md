# 1. tf broadcaster
http://wiki.ros.org/tf/Tutorials/Writing%20a%20tf%20broadcaster%20%28Python%29
## 1.1. Using
```
$ roslaunch tf_tutorials start_demo_turtle_tf_broadcaster.launch
```
## 1.2. Testing
```
$ rosrun tf tf_echo /world /turtle1
```

# 2. tf listener
http://wiki.ros.org/tf/Tutorials/Writing%20a%20tf%20listener%20%28Python%29
## 2.1. Using
```
$ roslaunch tf_tutorials start_demo_turtle_tf_listener.launch
```
## 2.2. Testing
```
$ rosrun tf tf_echo /turtle1 /turtle2
```
