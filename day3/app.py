from directions import Directions

if __name__ == '__main__':

    # Calculate values from input
    results = Directions('input.txt')
    at_least_one_present = str(results.houses_at_least_one_present)

    # Print out results
    print "The amount of houses that received at least one present: " + at_least_one_present
