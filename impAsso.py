from typing import List

class Order:
    def __init__(self, orderId: int, orderDate: str, orderTotal: float, orderItems: List[str]):
        self.orderId = orderId
        self.orderDate = orderDate
        self.orderTotal = orderTotal
        self.orderItems = orderItems

    def getOrderId(self) -> int:
        return self.orderId

    def getOrderDate(self) -> str:
        return self.orderDate

    def getOrderTotal(self) -> float:
        return self.orderTotal

    def getOrderItems(self) -> List[str]:
        return self.orderItems


class Customer:
    def __init__(self):
        self.customerId: int = 121
        self.customerName: str = "A"
        self.address: List[str] = []
        self.email: str = ""
        self.creditCardInfo: str = "X"
        self.accountBalance: float = 0.0
        self.orders: List[Order] = []

    def getCustomerId(self) -> int:
        return self.customerId

    def getName(self) -> str:
        return self.customerName

    def getEmail(self) -> str:
        return self.email

    def getOrders(self) -> List[int]:
        orderIds: List[int] = [order.getOrderId() for order in self.orders]
        return orderIds

    def addOrder(self, order: Order) -> None:
        self.orders.append(order)


# Create a Customer object
customer = Customer()

# Create two Order objects
order1 = Order(1, "2023-06-14", 100.0, ["Item 1", "Item 2"])
order2 = Order(2, "2023-06-15", 150.0, ["Item 3", "Item 4", "Item 5"])

# Add the orders to the customer using composition
customer.addOrder(order1)
customer.addOrder(order2)

# Get customer details
print(f"Customer ID: {customer.getCustomerId()}")
print(f"Customer Name: {customer.getName()}")
print(f"Customer Email: {customer.getEmail()}")

# Get the order IDs for the customer
orderIds = customer.getOrders()
print("Order IDs:")
for orderId in orderIds:
    print(orderId)
