import json
import random

def load_vocab_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def quiz(vocab):
    random.shuffle(vocab)
    for item in vocab:
        word, question = list(item.items())[0]
        print("===========================================================================================")
        print("Fill in the blank:")
        print(question)
        while 1:
            answer = input("Your answer: ")
            if answer.strip().lower() == word.lower():
                print("Correct!")
                break
            elif (answer == "0"):
                print("The correct answer is:", word)
                break
            elif (answer == "1"):
                print("Suggestion:", item["key"])
            else:
                print("Incorrect. Try again!")

def main():
    file_path = 'Unit1_Book1.json' 
    vocab = load_vocab_from_json(file_path)
    quiz(vocab)

if __name__ == "__main__":
    main()
