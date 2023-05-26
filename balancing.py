from __future__ import annotations
from threedeebeetree import Point

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
        qualified_x = ratio_recursion(px, x_coors, is_x= True)

        y_coors = [coor[1] for coor in my_coordinate_list if coor[0] in qualified_x]
        qualified_y = ratio_recursion(py, y_coors)

        if len(qualified_y) == 1:
            for coor in my_coordinate_list:
                if coor[1] == qualified_y[0]:
                    root = coor

        else:
            z_coors = [coor[2] for coor in my_coordinate_list if coor[0] in qualified_x and coor[1] in qualified_y]
            qualified_z = ratio_recursion(pz, z_coors)

        if len(qualified_z) == 1:
            for coor in my_coordinate_list:
                if coor[2] == qualified_z[0]:
                    root = coor


        for coor in my_coordinate_list:
            if coor[0] in qualified_x and coor[1] in qualified_y and coor[2] in qualified_z:
                root = coor
                break
        
        ordered_list = [root]
        my_coordinate_list.remove(root)

        octants = [[] for _  in range(8)]

        for coor in my_coordinate_list:
            octant = octant_check1(coor, root)
            octants[octant].append(coor)

        for oct in octants:
            if len(oct) == 0:
                octants.remove(oct)
            #recursively doing this
            ordered_list += make_ordering(oct)

        return ordered_list


def ratio_recursion(p, coor_list, a = 12.5, is_x = False): #a = 12.5
     #complexity doesnt matter lmao
    for coor in coor_list:
        p.add_point(coor)

    if not is_x:
        if len(coor_list) == 1:
            return coor_list
        
        qualified = p.ratio(a,a)
        return qualified
    
    qualified = p.ratio(a,a)

    # else: #if it is the x axis
    #     qualified = p.ratio(a,a)
    #     if len(qualified) == 0 or len(qualified) == 1: #cant be empty
    #         a -= 0.5
    #         ratio_recursion(coor_list, a, True)
    return qualified


def octant_check1(current, root) -> int:

    if root[0] >= current[0] and root[1] >= current[1] and root[2] >= current[2]:
        return 7
    elif root[0] <= current[0] and root[1] >= current[1] and root[2] >= current[2]:
        return 6
    elif root[0] <= current[0] and root[1] <= current[1] and root[2] >= current[2]:
        return 5
    elif root[0] >= current[0] and root[1] <= current[1] and root[2] >= current[2]:
        return 4
    elif root[0] >= current[0] and root[1] >= current[1] and root[2] <= current[2]:
        return 3
    elif root[0] <= current[0] and root[1] >= current[1] and root[2] <= current[2]:
        return 2
    elif root[0] <= current[0] and root[1] <= current[1] and root[2] <= current[2]:
        return 1
    elif root[0] >= current[0] and root[1] <= current[1] and root[2] <= current[2]:
        return 0