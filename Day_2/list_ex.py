from re import A


list_of_services = list(["Aws","Azure","GCP"])
list_of_services = ["dev","stg","prd"]
list_of_services.append("client")

for i in list_of_services:
    print("Deploying to")
    print(i)
#print(dir(list_of_services))
list_of_services.insert(0,"testing")
#print(list_of_services.sort.__doc__)
a=2
print(dir(a))
print(a.denominator.__doc__)
