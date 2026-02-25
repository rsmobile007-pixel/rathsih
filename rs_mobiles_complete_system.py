class MobileSystem:
    def __init__(self):
        self.products = {}
        self.stock = {}
        self.purchase_history = []

    def add_product(self, product_id, name, price, barcode):
        self.products[product_id] = {'name': name, 'price': price, 'barcode': barcode}
        self.stock[product_id] = 0

    def update_stock(self, product_id, quantity):
        if product_id in self.stock:
            self.stock[product_id] += quantity
        else:
            raise ValueError('Product not found')

    def sell_product(self, product_id, quantity):
        if product_id in self.stock and self.stock[product_id] >= quantity:
            self.stock[product_id] -= quantity
            self.purchase_history.append((product_id, quantity))
            print(f'Sold {quantity} of {product_id}')
        else:
            raise ValueError('Insufficient stock')

    def generate_invoice(self, customer_name, items):
        total = sum(self.products[item]['price'] * qty for item, qty in items.items())
        print(f'Invoice for {customer_name}')
        for item, qty in items.items():
            product = self.products[item]
            print(f'{product['name']} (x{qty}): ${product['price'] * qty}')
        print(f'Total: ${total}')

    def auto_fill_customer_info(self, customer_id):
        # Simulate customer auto-fill logic
        return {'name': 'John Doe', 'address': '123 Main St', 'id': customer_id}

    def get_purchase_history(self):
        return self.purchase_history

    def analytics_report(self):
        report = {'total_sales': sum(item[1] for item in self.purchase_history)}
        return report

    def display_stock(self):
        for product_id, quantity in self.stock.items():
            if quantity > 0:
                print(f'{product_id}: {quantity} in stock')

# Example usage
system = MobileSystem()
system.add_product('001', 'Smartphone', 299.99, '1234567890123')
system.update_stock('001', 50)
customer_info = system.auto_fill_customer_info('cust123')
system.generate_invoice(customer_info['name'], {'001': 2})
system.display_stock()

