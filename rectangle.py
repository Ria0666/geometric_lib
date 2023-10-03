def area(a, b):
    '''
    Возвращает площадь прямоугольника с указанными сторонами

        Параметры:
            a (int/float): длина первой стороны прямоугольника / длина прямоугольника
            b (int/float): длина второй стороны прямоугольника / ширина прямоугольника

        Возвращаемое значение:
            area (int/float): площадь прямоугольника со сторонами a и b
'''
    return a * b

def perimeter(a, b):
    '''
    Возвращает периметр прямоугольника с указанными сторонами

        Параметры:
            a (int/float): длина первой стороны прямоугольника / длина прямоугольника
            b (int/float): длина второй стороны прямоугольника / ширина прямоугольника

        Возвращаемое значение:
            perimeter (int/float): периметр прямоугольника со сторонами a и b
'''
    return 2*(a + b)
