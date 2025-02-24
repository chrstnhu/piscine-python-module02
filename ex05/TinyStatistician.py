#  All methods take a list or a numpy.ndarray as parameter.
# We are assuming that all inputs have a correct format, i.e. a list or array of numeric type or empty list or array.
# You don’t have to protect your functions against input errors.


class TinyStatistician:
    def mean(self, x):
        '''
        Calcul the mean(moyenne) of a given non-empty list or array x, using a for-loop.
        The method returns the mean as a float, 
        otherwise None if x is an empty list or array. 
        '''
        # Check if the list is empty or None
        if len(x) == 0 or x is None:
            return None

        # Add all the numbers in the list
        total = 0
        for num in x:
            total += num
        
        # Return the mean
        return float(total / len(x))


    def median(self, x):
        '''
        Calcul the median of a given non-empty list or array x. 
        The method returns the median as a float, 
        otherwise None if x is an empty list or array.
        '''
        # Check if the list is empty or None
        if len(x) == 0 or x is None:
            return None
        
        # Sort the list
        sortedX = sorted(x)
        lenX = len(sortedX)
        
        # Check if the list has an odd or even number of elements
        if lenX % 2 == 1:
            return float(sortedX[lenX // 2])
        else:
            mid1 = sortedX[(lenX // 2) - 1]
            mid2 = sortedX[lenX // 2]
            return float((mid1 + mid2) / 2)


    def quartile(self, x):
        '''
        Computes the 1st and 3rd quartiles of a given non-empty array x.
        The method returns the quartile as a float, 
        otherwise None if x is an empty list or array.
        '''
        # Check if the list is empty or None
        if len(x) == 0 or x is None:
            return None


    def var(self, x):
        '''
        Computes the variance of a given non-empty list or array x, using a for-loop. 
        The method returns the variance as a float, 
        otherwise None if x is an empty
        '''
    

    def std(self, x):
        '''
        computes the standard deviation of a given non-empty list or array x,using a for-loop. 
        The method returns the standard deviation as a float, 
        otherwise None if x is an empty list or array.
        '''