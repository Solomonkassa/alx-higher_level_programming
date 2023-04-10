#!/usr/bin/python3
"""Module inherits from int
"""


class MyInt(int):
    """Inherits from int but inverting == and !=
    """

    def __init__(self, num):
        """Initializes MyInt
        Args:
            num (int): int that's passed through
        """

        self.num = num

    def __eq__(self, value):
        """Inverts == to !=
            Returns:
                bool: true or false
        """

        if not isinstance(value, MyInt):
            return False

    def __ne__(self, value):
        """Inverts != to ==
            Returns:
                bool: true or false
        """

        if not isinstance(value, MyInt):
            return True
