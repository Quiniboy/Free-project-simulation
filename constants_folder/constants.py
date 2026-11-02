import numpy as np


# constants

GRAVITATIONAL_VELOCITY = 9.81               #[m/s^2]
LENGHT = 20.0                               #[m]
MASS = 20                                   #[kg]
RADIUS_CILINDER =  1                        #[m]
RADIUS_HOLE =   0.5                         #[m]
OFFSET_2 = 0.5                              #[m]
MASS_STEEL = 142e-3                         #[kg]
MASS_CONCRETE = 293.7e-3 + 142e-3           #[kg]
ADDED_MASS = MASS_STEEL + MASS_CONCRETE     #[kg]

#This is to turn on the specific case without the same density throughout the added mass
SPECIFIC_FOR_OURS = False

#np array can have as many angles as you want
#it has to be in radians to work
ANGLE_SLOPE = np.array([np.deg2rad(20), np.deg2rad(30), np.deg2rad(40), np.deg2rad(50), np.deg2rad(60)])


#variables
t0 = 0                              #initial time [s]
v0 = 0                              #initial velocity [m/s]
x0 = 0                              #initial position [m]
phi0 = -1 * 0.5 * np.pi             #initial angle [rad]
omega0 = 0                          #initial angular velocity = [rad/s]
v_cm0 = 0                           #initial velocity of the center of mass [m/s]
dt = 1e-4                           #time increments [s]
end_time = 15                       #time the ball rolls [s]





