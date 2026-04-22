import random

def run_quiz():
    score = 0

    questions = [
        {"question": "Capital of Kyrgyzstan?",
         "options": ["Osh", "Bishkek", "Naryn"],
         "answer": "b"},

        {"question": "How many continents are there?",
         "options": ["5", "6", "7"],
         "answer": "c"},

        {"question": "Highest mountain in the world?",
         "options": ["Everest", "Kilimanjaro", "Aconcagua"],
         "answer": "a"},

        {"question": "Closest planet to the Sun?",
         "options": ["Venus", "Mercury", "Mars"],
         "answer": "b"},

        {"question": "Largest country in the world?",
         "options": ["USA", "Russia", "Canada"],
         "answer": "b"},

        {"question": "Largest ocean in the world?",
         "options": ["Atlantic", "Indian", "Pacific"],
         "answer": "c"},

        {"question": "Chemical symbol O stands for?",
         "options": ["Gold", "Oxygen", "Silver"],
         "answer": "b"},

        {"question": "First human flight to space year?",
         "options": ["1961", "1957", "1969"],
         "answer": "a"},

        {"question": "Programming language used here?",
         "options": ["Python", "HTML", "Word"],
         "answer": "a"},

        {"question": "Longest river in the world?",
         "options": ["Nile", "Amazon", "Yangtze"],
         "answer": "a"}
    ]

    random.shuffle(questions)

    for i, q in enumerate(questions, start=1):
        print("\n{}. {}".format(i, q['question']))
        print("a) {}".format(q['options'][0]))
        print("b) {}".format(q['options'][1]))
        print("c) {}".format(q['options'][2]))

        answer = input("Your answer (a/b/c): ").lower()

        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong! Correct answer: {}\n".format(q['answer']))

    print("Quiz finished!")
    print("Your score: {} out of {}".format(score, len(questions)))

    percent = (score / len(questions)) * 100
    print("Percentage: {:.1f}%".format(percent))

    # Save result
    with open("quiz_result.txt", "w") as f:
        f.write("Score: {} out of {}\n".format(score, len(questions)))
        f.write("Percentage: {:.1f}%\n".format(percent))

    print("Result saved to quiz_result.txt")

def main():
    while True:
        print("\n=== Console Quiz ===")
        print("1. Start Quiz")
        print("2. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            run_quiz()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
