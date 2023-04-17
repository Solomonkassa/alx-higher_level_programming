#!/usr/bin/python3
"""Module containing the Super class for Square and Rectangle Classes"""
import json
import csv


class Base:
    """Base class needed by the Square
        class and the Rectangle Class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the Base class attributes
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def type_validator(attribute, value):
        """Validates the inputs passed"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(attribute))
        if attribute == "x" or attribute == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(attribute))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(attribute))

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of list_dictionaries
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return (json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation 'json_string'
        """

        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string representation of list_objs to a file
        """

        fn = cls.__name__
        filename = fn + ".json"
        new_list = []
        with open(filename, mode='w', encoding='utf-8') as f:
            if list_objs is None:
                f.write(cls.to_json_string([]))
            else:
                for obj in list_objs:
                    new_list.append(obj.to_dictionary())
                f.write(cls.to_json_string(new_list))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set
        """

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        import os

        instance_list = []
        fn = cls.__name__
        filename = fn + ".json"
        exists = os.path.isfile(filename)

        if not exists:
            return instance_list

        with open(filename, mode='r', encoding='utf-8') as f:
            for line in f:
                obj = cls.from_json_string(line)
                for i in obj:
                    instance_list.append(cls.create(**i))
        return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes a list of Rectangles/Squares in csv"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            if cls.__name__ is "Rectangle":
                for obj in list_objs:
                    csv_writer.writerow([obj.id, obj.width, obj.height,
                                         obj.x, obj.y])
            elif cls.__name__ is "Square":
                for obj in list_objs:
                    csv_writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """deserializes a list of Rectangles/Squares in csv"""
        filename = cls.__name__ + ".csv"
        l_list = []
        try:
            with open(filename, 'r') as csvfile:
                csv_reader = csv.reader(csvfile)
                for args in csv_reader:
                    if cls.__name__ is "Rectangle":
                        dictionary = {"id": int(args[0]),
                                      "width": int(args[1]),
                                      "height": int(args[2]),
                                      "x": int(args[3]),
                                      "y": int(args[4])}
                    elif cls.__name__ is "Square":
                        dictionary = {"id": int(args[0]), "size": int(args[1]),
                                      "x": int(args[2]), "y": int(args[3])}
                    obj = cls.create(**dictionary)
                    l_list.append(obj)
        except Exception as ex:
            pass
        return l_list
