# Band name generator
# 
# ## based on city and pet name
# * take input from user asking city and pet name
# * concat the user input
# * print band name

greeting = 'Welcome to the band name generator.'
print(greeting)

city = input("Where were you born? \n")
pet = input("What is your pet name? \n")
band_name = (city +" "+ pet)
print('Your band name could be' +' '+band_name)

