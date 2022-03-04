def myfunc(x1,x2,x3):
    if((x1+x2+x3) == 0):
        return 'Not a number – denominator equals zero'
    if(isinstance(x1, float)== False
     or isinstance(x2, float) == False or
     isinstance(x3, float) == False):
     return('Error: parameters should be float')
    return(((x1+x2+x3)*(x2+x3)*x3)/(x1+x2+x3))

def convert(hours, minutes):
    if(hours <= 0 or minutes <= 0):
        return("Input error!")
    return(hours * 60 * 60 + minutes * 60)
