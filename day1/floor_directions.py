import os
import sys

class Floor_Directions():

    def read_file(self, file):

        results = ''

        with open(file) as f:
            for line in f:
                results += line

        return results


    def parse_directions(self, directions, starting_floor):

        current_floor = starting_floor

        for char in directions:

            if char == '(':
                # Go up one floor
                current_floor += 1

            elif char == ')':
                # Go down one floor
                current_floor -= 1

            else:
                # Break if a character other than ( or )
                print "Invalid Character detected, stopping."
                sys.exit()

        return current_floor


    def __init__(self, file, starting_floor=0):

        directions = self.read_file(file)

        result = self.parse_directions(directions, starting_floor)

        print result


Floor_Directions('input.txt')
