def userInput():
    income_coll = []
    material_coll = []
    expenditure_coll = []
    while True:
        print()
        income = input("Enter income (or done to finish ) : ")
        if income == 'done':
            break
        income_coll.append(int(income))
        material = input("Enter type of Material : ")
        material_coll.append(material)
        expenditure = input(f"Enter Expenditure on {material}: ")
        expenditure_coll.append(int(expenditure))
    
    total_income = sum(income_coll)
    total_expenditure = sum(expenditure_coll)
    print(f"Total Income {total_income}") 
    print(f"The Total Savings {total_income-total_expenditure}")
    for mat,exp in zip(material_coll,expenditure_coll):
        print(f"{mat} : {exp}")

# userInput()

