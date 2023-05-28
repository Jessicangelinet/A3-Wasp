from __future__ import annotations
from threedeebeetree import Point, octant_check

from ratio import Percentiles

def make_ordering(my_coordinate_list: list[Point]) -> list[Point]:
    """
        reorder the input list of coordinates in 1:7 ratio 

        :complexity best: O(n) + comp <=), when the input list has 17 or less coordinates, 
        the function returns the input list

        :complexity worst: 3*(O(n) + O(ratio_helper()))
                        +  O(n) * [O(x) + O(y) + O(z)]
                        +  O(no)
                        when my_coordinate_list has more than 17 coordinates and after finding the root,
                        each remaining octant must be ordered again by calling this function to recursively do it
            
        where n is the number of coordinates in the list; len(my_coordinate_list)
        where x is the len(qualified_x), y is the len(qualified_y), and z is the len(qualified_z)
        where no is the new len(octants)
    """
    if len(my_coordinate_list) <= 17: #base case
        return my_coordinate_list 
    else:
        # find the root
        root = (0,0,0)

        px = Percentiles()
        py = Percentiles()
        pz = Percentiles()

        # --- 3*(O(n) + O(ratio_helper())) ---
        x_coors = [coor[0] for coor in my_coordinate_list]
        qualified_x = ratio_helper(px, x_coors) #so i do this instead, but it gives the same output. so i believe thats the only problm left

        y_coors = [coor[1] for coor in my_coordinate_list]
        qualified_y = ratio_helper(py, y_coors)

        z_coors = [coor[2] for coor in my_coordinate_list]
        qualified_z = ratio_helper(pz, z_coors)
        #-----

        for coor in my_coordinate_list: #O(n) * [O(x) + O(y) + O(z)]
            #O(x) + O(y) + O(z) from "in", where x is the len(qualified_x), y is the len(qualified_y), and z is the len(qualified_z)
            if coor[0] in qualified_x and coor[1] in qualified_y and coor[2] in qualified_z:
                root = coor
                break
        
        ordered_list = [root]
        my_coordinate_list.remove(root) #O(n)

        octants = [[] for _  in range(8)] #O(1)

        #find the correct octant for each coordinate respectively
        for coor in my_coordinate_list: #O(n)
            octant = octant_check(coor, root)
            octants[octant].append(coor)

        #disregard the octant that is empty so in recursive call, we can use the one that is not empty for recursing
        for oct in octants: #O(1) 
            if len(oct) == 0:
                octants.remove(oct)

        #recursively doing this
        for oct in octants: #O(no), where no is the new len(octants)
            ordered_list += make_ordering(oct)

        return ordered_list

def ratio_helper(p, coor_list, a = 1/8 * 100):
    """
        reorder the input list of coordinates in 1:7 ratio 

        :complexity best = worst: O(n) + O(Percentiles.ratio()), because no matter what the input list's length is,
        all the codes will run
        
        where n is the number of items in the input list
    """
    for coor in coor_list:
        p.add_point(coor)

    qualified = p.ratio(a,a)
    return qualified