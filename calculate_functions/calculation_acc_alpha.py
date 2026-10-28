from constants_folder.constants import *
from calculate_functions.calculation_mass_offset import calculate_mass_hole

#calculating the acceleration and angular acceleration
def calculating_acceleration_and_alpha(moment_of_inertia:float, mass_old:float, radius:float, angle_center_of_mass:float, angle_slope:float, omega:float, offset_1:float, radius_hole):

    '''
    moment_of_inertia: the moment of inertia of the cilinder with a hole [kg m^2] \\
    mass: the mass of the cilinder with hole [kg] \\
    radius: the radius of the cilinder [m] \\
    angle_center_of_mass: the angle of the center of mass of the cilinder with hole if you take the slope as the x-as [rad] \\
    angle_slope: the angle of the slope [rad]\\
    omega: the angular velocity of the cilinder\\
    offset_1: the distance between the center of mass and the rotation axis [m]
    '''
    mass_hole = calculate_mass_hole(mass_old, radius, radius_hole)
    mass_new = mass_old - mass_hole
    
    #calculating the acceleration    
    acceleration = ((radius) ** 2 * mass_new * GRAVITATIONAL_VELOCITY * (np.sin(angle_slope) + (offset_1 / radius) * np.cos(angle_slope - angle_center_of_mass))) / (((radius) ** 2) * mass_new + moment_of_inertia)
    #acceleration = ((radius) ** 2 * mass_new * GRAVITATIONAL_VELOCITY * (np.sin(angle_slope) + (offset_1 / radius) * ((np.cos(angle_slope) * np.cos(angle_center_of_mass) + np.sin(angle_slope) * np.sin(angle_center_of_mass))))) / (((radius) ** 2) * mass_new + moment_of_inertia)

    # calculating the angular acceleration It's an asumption that it rols smoothly, that obivously doesn't happend if angle slope is bigger than 90 deg
    if angle_slope < np.deg2rad(90) % (2 * np.pi):
        alpha = -acceleration / radius

    else:
        alpha = 0

    return acceleration, alpha 