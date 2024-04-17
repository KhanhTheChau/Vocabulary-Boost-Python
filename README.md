# English Vocabulary Quiz

This Python script `quiz.py` is designed to help you improve your English vocabulary through a simple quiz game. It loads vocabulary data from a JSON file, presents you with fill-in-the-blank questions, and provides feedback on your answers.

## Usage

1. **Install Dependencies**

   Ensure you have Python installed on your system. This script requires Python 3.x. No additional packages need to be installed.

2. **Prepare Vocabulary Data**

   Prepare your vocabulary data in a JSON format. Each JSON object should contain a word as the key and a corresponding fill-in-the-blank question as the value.

3. **Run the Script**

   Run the script `quiz.py` by executing the following command in your terminal:


4. **Take the Quiz**

Once the script is running, it will present you with fill-in-the-blank questions based on the vocabulary data. Type your answer and press Enter. If your answer is correct, it will display "Correct!". If you need a hint, type "1" and press Enter to display a suggestion. To reveal the correct answer, type "0" and press Enter.

## Customization

You can customize the script by modifying the following:

- **JSON File**: Update the `file_path` variable in the `main()` function to point to your JSON file containing vocabulary data.

### Example JSON Format

```json
[
 {"word1": "Question 1?"},
 {"word2": "Question 2?"},
 ...
]
