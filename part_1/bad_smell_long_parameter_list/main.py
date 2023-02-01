# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self, status: str, speed: int=1):
        self.speed = speed
        self.status = status
        self.coord_x = 0
        self.coord_y = 0


    def get_speed(self):
        if self.status == 'is_fly':
            return self.speed * 1.2
        else:
            return self.get_speed() * 0.5


    def move(self, direction):
        dir_list = [('UP', 0, 1), ('DOWN', 0, -1), ('LEFT', -1, 0), ('RIGHT', 1, 0)]
        for item in dir_list:
            dir, d_x, d_y = item
            if dir == direction:
                self.coord_x += self.get_speed() * d_x
                self.coord_y += self.get_speed() * d_y
                break
        field.set_unit(x=self.coord_x, y=self.coord_y, unit=self)


    """def move(self, field, x_coord, y_coord, direction, is_fly, crawl, speed = 1):

        if is_fly and crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_fly:
            speed *= 1.2
            if direction == 'UP':
                new_y = y_coord + speed
                new_x = x_coord
            elif direction == 'DOWN':
                new_y = y_coord - speed
                new_x = x_coord
            elif direction == 'LEFT':
                new_y = y_coord
                new_x = x_coord - speed
            elif direction == 'RIGTH':
                new_y = y_coord
                new_x = x_coord + speed
        if crawl:
            speed *= 0.5
            if direction == 'UP':
                new_y = y_coord + speed
                new_x = x_coord
            elif direction == 'DOWN':
                new_y = y_coord - speed
                new_x = x_coord
            elif direction == 'LEFT':
                new_y = y_coord
                new_x = x_coord - speed
            elif direction == 'RIGTH':
                new_y = y_coord
                new_x = x_coord + speed

            field.set_unit(x=new_x, y=new_y, unit=self)
"""

