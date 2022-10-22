from collections.abc import Iterable


class LinkedList:
    class __Node:
        def __init__(self, value: int) -> None:
            self.value = value
            self.nxt = None

    def __init__(self, *args) -> None:
        length = len(args)
        self.__length = length
        self.__head = self.__Node(args[0]) if length > 0 else None
        self.__tail = self.__head
        for i in range(1, length):
            self.__tail.nxt = self.__Node(args[i])
            self.__tail = self.__tail.nxt

    def __iter__(self) -> Iterable[int]:
        current = self.__head
        while current is not None:
            yield current.value
            current = current.nxt

    def __str__(self) -> str:
        return f"[{' '.join(str(i) for i in self)}]"

    def __len__(self) -> int:
        return self.__length

    def __index_check(self, index: int) -> None:
        if not 0 <= index < self.__length:
            raise IndexError

    def append(self, value: int) -> None:
        if self.__length > 0:
            self.__tail.nxt = self.__Node(value)
            self.__tail = self.__tail.nxt
        else:
            self.__head = self.__tail = self.__Node(value)
        self.__length += 1

    def get(self, index: int) -> int:
        self.__index_check(index)
        current = self.__head
        for _ in range(index):
            current = current.nxt
        return current.value

    def remove(self, index: int) -> None:
        self.__index_check(index)
        if self.__length == 1:
            self.__head = self.__tail = None
        elif index == 0:
            self.__head = self.__head.nxt
        else:
            current = self.__head
            for _ in range(index - 1):
                current = current.nxt
            current.nxt = current.nxt.nxt
            if index == self.__length - 1:
                self.__tail = current
        self.__length -= 1


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
