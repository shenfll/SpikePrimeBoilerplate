from math import *
import hub
import uos
import utime

#mission 2/3

#ports object
ports = {
    "A": hub.port.A,
    "B": hub.port.B,
    "C": hub.port.C,
    "D": hub.port.D,
    "E": hub.port.E,
    "F": hub.port.F,
    "a": hub.port.A,
    "b": hub.port.B,
    "c": hub.port.C,
    "d": hub.port.D,
    "e": hub.port.E,
    "f": hub.port.F
}

#define running
running = False

#set drive motors
drive = ports["D"].motor.pair(ports["E"].motor)

#set attachment motors
attachment = ports["A"].motor.pair(ports["C"].motor)

#move tank function
#mt(distance in degrees,left motor speed,right motor speed)
def mt(amount,ls,rs,wait = True):
    drive.run_for_degrees(round(amount),speed_0=round(-ls),speed_1=round(rs))
    global running
    running = True
    def event(details):
        if details == drive.primary().EVENT_COMPLETED:
            global running
            running = False
    drive.callback(event)
    while running and wait:
        pass

#start tank function
#st(left motor speed,right motor speed)
def st(ls,rs):
    drive.run_at_speed(round(-ls),round(rs))

#stop tank function
def pt():
    drive.brake()

#reset drive function
def rt():
    drive.preset(0,0)

#reset attachments function
def ra():
    attachment.preset(0,0)

#move attachment function
#ma(port letter of motor,distance in degrees,motor speed)
def ma(ml,amount,ms,wait = True):
    ports[ml].motor.run_for_degrees(round(amount),speed=round(ms))
    if wait:
        mwt(ml)

#start attachment function
#sa(port letter of motor,motor speed)
def sa(ml,ms):
    ports[ml].motor.run_at_speed(round(ms))
    mwt(ml)

#pause attachment function
def pa(ml):
    ports[ml].motor.brake()

#move attachments sync function
#mas(distance in degrees,left motor speed,right motor speed)
def mas(amount,ls,rs,wait = True):
    attachment.run_for_degrees(round(amount),speed_0=round(ls),speed_1=round(rs))
    global running
    running = True
    def event(details):
        if details == attachment.primary().EVENT_COMPLETED:
            global running
            running = False
    attachment.callback(event)
    while running and wait:
        pass

#get distance
def gd():
    return round((abs(drive.primary().get()[1]) + abs(drive.secondary().get()[1])) / 2)

#get reflected light function
#rl(port letter of light sensor)
def rl(ll):
    return ports[ll].device.get()

#wait function
#wt(time in milliseconds)
def wt(ms):
    utime.sleep_ms(ms)

#motor wait function (internal plz don't touch)
def mwt(ml):
    while ports[ml].motor.busy(ports[ml].motor.BUSY_MOTOR):
        pass

#get gyro angle function
def ga():
    return hub.motion.yaw_pitch_roll()[0]

#reset gyro function (plz don't call with arguments, all arguments are internal)
def rg(ang = 0, yc = 0):
    hub.motion.yaw_pitch_roll(ang,yc)

#calibrate gyro function
def cg():
    rg()
    mt(250,25,25)
    mt(2560,-25,25)
    mt(500,-25,-25)
    rg(yc = ga() / 5)

#line follow function
#lf(port letter of light sensor,distance in degrees,speed,acceleration/gain,side of line)
def lf(ln,amount,ts,ac,side):
    rt()
    while gd() < amount:
        if side == 0:
            st((rl(ln)-35)*ac+ts,(100-rl(ln))*ac+ts)
        else:
            st((100-rl(ln))*ac+ts,(rl(ln)-35)*ac+ts)
    pt()

#gyro follow function
#gf(distance in degrees,speed,acceleration/gain,heading in degrees,direction forward (1) or backward (0))
def gf(amount,ts,ac,ang,dn):
    rt()
    while gd() < amount:
        left = 180-(ga()-ang)*10
        right = (ga()-ang)*10+180
        left += (left-right)/2
        right += (left-right)/2
        if dn == 1:
            st(left*ac+ts,right*ac+ts)
        else:
            st(right*-ac-ts,left*-ac-ts)
    pt()

#gyro turn function
#gt(angle to turn to)
def gt(ang):
    rt()
    for i in range(5):
        while not(ga()<ang+(10-i) and ga()>ang-(10-i)):
            if ang-ga()>0:
                st((ang-ga()+70)/3,(ga()-ang-70)/3)
            else:
                st((ang-ga()-70)/3,(ga()-ang+70)/3)
    pt()

#play sound function
#sound(index of sound file in the sounds folder)
def sound(sn):
    hub.sound.play("/sounds/"+uos.listdir("/sounds")[sn])

#set hub led color function
#led(integer that corresponds to some color)
def led(n):
    hub.led(n)

#exit function
def exit():
    raise SystemExit

#get temperature function
def temp():
    return hub.temperature()*9/5+32

#main function
def main():
    #write ur code here

#run everything
main()