from datetime import datetime
from time import gmtime, strftime, strptime


class Publication:
    def __init__(self, name, text):
        self.name = name
        self.text = text


class News(Publication):
    def __init__(self, name, text, city):
        Publication.__init__(self, name, text)
        self.city = city
        self.current_date = strftime('%d/%m/%Y %H:%M', gmtime())


class Ad(Publication):
    def __init__(self, name, text, expiration_date):
        Publication.__init__(self, name, text)
        self.expiration_date = expiration_date
        self.current_date = strftime('%d/%m/%Y', gmtime())
        self.left_days = ''

    def checking_expiration_date(self):
        while True:
            try:
                self.expiration_date == strptime(self.expiration_date,
                                                 '%d/%m/%Y')
            except ValueError:
                print('Invalid date!')
                self.expiration_date = input("Please enter correct "
                                             "expiration date DD/MM/YYYY\n")
            else:
                self.expiration_date = str(self.expiration_date)
                break

    def foo_days_left(self):
        last = datetime.strptime(self.expiration_date, '%d/%m/%Y')
        now = datetime.strptime(self.current_date, '%d/%m/%Y')
        self.days_left = (last - now).days



class CarStore(Publication):
    def __init__(self, name, text):
        Publication.__init__(self, name, text)
        self.current_date = strftime('%d/%m/%Y %H:%M', gmtime())
        self.car_type = int()


class PrintIntoFile:
    def __init__(self, publication):
        self.publication = publication

    def print_publication(self):
        f = open('module_5_homework.txt', 'a')
        f.write(self.publication + '\n')


class MainClass:
    def __init__(self):
        self.record_type = int()
        self.car_type = int()

    def input_record_type(self):
        while True:
            while self.record_type not in (1, 2, 3, 4):
                try:
                    self.record_type = int(input("Please choose the type of "
                                                 "content:\n"
                                                 "1 - News\n"
                                                 "2 - Ad\n"
                                                 "3 - Car Shop\n"
                                                 "4 - For Exit\n"
                                                 "Please type here: "))
                except ValueError:
                    print("Please enter only numbers please")
                else:
                    if self.record_type == 4:
                        exit()
                    if self.record_type not in (1, 2, 3, 4):
                        print("Please make your choice 1, 2, 3, 4")
            else:

                if self.record_type == 1:
                    news = News('News -------------------------',
                                input("Please enter your News: "),
                                input("Please enter your City: "))
                    publication = f'{news.name}\n{news.text}\n{news.city}, ' \
                                  f'{str(news.current_date)}\n'
                    publication = PrintIntoFile(publication)
                    publication.print_publication()
                    self.record_type = 0

                if self.record_type == 2:
                    ad = Ad('Private Ad -------------------',
                            input("Please enter your Ad: "),
                            input("Please enter expiration date: "))
                    ad.checking_expiration_date()
                    ad.foo_days_left()
                    publication = f'{ad.name}\n{ad.text}\nActual until: ' \
                                  f'{str(ad.expiration_date)}, ' \
                                  f'{str(ad.days_left)} days left\n'
                    publication = PrintIntoFile(publication)
                    publication.print_publication()
                    self.record_type = 0

                if self.record_type == 3:
                    #def cars(self):
                    cars_shop = {'Long vehicle': ['Volvo FH long', 'Mercedes_Benz long', 'Scania long'],
                                'Cargo': ['Volvo Cargo', 'Mercedes-Benz Actros Cargo'],
                                 'SUV': ['Volvo XC90', 'BMW X5']}

                    car_type = int(input("Car types:\n" "1 - Long vehicle\n"
                                             "2 - Cargo\n"
                                             "3 - SUV\n"
                                             "4 - For Exit\n"
                                             "Please enter desired car type:"))

                    if car_type == 1:
                        longv = cars_shop['Long vehicle']
                        publication = (f'Car shop ---------------------\n'
                                        f'Available long trucks in the shop:\n'
                                        f'{str(longv)}\n')
                        publication = PrintIntoFile(publication)
                        publication.print_publication()
                        self.car_type = 0

                    elif car_type == 2:
                        cargo = cars_shop['Cargo']
                        publication = (f'Car shop ---------------------\n'
                                        f'Available cargo trucks in the shop:\n'
                                        f'{str(cargo)}\n')
                        publication = PrintIntoFile(publication)
                        publication.print_publication()
                        self.car_type = 0

                    elif car_type == 3:
                        suv = cars_shop['SUV']
                        publication = (f'Car shop ---------------------\n'
                                        f'Available SUVs in the shop:\n'
                                        f'{str(suv)}\n')
                        publication = PrintIntoFile(publication)
                        publication.print_publication()
                        self.car_type = 0

                    elif car_type == 4:
                        exit()



a = MainClass()
a.input_record_type()

