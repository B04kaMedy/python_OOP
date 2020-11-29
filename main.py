class Node():
    def __init__(self, contained_object, next_object):
        self.contained_object = contained_object
        self.next_object = next_object


class MyQueue():
    def __init__(self):
        self.head = ""

    def add(self, new_node):
        if self.head == "":
            self.head = Node(new_node, "")
            return
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
        self.head = ""

    def Queue_2_list(self):
        Queue_2_list = []
        if self.head == "":
            return Queue_2_list
        if self.head.next_object == "":
            Queue_2_list.append(self.head.contained_object)
            return Queue_2_list
        move = self.head
        while move.next_object != "":
            Queue_2_list.append(move.contained_object)
            move = move.next_object
        Queue_2_list.append(move.contained_object)
        return Queue_2_list


class Country():
    def __init__(self, population, capital, language):
        self.population = population
        self.capital = capital
        self.language = language

    def __str__(self):
        return 'Country( \n    population: '+str(self.population)+',\n    capital: '+self.capital+',\n    language: '+self.language+'\n)\n'


# Countries
Russia = Country(144000000, "Moscow", "Ru")
Finland = Country(5570000, "Helsinki", "Finnish")
Australia = Country(25200000, "Canberra", "Australian English")

countries = MyQueue()
countries.add(Russia)
countries.add(Finland)
countries.add(Australia)

# Вывод в виде очереди
move = countries.head
print(move.contained_object)
while move.next_object != "":
    move = move.next_object
    print(move.contained_object)

# Numbers

numbers = MyQueue()
numbers.add(0)
numbers.add(1)
numbers.add(2)
numbers.add(3)
numbers.add(4)

# Вывод в виде очереди
move = numbers.head
print(move.contained_object)
while move.next_object != "":
    move = move.next_object
    print(move.contained_object)
