# plain = "AL1"
# scr = "PUNE"
# dest = "MUMBAI"
# number = [101, 102, 103, 104, 105]
# print("The Ticket Number is:", plain + scr[0:4] + dest[0:4] + str(number[0]))
# print("The Ticket Number is:", plain + scr[0:4] + dest[0:4] + str(number[1]))
# print("The Ticket Number is:", plain + scr[0:4] + dest[0:4] + str(number[2]))
# print("The Ticket Number is:", plain + scr[0:4] + dest[0:4] + str(number[3]))
# print("The Ticket Number is:", plain + scr[0:4] + dest[0:4] + str(number[4]))

# Removes the duplicates from the given group of values to create the set
# flight_set={500,520,600,345,520,634,600,500,200,200}
# print("Remove duplicates from the set:",flight_set)


# Eliminating duplicates from a list
# passengers_list=["George", "Annie", "Jack", "Annie", "Henry", "Helen", "Maria", "George", "Jack", "Remo"]
# unique_passengers=set(passengers_list)
# print("Remove duplicates from the list:",unique_passengers)


	
# crew_details={ "Pilot":"Kumar","Co-pilot":"Raghav","Head-Strewardess":"Malini","Stewardess":"Mala" }
# print("Crew Details:",crew_details)
# print(crew_details["Pilot"])
# for key,value in crew_details.items():
#      print(key,":",value)

# Write a Python function proper_divisors(num) which returns a list of all the proper divisors of given number.
# divisor = [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
# print("The proper divisors of 220 are:", divisor)


# my_list=[0]*5
# for index in range(1,5):
# 	my_list[index]=(index-1)*10
# print(my_list)


# tuple1=(5,10,15,20,25)
# print(len(tuple1))
# tuple1[2]=100
# print(tuple1[2])
# print(tuple1[5])
# tuple1=tuple1+(8,9,"h")


# pancard_list=["AABGT6715H", "UFFAC4352T", "IFSBD9163K", "JOOEC1225H","RWXAFE187B"]
# print(pancard_list[3][6], end=" ")
# print(pancard_list[4][3:])

# message="welcome to Mysore"
# word=message[-7:]
# if(word=="Mysore"):
#     print("got it")
# else:
#     message=message[3:14]
#     print(message)

# import random
# x=10
# y=50
# print(random.randrange(x,y))


# import math
# num1=234.01
# num2=6
# num3=-27.01
# print("The smallest integer greater than or equal to num1,",num1,":",math.ceil(num1))
# print("The largest integer smaller than or equal to num1,",num1,":",math.floor(num1))
# print("The factorial of num2,",num2,":", math.factorial(num2))
# print("The absolute value of num3",num3,":",math.fabs(num3))


# import math
# num1=234.01
# num2=6
# num3=-27.01
# print("The smallest integer greater than or equal to num1,",num1,":",math.ceil(num1))
# print("The largest integer smaller than or equal to num1,",num1,":",math.floor(num1))
# print("The factorial of num2,",num2,":", math.factorial(num2))
# print("The absolute value of num3",num3,":",math.fabs(num3))


# boarding_call="Good Evening, this is the final call to AL passengers for the flight AL 466 which is planned to take off at 8.40A.M."
# if(boarding_call.startswith("Good Evening")):
#     print(boarding_call.replace("Good Evening","Good Morning"))
# if(boarding_call.find("AL"))>=0:
#     print("Welcome to Air Lines.")
# if(boarding_call.endswith("A.M.")):
#     print("Passengers are requested to have their breakfast.")
# a=boarding_call.split(" ")
# for i in a:
#     if(i.isdigit()):
#         print("Flight Number is specified to the passengers.")
# print("Total number of times flight service name is specified in the boarding call:",boarding_call.count("AL"))
# message="Thank you all..Have a nice journey!"
# print(message.upper())
# print(message.lower())


# crew_details={
#     "Pilot":"Kumar",
#     "Co-pilot":"Raghav",
#     "Head-Strewardess":"Malini",
#     "Stewardess":"Mala"
# }
# print("Before update:")
# print("Co-pilot:",crew_details.get("Co-pilot"))
# crew_details.update({"Flight Attendant":"Jane", "Co-pilot":"Henry"})
# print("\nAfter update:")
# print("Co-pilot:",crew_details.get("Co-pilot"))
# print("Flight Attendant:",crew_details["Flight Attendant"])


# crew_details={"Pilot":"Kumar","Co-pilot":"Raghav","Head-Strewardess":"Malini","Stewardess":"Mala"}
# print(crew_details.get("Pilot"))

# input_data = "Flight Savana Airlines a2134"
# # import re
# # if(re.search(r"Air","Airline")!=None):
# #     print("Pattern found")
# # else:
# #     print("Pattern not found")


# import re
# if(re.search(r"Air","airline")!=None):
#     print("Pattern found")
# else:
#     print("Pattern not found")


# import re
# flight_details="Flight Savana Airlines a2134"
# print(flight_details)
# print(re.sub(r"Flight",r"Plane",flight_details))


# song="JINGLE Bells jingle Bells Jingle All The Way"
# song.upper()
# song_words=song.split()
# count=0
# for word in song_words:
#     if(word.startswith("jingle")):
#         count=count+1
# print(count)


# sample_dict={'a':1,'b':2}
# sample_dict.update({'b':5, 'c':10 })
# print(sample_dict.get('a'),sample_dict.get('b'),sample_dict.get('c'))
 

# import re
# word="New Airlines4"
# if(re.search(r"^N",word) and re.search(r"e$",word)):
#     print(re.sub(r"New",r"Old",word))
# else:
#     print(re.sub(r"s(\d{1})",r"S\1",word))

import math
num_list=[100.5,30.465,-1.22,20.15]
num_list.insert(1, -100.5)
num_list.pop(0)
num_list.sort()
print(math.ceil(math.fabs(num_list[0])))