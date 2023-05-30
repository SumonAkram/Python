# Define the Customer class

class Customer:

    # Constructor method with default parameter values

    def __init__(self, customerId: int = 121, customerName: str = "A", address: list[str] = [], email: str = "",
                 creditCardInfo: str = "X", accountBalance: float = 0.0, orders: list[str] = []) -> None:

        # Assigning parameter values to object attributes

        self.customerId = customerId
        self.customerName = customerName
        self.address = address
        self.email = email
        self.creditCardInfo = creditCardInfo
        self.accountBalance = accountBalance
        self.orders = orders

    # Method to get the customer's ID

    def getCustomerId(self) -> int:
        return self.customerId

    # Method to get the customer's name

    def getName(self) -> str:
        return self.customerName

    # Method to get the customer's email

    def getEmail(self) -> str:
        return self.email

    # Method to get the customer's orders

    def getOrders(self) -> list[str]:
        return self.orders


# Create an instance of the Customer class

customer = Customer()

# Print the customer's ID, name, email, and orders

print("Customer ID:", customer.getCustomerId())
print("Customer Name:", customer.getName())
print("Email:", customer.getEmail())
print("Orders:", customer.getOrders())
