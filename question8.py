class Calculator:
    count = 0  # Static attribute to track the number of calls to add()

    @staticmethod
    def add(a, b):
        Calculator.count += 1  # Increment count each time add() is called
        return a + b

# Demonstration of using the static method and updating count
result1 = Calculator.add(5, 10)
print("Result of add(5, 10):", result1)
print("Add method called:", Calculator.count, "times")

result2 = Calculator.add(20, 30)
print("Result of adding(20, 30):", result2)
print("Add method called:", Calculator.count, "times")
