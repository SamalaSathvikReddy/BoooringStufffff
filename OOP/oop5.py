class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x1, y1, x2, y2):
        return (
            self.pos_x >= x1
            and self.pos_x <= x2
            and self.pos_y >= y1
            and self.pos_y <= y2
        )


# don't touch above this line


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, height, width, fire_range):
        super().__init__(name, pos_x, pos_y) 
        self.__height = height
        self.__width = width
        self.__fire_range = fire_range
        self.__hit_box = Rectangle(self.pos_x - width/2, self.pos_y - height/2, self.pos_x + width/2, self.pos_y + height/2)
    def in_area(self, x1, y1, x2, y2):
        rec = Rectangle(x1, y1, x2, y2)
        return rec.overlaps(self.__hit_box) 
    


class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):
        return min(self.__x1, self.__x2) 

    def get_right_x(self):
        return max(self.__x1, self.__x2) 

    def get_top_y(self):
        return max(self.__y1, self.__y2)

    def get_bottom_y(self):
        return min(self.__y1, self.__y2)

    def overlaps(self, rect):
        if(self.get_left_x() <= rect.get_right_x() and self.get_right_x() >= rect.get_left_x() and self.get_top_y() >= rect.get_bottom_y() and self.get_bottom_y() <= rect.get_top_y()):
            return True
        return False
    
class Sword:
    def __init__(self, sword_type):
        self.sword_type = sword_type

    def __add__(self, other_sword):
        if (self.sword_type == other_sword.sword_type == "bronze"):
            return "iron"
        elif (self.sword_type == other_sword.sword_type == "iron"):
            return "steel"
        else:
            raise Exception("cannot craft")
        
