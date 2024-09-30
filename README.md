Library Management Chatbot

This project is a simple, interactive Library Management Chatbot implemented in Python. It allows users to manage library-related tasks such as listing available books, borrowing, and returning books, and viewing book descriptions. The chatbot can also respond to friendly greetings and give suggestions for book names using fuzzy matching.

Key Features:
List available books: Users can see which books are currently available for borrowing.
Check availability: Users can check if a specific book is available or already borrowed by someone else.
Borrow books: Users can borrow available books by entering their name.
Return books: Users can return previously borrowed books by confirming the book and their name.
Book descriptions: Provides a brief description of the books available in the library.
Friendly interactions: The chatbot recognizes basic greetings and responds accordingly.
Book suggestions: If users input an unclear book name, the chatbot will suggest the closest matching book title.
How It Works:
Class Library: Manages the internal logic of the library, including the list of books, borrowing/returning functionality, and book availability checks.
Main chatbot function: Facilitates the interactive chat-based user experience, handling inputs, and calling the necessary methods in the Library class to process user commands.
Natural interaction: The chatbot supports friendly, conversational inputs such as greetings ("hello", "hi", "good morning", etc.) and common phrases like "thank you" or "bye".
Time-based greetings: The chatbot greets the user with a time-sensitive message (Good morning, Good afternoon, Good evening).
Technologies Used:
Python: The chatbot is implemented in Python and uses the standard library (datetime and difflib) for time-based greeting and fuzzy matching for book suggestions.
Example Interaction:
bash
Copy code
Chatbot: Hello! Welcome to the Library Management Chatbot!
Chatbot: Good afternoon! How can I assist you today?

You: list books
Chatbot: Here are the available books: 1984, To Kill a Mockingbird, The Great Gatsby, Moby Dick

You: borrow 1984
Chatbot: Please enter your name:
You: Alice
Chatbot: You have successfully borrowed '1984'.

You: return 1984
Chatbot: Please enter your name:
You: Alice
Chatbot: You have successfully returned '1984'.

You: description of The Great Gatsby
Chatbot: Here's a description of 'The Great Gatsby': A novel by F. Scott Fitzgerald that critiques the American Dream through the story of Jay Gatsby.

You: bye
Chatbot: Goodbye! Have a great day!
Installation Instructions:
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/library-management-chatbot.git
Navigate to the project directory:

bash
Copy code
cd library_management-chatbot
Run the chatbot:

bash
Copy code
python chatbot.py








