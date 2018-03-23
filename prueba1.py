
# coding: utf-8

# In[9]:


print('Hello World 2')


# In[10]:


print('Hola Mundo')


# In[8]:


a=2


# In[13]:


'''Esto es un comentario de multiple linea

#Esto es un comentario
a=34'''




# In[14]:


"""Esto es un comentario de doble comilla """


# In[15]:


""" Este comen ''' codigo   '''    tario  """


# In[16]:


type(a)


# In[17]:


B='Hola Mundo'


# In[18]:


type(B)


# In[19]:


type(True)


# In[20]:


type(3.14)


# In[21]:


a=23


# In[22]:


a='hello'


# In[23]:


2+3


# In[24]:


10/2


# In[25]:


7/4


# In[26]:


7//4


# In[27]:


7/2


# In[28]:


7//2


# In[29]:


7/6


# In[30]:


7//6


# In[31]:


10%3


# In[32]:


2**3


# In[33]:


4**5


# In[34]:


4**0.5


# In[36]:


(2+10)*(10+3)


# In[37]:


import math


# In[38]:


math.sin(30)


# In[39]:


a=5


# In[40]:


a+a


# In[41]:


a


# In[42]:


a+a+a


# In[43]:


a=a+a


# In[44]:


a


# In[45]:


b=40


# In[46]:


b+=10


# In[47]:


b


# In[48]:


b*=3


# In[49]:


b


# Tema STRINGS

# In[50]:


'Hello'


# In[51]:


"Hello2"


# In[53]:


"What's your name"


# In[57]:


print('Hello world1')
print('Hello world2 \n hello world3')


# In[58]:


len('Hello world')


# In[60]:


s='Hello world'


# In[62]:


s[-1]


# In[63]:


s[1:]


# In[64]:


s[:3]


# In[65]:


s[:]


# In[66]:


s[:-1]


# In[67]:


s[::1]


# In[68]:


s[::2]


# In[69]:


s[::3]


# In[70]:


s[::-1]


# In[71]:


s[0]='x'


# In[73]:


s+' concatenacion'


# In[74]:


letra='z'

letra
# In[75]:


print(letra)


# In[76]:


letra*10


# In[77]:


s


# In[78]:


s.upper()


# In[79]:


s.lower()


# In[80]:


s='Hola a varios mundos'


# In[81]:


s.split()


# In[82]:


s.split('a')


# In[83]:


print(s)


# In[87]:


print('Inserte una {} latra {} aca: '.format('letraJ', ('Letra H')))


# In[88]:


oracion='Inserte una {} latra {} aca: '.format('letraJ', ('Letra H'))


# In[89]:


print(oracion)


# In[90]:


var1='Letra Z'


# In[91]:


oracion='Inserte una {} latra {} aca: '.format('letraJ', (var1))


# In[92]:


print(oracion)


# In[98]:


var2='Inserte una letra {}'.format(' texto colado ')+' texto concatenado'


# In[99]:


print(var2)


# # LISTAS
# 

# In[100]:


mi_lista=[1,2,3]


# In[101]:


print(mi_lista)


# In[102]:


mi_lista=['A', 2, 4.14]


# In[103]:


len(mi_lista)


# In[104]:


mi_lista2=[1,2,3,4,5,'seis', 'siete']


# In[106]:


mi_lista2[4]


# mi_lista2[1:]

# In[107]:


mi_lista2[1:]


# In[108]:


mi_lista2[:3]


# In[109]:


mi_lista2 + mi_lista


# In[110]:


mi_lista2*2


# In[111]:


mi_lista3=[1,2,3,]


# In[112]:


print(mi_lista3)


# In[113]:


mi_lista3.append('agregame')


# In[114]:


print(mi_lista3)


# In[115]:


mi_lista3.pop(0)


# In[116]:


print(mi_lista3)


# In[117]:


retirado=mi_lista3.pop()


# In[118]:


print(retirado)


# In[119]:


mi_lista3[100]


# In[120]:


mi_lista4=['c','x','b', 'a', 'd', 'e']


# In[121]:


mi_lista4.reverse()


# In[122]:


print(mi_lista4)


# In[124]:


print(mi_lista4.sort())

mi_lista4.sort()
# In[127]:


print(mi_lista4)


# In[128]:


print(len(mi_lista4))


# # LISTAS ANIDADAS

# In[133]:


lista1=[1,2,3]
lista2=[4,5,6]
lista3=[7,8,9]


# In[134]:


matriz=[lista1, lista2, lista3]


# In[135]:


print(matriz)


# In[139]:


matriz[0]


# In[141]:


matriz[1][1]


# In[142]:


pr_col=[col[0] for col in matriz]


# In[143]:


pr_col


# In[144]:


lista1.shape()


# In[145]:


matriz.shape()


# # DICCIONARIOS

# In[146]:


mi_dic={'key1':'value1', 'key2':'value2'}


# In[147]:


mi_dic['key2']


# In[148]:


mi_dic={'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}


# In[149]:


mi_dic['key3']


# In[150]:


mi_dic['key3'][0]


# In[151]:


mi_dic['key3'][0].upper()


# In[152]:


mi_dic['key1']


# In[157]:


mi_dic['key1']=mi_dic['key1']*2


# In[159]:


mi_dic['key1']-=123


# In[162]:


len(mi_dic['key2'])


# In[163]:


d={}


# In[164]:


d['animal']='perro'


# In[165]:


d['numero']=42


# In[166]:


d


# In[167]:


d.keys()


# In[168]:


d.values()


# In[169]:


d.items()


# TUPLES

# In[170]:


t=(1,2,3)


# In[171]:


len(t)


# In[172]:


t=('one',2)


# In[176]:


t[-1]


# In[177]:


t.index('one')


# In[178]:


t.count('one')


# In[179]:


t[0]='cambio'


# In[180]:


print(t)


# In[181]:


t.append(4)


# SETS

# In[183]:


x=set()


# In[184]:


len(x)


# In[185]:


x.add(1)


# In[186]:


x.add(2)
x.add(3)


# In[187]:


x


# In[188]:


x.add(2)


# In[189]:


x


# In[190]:


lista1=[1,1,2,2,3,4,5,6,1,1]


# In[191]:


set(lista1)


# In[192]:


lista1


# In[193]:


len(set(lista1))


# In[194]:


len(lista1)


# BOOLEANS

# In[195]:


a=True


# In[196]:


a=true


# In[197]:


1>2


# In[198]:


1<2


# In[199]:


lista1=None


# In[200]:


print(lista1)

