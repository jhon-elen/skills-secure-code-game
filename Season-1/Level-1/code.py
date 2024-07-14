'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import Decimal

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    net = Decimal('0')

    for item in order.items:
        amount = item.amount
        quantity = item.quantity
        if item.type == 'payment':
            net += Decimal(amount)
        elif item.type == 'product':
            net -= Decimal(amount) * Decimal(quantity)
        else:
            return "Invalid item type: %s" % item.type

    if order.items[0].quantity > 1 or order.items[-1].quantity > 1:
        return "Total amount payable for an order exceeded"

    net_final = round(float(net))
    if net_final != 0:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net_final)
    else:
        return "Order ID: %s - Full payment received!" % order.id
    

""" num_items = 12
items = [Item(type='product', description='tv', amount=99999, quantity=num_items)]
for i in range(num_items):
    items.append(Item(type='payment', description='invoice_' + str(i), amount=99999, quantity=1))
order_1 = Order(id='1', items=items)
result1 = validorder(order_1), 'Total amount payable for an order exceeded'
print(result1)

# Put payments before products
items = items[1:] + [items[0]]
order_2 = Order(id='2', items=items)
result2 = validorder(order_2), 'Total amount payable for an order exceeded'
print(result2) """