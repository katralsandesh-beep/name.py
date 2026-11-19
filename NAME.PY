def main():
    # Prompt the user to enter their name
    name = input("Enter your name: ").strip()
    
    # Display a personalized greeting message
    if name:
        print(f"Hello, {name}! Welcome to your Python program.")
    else:
        print("Hello, stranger! Welcome to your Python program.")

if __name__ == "__main__":
    main()
