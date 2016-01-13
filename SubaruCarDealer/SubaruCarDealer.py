##Subaru CarDealer
##by raul_andres
##01.12.2016

def impreza_model():
    print("SUBARU Impreza 2016")
    print("Price: starting at $18,295")
    print("Symmetrical All-Wheel Drive")
    print("37-MPG Fuel Efficiency")
    print("5 Door Body Style")
    print("Leather-Trimmed Upholstery")

def brz_model():
    print("SUBARU BRZ 2016")
    print("Price: starting at $25,395")
    print("The ideal Sport Car")
    print("Direct Injected Subaru Engine")
    print("6-Speed Transmission")
    print("Sport-Design Instrumentation")

def crosstrek_model():
    print("SUBARU Crosstrek 2016")
    print("Price: starting at $30,395")
    print("Flexible Integrated Roof Rails")
    print("42-MPG Fuel Efficiency")
    print("Power Moonroof")
    print("In-Vehicle Technology")

print("Hello and Welcome to SUBARU")
init_ans = input("Are you ready to choose your new Car? ")

x = 0
while init_ans.upper() == "NO":
    print("really? I am going to ask you again!") # a fun game with user in case the answer is "NO"
    x += 1
    init_ans = input("Are you ready to choose your new Car? ")



