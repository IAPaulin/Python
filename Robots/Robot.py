class Robot:

    def __init__(self, name, type, mass, year, element):
        self.__name = name
        self.__type = type
        self.__mass = mass
        self.__year = year
        self.__element = element

    @property
    def get_name(self):
        return self.__name

    @property
    def get_type(self):
        return self.__type

    @property
    def get_mass(self):
        return self.__mass

    @property
    def get_year(self):
        return self.__year

    @property
    def get_element(self):
        return self.__element

    def pasport(self):
        print('name = ', self.__name)
        print('type = ', self.__type)
        print('mass = ', self.__mass)
        print('year release = ', self.__year)

        print('way to travel = ', end=' ')
        for i in range(len(self.__element)):
            if i == (len(self.__element) - 1):
                print(self.__element[i], end='.')
                print()
            else:
                print(self.__element[i], end=',')
