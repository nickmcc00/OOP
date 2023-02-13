import InsectClass as i

def main():

    mosquito = i.Insect()
    housefly = i.Insect()

    mosquito.length_of_flight()
    housefly.length_of_flight()

    print('The mosquito can fly up to:', mosquito.flight_length())

    print('The housefly can fly up to:', housefly.flight_length())


main()