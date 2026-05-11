def main():
   sides= int(input("How many sides does your dice have? "))
   result = random.randint(1, sides)
   print(f"Your roll is {result}")



if __name__ == '__main__':
    main()