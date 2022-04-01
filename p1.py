# you are given two numbers A and B . When A is raised to some power P we get a number X. what is the number X that is closest to B
def nearestPower(a,b):
   x=math.floor(math.log(b,a))
   xPlusOne=x+1
   number1=a**x
   number2=a**xPlusOne
   if(abs(number1-b)>abs(number2-b)):
       return number2
   else:
       return number1
