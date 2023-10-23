# Interface for sustech metamorphic hand
---
### support ROS1 & ROS2

### python
provide function that can control metahand directly

```
# example:
import hand
hand_ = hand.Hand() # Initialize
hand_.Run('idle') # gesture
```

### ROS1
Implemented through ROS service
```
# example:
# terminal 1:
roslaunch metahand_serial_interface hand.launch

# terminal 2:
rosservise call /metahand_serial_interface "command: data: 'idle'"
```
.srv file is determined in metahand_msgs/srv
```
std_msgs/String command
---
bool result
```