class Jar:
    def __init__(self, capacity=12):  # you can change the parameter
        self.capacity = capacity  # make variable private, so they can't get accessed from outside the class
        self.size = 0  # initially there are no cookies in the jar

    def __str__(self):  # method which is called with 'print'
        # check whether after all deposits and withdrawals size is still not greater than capacity
        if self.size <= self.capacity:
            return '🍪' * self.size
        else:
            raise ValueError('Jar is full')

    def deposit(self, n):  # this method adds cookies to the jar until it is full
        if self.size > self.capacity:  #
            raise ValueError("Jar is full")
        self.size += n

    def withdraw(self, n):  # this method takes cookies from the jar until it is empty
        self.size -= n
        if self.size < 0:
            raise ValueError("Jar is emply")

    def get_capacity(self):
        return self.capacity

    def set_capacity(self, capacity):
        if capacity < 0:  # check the parameter is valid
            raise ValueError('The jar is too small')
        self.capacity = capacity

    def get_size(self):
        return self.size

    def set_size(self, n):
        self.size = n


jar = Jar()
jar.deposit(3)
jar.withdraw(1)
jar.deposit(6)
print(jar)