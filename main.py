def print_greetings(unprinted_greetings, completed_greetings):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_greetings:
        current_greetings = unprinted_greetings.pop()
        print(f"Printing greeting: {current_greetings}")
        completed_greetings.append(current_greetings)


def show_completed_greetings(completed_greetings):
    """Show all the models that were printed."""
    print("\nThe following greetings have been printed:")
    for completed_greeting in completed_greetings:
        print(completed_greeting)


unprinted_greetings = ['Wazzzzz Up!', 'Yo!', 'Duuude!']
completed_greetings = []

print_greetings(unprinted_greetings, completed_greetings)

show_completed_greetings(['Wazzzzz Up!', 'Yo!', 'Duuude!'])

print(unprinted_greetings)
print(completed_greetings)
