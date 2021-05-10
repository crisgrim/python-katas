
def calculate_benefits(capital, percentage, years):
    benefit_per_year = (int(capital) * int(percentage)) / 100
    return round(benefit_per_year * int(years), 2)


capital = input("Capital to invest: ")
percentage = input("Percentage annual: ")
years = input("Years: ")

profits = calculate_benefits(capital, percentage, years)

print("Your profits will be: " + str(profits))
