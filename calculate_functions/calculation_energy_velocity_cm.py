import numpy as np
from constants_folder.constants import *
from calculate_functions.calculation_mass_offset import calculate_mass_hole


#function for calculating the energy
def calculating_energy(moment_of_inertia:float, velocity:float, mass_old:float, angular_velocity:float, radius_cilinder:float, radius_hole:float, angle_slope:float, position:float, angle_center_of_mass:float, offset_1:float, mass_added:float):
    
    '''
    moment_of_inertia: the moment of inertia of the cilinder with hole [kg m^2] \\
    velocity: the velocity of the cilinder with hole of the rotation axis [m/s] \\
    angular_velocity: the angular velocity of the cilinder with hole [rad/s] \\
    mass_old: the mass of the cilinder without a hole [kg] \\
    radius_cilinder: the radius of the complete cilinder [m] \\
    radius_hole: the radius of the hole we made in the cilinder [m] \\
    angle_slope: the angle of the slope [rad] \\
    position: the distance the object has already travelled [m] \\
    angle_center_of_mass: the angle of the center of mass of the cilinder with hole if you take the slope as the x-as [rad] \\
    offset_1: the distance between the center of mass and the rotation axis [m] \\
    mass_added: the mass of the weight that has been added to the hole [kg] 
    '''

    #calculating the height of the ball
    h = radius_cilinder * np.cos(angle_slope) + (LENGHT - position) * np.sin(angle_slope) + offset_1 * np.sin(angle_center_of_mass - angle_slope)

    #h = (length - position) * np.sin(angle_slope)

    #calculating the mass of the new cilinder with hole and mass of the hole
    mass_hole = calculate_mass_hole(mass_old, radius_cilinder, radius_hole)
    mass_new = mass_old - mass_hole + mass_added

    velocity_center_of_mass = calculate_velocity_center_of_mass(angle_center_of_mass, velocity, angular_velocity, offset_1)

    #calculating the kinetic and potential energy
    #kinetic_energy = 0.5 * mass_new * (velocity_center_of_mass) ** 2 + 0.5 * moment_of_inertia * (angular_velocity) ** 2
    kinetic_energy = 0.5 * mass_new * (velocity) ** 2 + 0.5 * moment_of_inertia * (angular_velocity) ** 2
    potential_engery = mass_new * GRAVITATIONAL_VELOCITY * h

    #calculating the total energy
    total_energy = kinetic_energy + potential_engery

    return total_energy, h, kinetic_energy, potential_engery

def calculate_velocity_center_of_mass(angle_center_of_mass:float, velocity_rotation_axis:float, angular_velocity:float, offset_1:float):
    '''
    angle_center_of_mass: the angle of the center of mass of the cilinder with hole if you take the slope as the x-as [rad] \\
    velocity_rotation_axis: the velocity of the cilinder with hole of the rotation axis [m/s] \\
    angular_velocity: the angular velocity of the cilinder with hole [rad/s] \\
    offset_1: the distance between the center of mass and the rotation axis [m] 
    '''
    #calculates the velocity from the point of view of the rotation axis
    relative_velocity_center_of_mass = angular_velocity * offset_1

    #splitting the relative velocity up into a x and y factor
    relative_velocity_center_of_mass_x = relative_velocity_center_of_mass * np.sin(angle_center_of_mass)
    relative_velocity_center_of_mass_y = relative_velocity_center_of_mass * np.cos(angle_center_of_mass)

    #calculating the total velocity of the center of mass
    velocity_center_of_mass = np.sqrt((relative_velocity_center_of_mass_x + velocity_rotation_axis) ** 2 + (relative_velocity_center_of_mass_y) ** 2)

    return velocity_center_of_mass