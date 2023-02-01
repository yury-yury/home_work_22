# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:

    def move_unit(self, field, coord_x, coord_y, direction: str, fly: bool, creep: bool, speed: int = 1):
        """Функция реализует перемещение юнита по полю. в качестве параметров принимает текущие координаты юнита, 
        направление его движения, состояние не летит ли он, состояние не крадется ли он и базовый параметр скорости с 
        которым двигается юнит
        """
        if fly and creep:
            raise ValueError('Рожденный ползать летать не должен!')

        if fly:
            speed *= 1.2
            if direction == 'UP':
                coord_y += speed
            elif direction == 'DOWN':
                coord_y -= speed
            elif direction == 'LEFT':
                coord_x -= speed
            elif direction == 'RIGHT':
                coord_x += speed
        if creep:
            speed *= 0.5
            if direction == 'UP':
                coord_y += speed
            elif direction == 'DOWN':
                coord_y -= speed
            elif direction == 'LEFT':
                coord_x -= speed
            elif direction == 'RIGHT':
                coord_x += speed

            field.set_unit(x=coord_x, y=coord_y, unit=self)
