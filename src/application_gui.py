from src.fetch_criterion import fetch_criterion
from src.fetch_criteria import fetch_criteria
from src.process_application import process_application
from src.application import Application

def quit():
    print('Exiting...')
    exit()


def print_available_criteria(criteria_list):
    print('Available criteria to choose from: \n')

    for i, criterion in enumerate(criteria_list):
        print(f' {i + 1}. {criterion}\n') 
    print()


def is_numeric_input(input):
    return all(item.strip().isdigit() for item in input.split(','))


def convert_to_indices(input):
    return [int(item.strip()) for item in input.split(',')]


def validate_indices(indices, criteria_list):
    return all(1 <= criteria <= len(criteria_list) for criteria in indices)


def select_criteria_by_indices(indices, criteria_list):
    return [criteria_list[criteria - 1] for criteria in indices]


def get_criteria(criteria_list):
    while True:
        criteria_input = input(
            'Enter the numbers of the criteria you want to use separated by commas (e.g., 1,2,3). Enter \'q\' to quit: ')

        if criteria_input.lower() == 'q':
            quit()

        if not is_numeric_input(criteria_input):
            print('Invalid input. Please enter a number or a list of numbers separated by commas.')
            continue

        indices = convert_to_indices(criteria_input)

        if not validate_indices(indices, criteria_list):
            print('Invalid input. Please enter a number or a list of numbers separated by commas.')
            continue

        return select_criteria_by_indices(indices, criteria_list)


def fetch_input_to_start_application():
    while True:
        user_input = input('\nWould you like to create an application? [y] / [n] : \n').strip().lower()

        if user_input == 'y':
            return True

        elif user_input == 'n':
            return quit()

        else:
            print("Invalid input. Enter 'y' for yes or 'n' for no.")


def input_values_for_selected_criteria(selected_criteria):
    user_inputs = {}

    for criterion in selected_criteria:
        formatted_criterion = criterion.replace(' ', '_')

        while True:
            value = input(f"\nEnter value for {criterion}, True or False, [t] / [f]: \n").strip().lower()

            if value in ['t', 'f']:
                user_inputs[formatted_criterion] = value == 't'
                break

            else:
                print("\nInvalid input. Please enter 't' for true or 'f' for false.\n")


    return user_inputs


def evaluate_application_results(results):

    if all(result[0].name == 'PASS' for result in results):
        print('\nApplication has PASSED:\n')

    else:
        print('\nApplication has FAILED:\n')

def create_application(user_inputs):
    return Application(**user_inputs)

def format_results(results):
    return '\n\n'.join(f' - {result[1]}' for result in results)

def application_synopsis(results):
    evaluate_application_results(results)

    print(format_results(results))

    

def main():
    criteria_list = fetch_criteria()

    print_available_criteria(criteria_list)

    selected_criteria = get_criteria(criteria_list)

    formatted_criteria = '\n\n'.join(f'- {criterion}' for criterion in selected_criteria)
    print(f"\nSelected criteria:\n\n{formatted_criteria}\n")

    while fetch_input_to_start_application():

        user_inputs = input_values_for_selected_criteria(selected_criteria)

        app = create_application(user_inputs)

        criterion_feedback = [fetch_criterion(criterion) for criterion in selected_criteria]

        results = [process_application(app, feedback) for feedback in criterion_feedback]

        application_synopsis(results)

                    
if __name__ == '__main__':
    main()
