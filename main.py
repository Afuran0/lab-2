import random

def has_duplicate_birthdays(birthdays):
    return len(birthdays) != len(set(birthdays))
def generate_birthdays(n):
    return [random.randint(1, 365) for _ in range(n)]
def birthday_paradox_experiment(n, trials=1000):
    duplicate_count = 0
    for _ in range(trials):
        birthdays = generate_birthdays(n)
        if has_duplicate_birthdays(birthdays):
            duplicate_count += 1
    return duplicate_count / trials
def main():
    results = []
    for n in range(5, 51, 5):
        probability = birthday_paradox_experiment(n)
        result = f"For n={n}, the probability of having at least one shared birthday is {probability:.2f}"
        results.append(result)
        print(result)
    with open("birthday_paradox_result.txt", "w") as file:
        for result in results:
            file.write(result + "\n")

if __name__ == "__main__":
    main()
