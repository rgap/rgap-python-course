# The `continue` statement is used to skip the current iteration of the loop and move on to the next one.
# When `continue` is encountered, the remaining code in the current iteration is skipped.
# Syntax:
#     for <variable> in <iterable>:
#         if <condition>:
#             continue
#         <code to execute>

# Example 1: Skipping out-of-stock products in a list
products = [
    "laptop",
    "tablet (out of stock)",
    "smartphone",
    "monitor (out of stock)"]
for product in products:
    if "out of stock" in product:
        continue  # Skip out-of-stock items
    print(f"Available product: {product}")


###############################################


# Example 2: Filtering out invalid email addresses
emails = ["user1@example.com", "invalid@", "user2@example.com", "@wrong.com"]
valid_emails = []
for email in emails:
    if "@" not in email or "." not in email:
        continue  # Skip invalid emails
    valid_emails.append(email)
print("Valid emails:", valid_emails)
