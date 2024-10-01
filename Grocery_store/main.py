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

    def item_change(self,coustomer_id,new_item_num)
        line_number = self.coustomer_line[coustomer_id]
        if new_item_num > self.coustomer_items[coustomer_id]:
            self.lines[line_number].remove[coustomer_id]
            self.lines[line_number].apend[coustomer_id]
        elif  new_item_num ==0:
            self.lines[line_number].remove[coustomer_id]
            del self.coustomer_line[coustomer_id]
            del self.coustomer_items[coustomer_id]
            self.Customer_exit(coustomer_id)
        else:
            self.coustomer_items[coustomer_id] = new_item_num
        





