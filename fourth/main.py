def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Name not found. Try adding the contact first."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command."
    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_data(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Phone number updated."
    else:
        raise KeyError


@input_error
def get_number(args, contacts):
    name = args[0]
    return contacts[name]


def get_all_info(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "stop"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_data(args, contacts))
        elif command == "phone":
            print(get_number(args, contacts))
        elif command == "all":
            print(get_all_info(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
