from uuid import uuid4
from typing import Any, Callable, Iterable, List, Iterator, Union, overload, Optional


class HashableList:
    def __init__(self, *args: Union[Any, Iterable[Any]]) -> None:
        items: Optional[List[Any]] = None
        if (
            len(args) == 1
            and isinstance(args[0], Iterable)
            and not isinstance(args[0], (str, bytes, bytearray))
        ):
            items = list(args[0])
        else:
            items = list(args)

        self.items = items
        self.hash_key = int(uuid4())

    def __hash__(self) -> int:
        return self.hash_key

    def __getitem__(self, index: int) -> Any:
        return self.items[index]

    def __setitem__(self, index: int, value: Any) -> None:
        self.items[index] = value

    def __delitem__(self, index: int) -> None:
        del self.items[index]

    def __len__(self) -> int:
        return len(self.items)

    def __iter__(self) -> Iterator[Any]:
        return iter(self.items)

    def __contains__(self, item: Any) -> bool:
        return item in self.items

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, HashableList):
            return self.items == other.items
        if isinstance(other, list):
            return self.items == other
        return False

    def append(self, value: Any) -> None:
        self.items.append(value)

    def extend(self, values: Iterable[Any]) -> None:
        self.items.extend(values)

    def insert(self, index: int, value: Any) -> None:
        self.items.insert(index, value)

    def remove(self, value: Any) -> None:
        self.items.remove(value)

    def pop(self, index: int = -1) -> Any:
        return self.items.pop(index)

    def clear(self) -> None:
        self.items.clear()

    def index(self, value: Any, start: int = 0, end: Optional[int] = None) -> int:
        if end is None:
            end = len(self.items)
        return self.items.index(value, start, end)

    def count(self, value: Any) -> int:
        return self.items.count(value)

    def sort(
        self, *, key: Optional[Callable[[Any], Any]] = None, reverse: bool = False
    ) -> None:
        self.items.sort(key=key, reverse=reverse)

    def reverse(self) -> None:
        self.items.reverse()

    def copy(self) -> "HashableList":
        new_copy = HashableList(self.items)
        new_copy.hash_key = self.hash_key
        return new_copy

    def __repr__(self) -> str:
        return repr(self.items)
