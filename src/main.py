from hashmap import HashMap

def is_search_complete(message: str) -> bool:
    user_choice = input(message)
    user_choice = user_choice.lower()

    if user_choice in ['y', 'n']:
        return user_choice == 'y'
    else:
        return None

def get_alphanumeric_characters() -> list[str]:

    lowercase_letters = [chr(i) for i in range(97, 123)]
    uppercase_letters = [chr(i).upper() for i in range(97, 123)]
    numbers = [str(i) for i in range(10)]

    alphanumeric_characters = numbers + lowercase_letters + uppercase_letters

    return alphanumeric_characters

def get_user_input(valid_characters: list[str], hash_table: HashMap, search_input='', repeated=False) -> None:
    if repeated == True:
        hash_table.display_history()

    current_searched_items = len(hash_table.searched_items)

    while not hash_table.is_empty(hash_table.dataset):
        user_input = input(f'Enter your search:\n{search_input}')

        if user_input in valid_characters:
            search_input += user_input
        elif len(user_input) > 1:
            for character in user_input:
                if character in valid_characters:
                    search_input += character
                else:
                    print('\nInvalid character found.\nPlease, enter a valid character: ')
                    break
        else:
            print('\nChoose a different character: ')
            continue

        hash_table.update_searched_items(search_input)
        updated_search_items = len(hash_table.searched_items)

        if hash_table.is_empty(hash_table.searched_items):
            print('\nThere is no exercise matching the search.\n')
            return
        
        if updated_search_items == 1:
            print(f'\nCurrently searching for "{search_input}".\n')
            hash_table.print_searched_items()
            break
        elif current_searched_items == updated_search_items:
            print(f'\nCurrently searching for "{search_input}".\n')
            hash_table.print_searched_items()

            while True:
                end_search = is_search_complete('Is the exercise you were looking for in the list above? [y/n]: ')
                if end_search == None:
                    print('Please choose either "y" or "n".')
                    continue
                else:
                    break

            if end_search == True:
                break
            else:
                continue
        else:
            current_searched_items = updated_search_items
            print(f'\nCurrently searching for "{search_input}".')
            hash_table.print_searched_items()

    searched_exercise = {}

    if updated_search_items != 1:
        while True:
            search_options = hash_table.list_searched_keys()
            user_choice = input(f'Choose one of the following options: {search_options}\n')

            if user_choice in search_options:
                searched_exercise.update(hash_table.get_user_choice(user_choice))
                break
    else:
        print(f'Only one exercise left: {hash_table.searched_keys.get("1")}\nReady to display info...\n')
        searched_exercise.update(hash_table.get_user_choice('1'))

    indexes_to_string = [str(idx) for idx in range(1, len(hash_table.info))]

    while True:
        print('Which info are you interested in? Choose the number associated to that category:')
        hash_table.print_info()
        chosen_info = input()

        if chosen_info in indexes_to_string:
            info = hash_table.get_info(int(chosen_info))
            print(f'\nYou have chosen "{info}":\n{searched_exercise.get(info)}\n')

            while True:
                request_more_info = is_search_complete('Do you need more info about this exercise? [y/n]: ')
                if request_more_info == None:
                    print('Please choose either "y" or "n".')
                    continue
                else:
                    break

            if request_more_info == False:
                return hash_table.searched_keys.get('1')


if __name__ == '__main__':

    valid_characters = get_alphanumeric_characters()
    repeated = False
    data = HashMap()

    while True:
        result_key = get_user_input(valid_characters, data, repeated=repeated)
        while True:
            search_again = is_search_complete('Do you want to search another exercise? [y/n] ')
            if search_again == True:
                data.clear_search(result_key)
                repeated = True
                break
            elif search_again == False:
                exit()
            else:
                print('Please choose either "y" or "n".')
                continue