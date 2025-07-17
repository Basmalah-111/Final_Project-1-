from animals import Dog,Cat,Cow

while True:

    def main():

            choice = input('Choose one of the following animals (dog,cat,cow) : ')
            dog=Dog()
            cat=Cat()
            cow=Cow()

            if choice == 'dog':
                return dog.make_sound() ,dog.describe()
            elif choice =='cat':
                return cat.make_sound(), cat.describe()
            elif choice =='cow':
                return cow.make_sound(),cow.describe()
            else:
                print('This animal is not on the list')

    if __name__ == "__main__":
        main()
