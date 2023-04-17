#Almost a Circle Project
------------------------------------------------------------------------------------------------------------------------------------------------
This project is part of the ALX curriculum, focused on learning and practicing Object Oriented Programming in Python.

The purpose of this project is to create a class hierarchy for the Rectangle and Square classes, that will eventually allow us to create a Circle class. We will use Test Driven Development (TDD) to ensure that our classes are well-designed and well-implemented.

Requirements
Python 3.4 or higher
How to Use
Clone this repository to your local machine.
```
git clone https://github.com/<username>/alx-higher_level_programming.git
```
Navigate to the 0x0C-python-almost_a_circle directory.
``
cd alx-higher_level_programming/0x0C-python-almost_a_circle
``
Run the test files to verify that the classes are working properly.
```
python3 -m unittest discover tests
```
Import the Rectangle and Square classes in your Python code.

from models.rectangle import Rectangle
from models.square import Square
File Structure
The project is organized as follows:

* models/ - Directory containing the Rectangle and Square classes.
* tests/ - Directory containing the test files for the classes.
README.md - This file.
models/
* base.py - Defines the Base class that other classes inherit from.
* __init__.py - Initializes the package.
* rectangle.py - Defines the Rectangle class, a subclass of Base.
* square.py - Defines the Square class, a subclass of Rectangle.
tests/
* __init__.py - Initializes the package.
* test_models/ - Directory containing the test files for the classes.
* test_models/test_base.py - Tests for the Base class.
* test_models/test_rectangle.py - Tests for the Rectangle class.
* test_models/test_square.py - Tests for the Square class.

#Author

This project was created by [Solomon Kassa](https://github.com/Solomonkassa) as a student at ALX.
