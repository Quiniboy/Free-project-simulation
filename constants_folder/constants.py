import numpy as np
from fractions import Fraction

#constants
GRAVITATIONAL_VELOCITY = Fraction(981, 100)       #[m/s^2]
LENGHT = 2.0                       #[m]
MASS = Fraction(3, 2)                          #[kg]
RADIUS_CILINDER = 1                 #[m]
RADIUS_HOLE =  Fraction(1, 2)                 #[m]
OFFSET_2 = Fraction(1,3)                     #[m]


#np array can have as many angles as you want
#it has to be in radians to work
ANGLE_SLOPE = np.array([np.deg2rad(20), np.deg2rad(30), np.deg2rad(40), np.deg2rad(50), np.deg2rad(60)])


#variables
t0 = 0                  #initial time [s]
v0 = 0                  #initial velocity [m/s]
x0 = 0                  #initial position [m]
phi0 = np.pi            #initial angle [rad]
omega0 = 0              #initial angular velocity = [rad/s]
v_cm0 = 0               #initial velocity of the center of mass [m/s]
dt = Fraction(1, 1000)               #time increments [s]
end_time = 1000           #time the ball rolls [s]





