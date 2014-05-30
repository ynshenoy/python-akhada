class fib(object):
    """ A program to generate fibonacci numbers and test them using nose"""
    
    """def __init__(self):
        self.dp = [0, 1]"""

    def reset(self):
        self.dp = [0, 1]
    
    def calculate(self,num):
        self.reset()
        if num == 0 or num == 1:
	    return self.dp[num]
        i = 1
	while i != num:
	    temp = sum(self.dp)
	    self.dp[0] = self.dp[1]
	    self.dp[1] = temp
	    i+=1
	return self.dp[1]


if __name__ == "__main__":
    try:
        num = int(raw_input("enter a number\n"))
    except (ValueError, KeyboardInterrupt):
        print "oops"
    else:
        c = fib()
        c.calculate(num)
        print c.dp[1]
    
		
    """for i in xrange(10):
       print c.calculate(i)"""


        	
    	

