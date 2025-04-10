# creating the ship class - it is represented by the string "s"
class Ship:
    def __init__(self, size, orientation, location):
        self.coordinates = []
        self.size = size

        try:
            if orientation == 'horizontal' or orientation == 'vertical':
                self.orientation = orientation
        except ValueError as v:
            
            print('value must be horizontal or vertical')

        # check if the ship can be put on the board and also puts it on the board
        if orientation == 'horizontal':
            for i in range(size):
                self.coordinates.append((location[0], location[1] + i))
        elif orientation == 'vertical':
            for i in range(size):
                self.coordinates.append((location[0] + i, location[1])) 
        else:
            raise ValueError('orientation must horizontal or vertical')
        self.coordinates = tuple(self.coordinates)

    def get_coordinates(self):
        #returns the coordinates of the ship
        return self.coordinate
    
    def __len__(self):
        # returns the length of the ship 
        return self.size
    
    def __eq__(self, other):
        # checks if the ship is equal to the other ship 
        return self.coordinates == other.coordinates
    







# sus
# print(chr(sum(range(ord(min(str(True)))))))