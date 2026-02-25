class Customer:
    def __init__(self, customer_id, name, phone):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone

class Invoice:
    def __init__(self, invoice_id, customer, amount):
        self.invoice_id = invoice_id
        self.customer = customer
        self.amount = amount
        self.paid = False

    def mark_as_paid(self):
        self.paid = True

class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        self.stock += quantity

class RS_Mobiles:
    def __init__(self):
        self.customers = {}
        self.products = {}
        self.invoices = {}

    def add_customer(self, customer):
        self.customers[customer.customer_id] = customer

    def add_product(self, product):
        self.products[product.product_id] = product

    def generate_invoice(self, customer_id, product_id, quantity):
        if product_id in self.products and self.products[product_id].stock >= quantity:
            total_amount = self.products[product_id].price * quantity
            invoice_id = len(self.invoices) + 1
            invoice = Invoice(invoice_id, self.customers[customer_id], total_amount)
            self.invoices[invoice_id] = invoice
            self.products[product_id].stock -= quantity
            return invoice
        else:
            return None

    def report(self):
        # generate a simple report
        total_sales = sum(invoice.amount for invoice in self.invoices.values())
        return f'Total Sales: {total_sales}'

# Example usage:
if __name__ == '__main__':
    rms = RS_Mobiles()
    rms.add_customer(Customer(1, 'John Doe', '123-456-7890'))
    rms.add_product(Product(1, 'Smartphone', 699.99, 50))
    invoice = rms.generate_invoice(1, 1, 2)
    if invoice:
        print(f'Invoice {invoice.invoice_id} generated for {invoice.customer.name} for amount {invoice.amount}.')
    print(rms.report())