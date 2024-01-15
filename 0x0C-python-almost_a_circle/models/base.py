#!/usr/bin/python3
"""
Class Module
"""
import json
import csv


class Base:
    """
    base of all other classes in this project

    Attributes:
        _nb_objects: number of objects
        id: id of object
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initiation method
        args:
            id: id of object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def integer_check(self, name, value):
        """check if value is an integer"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be > 0'.format(name))

    def integer_check2(self, name, value):
        """check if value is an integer"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value < 0:
            raise ValueError('{} must be >= 0'.format(name))

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string
        args:
            list_dictionaries: list of dictionaries
        return:
            return seralized list or empty list
        """
        return json.dumps(list_dictionaries or [])

    @staticmethod
    def from_json_string(json_string):
        """json to string static method
        args:
            json_string: json object string type
        return:
            list of json strings
        """
        if json_string:
            return json.loads(json_string)
        return []

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string to a file
        args:
            list_objs: list of objects
        return:
            na
        """
        if list_objs:
            j = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        else:
            j = '[]'
        with open(cls.__name__ + '.json', 'w') as f:
            f.write(j)

    @classmethod
    def create(cls, **dictionary):
        """return instance with all attributes set
        args:
            dictionary: double pointer
        return:
            instance with set attribute
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''Returns a list of instances
        return:
            list of instance json string
        '''
        try:
            filename = cls.__name__ + '.json'
            with open(filename, mode='r') as f:
                data = cls.from_json_string(f.read())
            return [cls.create(**x) for x in data]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        write to csv file
        Args:
            list_objs
        """
        filename = cls.__name__ + '.csv'
        with open(filename, 'w')as csv_file:
            if list_objs is None or list_objs == []:
                csv_file.write("[]")

            else:
                if cls.__name__ == "Rectangle":
                    fieldname = ["id", "width", "height", "x", "y"]
                else:
                    fieldname = ["id", "size", "x", "y"]
                    csv_writer = csv.Dictwriter(csv_file, fieldnames=fieldname)

                    for obj in list_objs:
                        csv_writer.writerow(obj.to_dictionary)

    @classmethod
    def load_from_file_csv(cls):
        """
        read from csv
        Args
        class
        """
        filename = cls.__name__ + '.csv'
        with open(filename, 'r')as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for line in csv_reader:
                print(line)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        opens a window and draws all the Rectangles and Squares

        args:
        list_rectangle: rectangle instances
        list_squares:square instances
        """
        window = turtle.Screen()
        pen = turtle.pen()
        figures = list_rectangles + list_squares

        for figure in figures:
            pen.up()
            pen.goto(figure.x, figure.y)
            pen.down()
            pen.foward(figure.width)
            pen.right(90)
            pen.foward(figure.height)
            pen.right(90)
            pen.foward(figure.width)
            pen.right(90)
            pen.foward(figure.height)
            pen.right(90)
        widow.exitonclick()
