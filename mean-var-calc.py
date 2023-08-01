import numpy as np

# Get input from user for array numbers
list = input('Please give 9 numbers: ')
# Converts input to string and iterates over values adding commas
nlist = [int(d) for d in str(list)]

def calculate():
    # If user gives 9 numbers, program will run
    if len(list) == 9:
        # Creates a flattened array of user input
        arr = np.array(nlist)
        # Create a 3,3 array
        narr = arr.reshape(3, 3)
        print(narr)
        print('Mean: ', np.mean(narr, axis=0), np.mean(narr, axis=1), np.mean(narr))
        print('Variance: ', np.var(narr, axis=0), np.var(narr, axis=1), np.var(narr), )
        print('Standard deviation: ', np.std(narr, axis=0), np.std(narr, axis=1), np.std(narr), )
        print('Max: ',  np.max(narr, axis=0), np.max(narr, axis=1), np.max(narr), )
        print('Min: ', np.min(narr, axis=0), np.min(narr, axis=1), np.min(narr), )
        print('Sum: ', np.sum(narr, axis=0),  np.sum(narr, axis=1), np.sum(narr))
    #If user gives less or more than 9 numbers will be prompted to input 9
    else:
        print('Please enter 9 numbers!')

calculate()