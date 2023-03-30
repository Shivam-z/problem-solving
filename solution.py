#creating candidate list
#candidates=['pratik','raj','ram','rohan','ravi','sonal','shivam','gopal','mohan','umesh']   #len=10


#creating locations list
locations=['Bangalore','chennai','mumbai','kolkata']   #len=4

# Match candidate to their preferred locations
#For this I am creating a dictionary and map candidates with their preferred locations


print("Choose the preferred locations from the list")

print(locations)


#n=input("Enter length")
d={input("Enter Candidate Name: "):input("Enter preferred location:") for x in range(3)}

print("Final output")

for candidate in d:
    if(d[candidate] in locations):
        print(candidate , d[candidate])
