
# coding: utf-8

# In[7]:


from random import randint


num=randint(1,100)


# In[8]:


nveces=[0]
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
    #print('Cantidad de veces: ', len(nveces))
    #print()
    #print(nveces)
    #print(nveces[-2])
    
    #Buscar en el intento anterior utilizando [-2], al primer intento nveces[-2]==0
    #que retorna un False, no entrando a la siguiente condicional
    
    if nveces[-2]:
        if abs(num-usuario)< abs(num-nveces[-2]):
            print('Mas Caliente!')
        else:
            print('Mas Frio!')
    else:
        if abs(num-usuario) <=10:
            print('Caliente')
        else:
            print('Frio')
    


# In[9]:


0==True


# In[18]:


lista=[0,4]


# In[19]:


lista[-2]


# In[13]:


lista2=[0]


# In[14]:


lista2


# In[17]:


lista2[-2]


# METODOS

# In[20]:


lista=[1,2,3,4,5]


# In[21]:


lista.append(6)


# In[22]:


lista.count(2)


# FUNCIONES

# In[28]:


#funcion para retornar el menor de numero de 2 numeros dados,
#pero si ambos son pares, retorna el menor
def num_menor( a, b):
    '''funcion para retornar el menor de numero de 2 numeros dados,
        pero si ambos son pares, retorna el menor'''
    if a%2==0 and b%2==0:
        print('Numero sosn pares')
        return min(a,b)
    else:
        print('Numeros son impares')
        return min(a,b)
    
        


# In[29]:


num_menor(46,34)


# In[30]:


num_menor(11,35) 


# In[38]:


#hacer una funcion que coja la primera letra de 2 palabras  ingresadas
#retorne True o False si son iguales
def comparador(le1):
    palabra=le1.split()
    print(palabra)
    return palabra[0][0] == palabra[1][0]


# In[39]:


comparador('Llama Llave')


# In[37]:


comparador('Llama', 'Fuego')


# In[46]:


#Hacer una funcion de BlackJack , pida ingresar 3 numeros, entre 1 y 11
#1.Si la suma es menor a 21, retorna la suma
#2.si la suma es excede 21, pero menor que 31 Y hay un 11 en los numeros
# le resto 10
#3.si mayor a 21, retorna perdio
#4.Si es igual a 21, imprimre 'Ganaste'

def blackjack(a,b,c):
    if sum((a,b,c))<21:
        return sum((a,b,c))
    elif sum((a,b,c))<=31 and 11 in (a,b,c):
        resta=sum((a,b,c)) -10
        if resta==21:
                print('Ganaste')
        else:
            return resta
    elif sum((a,b,c))==21:
        print('Ganaste')
    else:
        print ('Perdiste')


# In[47]:


blackjack(5,6,7)


# In[48]:


blackjack(10,10,10)


# In[49]:


blackjack(10,10,11)


# In[45]:


blackjack(3,8,10)


# In[50]:




#hacer una funcion que retorne la oracion ingresada pero al reves
#'Estoy en casa' = 'Casa en estoy'


# In[54]:


s=' '


# In[58]:


seq=['a','b', 'c']


# In[59]:


print(s.join(seq))


# In[62]:


def reves(texto):
    texto2=texto.split()
    texto2.reverse()
    s=' '
    print(s.join(texto2))


# In[63]:


reves('Estoy en casa')


# In[65]:


def reves2(texto):
    print(' '.join(texto.split()[::-1]))


# In[66]:


reves2('Maestro Yoda soy')


# In[67]:


s.replace(' ','')


# In[75]:


def palindromo(s):
    s=s.replace(' ','')
    s=s.lower()
    return s==s[::-1]


# In[76]:


palindromo('ava')


# In[77]:


palindromo('solo di sol a los idolos')


# In[78]:


palindromo('Anita lava la tina')

