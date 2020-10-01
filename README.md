In this second example of a Python Object Oriented Programming, we use the constructor class Cat.
This class is then to instantiated different vairables of cat, such as Felix, TomCat, and HouseCat.
In this program, I also dxetermined the output to display the oldest cat via a funciton that passes 
*args into OlderCat. This is a unique part of this program that takes the max method function and calls 
the instantation of Felix, TomCat and HouseCat as positional arguments. Thus the output then takes a string
format with the OlderCat function call within the string format, to determine the older cat.

The following is a brief explanation of the def OlderCat():

I used def OlderCat to determine the older cat by:

    1. Passing Felix, TomCat, and HouseCat as *args for arguments.
    2. Then I returned the args by passing it on the max() method.
    3. The output from the string format included the OlderCat()
    function call by passing their instantiation of age, such as 
    Felix.age, TomCat.age, HouseCat.age to access the age and make 
    determination based on the return max(args), which would return the 
    age of the older cat.