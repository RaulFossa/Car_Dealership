##Subaru CarDealer
##by raul_andres
##01.12.2016

def impreza_model():
    print("-SUBARU Impreza 2016 \n")
    print("-Price: starting at $18,395")
    print("-Symmetrical All-Wheel Drive")
    print("-37-MPG Fuel Efficiency")
    print("-5 Door Body Style")
    print("-Leather-Trimmed Upholstery")

def brz_model():
    print("-SUBARU BRZ 2016")
    print("-Price: starting at $25,395")
    print("-The ideal Sport Car")
    print("-Direct Injected Subaru Engine")
    print("-6-Speed Transmission")
    print("-Sport-Design Instrumentation")

def crosstrek_model():
    print("-SUBARU Crosstrek Hybrid 2016")
    print("-Price: starting at $30,395")
    print("-Flexible Integrated Roof Rails")
    print("-42-MPG Fuel Efficiency")
    print("-Power Moonroof")
    print("-In-Vehicle Technology")

def thank_you():
    print("Thank you for shopping us")

print("Hello and Welcome to SUBARU")
init_ans = input("Are you ready to choose your new Car? ")

## a fun game with user in case the answer is "NO"
x = 0
while init_ans.upper() == "NO":
    print("really? I am going to ask you again!") 
    x += 1
    init_ans = input("Are you ready to choose your new Car? ")

print(" ")
print("Awesome! SUBARU CarDealer offers 3 Brand New 2016 Models.")
print("Impreza, BRZ and Crosstrek \n")

car_model = input("Which car SUBARU model would you like to buy? ")

if car_model.upper() == "IMPREZA":
    print(" ")
    impreza_model() ## call function for impreza_model()
    print(" ")
    dealer_fee = float(input("Please enter the Dealer Fee for this model: $"))
    ask_tax = float(input("Please enter the tax percentage: "))
    subtotal = 18395 + dealer_fee
    tax = subtotal * ask_tax
    total_car = subtotal + tax
    print("Your Brand New SUBARU Impreza 2016 has a total of $", "%.2f" % total_car) 

if car_model.upper() == "BRZ":
    print(" ")
    brz_model() ## call function for brz_model()
    print(" ")
    dealer_fee = float(input("Please enter the Dealer Fee for this model: $"))
    ask_tax = float(input("Please enter the tax percentage: "))
    subtotal = 25395 + dealer_fee
    tax = subtotal * ask_tax
    total_car = subtotal + tax
    print("Your Brand New SUBARU BRZ Sport 2016 has a total of $", "%.2f" % total_car)

if car_model.upper() == "CROSSTREK":
    print(" ")
    crosstrek_model() ## call function for crosstrek_model()
    print(" ")
    dealer_fee = float(input("Please enter the Dealer Fee for this model: $"))
    ask_tax = float(input("Please enter the tax percentage: "))
    subtotal = 30395 + dealer_fee
    tax = subtotal * ask_tax
    total_car = subtotal + tax
    print("Your Brand New SUBARU Crosstrek Hybrid 2016 has a total of $", "%.2f" % total_car)

   




















