class Array:

    def __init__(self) -> None:
        self.length = 0
        self.data = {}

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length += 1

    def __str__(self) -> str:
        return str({"length": self.length, "data": self.data})

    def pop(self):
        item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return item

    def shift_items(self, index):

        while index < self.length - 1:
            self.data[index] = self.data[index + 1]

            index += 1

        del self.data[self.length - 1]
        self.length -= 1

    def delete(self, index):
        value = self.data[index]

        self.shift_items(index)

        return value

    def re_arrange_items_for_insert(self, index):
        index_top = self.length

        while index_top > index:
            self.data[index_top] = self.data[index_top - 1]

            index_top -= 1

    def insert(self, index, value):

        self.re_arrange_items_for_insert(index)
        self.data[index] = value

        self.length += 1


new_array = Array()
new_array.push("Hi")

# print(new_array.get(0))
new_array.push("There")
new_array.push("There")
new_array.push("you")
new_array.push("are")


print(new_array)
item = new_array.pop()
print(item)

print(new_array)
item = new_array.delete(1)
print(new_array)


new_array.insert(1, "How are you")

print(new_array)
