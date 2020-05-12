class SuperList(list):
    items = []

    def append(self, item):
        self.items.append(item)

    def __getitem__(self, index):
        return self.items[index]

    def __len__(self):
        return self.items.__len__()


super_list = SuperList()
super_list.append(3)
super_list.append(4)
super_list.append('hi')
super_list.append('hi')
super_list.append('hi')
super_list.append('hi')
print(super_list[1])
print(len(super_list))
print(issubclass(SuperList, list))
