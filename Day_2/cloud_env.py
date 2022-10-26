cloud_env=input("Enter your cloud environment : \n")
service = input("Enter your service : \n")
if cloud_env.lower() =="aws":
    print("Yor are using AWS: ")
    if service == "ec2":
        print("Your are using AWS with service ec2")
    else:
        print("You are using aws environment but not ec2 service")
elif cloud_env.lower() == "azure":
    print("You are using azure")
elif cloud_env.lower() == "gcp": 
    print("You are using GCP")
else:
    print("Your are not using any cloud service")

    
