from wrapping_paper import Wrapping_Paper

if __name__ == '__main__':

    # Calculate values from input
    results = Wrapping_Paper('input.txt')
    total_wrapping_paper = str(results.paper_total)
    total_ribbon_length = str(results.ribbon_total)

    # Print out results
    print "The amount of wrapping paper you need is: " + total_wrapping_paper + " square feet"
    print "The amount of ribbon you need is: " + total_ribbon_length + " feet"