#coding=UTF8
list_data = ["aa",'bbb','cc','dd']

#遍历list
for i,v in enumerate(list_data):
    print  i,v

print "-----------------------操作list列表------------------------------------"

list_data.append("ee");print list_data #添加元素
list_data.__delitem__(2);print list_data #删除元素
list_data[2] = "tt" ;print list_data #修改元素
print list_data[2]; #查看元素
print list_data[1:-1]

list_data.reverse();print list_data
print list_data.count("bb")
print list_data.__len__()
print list_data.__sizeof__()
print list_data.__class__
print list_data.__doc__
print list_data.__str__()