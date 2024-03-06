def calculate_discount(price, discount_percent):
    return price * (1 - discount_percent / 100) if discount_percent >= 20 else price

original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

final_price = calculate_discount(original_price, discount_percentage)

print("Final price after applying discount:", final_price if final_price < original_price else "No discount applied. Final price:", original_price)
