#!/usr/bin/python3
"""Contains  function that appends a string
at the end of a text file (UTF8) and
returns the number of characters added
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text
        file (UTF8) and returns the number of characters added
        Args:
            filename (str): name of the file
            text (str): what to write
        Returns:
            int: number of characters written
    """
    with open(filename, "a", encoding="utf-8") as f:
        count = f.write(text)

    return count


if __name__ == "__main__":
    nb_characters_added = append_write(
        "file_append.txt", "This School is so cool!\n")
    print(nb_characters_added)
