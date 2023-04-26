class StringPrinter:
    def __init__(self):
        pass

    def accept_string(self):
        self.string = input("Enter a string: ")

    def print_string(self):
        print(self.string)
s = StringPrinter()
s.accept_string()
s.print_string()