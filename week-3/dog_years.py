# Each year for a human is like 7.18 years for a dog
DOG_YEARS_MULTIPLIER = 7.18  

def main():
    calendar_year = float(input("Enter an age in calendar years: "))
    dog_years = calendar_year*DOG_YEARS_MULTIPLIER

    print(f"That's {dog_years} in dog years!")


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()