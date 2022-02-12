""" Definition of a ringbuffer.
    The buffer can be iterated over, just like a list
    but if the last element is overstepped, the cicle
    restarts with the first element in the list.

Created 29.08.2021
@author Max Weise
"""


class CustomBaseException(Exception):
    """ Baseclass to unify the definition of all other custom exceptions."""

    def __init__(self, message: str = None) -> None:
        self.message = message

    def __str__(self) -> str:
        return f'E ({type(self)}): {self.message}'


class BufferOverflowException(CustomBaseException):
    """ This Exception is raised when the ringbuffer is full
        and another elements is to be inserted in the buffer.
    """
    pass


class BufferEmptyException(CustomBaseException):
    """ This Exception is raised when the ringbuffer is empty
        and another elements is to be removed from the buffer.
    """
    pass


class IndexOutOfBoundsException(CustomBaseException):
    """ This Exception is raised when a specified index is not
        included in the buffer.
    """
    pass


class InputError(CustomBaseException):
    """ This Exception will be thrown if the input given to
        a method does not fulfill its requirements.
    """
    pass


class Ringbuffer:
    """ Implementation of a circular buffer.
        The size of the step per iteration can be customized.
        It is not intended for the elements to be swapped out mid-iteration.

        Params:
            size (int): Fixed size of the buffer
    """

    __elements: list[object]
    __head: object
    __tail: object
    __size: int
    __pointer: int
    __not_supported = [list, tuple, dict]

    def __init__(self, size: int) -> None:
        """ Initialize a buffer by giving it a size."""
        self.__elements = []
        self.__head = None
        self.__tail = None
        self.__size = size
        self.__pointer = 0

    # Getter | Setter
    def get_pointer(self) -> int:
        """ Returns the zero-based index of the current pointer."""
        return self.__pointer

    def set_pointer(self, pointer: int) -> None:
        """ Utility method. Set the pointer to a specified index."""
        self.__pointer = pointer

    def get_elements(self) -> list[object]:
        """ Returns the list of all current elements."""
        return self.__elements

    def set_elements(self, elements: list[object]) -> None:
        """ Utility method. Sets elements to a specified list. Should not be used to fill the buffer."""
        self.__elements = elements

    def get_head(self) -> object:
        """ Returns the head of the buffer."""
        return self.__head

    def set_head(self, head: object) -> None:
        """ Sets the head of the buffer."""
        self.__head = head

    def get_tail(self) -> object:
        """ Returns the tail of the buffer."""
        return self.__tail

    def set_tail(self, tail: object) -> None:
        """ Sets the tail of the buffer."""
        self.__tail = tail

    def get_size(self) -> int:
        """ Returns the size of the buffer."""
        return self.__size

    def set_size(self, size: int) -> None:
        """ Utility method. Sets the size of the buffer."""
        self.__size = size

    def get_element(self) -> object:
        """ Returns the element under the pointer."""
        return self.get_elements()[self.get_pointer()]

    # Methods
    def enqueue(self, element: object) -> None:
        """ Add an element to the buffer. If the buffer is already full,
            an exception gets raised.

            Raises:
                BufferOverflowException: Will be thrown, when the inserted
                                         element exceeds the size of the buffer.
        """
        # Check for unsupported types
        if type(element) in self.__not_supported:
            raise InputError(f'The type of {element} is not supported.')

        current_buffer = self.get_elements()

        if len(current_buffer) == self.get_size():
            raise BufferOverflowException('Cannot insert into full buffer')

        if len(current_buffer) == 0:
            current_buffer.append(element)
            self.set_head(element)
            self.set_tail(element)
        else:
            current_buffer.append(element)
            self.set_tail(element)

    def dequeue(self, index: int = None) -> object:
        """ Remove and return the element at the specified index from the buffer.
            If no index is specified remove the last element from the buffer.
            If the buffer is empty or the index is not in
            the buffer, an exception is raised.

            Raises:
                IndexOutOfBoundsException: When the given index is not included
                                           in the buffer (either too high or too
                                           low).
                BufferEmptyException:      When the buffer is empty but the user
                                           wants to remove another item

        """
        current_buffer = self.get_elements()
        output = None

        if index and not (0 <= index < len(current_buffer)):
            raise IndexOutOfBoundsException(f'Cannot reach index {index}')

        try:
            if index is None:
                output = current_buffer.pop()
            else:
                output = current_buffer.pop(index)

            if len(current_buffer) > 0:
                self.set_tail(current_buffer[-1])
            else:
                self.set_head(None)
                self.set_tail(None)
        except IndexError:
            raise BufferEmptyException('Cannot pop from an empty buffer!')
        except Exception as e:
            print(e)

        return output

    def __increase_pointer(self) -> None:
        """ Increase the position of the pointer by one."""
        if self.get_element() is self.get_tail():
            self.set_pointer(0)
        else:
            self.set_pointer(self.get_pointer() + 1)

    def step(self, size_of_step: int = 1) -> None:
        """ Increase the position of the pointer by the specified amount.
            size_of_step should be an integer greater than 0.
            If this is not the case, an exception is thrown.

            Raises:
                InputError: When the input does not match the specified
                            requirements of the method.
        """
        if type(size_of_step) is not int:
            raise InputError('The input must be of type integer!')

        if size_of_step < 1:
            raise InputError('The step must have a value of at least 1!')

        for _ in range(size_of_step):
            self.__increase_pointer()

    def __str__(self) -> str:
        elements = self.get_elements()
        pointer = self.get_pointer()
        head = self.get_head()
        tail = self.get_tail()

        return f'{elements} | {pointer} | ({head} / {tail})'


# Testrun for the buffer
def test():
    test_elements = [1, 2, 3]
    buffer = Ringbuffer(len(test_elements))

    # Test for functionality
    for ele in test_elements:
        buffer.enqueue(ele)
        print(buffer)

    try:
        buffer.enqueue(1)
    except Exception as e:
        print(e)

    for _ in range(3):
        buffer.step()
        print(buffer)

    while len(buffer.get_elements()) > 0:
        a = buffer.dequeue()
        print(f'Current buffer: {buffer}\nElement: {a}')


if __name__ == '__main__':
    test()
