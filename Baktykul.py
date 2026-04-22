import random

def run_quiz():
    score = 0

    questions = [
        {"question": "Столица Кыргызстана?", "options": ["Ош", "Бишкек", "Нарын"], "answer": "б"},
        {"question": "Сколько континентов на Земле?", "options": ["5", "6", "7"], "answer": "в"},
        {"question": "Какой язык программирования мы используем?", "options": ["Python", "HTML", "Word"], "answer": "а"},
        {"question": "Самая высокая гора в мире?", "options": ["Эверест", "Килиманджаро", "Аконкагуа"], "answer": "а"},
        {"question": "Самая длинная река мира?", "options": ["Нил", "Амазонка", "Янцзы"], "answer": "а"},
        {"question": "В каком году человек впервые полетел в космос?", "options": ["1961", "1957", "1969"], "answer": "а"},
        {"question": "Какая планета ближе всех к Солнцу?", "options": ["Венера", "Меркурий", "Марс"], "answer": "б"},
        {"question": "Какой элемент обозначается символом O?", "options": ["Золото", "Кислород", "Серебро"], "answer": "б"},
        {"question": "Самая большая страна по территории?", "options": ["США", "Россия", "Канада"], "answer": "б"},
        {"question": "Какой океан самый большой?", "options": ["Атлантический", "Индийский", "Тихий"], "answer": "в"}
    ]

    random.shuffle(questions)

    for i, q in enumerate(questions, start=1):
        print("{}. {}".format(i, q['question']))
        print("а) {}".format(q['options'][0]))
        print("б) {}".format(q['options'][1]))
        print("в) {}".format(q['options'][2]))

        answer = input("Ваш ответ: ").lower()
        if answer == q["answer"]:
            print("Правильно!\n")
            score += 1
        else:
            print("Неправильно! Правильный ответ: {}\n".format(q['answer']))

    print("Викторина завершена!")
    print("Ваш результат: {} из {}".format(score, len(questions)))
    percent = (score / len(questions)) * 100
    print("Процент правильных ответов: {:.1f}%".format(percent))

    # Сохраняем результат в файл
    with open("quiz_result.txt", "w") as f:
        f.write("Результат викторины: {} из {}\n".format(score, len(questions)))
        f.write("Процент правильных ответов: {:.1f}%\n".format(percent))
    print("Результат сохранён в файл quiz_result.txt")

# Главное меню
def main():
    while True:
        print("\n=== Консольная Викторина ===")
        print("1. Начать викторину")
        print("2. Выйти")
        choice = input("Выберите пункт: ")

        if choice == "1":
            run_quiz()
        elif choice == "2":
            print("Спасибо за участие! До встречи!")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

# Запуск программы
if __name__ == "__main__":
    main()
