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

        total_sqft = 0

        # Get individual lwh sets
        for record in lwh_array:

            length = int(record['l'])
            width = int(record['w'])
            height = int(record['h'])

            lw = length*width
            wh = width*height
            hl = height*length

            # Determine smallest size
            smallest = min([lw, wh, hl])
            
            # ( 2*l*w + 2*w*h + 2*h*l )
            surface_area = 2*lw + 2*wh + 2*hl

            total_sqft += surface_area + smallest

        return total_sqft


    def __init__(self, input_file):

        lwh_array = self.read_file(input_file)

        self.total = self.calculate_sqft(lwh_array)


        

