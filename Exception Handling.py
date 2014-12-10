__author__ = 'Luke'
class InvalidSocial(ValueError):
    pass

class Slave:
    pass

def validatess(slave_class):
    #check that employee_class.ss is valid
    #Anywhere that you find the ss is invalid raise InvalidSocial
    slave_class.ss = input("Input your social security number: ")
    try:
        area, group, serial = slave_class.ss.split("-")
        t = area, group, serial
        if len(t) == 3:
            if "666" in area:
                raise InvalidSocial
            elif "00" in area:
                raise InvalidSocial
            elif "000" in group:
                raise InvalidSocial
            elif "0000" in serial:
                raise InvalidSocial
            elif len(area) != 3:
               raise InvalidSocial
            elif len(group) != 2:
                raise InvalidSocial
            elif len(serial) != 4:
                raise InvalidSocial
            elif "078" in area + "05" in group + "1120" in serial:
                raise InvalidSocial
        else:
            print("Please retype your number correctly.")
        area = int(area)
        group = int(group)
        serial = int(serial)
        if 900<= area <= 999:
            raise InvalidSocial
    except ValueError:
        raise InvalidSocial
    exit()

def getss(slave_class):
    slave_class.ss = input("Social: ")
    try:
        validatess(slave_class)
    except InvalidSocial:
        print("Invalid SS, please try again\n")
        getss(slave_class)

peon = Slave()
getss(peon)
print(peon.ss)