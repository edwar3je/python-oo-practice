"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """initializes the start value based on user input and a counter value at -1"""
        self.start = start
        self.counter = -1
    
    def generate(self):
        """adds 1 to self.counter each time it is executed and returns the sum of
        self.start + self.counter"""
        self.counter += 1
        return self.start + self.counter
    
    def __repr__(self):
        if self.counter <= 0:
            return f'<Serial Generator start = {self.start} next = {self.start + 1}'
        return f'<Serial Generator start = {self.start + self.counter} next = {self.start + self.counter + 1}'
    
    def reset(self):
        """resets self.counter to -1"""
        self.counter = -1