import math

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

        # Sum all the number
        total = 0
        for num in x:
            total += num
        
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
        Quartile (25, 50, 75 percrent) is a type of quantile -- a cut point that divides a dataset into equal parts.
        Computes the 1st and 3rd quartiles of a given non-empty array x.
        The method returns the quartile as a float, 
        otherwise None if x is an empty list or array.
        '''
        # Check if the list is empty or None
        if len(x) == 0 or x is None:
            return None
        
        # Sort the list
        sortedX = sorted(x)
        lenX = len(sortedX)

        # Find the quartile 1/4 and 3/4
        mid = lenX // 2
        q1 = sortedX[mid // 2]
        q3 = sortedX[mid + (mid // 2)]

        quartile = [float(q1), float(q3)]
        return quartile


    def var(self, x):
        '''
        Computes the variance of a given non-empty list or array x, using a for-loop. 
        The method returns the variance as a float, 
        otherwise None if x is an empty
        '''
        # Check if the list is empty or None
        if len(x) == 0 or x is None:
            return None
        
        # Sum all the number
        total = 0
        for num in x:
            total += num
         
        # Calculate the mean
        mean = total / len(x)

        # Sum of the square of the difference between each number and the mean
        var = 0
        for nb in x:
            var += (nb - mean) ** 2
        
        # Return the variance
        return float(var / len(x))

    def std(self, x):
        '''
        computes the standard deviation of a given non-empty list or array x,using a for-loop. 
        The method returns the standard deviation as a float, 
        otherwise None if x is an empty list or array.
        '''
        # Check if the list is empty or None
        if len(x) == 0 or x is None:
            return None
    
        # Sum all the number
        total_sum = 0
        for num in x:
            total_sum += num
        
        # Divide the sum by the number of elements
        mean = 0 
        mean = total_sum / len(x)

        # Calcule the difference between each number and the mean
        total_mean = 0
        for num in x:
            difference = num - mean
            total_mean += difference * difference

        #  Divide the sum by the number of elements
        total = total_mean / len(x)

        # Return the standard deviation
        return float(math.sqrt(total))
