from typing import List

class Customer:
    def __init__(self):
        self.customerId: int = 121
        self.customerName: str = "A"
        self.address: List[str] = []
        self.email: str = ""
        self.creditCardInfo: str = "X"
        self.accountBalance: float = 0.0
        self.orders: List[str] = []

    def getCustomerId(self) -> int:
        return self.customerId

    def getName(self) -> str:
        return self.customerName

    def getEmail(self) -> str:
        return self.email

    def getOrders(self) -> List[str]:
        return self.orders


class Menu:
    def __init__(self):
        self.menuId: int = 0
        self.menuName: str = ""
        self.menuItems: List[str] = []

    def getMenuId(self) -> int:
        return self.menuId

    def getMenuName(self) -> str:
        return self.menuName

    def getMenuItems(self) -> List[str]:
        return self.menuItems


def get_valid_input(prompt: str, input_type: type) -> type:
    while True:
        try:
            user_input = input_type(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please try again.")


def main() -> None:
    # Create a customer
    customer: Customer = Customer()

    # Get customer details
    print("Customer Details:")
    print("Customer ID:", customer.getCustomerId())
    print("Customer Name:", customer.getName())
    print("Customer Email:", customer.getEmail())
    print("Customer Orders:", customer.getOrders())
    print()

    # Get menu details from user input
    menu: Menu = Menu()
    menu.menuId = get_valid_input("Enter menu ID: ", int)
    menu.menuName = get_valid_input("Enter menu name: ", str)

    # Get menu items from user input
    print("Enter menu items (separated by commas, press Enter to finish):")
    while True:
        item: str = input()
        if item == "":
            break
        menu.menuItems.append(item)

    # Get menu details
    print("\nMenu Details:")
    print("Menu ID:", menu.getMenuId())
    print("Menu Name:", menu.getMenuName())
    print("Menu Items:", menu.getMenuItems())

if __name__ == "__main__":
    main()
