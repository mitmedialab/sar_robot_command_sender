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

- -i \[ID\], --id \[ID\]
    - provide a ID string to send alongside the command

## Details about arguments

### DO

The "DO" command tells a robot to speak and/or perform the specified actions or
behaviors, using a string of the format:

`"Hi <smile> I am a robot! <wave>"`

The string contains text the robot should say, with embedded actions the robot
should do.

Some additional optional flags, such as whether the action should be blocking
or non-blocking, or where to direct the behavior, may be provided next to each
action, e.g.: 

`"Hi <smile,nb,at-person> I am a robot! <wave,b>"`

These arguments could contain just speech or just actions, e.g.:

`"Hi I am a robot!"`

or

`"<smile>"`

For up-to-date information about the format of DO commands, see
[sar\_robot\_command\_msgs](https://github.com/personal-robots/sar_robot_command_msgs).

### ID

Some robots require DO commands to be tagged with a unique ID string. You can
provide a string containing an ID using the -i or --id flag.

## Version and dependency notes

This program was built and tested with:

- Python 2.7.6 
- ROS Indigo
- sar\_robot\_command\_msgs 1.0.0
- Ubuntu 14.04 LTS (64-bit)

## Bugs and issues

Please report all bugs and issues on the [sar\_robot\_command\_sender github
issues
page](https://github.com/personal-robots/sar_robot_command_sender/issues).


