import random

# edit this list - get more from Chat GPT
words = [
    {"bengali":"এ", "english":"this"},
    {"bengali":"তার", "english":"his"},
    {"bengali":"যে", "english":"who"},
    {"bengali":"এবং", "english":"and"},
    {"bengali":"থেকে", "english":"from"},
    {"bengali":"একটি", "english":"a/an"},
    {"bengali":"হয়", "english":"be"},
    {"bengali":"যে", "english":"that"},
    {"bengali":"তা", "english":"it"},
    {"bengali":"তিনি", "english":"he/she"},
    {"bengali":"না", "english":"not"},
    {"bengali":"সাথে", "english":"with"},
    {"bengali":"তারা", "english":"they"},
    {"bengali":"হয়েছে", "english":"has/have"},
    {"bengali":"আমি", "english":"I"},
    {"bengali":"এটি", "english":"it"},
    {"bengali":"আপনি", "english":"you"},
    {"bengali":"করা", "english":"do"},
    {"bengali":"এ", "english":"he"},
    {"bengali":"যার", "english":"whose"},
]


def quiz_user(words):
    """Quiz the user with words."""
    random.shuffle(words)  # Shuffle the list of words
    score = 0

    for word in words:
        print(f"What is the English translation of '{word['bengali']}'?")
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = word['english'].lower()

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{word['english']}'.\n")

    print(f"Quiz complete! Your score: {score}/{len(words)}")

def main():
    print("Welcome to the Language Learning Flashcards App!")
    input("Press Enter to start the quiz...")
    quiz_user(words)

if __name__ == "__main__":
    main()