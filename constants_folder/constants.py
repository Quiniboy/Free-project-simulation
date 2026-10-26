import numpy as np

#constants
GRAVITATIONAL_VELOCITY = 9.81       #[m/s^2]
LENGHT = 20.0                       #[m]
MASS = 1.5                          #[kg]
RADIUS_CILINDER = 1                 #[m]
RADIUS_HOLE =  0.50                 #[m]
OFFSET_2 = 0.50                     #[m]


#np array can have as many angles as you want
#it has to be in radians to work
ANGLE_SLOPE = np.array([np.deg2rad(20), np.deg2rad(30), np.deg2rad(40), np.deg2rad(50), np.deg2rad(60), np.deg2rad(0)])


#variables
t0 = 0                  #initial time [s]
v0 = 0                  #initial velocity [m/s]
x0 = 0                  #initial position [m]
phi0 = np.pi            #initial angle [rad]
omega0 = 0              #initial angular velocity = [rad/s]
v_cm0 = 0               #initial velocity of the center of mass [m/s]
dt = 1e-3               #time increments [s]
end_time = 10           #time the ball rolls [s]



