set_of_num1={1,1,1,2,3,4,5,8,9,45,34,75}
set_of_num2={1,1,10,21,3,34,5,8,9,45,34,75}
print(set_of_num1.intersection(set_of_num2))
print(set_of_num1.union(set_of_num2))

list_of_env=["qa","dev","prod","uat","qa","dev"]
print(list_of_env)
list_of_env=list(set(list_of_env))
print(list_of_env)