from random import randint


class Train:

    def __init__(self, trainNo) -> None:
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}.")

    def getStatus(self):
        print(f"Train number {self.trainNo} is running on time.")

    def getFareInformation(self, fro, to):
        print(
            f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222,555)}."
        )


t = Train(223)
t.book("Rampur", "Delhi")
t.getStatus()
t.getFareInformation("Rampur", "Delhi")
