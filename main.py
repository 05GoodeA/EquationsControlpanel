
# Topic Select Control Panel

print("Hello, and welcome to the Physics Equations Calculator:")
print("1) Electricity")
topic_choice = str(input("Pick a Topic:"))

if topic_choice == "1":
    print("Electricity Equations:")
    print("1) V=IR  Voltage = Current x Resistance")
    print("2) P=VI  Power   = Voltage x Current")
    print("3) Q=IT  Charge  = Current x Time")
    topic1_equations = str(input("Choose an Equation:"))

    if topic1_equations == "1":
        print("What do you want to work out:")
        print("1) Voltage")
        print("2) Current")
        print("3) Resistance")
        topic1_equations1 = str(input("Choose what you want to work out:"))

        if topic1_equations1 == "1":
            topic1_equations1_current = int(input("Enter the current:"))
            topic1_equations1_resistance = int(input("Enter the resistance:"))
            topic1_equations1_voltage = topic1_equations1_current*topic1_equations1_resistance
            print("The voltage is:", topic1_equations1_voltage)
        elif topic1_equations1 == "2":
            topic1_equations1_resistance = int(input("Enter the resistance:"))
            topic1_equations1_voltage = int(input("Enter the voltage:"))
            topic1_equations1_current = topic1_equations1_voltage/topic1_equations1_resistance
            print("The current is", topic1_equations1_current)
        elif topic1_equations1 == "3":
            topic1_equations1_voltage = int(input("Enter the voltage:"))
            topic1_equations1_current = int(input("Enter the current:"))
            topic1_equations1_resistance = topic1_equations1_voltage/topic1_equations1_current
            print("The resistance is", topic1_equations1_resistance)