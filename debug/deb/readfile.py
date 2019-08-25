user_L=[]
pw_L=[]
with open('failed.txt', 'r') as f:
    datas=f.readlines()
    for data in datas:
        data=data.strip().split(' ')
        user_L.append(data[0])
        pw_L.append(data[1])
print(user_L)
print(pw_L)