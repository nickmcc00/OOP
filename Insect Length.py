import InsectClass as i

def main():

    len_flight = i.Insect()

    print('This is the length of flight:', len_flight.flight_length())


    for count in range(1, 10):
        len_flight.length_of_flight()

    print('This is the length of flight:', len_flight.flight_length())


main()