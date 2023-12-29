from enum import Enum
from dataclasses import dataclass
import random


class OrderType(Enum):
    BUY = "buy"
    SELL = "sell"
    NOOP = "noop"


@dataclass
class Order:
    type: OrderType = OrderType.NOOP
    security: str = ""
    weight: float = 0.0


class Strategy:
    def __init__(self, portfolio, target_security):
        pass

    def get_order(self, cur_date):
        pass


class BuyAllAtFirstDay(Strategy):
    def __init__(self, portfolio):
        self.portfolio = portfolio

    def get_order(self, target_security: str, cur_date):
        if cur_date == self.portfolio.start_date:
            return Order(OrderType.BUY, target_security, 1)
        else:
            return Order(OrderType.NOOP)


class RandomBuyAndSell(Strategy):
    def __init__(self, portfolio):
        self.portfolio = portfolio
        self.state = True

    def get_order(self, target_security: str, cur_date):
        rand = random.random()
        if rand > 0.99:
            if self.state:
                self.state = not (self.state)
                return Order(OrderType.BUY, target_security, 1)
            else:
                self.state = not (self.state)
                return Order(OrderType.SELL, target_security, 1)
        else:
            return Order(OrderType.NOOP)
