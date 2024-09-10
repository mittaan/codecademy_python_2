from dataset import get_dataset, normalize_string, matches, same_length

class HashMap:
    def __init__(self):
        self.dataset, self.info = get_dataset()
        self.searched_items = {}
        self.searched_keys = {}
        self.history = [(None, None) for _ in range(5)]

    def get_data(self, key: str) -> str:
        return self.dataset.get(key)
    
    def get_info(self, idx: int) -> str:
        return self.info[idx]
    
    def update_dataset(self) -> None:
        self.dataset = self.searched_items.copy()

    def set_searched_item(self, key: str) -> None:
        payload = self.get_data(key)
        self.searched_items.update({key: payload})

    def set_searched_keys(self, idx: str, key:str) -> None:
        self.searched_keys.update({idx: key})

    def get_searched_item(self, key: str) -> str:
        return self.searched_items.get(key)

    def clear_search(self, key: str) -> None:
        self.history.append((key, self.searched_items.get(key)))
        self.history.pop(0)
        self.searched_items.clear()
        self.searched_keys.clear()
        self.dataset = get_dataset()

    def update_searched_items(self, search_input: str) -> None:
        self.searched_items.clear()
        search_input_normalized = normalize_string(search_input)
        for key in self.dataset.keys():
            normalized_key = normalize_string(key)
            if (matches(search_input_normalized, normalized_key) or matches(search_input, key)) and (same_length(search_input_normalized, normalized_key) or same_length(search_input, key)):
                self.set_searched_item(key)
                break
            if matches(search_input_normalized, normalized_key) or matches(search_input, key):
                self.set_searched_item(key)
        self.update_dataset()

    def is_empty(self, dictionary: dict) -> bool:
        return dictionary == {}
    
    def print_searched_items(self) -> None:
        self.searched_keys.clear()
        for idx, item in enumerate(list(self.searched_items)):
            self.set_searched_keys(str(idx+1), item)
            print(f'{idx+1}: {item}')
        print()

    def print_info(self) -> None:
        for idx in range(1, len(self.info)):
            info = self.get_info(idx)
            cleaned_info = info.replace('_', ' ')
            print(f'{idx}: {cleaned_info}')

    def display_history(self) -> None:
        print('Last 5 exercises searched:')
        for search, content in self.history[::-1]:
            if search or content:
                print(f'• {search}')

    def list_searched_keys(self) -> list[str]:
        key_indexes = list(self.searched_keys.keys())
        key_indexes.sort()
        return key_indexes

    def get_user_choice(self, user_choice: str) -> str:
        key = self.searched_keys.get(user_choice)
        return self.get_searched_item(key)