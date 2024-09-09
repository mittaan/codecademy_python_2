from dataset import get_dataset, normalize_string, matches

class HashMap:
    def __init__(self):
        self.dataset = get_dataset()
        self.searched_items = {}
        self.searched_keys = {}
        self.history = []

    def get_data(self, key):
        return self.dataset.get(key)

    def set_searched_item(self, key):
        payload = self.get_data(key)
        self.searched_items.update({key: payload})

    def set_searched_keys(self, idx, key):
        self.searched_keys.update({idx: key})

    def get_searched_item(self, key):
        return self.searched_items.get(key)

    def delete_search(self, key):
        self.history.append((key, self.searched_items.get(key)))
        self.searched_items.clear()
        self.searched_keys.clear()
        self.dataset = get_dataset()

    def update_searched_items(self, search_input):
        search_input_normalized = normalize_string(search_input)
        for key in self.dataset:
            normalized_key = normalize_string(key)
            if matches(search_input_normalized, normalized_key) or matches(search_input, key):
                self.set_searched_item(key)
        self.dataset = self.searched_items.copy()

    def is_empty(self, dictionary):
        return dictionary == {}
    
    def print_searched_items(self):
        idx = 1
        for item in self.searched_items:
            self.set_searched_keys(idx, item)
            print(f'{str(idx)}: {item}')

    def list_searched_keys(self):
        key_indexes = list(self.searched_keys.keys())
        key_indexes.sort()
        return key_indexes

    def get_user_choice(self, user_choice):
        return self.searched_keys.get(user_choice)
            

def is_search_complete():
    user_choice = input('Is the exercise you were looking for in the list above?')
    user_choice = user_choice.lower()

    if user_choice in ['y', 'n']:
        return user_choice == 'y'
    else:
        return None

def get_alphanumeric_characters():

    lowercase_letters = [chr(i) for i in range(97, 123)]
    uppercase_letters = [chr(i).upper() for i in range(97, 123)]
    numbers = [str(i) for i in range(10)]

    alphanumeric_characters = numbers + lowercase_letters + uppercase_letters

    return alphanumeric_characters

def get_user_input():
    valid_characters = get_alphanumeric_characters()
    search_input = ''
    hash_table = HashMap()
    current_searched_items = len(hash_table.searched_items)

    while not hash_table.is_empty(hash_table.dataset):
        user_input = input('\nEnter your search:\n')
        if user_input in valid_characters:
            search_input += user_input
        else:
            print('\nChoose a different character:')
            continue
        hash_table.update_searched_items(search_input)
        updated_search_items = len(hash_table.searched_items)
        if hash_table.is_empty(hash_table.searched_items):
            print('\nThere is no exercise matching the search.')
            return
        if current_searched_items == updated_search_items:
            print(f'\nCurrently searching for "{search_input}".')
            hash_table.print_searched_items()
            while True:
                end_search = is_search_complete()
                if end_search == None:
                    print('Please choose either "y" or "n".')
                    continue
                else:
                    break
            if end_search:
                break
            else:
                continue
        else:
            current_searched_items = updated_search_items
            print(f'\nCurrently searching for "{search_input}".')
            hash_table.print_searched_items()

    while True:
        search_options = hash_table.list_searched_keys()
        user_choice = input(f'Choose one of the following options: {search_options}')
        if user_choice in search_options:
            return # TODO Either return the data or create a second function to ask which data is relevant (or maybe format all of it)


get_user_input()