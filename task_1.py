# Створюємо зв'язний список
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    
    # Функція реверсування однозв'язного списку
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Сортування вставками для однозв'язного списку
    def sorted_insert(self, new_node):
        if self.head is None or self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def sort(self):
        sorted_list = LinkedList()
        current = self.head
        while current:
            next_node = current.next
            current.next = None
            sorted_list.sorted_insert(current)
            current = next_node
        self.head = sorted_list.head

# Функція для об'єднання двох відсортованих списків
def merge_sorted_lists(list1: LinkedList, list2: LinkedList) -> LinkedList:
    merged = LinkedList()
    dummy = Node()
    tail = dummy
    a = list1.head
    b = list2.head
    while a and b:
        if a.data <= b.data:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next
    if a:
        tail.next = a
    elif b:
        tail.next = b
    merged.head = dummy.next
    return merged

# Створюємо екземпляр зв'язного списку та перевіряємо всі функції
if __name__ == "__main__":
    print("1. Тест реверсу:")
    llist = LinkedList()
    for value in [1, 2, 3, 4, 5]:
        llist.insert_at_end(value)
    print("Оригінальний список:")
    llist.print_list()

    llist.reverse()
    print("Після реверсу:")
    llist.print_list()

    print("\n2. Тест сортування:")
    unsorted_list = LinkedList()
    for value in [4, 2, 5, 1, 3]:
        unsorted_list.insert_at_end(value)

    print("До сортування:")
    unsorted_list.print_list()

    unsorted_list.sort()
    print("Після сортування:")
    unsorted_list.print_list()

    print("\n3. Тест об'єднання:")
    list1 = LinkedList()
    list2 = LinkedList()

    for value in [1, 3, 5]:
       list1.insert_at_end(value)
    for value in [2, 4, 6]:
       list2.insert_at_end(value)

    print("Список 1:")
    list1.print_list()
    print("Список 2:")
    list2.print_list()

    merged = merge_sorted_lists(list1, list2)
    print("Об'єднаний список:")
    merged.print_list()