
#Topic Select Control Panel

topic_choice = 0



print("Hello, and welcome to the Physics Equations Calculator.\nPlease select a topic:")
print("1) Electricity")
topic_choice = str(input("Pick a Topic:"))




if topic_choice == "1":
    print("Electricity Equations:")
    print("1) V=IR  Voltage = Current x Resistance")
    print("2) P=VI  Power   = Voltage x Current")
    print("3) Q=IT  Charge  = Current x Time")
    topic1_equations = str(input("Choose an Equation:"))

    if topic1_equations == "1":
        