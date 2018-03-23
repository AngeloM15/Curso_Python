
# coding: utf-8

# In[1]:


class Employee_details():
    
    def __init__(self,name,position):
        self.employee_name = name
        self.employee_position = position
        
    def set_employee_name(self,name):
        self.employee_name = name
        
    def set_employee_position(self,position):
        self.employee_position = position
        
    def get_employee_name(self):
        return self.employee_name
    
    def get_employee_position(self):
        return self.employee_position


# In[2]:


trab1=Employee_details('Juan', 'CEO')
trab2=Employee_details('Pepe', 'ADM')
trab3=Employee_details('Jose', 'Conta')


# In[4]:


trab1.get_employee_name()


# In[5]:


trab1.set_employee_position('CTO')


# In[7]:


trab1.get_employee_position()


# In[8]:


class Circle:
    pi = 3.14

    # Circle gets instantiated with a radius (default is 1)
    def __init__(self, radius=1):
        self.radius = radius 
        self.area = radius * radius * Circle.pi

    # Method for resetting Radius
    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius * new_radius * self.pi

    # Method for getting Circumference
    def getCircumference(self):
        return self.radius * self.pi * 2
c = Circle()

print('Radius is: ',c.radius)
print('Area is: ',c.area)
print('Circumference is: ',c.getCircumference())


# In[11]:


c.setRadius(2)


# In[12]:


c.getCircumference()


# In[16]:


class Courses():
    
    def set_course(self,course):
        self.course = course
        
    def get_course(self):
        return self.course
    
def create_list():
    course_list = []
    print ("Enter nothing to quit")
    while True:
        courses = input("Enter the course you did:")
        if courses == "":
            break
        year_4_courses = Courses()
        year_4_courses.set_course(courses)
        course_list.append(year_4_courses)
    return course_list

def display_list(course_list):
    
    for my_course in course_list:
        print(my_course.get_course())
    
def main():
    chemical_courses = create_list()
    print("Here is your course list")
    display_list(chemical_courses)

if __name__ == "__main__":
    main()


# In[19]:


class Animal:
    def __init__(self):
        print("Animal creado")

    def quiensoy(self):
        print("Animal")

    def come(self):
        print("Comiendo")


class Perro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Perro creado")

    def quiensoy (self):
        print("Perro")

    def ladrido(self):
        print("Woof!")


# In[21]:


d=Perro()


# In[22]:


d.quiensoy()


# In[23]:


d.come()


# In[25]:


d.ladrido()


# In[45]:


class Papa():
    def __init__(self, nombre):
        self.nombre=nombre
    def ojos(self):
        return "cafe"
    
    def talla(self):
        return "bajo"
    
    def estudios(self):
        return "medicina"
    def ocupacion(self):
        return "Doctor"
   
class Mama():
    def __init__(self, nombre):
        self.nombre=nombre
    def ocupacion(self):
        return "Profesora"

class Hijo(Mama,Papa):
    def color_pelo(self):
        return "castanho"
padre=Papa("Carlos")
madre=Mama("Carla")
yo = Hijo("Jose")
print( "Hijo tiene una ocupacion",yo.ocupacion())


# In[34]:


class Animal():
    def __init__(self, name):
        self.name = name

    def habla(self):
        pass

class Perro(Animal):
    def __init__(self, name):
        self.name = name

    def habla(self):
        return self.name+' dice Woof!'
    
class Gato(Animal):
    def __init__(self, name):
        self.name = name

    def habla(self):
        return self.name+' dice Meow!' 
    
niko = Perro('Niko')
felix = Gato('Felix')

print(niko.habla())
print(felix.habla())


# In[35]:


#EJERCICIO CAJERO
# crear una clase cajero, donde habra 2 atributos:
# Duenho y Balance
# y 2 metodos:
# Deposito y retiro

#Cuando se haga retiros, no puede exceder el balance


# In[36]:


class Cajero:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self,dep_amt):
        self.balance += dep_amt
        print('Deposito Aceptado')
        
    def withdraw(self,wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print('Retiro Aceptado')
        else:
            print('Fondos No disponibles!')


# In[37]:


usu1=Cajero('jose', 100)


# In[38]:


usu1.owner


# In[39]:


usu1.balance


# In[40]:


usu1.deposit(5000)


# In[41]:


usu1.withdraw(4300
            )


# In[42]:


usu1.withdraw(4300)


# In[52]:


def askint():
    try:
        val1 = int(input("Please enter an integer: "))
        val2 = int(input("Please enter an integer: "))
    except:
        print("Looks like you did not enter an integer!")

    finally:
        print(val1)
        print(val2)
        print("Finally, I executed!")
    print(val1+val2)
    


# In[53]:


askint()


# In[54]:


askint()


# In[55]:


def askint():
    while True:
        try:
            val = int(input("Please enter an integer: "))
        except:
            print("Looks like you did not enter an integer!")
            continue
        else:
            print("Yep that's an integer!")
            print(val)
            break
        finally:
            print("Finally, I executed!")


# In[56]:


askint()


# In[57]:


askint()


# In[58]:


#Ejemplos


# In[59]:


x=5


# In[62]:


y=0


# In[63]:





# In[68]:


x=5
y=0

try:
    z=x/y
except ZeroDivisionError:
    print('no se puede dividir entre 0')
finally:
        print('fin')


# In[66]:


z


# # Formato para impimir cadenas

# In[73]:


jugador='Pizarro'
goles=15
print('%s no metio %s goles \t con la \n seleccion' %(jugador, goles))


# In[ ]:





# In[75]:


#impresion de decimales
print('5 puntos flotantes: %.2f' %(13.144))


# In[76]:


print('puntos flotantes: %.5f' %(13.144))


# In[78]:


print('5 puntos flotantes: %.10f' %(8/3))


# In[79]:


print( 'primero: %s, Segundo: %s, Tercero: %s' %('Ivan', 'Giorgio', 'Daniel'))


# In[81]:


print( 'primero: {a}, Segundo: {a}, Tercero: {c}'.format(a='Ivan', c='Giorgio', b='Daniel'))


# In[82]:


nombre= 'david'


# In[83]:


print(f"Su nombre es {nombre}")

