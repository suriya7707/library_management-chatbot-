import difflib
from datetime import datetime

class Library:
    def __init__(self):
        self.books = {
            "1984": {
                "available": True,
                "borrowed_by": None,
                "description": "A dystopian novel by George Orwell that explores the dangers of totalitarianism."
            },
            "To Kill a Mockingbird": {
                "available": True,
                "borrowed_by": None,
                "description": "A novel by Harper Lee published in 1960, addressing serious issues of race and injustice."
            },
            "The Great Gatsby": {
                "available": True,
                "borrowed_by": None,
                "description": "A novel by F. Scott Fitzgerald that critiques the American Dream through the story of Jay Gatsby."
            },
            "Moby Dick": {
                "available": True,
                "borrowed_by": None,
                "description": "A novel by Herman Melville that follows Captain Ahab's obsessive quest for revenge against Moby Dick."
            },
        }
        self.history = []

    def list_books(self):
        return [book for book, details in self.books.items() if details["available"]]

    def check_availability(self, book_name):
        return self.books.get(book_name)

    def borrow_book(self, book_name, user):
        if book_name in self.books:
            if self.books[book_name]["available"]:
                self.books[book_name]["available"] = False
                self.books[book_name]["borrowed_by"] = user
                self.history.append(f"{user} borrowed '{book_name}'.")
                return f"You have successfully borrowed '{book_name}'."
            else:
                return f"'{book_name}' is currently borrowed by {self.books[book_name]['borrowed_by']}."
        else:
            return f"The book '{book_name}' is not available in our library."

    def return_book(self, book_name, user):
        if book_name in self.books:
            if self.books[book_name]["borrowed_by"] == user:
                self.books[book_name]["available"] = True
                self.books[book_name]["borrowed_by"] = None
                self.history.append(f"{user} returned '{book_name}'.")
                return f"You have successfully returned '{book_name}'."
            else:
                return f"You did not borrow '{book_name}'."
        else:
            return f"The book '{book_name}' is not available in our library."

    def extract_book_name(self, user_input):
        for book in self.books.keys():
            if book.lower() in user_input:
                return book
        return None

    def suggest_book(self, user_input):
        possible_books = list(self.books.keys())
        suggestions = difflib.get_close_matches(user_input, possible_books, n=1)
        if suggestions:
            return suggestions[0]
        return None

    def get_book_description(self, book_name):
        return self.books[book_name]["description"]

    def greet_user(self):
        current_hour = datetime.now().hour
        if current_hour < 12:
            return "Good morning! How can I assist you today?"
        elif 12 <= current_hour < 18:
            return "Good afternoon! How can I assist you today?"
        else:
            return "Good evening! How can I assist you today?"

    def friendly_responses(self, user_input):
        greetings = {
            "good morning": "Good morning!",
            "gud mrng": "Good morning!",
            "good afternoon": "Good afternoon!",
            "gud afternoon": "Good afternoon!",
            "good evening": "Good evening!",
            "gud evening": "Good evening!",
            "hi": "Hello!",
            "hello": "Hello!",
            "hey": "Hello!",
            "thank you": "You're welcome!",
            "thanks": "You're welcome!",
            "bye": "Goodbye! Have a great day!",
            "okay": "Alright! Let me know if you need anything else."
        }
        for key in greetings:
            if key in user_input:
                return greetings[key]
        return None

def chatbot():
    library = Library()
    print("Chatbot: Hello! Welcome to the Library Management Chatbot!")
    print("Chatbot:", library.greet_user())
    
    while True:
        user_input = input("\nYou: ").strip().lower()

        # Check for friendly responses
        friendly_response = library.friendly_responses(user_input)
        if friendly_response:
            print("Chatbot:", friendly_response)
            if friendly_response.startswith("Goodbye"):
                break
            continue
        
        if user_input == "exit":
            print("Chatbot: Thank you for using the Library Management Chatbot. Goodbye!")
            break
        elif "list books" in user_input or "available books" in user_input:
            available_books = library.list_books()
            if available_books:
                print("Chatbot: Here are the available books:", ", ".join(available_books))
            else:
                print("Chatbot: No books are currently available.")
        elif "borrow" in user_input:
            book_name = library.extract_book_name(user_input)
            if book_name:
                user_name = input("Chatbot: Please enter your name: ")
                print("Chatbot:", library.borrow_book(book_name, user_name))
            else:
                print("Chatbot: Please specify the name of the book you wish to borrow.")
        elif "return" in user_input:
            book_name = library.extract_book_name(user_input)
            if book_name:
                user_name = input("Chatbot: Please enter your name: ")
                print("Chatbot:", library.return_book(book_name, user_name))
            else:
                print("Chatbot: Please specify the name of the book you wish to return.")
        elif "about" in user_input or "description" in user_input:
            book_name = library.extract_book_name(user_input)
            if book_name:
                description = library.get_book_description(book_name)
                print(f"Chatbot: Here's a description of '{book_name.title()}': {description}")
            else:
                print("Chatbot: I didn't understand that. Please enter the book name clearly.")
        else:
            book_name = library.extract_book_name(user_input)
            if book_name:
                availability = library.check_availability(book_name)
                if availability and availability["available"]:
                    print(f"Chatbot: '{book_name.title()}' is available for borrowing.")
                elif availability:
                    print(f"Chatbot: '{book_name.title()}' is currently borrowed by {availability['borrowed_by']}.")
                else:
                    print(f"Chatbot: I'm sorry, but '{book_name.title()}' is not available in our library. Please check the title and try again.")
            else:
                print("Chatbot: I didn't understand that. Please enter the book name clearly.")

if __name__ == "__main__":
    chatbot()
