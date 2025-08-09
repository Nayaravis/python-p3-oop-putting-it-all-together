#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, shoe_size):
        if not isinstance(shoe_size, int):
            print("size must be an integer")
        else:
            self._size = shoe_size

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")