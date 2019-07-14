#All Rights Reserved to Ahmed Ezzat -> https://fb.com/ezzat001
import random
print('All Rights Reserved to Ahmed Ezzat -> https://fb.com/ezzat001')
print("[1] Gmail Mail List")
print("[2] Yahoo Mail List")
print("[3] Hotmail List")
type = int(input("Enter The Number : "))
nums = int(input("Do You want it example@email.com or example23@email.com Choose 1 or 2 :"))
amount = int(input("How Many E-Mails you Want : "))
name_listfile = open('name_list.txt','r')

content = name_listfile.readlines()
name_list1 = []
name_list2 = []
last_name_list = []
_last_name_list = []
for i in content:
    i = i.replace('\n', '')
    name_list1.append(i)
    name_list2.append(i)

random.shuffle(name_list1)
random.shuffle(name_list2)

for i in range(len(name_list1)):
    first_name = name_list1[i]
    last_name = name_list2[i]
    name = (first_name+''+last_name).lower()
    _name = (first_name+'_'+last_name).lower()
    last_name_list.append(name)
    _last_name_list.append(_name)
c = 0
if type == 1: #Gmail
    x = random.randint(1,2)
    if x == 1:
        if nums == 1:
            for i in last_name_list:
                c+=1
                i = i+'@gmail.com'
                print(i)
                if c == amount:
                    break
        elif nums ==2:
            for i in last_name_list:
                c+=1
                r = random.randint(0,999)
                i = i+str(r)+'@gmail.com'
                print(i)
                if c == amount:
                    break

    else:
        if nums == 1:
            for i in _last_name_list:
                c+=1
                i = i+'@gmail.com'
                print(i)
                if c == amount:
                    break
        if nums == 2:
            for i in _last_name_list:
                c+=1
                r = random.randint(0,999)
                i = i+str(r)+'@gmail.com'
                print(i)
                if c == amount:
                    break
elif type == 2: #Yahoo
    x = random.randint(1,2)
    if x == 1:
        if nums == 1:
            for i in _last_name_list:
                c+=1
                i = i+'@yahoo.com'
                print(i)
                if c == amount:
                    break
        elif nums ==2 :
            for i in _last_name_list:
                c+=1
                r = random.randint(0,999)
                i = i+str(r)+'@yahoo.com'
                print(i)
                if c == amount:
                    break
            
    else:
        if nums == 1:
            for i in last_name_list:
                c+=1
                i = i+'@yahoo.com'
                print(i)
                if c == amount:
                    break
        elif nums == 2:
            for i in last_name_list:
                c+=1
                r = random.randint(0,999)
                i = i+str(r)+'@yahoo.com'
                print(i)
                if c == amount:
                    break
elif type == 3: #Hotmail
    x = random.randint(1,2)
    if x == 1:
        if nums ==1:
            for i in _last_name_list:
                c+=1
                i = i+'@hotmail.com'
                print(i)
                if c == amount:
                    break
        elif nums ==2:
            for i in _last_name_list:
                c+=1
                r = random.randint(0,999)
                i = i+str(r)+'@hotmail.com'
                print(i)
                if c == amount:
                    break

    else:
        if nums ==1:
            for i in last_name_list:
                c+=1
                i = i+'@hotmail.com'
                print(i)
                if c == amount:
                    break
        elif nums ==2:
            for i in last_name_list:
                c+=1
                r = random.randint(0,999)
                i = i+str(r)+'@hotmail.com'
                print(i)
                if c == amount:
                    break
else:
    print("Please Choose Between 1 , 2 and 3")

