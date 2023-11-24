import random

class Friend:
    def __init__(self, name):
        self.name = name

    def hang_out_with(self, student):
        print(f"{self.name} пришел в гости {student.name}у")
        student.happines += 3  
        student.progress += 2  

    def go_to_the_party(self, student):
        print(f"{self.name} тусуется у {student.name}а")
        student.happines += 5
        student.progress -= 5

    def eat_lunch(self, student):
        print(f"{self.name} поел с {student.name}ом")
        student.money -= 5
        student.happines += 2


class Student:
    def __init__(self, name):
        self.name = name
        self.happines = 50
        self.progress = 9
        self.alive = True
        self.money = 15

    def oplata_xati(self):
        self.happines -= 2
        self.money -= 7

    def eat_lunch(self, friend):
        friend.eat_lunch(self)

    def go_to_the_party(self, friend):
        friend.go_to_the_party(self)

    def hang_out_with_friend(self, friend):
        friend.hang_out_with(self)

    def family(self):
        print("Встреча с семьей")
        self.happines += 5
        self.progress += 3
        self.money += 5

    def study(self):
        print("Время учится")
        self.progress += 12
        self.happines -= 3

    def chill(self):
        if self.money >= 10:
            print("Отдых")
            self.happines += 5
            self.progress -= 1
            self.money -= 10
        else:
            print("Не достаточно денег для отдыха время работать")
            self.work()

    def to_sleep(self):
        print("Время спать")
        self.happines += 2
        self.progress -= 1

    def work(self):
        print("Время работать")
        self.money += 20
        self.progress -= 1

    def is_alive(self):
        if self.progress < -0.5:
            print("Выгнали")
            self.alive = False
        elif self.happines <= 0:
            print("Грустно")
            self.alive = False
        elif self.money < -10:
            print("Нечем платить за квартиру")
            self.alive = False
        elif self.progress > 450:
            print("Прошел с трудом...")
            self.alive = False

    def end_of_day(self):
        print(f"Щастье = {self.happines}")
        print(f"Прогресс = {round(self.progress, 2)}")
        print(f"Деньги = {self.money}")

    def __iter__(self):
        return self

    def __next__(self):
        if not self.alive:
            raise StopIteration

        live_rand = random.randint(1, 9)

        if live_rand == 1:
            self.study()
        elif live_rand == 2:
            self.to_sleep()
        elif live_rand == 3:
            self.chill()
        elif live_rand == 4:
            self.work()
        elif live_rand == 5:
            self.family()
        elif live_rand == 6:
            kostya.hang_out_with(slavic)
        elif live_rand == 7:
            kostya.go_to_the_party(slavic)
        elif live_rand == 8:
            kostya.eat_lunch(slavic)


        elif live_rand == 9:
            self.oplata_xati()

        self.end_of_day()
        self.is_alive()

        if not self.alive:
            raise StopIteration

if __name__ == "__main__":
    kostya = Friend("Костян")
    slavic = Student("Славик")
    slavic.hang_out_with_friend(kostya)

    for _ in slavic:
        pass
