from __future__ import annotations
from threedeebeetree import Point, octant_check

from ratio import Percentiles

def make_ordering(my_coordinate_list: list[Point]) -> list[Point]:
    if len(my_coordinate_list) <= 17: #base case
        return my_coordinate_list 
    else:
        # find the root
        root = (0,0,0)

        px = Percentiles()
        py = Percentiles()
        pz = Percentiles()

        x_coors = [coor[0] for coor in my_coordinate_list]
        qualified_x = ratio_helper(px, x_coors) #so i do this instead, but it gives the same output. so i believe thats the only problm left

        y_coors = [coor[1] for coor in my_coordinate_list]
        qualified_y = ratio_helper(py, y_coors)

        z_coors = [coor[2] for coor in my_coordinate_list]
        qualified_z = ratio_helper(pz, z_coors)

        for coor in my_coordinate_list:
            if coor[0] in qualified_x and coor[1] in qualified_y and coor[2] in qualified_z:
                root = coor
                break
        
        ordered_list = [root]
        my_coordinate_list.remove(root)

        octants = [[] for _  in range(8)]

        #find the correct octant for each coordinate respectively
        for coor in my_coordinate_list:
            octant = octant_check(coor, root)
            octants[octant].append(coor)

        #disregard the octant that is empty so in recursive call, we can use the one that is not empty for recursing
        for oct in octants:
            if len(oct) == 0:
                octants.remove(oct)

        #recursively doing this
        for oct in octants:
            ordered_list += make_ordering(oct)

        return ordered_list

def ratio_helper(p, coor_list, a = 1/8 * 100):
    for coor in coor_list:
        p.add_point(coor)

    qualified = p.ratio(a,a)
    return qualified

def ratio_recursion(p, coor_list, a = 12.5, is_x = False): #a = 12.5
    for coor in coor_list:
        p.add_point(coor)

    if not is_x:
        if len(coor_list) <= 1:
            return coor_list
        
        qualified = p.ratio(a,a)
        return qualified
    
    qualified = p.ratio(a,a)
    
    return qualified
