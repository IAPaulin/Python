import OOP.Robots.Robot as Robot
import OOP.Robots.MyError as Error


class Soldier(Robot.Robot):
    __life = True

    def __init__(self, name, type, mass, year, element, weapon_category):
        try:
            super().__init__(name, type, mass, year, element)
            self.__weapon_category = weapon_category

            if self.__weapon_category == 1 and self.get_mass > 500:
                raise Error.MyError('Error')
            elif self.__weapon_category == 2 and (self.get_mass < 500 or self.get_mass > 5000):
                raise Error.MyError('Error')
            elif self.__weapon_category == 3 and self.get_mass < 5000:
                raise Error.MyError('Error')

        except Error.MyError as err:
            self.__life = False
            print(err, ' robot creates, but weapon does not install')

    @property
    def get_weapon_category(self):
        return self.__weapon_category

    def pasport(self):
        if not self.__life:
            return None
        super().pasport()
        print('weapon category = ', self.__weapon_category)
