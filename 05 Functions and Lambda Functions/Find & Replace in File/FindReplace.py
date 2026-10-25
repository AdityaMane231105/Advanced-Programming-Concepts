import re

def find_replace():
    input_file = r"C:/Users/Aditya/OneDrive/Documents/Advanced Programming Concepts/Find & Replace in File/input.txt"
    output_file = r"C:/Users/Aditya/OneDrive/Documents/Advanced Programming Concepts/Find & Replace in File/output.txt"
    target = input("Enter word/phrase to replace: ")
    replacement = input("Enter replacement word/phrase: ")
    case_choice = input("Case-sensitive? (yes/no): ").strip().lower()
    case_sensitive = True if case_choice == "yes" else False

    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    if case_sensitive:
        new_text = text.replace(target, replacement)
    else:
        new_text = re.sub(target, replacement, text, flags=re.IGNORECASE)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(new_text)

    print("Original text:\n", text)
    print("\nModified text:\n", new_text)

find_replace()
