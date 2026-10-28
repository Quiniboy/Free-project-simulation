from calculate_functions.calculation_mass_offset import calculate_mass_hole

#funtion to calculate the moment of inertia of the cilinder with a hole
def calucate_moment_of_inertia(mass_old:float, radius_cilinder:float, radius_hole:float, offset_1:float, offset_2:float, mass_added:float):

    '''
    mass_old: the mass of the cilinder without a hole [kg] \\
    radius_cilinder: the radius of the complete cilinder [m] \\
    radius_hole: the radius of the hole we made in the cilinder [m] \\
    offset_1: the distance between the center of mass and the rotation axis [m] \\
    offset_2: the distance between the center of the cut out hole and the rotation axis [m]\\
    mass_added: the mass of the weight that has been added to the hole [kg]
    '''

    #calculating the mass of the new cilinder with hole and mass of the hole
    mass_hole = calculate_mass_hole(mass_old, radius_cilinder, radius_hole)
    mass_new = mass_old - mass_hole + mass_added
    print(mass_new)

    #calculating the moment of inertia of the old cilinder and the hole of the cilinder
    moment_of_inertia_old_cilinder = 0.5 * mass_old * (radius_cilinder) ** 2
    moment_of_inertia_hole = 0.5 * mass_hole * (radius_hole) ** 2 + mass_hole * (offset_2) ** 2
    moment_of_inertia_added_weight = 0.5 * mass_added * (radius_hole) ** 2 + mass_added * (offset_2) ** 2

    #calculating the moment of inertia of the new cilinder looking at it from the center of mass
    moment_of_inertia = moment_of_inertia_old_cilinder - moment_of_inertia_hole + moment_of_inertia_added_weight

    #calculating the moment of inertia of the new cilinder looking at it form the ratation axis


    #Sanders formula to test our energy
    #moment_of_inertia = 0.5 * mass_new * (radius_cilinder ** 2 + radius_hole ** 2 - (2 * offset_2 ** 2 * radius_hole ** 2) / (radius_cilinder ** 2 - radius_hole ** 2))

    return moment_of_inertia