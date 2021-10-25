#!/usr/bin/env python
# coding: utf-8

# # Aula 4 25-10

# ## Exercício 1

# fração própria - denominador maior que numerador <p>
# fração imprória - o contrário

# **Frações**

# **Definição de modelo**

# Podemos representar em tuplos, primeiro elemento numerador e segundo denominador <p>
# Tuplo = (numerador,denominador)<p>
# 3/4 == (3,4)

# ### Construtor

# In[58]:


def criarfracao(numerador, denominador):
    return (numerador, denominador)


# In[59]:


def verFracao(f):
    print(str(f[0])+"/"+str(f[1]))


# In[60]:


f1 = criarfracao(2,7)
print(f1)
verFracao(f1)


# In[61]:


verFracao(criarfracao(15,20))


# ### Simplificação de frações

# In[62]:


def mdc(a,b):
    if a<b:
        return mdc(b,a)
    elif a%b == 0:
            return b
    else:
            return mdc(a, a%b)
    


# In[63]:


mdc(14,49)
    


# In[64]:


def simplificarFracao(f):
    num, denom = f
    a = mdc(num, denom)
    return (num/a, denom/a)


# In[65]:


simplificarFracao((14,49))


# In[75]:


#o resultado é a fração simplicada de f1+f2
def somaFrac(f1,f2):
    n1, d1 = f1
    n2, d2 = f2
    return simplificarFracao((n1*d2+n2*d1 ,d1*d2))

somaFrac((3,5), (2,7))


# In[85]:


listaFrac = [(1,3), (1,4), (1,2), (1,5), (3,8), (23,39)]
res = (0,1)
for elem in listaFrac:
    res = somaFrac( res, elem)
verFracao(res)


# In[87]:


listaInt = [1,2,3,4,5,6,7,8,9,10]
listaRes = []
for elem in listaInt:
    listaRes.append(elem *2)
print (listaRes)


# Subtração 
# Multiplicação 
# Divisão
# Aplicação
# 0 - sair <p>
# 1 - criarfracao <p>
# 2 - simplificarfracao <p>
# 3 - somar <p>
# 4 - subtrair <p>
# 5 - multiplicar <p>
# 6 - dividir <p>
# 7 - gerar lista de n frações <p>
# 8 - somarlista <p>
# 9 - maiorfracao <p>

# In[ ]:




