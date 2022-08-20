class Bank:
    def card(number):
        return '*' * len(number[:-4]) + number[-4:]
