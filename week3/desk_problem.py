class Bill:
    def __init__(self, amount):
        if type(amount) != int:
            raise TypeError
        elif amount < 0:
            raise ValueError
        else:
            self.amount = amount

    def __str__(self):
        return "A {0}$ bill".format(self.amount)

    def __repr__(self):
        return str(self)

    def __int__(self):
        return self.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(bill):
        if bill.amount > 0:
            return hash(str(bill.amount))
        else:
            raise ValueError


class BatchBill:
    def __init__(self, *args):
        self.bills = list()
        if args[0]:
            self.bills = args[0]

    def __getitem__(self, index):
        if len(self.bills) > index:
            return self.bills[index]
        else:
            raise IndexError

    def __len__(self):
        return len(self.bills)

    def total(self):
        res = 0
        for bill in self.bills:
            res += bill.amount
        return res


class CashDesk:
    def __init__(self):
        self.bills = list()
        self.bill_batches = list()

    def take_money(self, money):
        if money.__class__.__name__ == 'Bill':
            self.bills.append(money)
        elif money.__class__.__name__ == 'BatchBill':
            self.bill_batches.append(money)

    def total(self):
        res = 0
        if len(self.bills) > 0:
            for i in self.bills:
                res += i.amount
        if len(self.bill_batches) > 0:
            for j in self.bill_batches:
                res += j.total()
        return res

    def inspect(self):
        result = ("We have a total of " + str(self.total()) + "$ in the desk")
        print_list = list()
        if len(self.bills) > 0:
            for i in self.bills:
                print_list.append(i.amount)
        if len(self.bill_batches) > 0 and len(self.bills) > 0:
            print_list = list()
            self.bill_batches.append(self.bills)
            for i in range(len(self.bill_batches)):
                for bill in self.bill_batches[i]:
                    print_list.append(bill.amount)

        res_dict = {}
        for i in print_list:
            if i in res_dict:
                res_dict[i] += 1
            else:
                res_dict[i] = 1
        result += ("\nWe have the following count of bills, sorted in ascending order:")
        my_dict_keys = list(res_dict.keys())
        my_dict_keys.sort()
        for key in my_dict_keys:
            result += ("\n" + str(key) + "$ bills - " + str(res_dict[key]))
        # for k, v in res_dict.items():
            # result += (str(k) + "$ bills - " + str(v) + "\n")

        return result


# desk = CashDesk()
# desk.take_money(Bill(10))
# desk.take_money(Bill(5))
# desk.take_money(Bill(25))
# desk.take_money(Bill(50))
# desk.take_money(BatchBill([Bill(10), Bill(5)]))
