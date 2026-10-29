#function to calculate the mass of the hole that is cut out
def calculate_mass_hole(mass_old:float, radius_cilinder:float, radius_hole:float):

    '''
    mass_old: the mass of the cilinder without a hole [kg] \\
    radius_cilinder: the radius of the complete cilinder [m] \\
    radius_hole: the radius of the hole we made in the cilinder [m]
    '''

    #calculating the mass of the taken out hole
    mass_hole = (((radius_hole) / (radius_cilinder)) ** 2) * mass_old
    return mass_hole

#calculating the distance between the center of mass and the rotation axis
def calculating_offset_1(offset_2:float, mass_old:float, radius_cilinder:float, radius_hole:float, mass_added:float):
    
    '''
    offset_2: the distance between the center of the cut out hole and the rotation axis [m]\\
    mass_old: the mass of the cilinder without a hole [kg] \\
    radius_cilinder: the radius of the complete cilinder [m] \\
    radius_hole: the radius of the hole we made in the cilinder [m]\\
        mass_added: the mass of the weight that has been added to the hole [kg] 
    '''

    #calling the calculate_mass_function
    mass_hole = calculate_mass_hole(mass_old, radius_cilinder, radius_hole)
    mass_without_weight = mass_old - mass_hole

    #calculating the distance between the center of mass and the rotation axis
    offset_1_without_added_mass = abs((-1 * mass_hole * offset_2) / (mass_old + -1 * mass_hole))

    offset_1 = abs(offset_1_without_added_mass - (mass_added * (offset_2 + offset_1_without_added_mass)) / (mass_without_weight + mass_added))

    return offset_1