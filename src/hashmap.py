from dataset import get_dataset, normalize_string, matches

class HashMap:
    def __init__(self, size=0):
        self.size = size
        self.dataset = get_dataset()
        self.searched_items = {}
        self.history = []

    def get_data(self, key):
        return self.dataset.get(key)

    def set_searched_item(self, key):
        payload = self.get_data(key)
        self.searched_items.update({key: payload})

    def get_searched_item(self, key):
        return self.searched_items.get(key)

    def delete_search(self, key):
        self.history.append((key, self.searched_items.get(key)))
        self.searched_items.clear()

    def update_searched_items(self, search_input):
        search_input_normalized = normalize_string(search_input)
        for key in self.dataset:
            normalized_key = normalize_string(key)
            if matches(search_input_normalized, normalized_key) or matches(search_input, key):
                self.set_searched_item(key)

    def is_dataset_empty(self):
        return self.dataset == {}


def get_alphanumeric_characters():

    letters = [chr(i).upper() + chr(i) for i in range(97, 123)]
    numbers = [str(i) for i in range(10)]

    alphanumeric_characters = numbers + letters

    return alphanumeric_characters

# def get_user_input():
#     valid_characters = get_alphanumeric_characters()
#     search_input = ''

#     while True:
#         user_input = input()
#         if user_input in valid_characters:
#             search_input += user_input

    
