
# Topic Select Control Panel

print("Hello, and welcome to the Physics Equations Calculator:")
program_state = 0

while program_state == 0:
    print("1) Electricity")
    topic_choice = str(input("Pick a Topic:"))

    if topic_choice == "1":
        print("Electricity Equations:")
        print("1) V=IR  Voltage = Current x Resistance")
        print("2) P=VI  Power   = Voltage x Current or Power = (Current x Current) x Resistance")
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

        elif topic1_equations == "2":
            print("What do you want to work out:")
            print("1) Power")
            print("2) Voltage")
            print("3) Current")
            print("4) Resistance")
            topic1_equations2 = str(input("Choose what you want to work out:"))

            if topic1_equations2 == "1":
                print("Which equation do you want to use:")
                print("1) Power = Voltage x Current")
                print("2) Power = (Current x Current) x Resistance")
                topic1_equations2_1 = str(input("Choose an equation:"))

                if topic1_equations2_1 == "1":
                    topic1_equations2_1_voltage = float(input("Enter the voltage:"))
                    topic1_equations2_1_current = float(input("Enter the current:"))
                    topic1_equations2_1_power = topic1_equations2_1_voltage*topic1_equations2_1_current
                    print("The power is", topic1_equations2_1_power)
                elif topic1_equations2_1 == "2":
                    topic1_equations2_1_current = float(input("Enter the current:"))
                    topic1_equations2_1_resistance = float(input("Enter the resistance:"))
                    topic1_equations2_1_power = topic1_equations2_1_current*topic1_equations2_1_current*topic1_equations2_1_resistance
                    print("The power is", topic1_equations2_1_power)

            elif topic1_equations2 == "2":
                topic1_equations2_power = float(input("Enter the power:"))
                topic1_equations2_current = float(input("Enter the current:"))
                topic1_equations2_voltage = topic1_equations2_power/topic1_equations2_current
                print("The voltage is", topic1_equations2_voltage)
            elif topic1_equations2 == "3":
                topic1_equations2_power = float(input("Enter the power:"))
                topic1_equations2_voltage = float(input("Enter the voltage:"))
                topic1_equations2_current = topic1_equations2_power/topic1_equations2_voltage
                print("The current is", topic1_equations2_current)
            elif topic1_equations2 == "4":
                topic1_equations2_power = float(input("Enter the power:"))
                topic1_equations2_current = float(input("Enter the current:"))
                topic1_equations2_current = topic1_equations2_current*topic1_equations2_current
                topic1_equations2_resistance = topic1_equations2_power/topic1_equations2_current
                print("The resistance is", topic1_equations2_resistance)



