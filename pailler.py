from phe import paillier
import math


################################

def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m

################################

def toString(a):
  l=[]
  m=""
  for i in a:
    b=0
    c=0
    k=int(math.log10(i))+1
    for j in range(k):
      b=((i%10)*(2**j))   
      i=i//10
      c=c+b
    l.append(c)
  for x in l:
    m=m+chr(x)
  return m

#######################################
############ Génération des clés ######

public_key, private_key = paillier.generate_paillier_keypair()

#######################################

def CryptHomomr(public_cle,message):
    m=toBinary(message)
    # print(m)
    cipher_text=[]
    for lt in m:
        cipher_text.append(public_cle.encrypt(lt))
    t=[]
    for en in cipher_text:
      # t.append(str(en.ciphertext()))
      t.append((en.ciphertext()))
    text_crypté=str(t)
    return text_crypté



#######################################

def DecryptHomomr(public_key,private_cle,message_chiffré):
    mss= message_chiffré.strip('][').split(', ')
    text=[]
    for lt in mss:
        paillier.EncryptedNumber(public_key,lt)
        text.append(private_cle.decrypt(paillier.EncryptedNumber(public_key,int(lt))))
    m=toString(text)
    return m

#######################################

##### Déroulement sur un exemple ######


msg1="hello"
msg2= "1405.45"

m1=CryptHomomr(public_key,msg1)
print(m1)
print(type(m1))

m2=DecryptHomomr(public_key,private_key,m1)
print(m2)
print(type(m2))


# l=[]

# for i in m1:
  # l.append(i.ciphertext())
  # print((str(i.ciphertext()), i.exponent))
  # t=(str(i.ciphertext()))
  # print(t)
  # c=paillier.EncryptedNumber(public_key,t)
  # print(c)




  # enc_with_pub_key['enc_value']

# print(l)
# mstr=str(m1)


# c1= DecryptHomomr(private_key,m1)
# c1= DecryptHomomr(private_key,l)
# print(c1)



# print(m1)

# print(type(m1))
# print(c1)


# m2=CryptHomomr(public_key,msg2)
# c2= DecryptHomomr(private_key,m2)
# print(m2)
# print(c2)

