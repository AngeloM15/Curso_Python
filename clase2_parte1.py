
# coding: utf-8

# OPERADORES DE COMPARACION

# In[1]:


# ==
'a'=='b'


# In[2]:


2==2 


# In[3]:


'Hello world'=='Hola mundo'


# In[4]:


len([1,2,3,])==len(['a','c','d'])


# In[5]:


2<3


# In[6]:


'a'>'z'


# In[7]:


#OPerador en cadena
1<2 and  2<3


# In[8]:


1<2>3


# In[9]:


1==1 or 1==100


# In[10]:


(45<32)==(5<34)and 8>42


# SENTENCIAS CONDICIONALES

# #if

# In[11]:


a=3
if a==3:
    print('it was true')
    


# In[12]:


x=False
if x:
    print('x es verdadero')
else:
    print('igual se va a imprimir')


# In[13]:


0==False


# In[14]:


1==True


# In[15]:


1000==False


# In[16]:


# 0==False
# int >0 ==True


# In[17]:


ubicacion='Banco'

if ubicacion=='Lavando de carros':
    print('Bienvenido al lavadero')
elif ubicacion=='Banco':
    print('bienvenido al Banco')
else:
    print('Donde estas?')


# BUCLE FOR

# In[18]:


#Automitaaziar esta linea
lista1=[1,2,3,4,5,6,7,8,9,10]


# In[19]:


for num in lista1[0:5]:
    print(num)


# In[20]:


#Imprimir numeros pares
for num in lista1:
    if num%2==0:
        print(num)


# In[21]:


for num in lista1:
    if num%2==0:
        print(num)
    else:
        print("Numero impar")


# In[22]:


#acum=0
for num in lista1:
    acum=acum+num

print(acum)
    


# In[ ]:


sum(lista1)


# In[ ]:


acum2=0
for num in lista1:
    acum2+=num

print(acum2)
    


# In[ ]:


for letra in ('esto es una oracion'):
    print(letra)


# In[ ]:


tup=(1,2,3,4,5,)
for t in tup:
    print (t)


# In[ ]:


list2 = [(2,4),(6,8),(10,12)]


# In[ ]:


for tup in list2:
    print(tup)


# In[ ]:


for (t1,t2) in list2:
    print(t1)


# In[ ]:


#diccionarios
d = {'k1':1,'k2':2,'k3':3}


# In[ ]:


for item in d:
    print(item)


# In[ ]:


d.items()


# In[ ]:


for k,v in d.items():
    print('esta es la llave: {} y este es el item:{}' .format(k,v))


# BUCLE WHILE

# In[ ]:


x=0


# In[ ]:


while x<10:
    print('x is actualmente: ', x)
    print('x es menos que 10, sumando 1')
    x+=1


# In[ ]:


while True:
    print('Hola')


# In[ ]:


x=0
while x<15:
    print('x is actualmente: ', x)
    print('x es menos que 10, sumando 1')
    x+=1
    if x==3:
        print('x igual a 3')
        
        
    else:
        print('continuando')
        


# In[ ]:


x=0
while x<15:
    print('x is actualmente: ', x)
    print('x es menos que 10, sumando 1')
    x+=1
    if x==3:
        print('x igual a 3')
        break        
    else:
        print('continuando')


# In[ ]:


num= int(input('ingresa un numero: '))


# In[ ]:


num


# El reto:
# Escriba un programa que escoja un entero aleatorio de 1 a 100, y los jugadores adivinen el número. 
# 
# 
# Las reglas son:
# Si la conjetura de un jugador es menor que 1 o mayor que 100, di "FUERA DE LOS LÍMITES"
# 
# En el primer turno de un jugador, si su conjetura es
# dentro de 10 del número, devuelve "WARM!"
# 
# más allá de 10 lejos del número, regresa "¡FRÍO!"
# 
# En todos los turnos siguientes, si es una suposición
# más cerca del número que la predicción anterior, ¡devuelve "WARMER!"
# más lejos del número que la suposición anterior, regresa "COLDER!"
# ¡Cuando la conjetura del jugador sea igual al número, dígales que han adivinado correctamente y cuántas conjeturas tomó!

# In[ ]:


from random import randint


num=randint(1,100)



# In[ ]:


nveces=[]
while True:
        #requerir el numero de entrada
    usuario=int(input('Adivine un numero entre 1 y 100: ')) 
    if usuario < 1 or usuario >100:
        print('fuera de los limites, intente de nuevo: ')
        continue
    #si adivina:
    if usuario == num:
        print('Felicidades, adivino en {} veces'.format(len(nveces)))
        break
    nveces.append(usuario)
    print()
    print('Cantidad de veces: ', len(nveces))
    

