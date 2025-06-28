def parse_input(user_input): # модуль розподілу команда + додаткові параметри
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):  # модуль перевірки на помилки
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Not enough arguments."
        except TypeError:
            return "Invalid input format."
    return inner

@input_error
def add_contact(args, contacts): # модуль добавки контакту
    name, phone = args 
    contacts[name] = phone # добавка номеру
    return "Contact added."
    
@input_error
def change_contact(args, contacts):  # модуль зміни контакту
    name, phone = args
    _ = contacts[name]   # Примусова перевірка на існування
    contacts[name] = phone
    return "Contact phone changed."

@input_error    
def show_phone(args, contacts):
    name = args [0]
    return ("Contact phone :" + contacts[name])
    
def all_phone(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])  # вивід списку построково

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]: # команда вихід
            print("Good bye!")
            break
        elif command in ["hello", "hi"]: # команда привіт
            print("How can I help you?")
        elif command == "add":            # команда добавити номер
            print(add_contact(args, contacts))
        elif command == "change":         # команда змінити номер
            print(change_contact(args, contacts))
        elif command == "phone":          # команда на запит номеру
            print(show_phone(args, contacts))
        elif command == "all":            # команда вивести все
            print(all_phone (contacts))
        elif command == "help":
            print("Available commands: add, change, phone, all, exit")

        else:
            print("Error: Invalid command.")    # команда не визначена

if __name__ == "__main__":
    main()