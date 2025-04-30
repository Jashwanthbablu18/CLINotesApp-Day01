# Day 1 - Note taking CLI app.
# topic - Programming Basics.

# Importing Datetime module for time stamps.
import datetime

# A Function to represent introduction of this assignment / Project. Starting with a little welcome message.
def show_intro():
    print("🔹 Welcome to Day 1 of Python 30-Day Challenge!")
    print("🔹 Topic: Programming Basics")
    print("🔹 What is a program?")
    print("   👉 A program is a set of instructions that a computer can follow to perform a task.")
    print("   👉 In this app, we’re writing instructions to take and save our notes.\n")

# To save a note to a text file.
def save_note(MyNote):
    now = datetime.datetime.now()

    # Time stamp for note.
    stamp = now.strftime("%d-%m-%Y, %H:%M:%S")  

    # Open's notes.txt in append mode to write new content / new note into notes.txt file.  Appends the note with time stamp.
    with open("notes.txt", "a") as f:
        f.write(f"[{stamp}] {MyNote}\n")

    # Displays success message after successful append of note into notes.txt file.
    print("✅ Note saved successfully!\n")

# A Function to display the contents of notes.txt file. It opens the notes.txt file in read mode to read contents of file.
def view_notes():
    try:
        # Handles the error by opening file in read mode.
        with open("notes.txt", "r") as f:
            print("\n📝 Your Notes Log:\n------------------")

            # Reading the file.
            all_notes = f.read()

            # If file have contents then it dispalys if not displays else statement.
            print(all_notes if all_notes else "(No notes yet?)")  

            # If file not found it can be handled by this instruction.
    except FileNotFoundError:
        print("⚠️ No notes found yet. Start by adding one!\n")

# Main function.
def main():

    # Calling intro function to give introduction about assignment.
    show_intro()

    # A loop to run over the file. To write, read and exit.
    while True:
        print("Choose an option:")
        print("1> Add a new note")
        print("2> View notes")
        print("3> Exit")
        
        # User choosing option.
        user_choice = input("Enter your choice (1/2/3): ")

        ## If user chooses option 1:
        if user_choice == "1":

            # Taking input note from user.
            new_note = input("🖊️ Enter your note: ")

            # Appending new note into notes file by calling save_note() function.
            save_note(new_note)

        ## If user chooses option 2:
        elif user_choice == "2":

            # Calling view_notes() function to read content from file.
            view_notes()

        ## If user chooses option 3:
        elif user_choice == "3":
            print("👋 Exiting Note-Taking app...")
            break

        # If user opts invalid selection, then that is managed by this instruction.
        else:
            print("❌ Invalid option. Please try again\n")

# calling main() to starting execution of program
if __name__ == "__main__":
    main()