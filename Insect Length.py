import InsectClass as i

def main():

    #creates instance of class
    mosquito = i.Insect('mosquito', 2, 4)
    housefly = i.Insect('housefly', 2, 4)

    mosquito.length_of_flight()
    housefly.length_of_flight()

    print(f'The {mosquito.get_name()} can fly up to', mosquito.flight_length(), 'miles')

    print(f'The {housefly.get_name()} can fly up to', housefly.flight_length(), 'miles')


main()