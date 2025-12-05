class ManulCalculator:
    def __init__(self, initial_count: int):
        self.count = initial_count

    def add(self, number: int) -> None:
        self.count += number

    def subtract(self, number: int) -> None:
        if number > self.count:
            raise ValueError("Cannot have negative manuls.")
        self.count -= number

    def get_count(self) -> int:
        return self.count

    def main(self):
        print("Here you can count manuls (Pallas's cat)!")
        manul_count = int(input("Enter the number of manuls: "))
        calculator = ManulCalculator(manul_count)  # Створіть екземпляр
        
        while True:
            print("What are you going to do with them?")
            print("1. Add")
            print("2. Subtract")
            action = input("Choose an action (1 or 2): ")
            if action == "1":
                add_count = int(input("How many manuls to add? "))
                calculator.add(add_count)
                print(f"You now have {calculator.get_count()} manuls.")
            elif action == "2":
                sub_count = int(input("How many manuls to subtract? "))
                calculator.subtract(sub_count)
                print(f"You now have {calculator.get_count()} manuls.")
    
if __name__ == "__main__":
    calculator = ManulCalculator(0)
    calculator.main()