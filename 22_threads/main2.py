from threading import Thread


class BankFacilito:

    def __init__(self):
        self.balance = 0

    def deposit(self):
        for _ in range(1000_000_000):
            self.balance += 1

    def withdraw(self):
        for _ in range(1000_000_000):
            self.balance -= 1


bank = BankFacilito()

t1 = Thread(target=bank.deposit)
t2 = Thread(target=bank.withdraw)

t1.start()
t2.start()

t1.join()
t2.join()

print(bank.balance)
