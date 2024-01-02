class BusinessMan:
    def __init__(self, name) -> None:
        self.name = name
        self.businesses = {}

    def add(self, business):
        self.businesses[business.name] = business
        print(f'{self.name} has a new business: {business.name}')

    def close(self, business_name):
        if business_name in self.businesses:
            self.businesses.pop(business_name)
            print(f'{self.name} closed {business_name}')
        else:
            print(f'{self.name} does not have {business_name}')

    def sum_income(self):
        return sum(business.income for business in self.businesses.values())

    def __str__(self) -> str:
        business_names = ', '.join(self.businesses.keys())
        return f'{self.name} has {len(self.businesses)} business(es): {business_names}'
       
class Shop:
    def __init__(self, name) -> None:
        self.name = name
        self.products = {}
        self.income = 0

    def add(self,product_name,quantity,price=None):
        if product_name in self.products:
            if price is not None and price > self.products[product_name]['price']:
                self.products[product_name]['price'] = price
            self.products[product_name]['quantity'] += quantity
        else:
            if price is None:
                print(f'{product_name} con not add to the {self.name} without price')
                return False
            else:
                self.products[product_name] = {'quantity':quantity,'price':price}
        print(f'{product_name} Amount in {self.name}: {self.products[product_name]['quantity']}, price: {self.products[product_name]['price']}$')
   
    def sell(self,product_name,quantity=1,bag =False):
        if product_name not in self.products or self.products[product_name]['quantity'] == 0:
            print(f'{product_name} not in {self.name}')
            return
        if quantity > self.products[product_name]['quantity']:
            print(f'{self.name} dose not have enoght {product_name} only {self.products[product_name]['quantity']} avalabel')
            return
        
        self.products[product_name]['quantity'] -= quantity
        total_price = quantity * self.products[product_name]['price']
        if bag:
            self.income += 1
            total_price += 1

        self.income += total_price
        print(f'{self.name} sold {product_name} ({quantity}) for {total_price}$')

    def __str__(self) -> str:
        return str(self.products)

class GroceryShop(Shop):
    def sell(self, product_name, quantity=1, bag=False):
        super().sell(product_name, quantity, bag)

class CoffeeShop(Shop):
    def __init__(self, name, coffee_price) -> None:
        super().__init__(name)
        self.coffee_price = coffee_price

    def serve_coffee(self):
        self.income += self.coffee_price
        print(f'{self.name} served coffee for {self.coffee_price}')

johndoe = BusinessMan('John Doe')
tesco = GroceryShop('Tesco') 
starbuks = CoffeeShop('StarBuks',3)   
johndoe.add(tesco)
johndoe.add(starbuks)
print(johndoe)
tesco.add('milk',10)
tesco.add('milk',10,2)
tesco.add('milk',5,1)
tesco.add('potato', 1, 1)
tesco.sell('beer') # should print: There's no beer in Tesco
tesco.sell('butter')
tesco.sell('potato', 5)
tesco.sell('potato')
tesco.sell('potato')
tesco.sell('milk', 3)
tesco.sell('milk', 2, True)
tesco.add('milk', 5, 2.5)
tesco.sell('milk', 16)
starbuks.add('milk', 10, 2)
starbuks.sell('milk')
tesco.sell('milk')
starbuks.serve_coffee()
print(johndoe.sum_income())
johndoe.close('McDonalds') # should print: John Doe doesn't have business called McDonalds
johndoe.close('StarBuks') # should print: John Doe closed StarBucks
print(johndoe)