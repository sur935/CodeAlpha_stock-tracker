stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 120,
    "MSFT": 330
}

user_stocks = {}

while True:
    stock = input("Enter stock symbol (e.g., AAPL), or type 'done' to finish: ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found. Available stocks:", ', '.join(stock_prices.keys()))
        continue
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        user_stocks[stock] = user_stocks.get(stock, 0) + quantity
    except ValueError:
        print("Please enter a valid number.")

total_investment = 0
print("\nYour Portfolio:")
for stock, qty in user_stocks.items():
    value = stock_prices[stock] * qty
    total_investment += value
    print(f"{stock}: {qty} shares x ₹{stock_prices[stock]} = ₹{value}")

print(f"\nTotal Investment Value: ₹{total_investment}")

save = input("\nDo you want to save this to 'portfolio.txt'? (yes/no): ").lower()
if save == "yes":
    with open("portfolio.txt", "w") as file:
        for stock, qty in user_stocks.items():
            value = stock_prices[stock] * qty
            file.write(f"{stock}: {qty} shares x ₹{stock_prices[stock]} = ₹{value}\n")
        file.write(f"\nTotal Investment Value: ₹{total_investment}")
    print("Portfolio saved to 'portfolio.txt'.")
