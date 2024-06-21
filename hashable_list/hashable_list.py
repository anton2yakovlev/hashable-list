from uuid import uuid4, UUID


class HashableList(list):
    def __init__(self, *args):
        super().__init__(args)
        self.hash_key = int(uuid4())

    def __hash__(self) -> UUID:
        return self.hash_key
