dict_of_items_1={
    "env":"dev",
    "server":"aws linux1",
    "RAM":1024,
    "CPU":4,
    "Active":True

}
dict_of_items_2={
    "env":"prod",
    "server":"aws linux2",
    "RAM":10240,
    "CPU":8,
    "Active":False
}
list_of_items=[dict_of_items_1,dict_of_items_2]
for env in list_of_items:
    for key,value in env.items():
        if key == "Active" and value==True:
            print(env.values())