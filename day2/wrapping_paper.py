class Wrapping_Paper():

    def read_file(self, input_file):

        data = []

        # Read the file
        with open(input_file) as file:
            for line in file:
                if 'x' in line:

                    lwh = line.split('x')

                    if len(lwh) == 3:

                        lwh_dict = {
                            'l': lwh[0],
                            'w': lwh[1],
                            'h': lwh[2]
                        }

                        data.append(lwh_dict)

        return data


    def calculate_sqft(self, lwh_array):

        results = {
            "total_sqft": 0,
            "total_ribbon_feet": 0
        }

        # Get individual lwh sets
        for record in lwh_array:

            length = int(record['l'])
            width = int(record['w'])
            height = int(record['h'])

            lw = length*width
            wh = width*height
            hl = height*length

            # Determine smallest size
            lwh_array_mod = [length, width, height]
             
            # Find smallest
            smallest = min(lwh_array_mod)

            # Remove smallest from array
            lwh_array_mod.remove(smallest)

            # Find second smallest
            second_smallest = min(lwh_array_mod)

            # Get ribbon sizes
            ribbon_wrap = smallest + smallest + second_smallest + second_smallest
            bow_size = length * width * height

            results['total_ribbon_feet'] += ribbon_wrap + bow_size
            
            # Get Wrapping paper sizes
            surface_area = 2*lw + 2*wh + 2*hl

            results['total_sqft'] += surface_area + smallest

        return results


    def __init__(self, input_file):

        lwh_array = self.read_file(input_file)

        calc = self.calculate_sqft(lwh_array)

        self.paper_total = calc['total_sqft']
        self.ribbon_total = calc['total_ribbon_feet']


        

