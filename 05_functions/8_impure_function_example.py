# Impure functions may produce different results even with the same inputs
# and can modify external state or produce side effects.

# Impure Function Example

def impure_add_and_log(a, b, log):
    # This function adds two numbers and appends the result to a log list.
    # Modifying the log list is a side effect, making this function impure.
    # Key point: The function may produce different results even if the inputs are the same,
    # because it depends on and modifies external state.
    result = a + b
    log.append(result)  # Side effect: modifying the external 'log' list
    return result


# Call the function
log_list = []  # External state that will be modified by the function
impure_result_1 = impure_add_and_log(5, 3, log_list)  # Outputs: 8, log_list: [8]
impure_result_2 = impure_add_and_log(5, 3, log_list)  # Outputs: 8, log_list: [8, 8]

# The log_list is modified as a side effect, making the function impure.
print(f"Impure Function Result 1: {impure_result_1}")  # Outputs: Impure Function Result 1: 8
print(f"Impure Function Result 2: {impure_result_2}")  # Outputs: Impure Function Result 2: 8
print(f"Log List: {log_list}")  # Outputs: Log List: [8, 8]


# Advantages of Impure Functions:
# - Flexibility: Can modify external state or interact with external systems.
# - Direct and Practical: Useful for tasks requiring side effects (e.g., logging, database updates, random number generation).

# Disadvantages of Impure Functions:
# - Unpredictability: Can be harder to test and debug due to their reliance on external state and side effects.
# - Potential for Bugs: Side effects can lead to unintended changes and subtle bugs, especially in complex systems.


##########################################################


# Passing External State to Functions
# To avoid global variables, external state can be passed as an argument.
# While this reduces reliance on global state, the function can still be impure
# if it modifies the external state.

# A better approach is to return the modified state rather than directly modifying it:
def improved_impure_add_and_log(a, b, log):
    # This function adds two numbers and returns a new log list with the result appended.
    # This approach avoids directly modifying the external state, making it slightly better,
    # but it is still considered impure.
    result = a + b
    new_log = log + [result]  # Create a new list instead of modifying the original
    return result, new_log


# Call the function
log_list = []  # External state
impure_result_3, updated_log = improved_impure_add_and_log(5, 3, log_list)

# The original log_list remains unchanged, but the function is still impure since it relies on external state.
print(f"Impure Function Result 3: {impure_result_3}")  # Outputs: Impure Function Result 3: 8
print(f"Original Log List: {log_list}")  # Outputs: Original Log List: []
print(f"Updated Log List: {updated_log}")  # Outputs: Updated Log List: [8]

# Conclusion:
# - Pure functions are generally preferred for their predictability, ease of testing, and lack of side effects.
# - Impure functions are necessary for tasks that require interaction with external systems or modification of external state.
# - In practice, a mix of both pure and impure functions is often used, with pure functions handling the core logic and impure functions managing side effects.
