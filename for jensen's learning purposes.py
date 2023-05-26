# First attempt:
def make_ordering(my_coordinate_list):

    # print("Coordinate List:",my_coordinate_list)
    if len(my_coordinate_list) >= 18:
        x = 0
        y = 0
        z = 0
        for coordinate in my_coordinate_list: #sum
            x += coordinate[0]
            y += coordinate[1]
            z += coordinate[2]

        # find the mean
        x = x/len(my_coordinate_list)
        y = y/len(my_coordinate_list)
        z = z/len(my_coordinate_list)
        
        #Find the closest to the average
        bestCoordinate = (9000000, None) #(distance, (coordinate))
        for coordinate in my_coordinate_list:
            diff = abs(coordinate[0] - x) + abs(coordinate[1] - y) + abs(coordinate[2] - z) #Find the absolute difference between the average point
            # print("diff",diff)
            if diff < bestCoordinate[0]:
                bestCoordinate = (diff, coordinate)
            # print("best coordinate",bestCoordinate)
        


        #this afterwards r ok
        returnList = [bestCoordinate[1]] #put the root at the front
        quadrants = [[] for i in range(8)]
        my_coordinate_list.remove(bestCoordinate[1]) #remove from the input list

        # Separate all remaining points into 8 quadrants based on the curent best quadrant
        for coordinate in my_coordinate_list:
            oct = octant(coordinate, bestCoordinate[1])
            quadrants[oct].append(coordinate) #append the inner list according to this index
        
        # Recursively call the quadrants which are not empty.
        quadrants = [inList for inList in quadrants if len(inList)>0] #disregard all the empty lists
        for inLIst in quadrants:
            returnList += make_ordering(inLIst)

        return returnList
    else:
        # Return if the length of the list is 2 or less
        return my_coordinate_list