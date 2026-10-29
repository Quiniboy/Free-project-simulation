import numpy as np

#constants bij data
'''
GRAVITATIONAL_VELOCITY = 9.81       #[m/s^2]
LENGHT = 2.0                      #[m]
MASS = 0.9                         #[kg]
ADDED_MASS = 0
RADIUS_CILINDER =  0.075               #[m]
RADIUS_HOLE =   0.0175               #[m]
OFFSET_2 = 0.0225                     #[m]
'''

#stress testing constants

GRAVITATIONAL_VELOCITY = 9.81       #[m/s^2]
LENGHT = 20.0                      #[m]
MASS = 20                         #[kg]
ADDED_MASS = 0
RADIUS_CILINDER =  1               #[m]
RADIUS_HOLE =   0.5               #[m]
OFFSET_2 = 0.5                   #[m]

#np array can have as many angles as you want
#it has to be in radians to work
ANGLE_SLOPE = np.array([np.deg2rad(20), np.deg2rad(30), np.deg2rad(40), np.deg2rad(50), np.deg2rad(60)])


#variables
t0 = 0                  #initial time [s]
v0 = 0                  #initial velocity [m/s]
x0 = 0                  #initial position [m]
phi0 = 0.5 * np.pi            #initial angle [rad]
omega0 = 0              #initial angular velocity = [rad/s]
v_cm0 = 0               #initial velocity of the center of mass [m/s]
dt = 1e-4               #time increments [s]
end_time = 15           #time the ball rolls [s]





