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

        results = {
            'current_floor': starting_floor,
            'first_basement_charpos': 0
        }

        string_index = 0
        entered_basement = False

        for char in directions:

            string_index += 1

            if char == '(':
                # Go up one floor
                results['current_floor'] += 1

            elif char == ')':
                # Go down one floor
                results['current_floor'] -= 1

                # Determine what character in directions basement is first entered at
                if results['current_floor'] == -1 and entered_basement == False:
                    entered_basement = True
                    results['first_basement_charpos'] = string_index

            else:
                # Break if a character other than ( or )
                print "Invalid Character detected, stopping."
                sys.exit()

        return results


    def __init__(self, file, starting_floor=0):

        directions = self.read_file(file)

        self.result = self.parse_directions(directions, starting_floor)
