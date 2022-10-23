
# Spike Prime Boilerplate
A collection of a few useful functions and tools for FLL teams using the Spike Prime created by FLL team #3249 with the help of FRC team #20 member Gabe West.
  
# Index
  - [Tank Movement](#tank-movement)
  - [Attachment Movement](#attachments)
  - [Line Following](#line-following)
  - [Gyro Sensor](#gyro-sensor)
  - [Miscellaneous](#miscellaneous)
# Tank Movement

### Move Tank 

```python
mt(amount, ls, rs, wait = True)
```

Controls the drive base given a left motor speed and a right motor speed  
<b>Parameters:</b>  
>amount => Distance in degrees  
>ls => Left motor speed  
>rs => Right motor speed  
>wait => Wait until complete to resume flow of code?

### Start Tank 

```python
st(ls, rs)
```

Starts the drive base motors at a given left motor speed and right motor speed  
<b>Parameters:</b>  
>ls => Left motor speed  
>rs => Right motor speed  

### Stop Tank 

```python
pt()
```
Stops the drive base motors  

### Reset Tank

```python
rt()
```
Resets the drive motors to 0  

### Get Distance
```python
gd()
```
Returns the average distance traveled by the 2 drive motors  


## Attachments

### Reset Attachments 
```python
ra()
```
Resets the motor attachment to 0  


### Move Attachment
```python
ma(ml, amount, ms, wait = True)
```
Moves an attachment a given amount
<b>Parameters:</b>  
>ml => Port letter of motor  
>amount => Distance in degrees  
>ms => Motor speed
>wait => Wait until complete to resume flow of code?  

### Start Attachment
```python
ma(ml, ms)
```
Starts an attachment at a given speed  
<b>Parameters:</b>  
>ml => Port letter of motor  
>ms => Motor speed


### Pause Attachment
```python
pa(ml)
```
Breaks a given attachment motor  
<b>Parameters:</b>  
>ml => Port letter of motor  


### Move Attachments in sync
```python
mas(amount, ls, rs, wait = True)
```
Breaks a given attachment motor  
<b>Parameters:</b>  
>amount=> Distance in degrees
>ls=> Left motor speed
>rs=> Right motor speed  
>wait => Wait until complete to resume flow of code?



## Line Following

### Get Reflected Light
```python
rl(ll)
```
Returns the reflected light intensity by a given light sensor  
<b>Parameters:</b>  
>LL  => Port letter of light sensor


### Line Follow
```python
lf(ln, amount, ts, ac, side)
```
Follows a line
<b>Parameters:</b>  
>ln=> Port letter of light sensor
>amount=> Distance in degrees
>ts=> Speed
>ac=> Acceleration / Gain
>side=> Side of line to follow (0 or 1)


## Gyro Sensor

### Get Gyro Angle
```python
ga()
```
Returns the angle measured by the gyro sensor

### Reset Gyro Angle
```python
rg()
```
Resets the gyro angle

### Calibrate Gyro
```python
cg()
```
Calibrates the gyro


### Gyro Straight
```python
gf(amount, ts, ac, ang, dn)
```
Uses the gyro to go in a straight line  
<b>Parameters:</b>  
>amount=> Distance in degrees
>ts=> Speed
>ac=> Acceleration 
>ang=> Target angle
>dn=> Direction (0: backward, 1: forward)

### Gyro Turn
```python
gt(ang)
```
Uses the gyro to turn to a specific angle  
<b>Parameters:</b>  
>ang=> The angle to turn to


## Miscellaneous

### Wait Time
```python
wt(ms)
```
Waits for a given amount of milliseconds  
<b>Parameters:</b>  
>ms  => The amount of time to wait in milliseconds

### Play Sound
```python
sound(sn)
```
Plays a sound on the brick  
<b>Parameters:</b>  
>sn  => Index of sound file in the sounds folder


### Set Button LED
```python
led(n)
```
Plays a sound on the brick  
<b>Parameters:</b>  
>n=> color  
>
OFF =  0 PINK =  1 PURPLE =  2 BLUE =  3 TEAL =  4 GREEN =  5 LIME =  6 YELLOW =  7 ORANGE =  8 RED =  9 WHITE =  10 GREY =  11


### Get Temperature
```python
temp()
```
Gets the temperature of the hub

### Exit
```python
exit()
```
Stops the program
