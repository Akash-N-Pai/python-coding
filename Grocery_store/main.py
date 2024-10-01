from collections import deque

class Grocery_Store_checkout:
    def __init__(self) -> None:
        self.lines ={}
        self.coustomer_line = {}
        self.coustomer_items = {}

    def Customer_enter(self,customer_id,line_number,number_Of_items):
        if line_number not in self.lines:
            self.lines[line_number] = deque()
        self.lines[line_number].apend(customer_id)
        self.coustomer_line[customer_id] = line_number
        self.coustomer_items[customer_id] = number_Of_items

        


