
class OrderCost:
    close_tax = 0.001
    open_commission = 0.0003
    close_commission = 0.0003
    min_commission = 5.0

    def __init__(self, close_tax = 0.001, open_commission = 0.0003, close_commission = 0.0003, min_commission = 5.0):
        self.close_tax = close_tax
        self.open_commission = open_commission
        self.close_commision = close_commission
        self.min_commission = min_commission
