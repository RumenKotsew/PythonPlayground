class Bill():
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return "{0}".format(self.amount)

    def __repr__(self):
        return str(self.amount)

    def __int__(self):
        return int(self.amount)

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(bill):
        if bill.amount > 0:
            return hash(str(bill.amount))
        else:
            return "valueError"


class BatchBill():
    def __init__(self, list_of_bills):
        self.list_of_bills = list_of_bills

    # def type_check():
    #   if type(list_of_bills) is not type(list()):
    #       return "wrong type"

    # type_check()

    def __len__(self):
        index = 0
        for bill in self.list_of_bills:
            index += 1

        return index

    def __str__(self):
        return str(self.list_of_bills)

    def total(self):
        total_sum = 0
        for bill in self.list_of_bills:
            total_sum += bill

        return total_sum

    def __iter__(self):
        for x in self.list_of_bills:
            yield x


class CashDesk():
    def __init__(self, batch_bills):
        self.batch_bills = batch_bills

    def take_money(self, money):
        if money in self.batch_bills:
            self.batch_bills.remove(money)

    def total(self):
        total_cash = 0
        for cash_batches in self.batch_bills:
            for cash in cash_batches:
                total_cash += cash
        return total_cash

    def inspect(self):
        bills_histogram = dict()
        for count in self.batch_bills:
            if count in bills_histogram:
                bills_histogram[count] += 1
            else:
                bills_histogram[count] = 1
        return bills_histogram


batch_of_bills = BatchBill([10, 20, 50, 100, 100, 100])
desk = CashDesk(batch_of_bills)

print(desk.inspect())
