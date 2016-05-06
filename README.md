# sar\_robot\_command\_sender

SAR robot command sender is a ROS package that allows you to enter generic
robot commands to send to a specific SAR robot, via the robot translation
node.

## Usage

robot\_command\_sender.py \[-h\] \[-d \[DO\]\] \[-s \{sleep,s,wakeup,w\}\] 

Sends a message to a SAR robot. Must have roscore running for message to be sent.

Optional arguments:

- -h, --help  
    - show this help message and exit

- -d \[DO\], --do \[DO\]  
    - tell robot to speak and/or do actions or behaviors, specified in the "DO" argument

- -s \{sleep,s,wakeup,w\}, --sleep \{sleep,s,wakeup,w\}  
    - tell robot to sleep or to wake up

## Details about arguments

### DO

The "DO" command tells a robot to speak and/or perform the specified actions or
behaviors. The exact format of this command's argument is yet to be determined,
but may be a string of the format:

`"Hi <smile> I am a robot! <wave>"`

where the string contains text that the robot should say, with embedded
actions that the robot should do. We could add additional optional flags,
such as whether the action should be blocking or non-blocking, or where to
direct the behavior, next to each action, e.g.:

`"Hi <smile,nb,at-person> I am a robot! <wave,b>"`

These arguments would not have to contain both speech and actions, e.g.:

`"Hi I am a robot!"`

or

`"<smile>"`

