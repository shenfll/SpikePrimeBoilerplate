# SpikePrimeBoilerplate
A collection of a few useful functions and tools for FLL teams using the Spike Prime created by FLL team #3249 with the help of FRC team #20 member Gabe West.
  
# Index
  - [Tank Movement](#tank-movement)
  - [Attachment Movement](#attachments)
  - [Line Following](#line-following)
  - [Gyro Sensor](#gyro-sensor)
  
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
>wait => Run motor asynchronously?  

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

Resets the drive direction to 0  


## Attachments

### Reset Attachments 

```python
ra()
```

### Move Attachment

```python
ma(ml,amount,ms,wait = True)
```

Starts the drive base motors at a given left motor speed and right motor speed  
<b>Parameters:</b>  
>ml => Port letter of motor  
>amount => Distance in degrees  
>ms => Motor speed
>wait => Run attachment motor asynchronously?  

Moves a specific attachment motor a given amound

## Line Following

## Gyro Sensor
