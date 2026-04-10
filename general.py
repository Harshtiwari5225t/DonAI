# st="abaabbaaabbbaaaabbbb"
# lst=[]
# i=0
# j=0
# while(i<len(st)-1):
#     if st[i]=="b"and st[i+1]=="a":
#         lst.append(st[j:i+1])
#         j=i+1
#     i+=1
# lst.append(st[j:])
# print(lst)


l=[7,"$",5,9,".",1]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if type(l[i])==int and type(l[j])==int:
            if l[i]>l[j]:
                temp=l[i]
                l[i]=l[j]
                l[j]=temp

print(l)

l=[7,"$",5,9,".",1]
num=sorted([x for x in l if isinstance(x,int)])
print(num)


# # print("Hello World!!!")

# data={
# "Name":["harsh","nanu","kshitij"],
# "Age":[21,20,20],
# }


# df=pd.read_csv("data.csv")
# print(df.head())

# import browser