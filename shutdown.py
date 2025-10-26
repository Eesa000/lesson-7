def shutdown():
    user_input = input("Do you want to shut down the system? (Yes/No): ")

    if user_input == "Yes":
        print("Shutting down...")
    elif user_input == "No":
        print("Shutdown aborted.")
    else:
        print("Sorry.")

# Call the function
shutdown()
