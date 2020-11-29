class Node():
    """Узел очереди."""
    def __init__(self, contained_object, next_object):
        """Конструктор: ссылки на содержащийся объект и последующий элементы."""
        self.contained_object = contained_object
        self.next_object = next_object
        # print("Узел " + self.contained_object.title() + " создан!")

class MyQueue():
    """Очередь. Нужно указать ссылку на голову."""
    def __init__(self, head):
        self.head = head
        self.head = Node(head, "")
        # print("Очередь, в голове которой находится элемент \"" + self.head.contained_object + "\", создана!")

    def add(self, new_node):
        if self.head.next_object == "":
            self.head.next_object = Node(new_node, "")
            return
        move = self.head
        while move.next_object != "":
            move = move.next_object
        move.next_object = Node(new_node, "")
        # print("Элемент " + str(new_node) + " добавлен в очередь.")

    def remove(self, node_name):
        move = self.head
        if move.contained_object == node_name:
            self.head = move.next_object
            return
        while move.next_object.contained_object != node_name:
            move = move.next_object
            if move.next_object == "":
                print("Элемента \"" + str(node_name) + "\" нет в очереди.")
                return
        if move.next_object.next_object == "":
            move.next_object = ""
            return
        move.next_object = move.next_object.next_object

    def clear(self):
        self.head.next_object = ""

    def Queue_2_list(self):
        Queue_2_list = []
        if self.head.next_object == "":
            Queue_2_list.append(self.head.contained_object)
            return Queue_2_list
        move = self.head
        while move.next_object != "":
            Queue_2_list.append(move.contained_object)
            move = move.next_object
        Queue_2_list.append(move.contained_object)
        return Queue_2_list


new_queue = MyQueue("Первый")
new_queue.add("Второй")
new_queue.add("Третий")
new_queue.add("Четвёртый")
# new_queue.add("5")

# print("This is 2nd object: " + str(new_queue.head.next_object.contained_object))
print(new_queue.Queue_2_list())

new_queue.remove("5")
print(new_queue.Queue_2_list())

new_queue.clear()
print(new_queue.Queue_2_list())

# print("")
# print(new_queue.head.contained_object)
# print(new_queue.head.next_object)