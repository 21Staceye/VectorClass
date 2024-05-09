#Erin Stacey
#ETGG 1803 Lab#3
#Professor Skaggs
##2/10/22
#Some from notes in class
#Some from python.docs
import math
class Vector(object):
    """Finds the demions of a vector, adds, multiplys,subtracts,and divids the passed in vector."""
    def __init__(self,*args):
        """Makes the constructors for the class as of self.data and self.dem."""
        if isinstance(args,str):
            raise TypeError("The Values must be a float or int.")
        self.dem = len(args)
        if self.dem == 3:
            self.__class__ = Vector3
        if self.dem == 2:
            self.__class__ = Vector2
            
        if self.dem <= 1:
            raise TypeError("Does not fit in to the vector class.")
        self.data = []
        for i in args:
            i = float(i)
            self.data.append(i)
       
       
       
    def __str__(self):
        """Makes the passed in vector a string."""
        if len(self.data) >= 1:
            for toppings in self.data:
                return f"<Vector{self.dem}:{self.data}>"       

    def __len__(self):
        """Finds the length of the list."""
        return len(self.data)

    def __eq__(self,other):
        """Finds out if two vectors are the same."""
        if self.data == other.data and self.dem == other.dem :
            return f"True"
        elif self.data != other.data and self.dem != other.dem:
            return f"False"
        else:
            raise TypeError("The values must be a int or float.")

    def __getitem__(self,value):
        """Gets the item in the self.data list."""
        return self.data[value]
        
    def __setitem__(self,value,data):
        """Sets the item in the self.data list."""
        self.data[value] = float(data)

    def copy(self):
        """Makes a copy of the list. """
        cop = self.data[:]
##        if self.dem == 3:
##            self.__class__ = Vector3
##        if self.dem == 2:
##            self.__class__ = Vector2
            
        return cop
    def __neg__(self):
        
        """If the vector has a negative sign it is switched."""
        copp = self.data[:]
        co = []
        for c in copp:
            c = -c
            co.append(c)
        return Vector(*co)

    def __mul__(self,other):
        """Multiplys a scaler with a vector."""
        if isinstance(other,int) or isinstance(other,float):
            bob = self.data[:]
            copp = self.data[:]
            m = []
            for h in copp:
                z = other * h
                m.append(z)
            return Vector(*m)
        else:
            raise TypeError("You can only multiply a vector with a int or float.")
                            
       
        
       
    def __rmul__(self,other):
        """Multiplys a vector with a scaler"""
        if isinstance(other,int) or isinstance(other,float):
            copp = self.data[:]
            m = []
            for h in copp:
                z = other * h
                m.append(z)
            return Vector(*m)
        else:
             raise TypeError("You can only multiply a vector with a int or float.")
                            
       
       
       
    def __add__(self,other):
        """ Adds vectors togehter."""
        if isinstance(other,Vector) and self.dem == other.dem :
             o = self.data[:]
             c = other.data[:]
             a = []
             k = []
             sum_list = []
             for h in o:
                 a.append(h)
             for y in c:
                 k.append(y)
                 
             res_lt = []
             for x in range(0,len(a)):
                 res_lt.append(a[x] + k[x])
             return Vector(*res_lt)
        else:
            raise TypeError(" You can only add a vector together with a vector or the dimenons don't match.")

    def __sub__(self,other):
       """Subtracts a vector with a vector"""
       if isinstance(other,Vector) and self.dem == other.dem:
            o = self.data[:]
            c = other.data[:]
            a = []
            k = []
            sum_list = []
            for h in o:
                a.append(h)
            for y in c:
                k.append(y)
                 
            res_lt = []
            for x in range(0,len(a)):
                res_lt.append(a[x] - k[x])
            return Vector(*res_lt)
       else:
            raise TypeError(" You can only subtract a vector together with a vector or the dimenisons don't match.")

    def __truediv__(self,other):
        """Divids a scaler with a a vector."""
        if isinstance(other,int) or isinstance(other,float):
           a = self.data[:]
           j = []
           for h in a:
                z = other / h
                j.append(z)
           return Vector(*j)
        else:
            raise TypeError("Only ints or floats for the scaler.")


class Vector2(Vector):
   """Gives the spaces where x and y are and there values."""
   def __init__(self,x,y):
        """Sets the value for vector 2 classes and x and y componets as well."""
        self.data = [float(x),float(y)]
        self.dem = len(self.data)

   def __str__(self):
        """ Makes the string for the vector2 class."""
        for i in self.data:
            
            return f"<Vector3: {self.data[0]} , {self.data[1]} >" 


   @property
   def x(self):
       """Get x as a property of the class."""
       return self.data[0]

   @x.setter
   def x(self,value):
       """Set x as a property of the class."""
       self.data[0]

   @property
   def y(self):
       """Get y as a property of the class."""
       return self.data[1]
   @y.setter
   def y(self,value):
       """Set x as a property of the class."""
       self.data[1]
        

class Vector3(Vector):
    """Gives the spaces where x,y, and z are and there values."""
    def __init__(self,x,y,z):
        
        """ Sets x,y, and z to the init"""
        self.data = []
        self.dem = len(args)
        for i in args:
            
            i = float(i)
            self.data.append(i)
       
    def __str__(self):
        """ makes the data into a string."""
        for b in self.data:
            return f"<Vector3: {self.data[0]} , {self.data[1]}, {self.data[2]} >"
    @property
    def x(self):
        """Gets  as a property of the class."""
        return self.data[0]
    @x.setter
    def x(self,value):
        """Sets  as a property of the class."""
        self.data[0]

    @property
    def y(self):
        """Get y as a property of the class."""
        return self.data[1]
    @y.setter
    def y(self,value):
        """Set x as a property of the class."""
        self.data[1]
    @property
    def z(self):
        """Get z as a property of the class."""
        return self.data[2]
    @z.setter
    def z(self,value):
        """Set x as a property of the class."""
        self.data[2]

    

if __name__ == "__main__": 
# Testing class
    a = Vector(1, 2, 3, 4)
    v = Vector(1, 2, 3)
    w = Vector(4, 5, 6)
    z = v + w
    print(a)				# <Vector4: 1.0, 2.0, 3.0, 4.0>
    print(z)            		# <Vector3: 5.0, 7.0, 9.0>
##    print("v + 5 =", v + 5) 	# TypeError: You can only add another 
##    # Vector3 to this Vector3 (You passed
    # '5'.)
    q = v - w
    print(q)            		# <Vector3: -3.0, -3.0, -3.0>
    a = v * -2
    print(a)            		# <Vector3: -2.0, -4.0, -6.0>
    a = -2 * v
    print(a)            		# <Vector3: -2.0, -4.0, -6.0>
    b = a + (v + w)
    print(b)           		# <Vector3: 3.0, 3.0, 3.0>
    d = v + (v + v) + w
    print(d)           		# <Vector3: 7.0, 11.0, 15.0>
    n = -v
    print(n)		  		# <Vector3: -1.0, -2.0, -3.0>
    s = Vector2(3, -2)
    print(s)		  		# <Vector2: 3.0, -2.0)
    print(s.x)		  		# 3.0
    t = Vector(3, -2)
    print(t)		  		# <Vector2: 3.0, -2.0>
    print(t.y)		 	 	# -2.0
    print(s == t)	  		# True
    print(d.x)
    
