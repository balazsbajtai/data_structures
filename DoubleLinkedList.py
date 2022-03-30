class Element:
    """
    Helper class for LinkedList.
    """
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class LinkedList:
    """
    LinkedList class where each element is linked to the previous element.
    """
    def __init__(self, head=None):
        self.head = head

    def __getitem__(self, item):
        return self.get_element(item)

    def __setitem__(self, key, value):
        self.set_element(key, value)

    def __len__(self):
        return self.length()

    def length(self):
        """Returns the length of the LinkedList.

        :return: Integer - length of the list.
        """
        if self.head is None:
            return 0
        else:
            length = 1
            iterator = self.head
            while iterator.next:
                length += 1
                iterator = iterator.next

            return length

    def get_element(self, index):
        """Returns the element at the given index.

        :param index: Integer - position of the element in the list.
        :return: Object - the element at the given index.
        """
        if index < 0 or index > self.length() - 1:
            raise IndexError('Invalid index.')
        else:
            position = 0
            iterator = self.head
            while position != index:
                iterator = iterator.next
                position += 1

            return iterator.data

    def set_element(self, index, data):
        """Sets the element at the given index to the provided object.

        :param index: Integer - position of the element to set.
        :param data: Object - the data for the element to be set.
        """
        if index < 0 or index > self.length() - 1:
            raise IndexError('Invalid index.')
        else:
            position = 0
            iterator = self.head
            while position != index:
                iterator = iterator.next
                position += 1

            iterator.data = data

    def insert_at_start(self, value):
        """Inserts a provided element at the start of the list.

        :param value: Object - the data to be inserted to the start of the list.
        """
        if self.head is None:
            self.head = Element(value)
        else:
            element = Element(value)
            element.next = self.head
            self.head.prev = element
            self.head = element

    def insert_at_end(self, value):
        """Inserts a provided element at the end of the list.

        :param value: Object - the data to be inserted to the end of the list.
        """
        if self.head is None:
            self.head = Element(value)
        else:
            last_element = self.head
            while last_element.next:
                last_element = last_element.next

            element = Element(value)
            element.prev = last_element
            last_element.next = element

    def insert_at_index(self, index, value):
        """Inserts an element at the provided index of the list.

        :param index: Integer - the position of the element to be inserted.
        :param value: Object - the data to be inserted to the provided index.
        """
        if index < 0 or index > self.length() - 1:
            raise IndexError('Invalid index.')
        else:
            position = 0
            iterator = self.head
            while position != index - 1:
                iterator = iterator.next
                position += 1

            element = Element(value)
            element.next = iterator.next
            element.prev = iterator
            iterator.next.prev = element
            iterator.next = element

    def insert_before_element(self, element_value, element_before):
        """Inserts a provided element before another element in the list.

        :param element_value: Object - the data to be inserted.
        :param element_before: Object - the element before which the data is inserted.
        """
        if element_before in self.get_elements():
            iterator = self.head
            if iterator.data == element_before:
                new_element = Element(element_value)
                new_element.next = iterator
                self.head = new_element
            else:
                while iterator.next:
                    if iterator.next.data == element_before:
                        new_element = Element(element_value)
                        new_element.next = iterator.next
                        new_element.prev = iterator
                        iterator.next.prev = new_element
                        iterator.next = new_element
                        break

                    iterator = iterator.next
        else:
            print("Element doesn't exist in the LinkedList.")

    def insert_after_element(self, element_value, element_after):
        """Inserts a provided element after another element in the list.

        :param element_value: Object - the data to be inserted.
        :param element_after: Object - the element after which the data is inserted.
        """
        if element_after in self.get_elements():
            iterator = self.head
            if iterator.data == element_after:
                new_element = Element(element_value)
                new_element.next = iterator.next
                iterator.next = new_element
            else:
                while iterator.next:
                    iterator = iterator.next
                    if iterator.data == element_after:
                        new_element = Element(element_value)
                        new_element.next = iterator.next
                        new_element.prev = iterator
                        iterator.next.prev = new_element
                        iterator.next = new_element
                        break
        else:
            print("Element doesn't exist in the LinkedList.")

    def insert_range(self, insert_range):
        """Inserts a range of provided values to the list. Doesn't keep previous values.

        :param insert_range: List - The list of values to be inserted.
        """
        if len(insert_range) == 0:
            raise IndexError('Invalid index.')
        else:
            self.head = Element(insert_range[0])
            iterator = self.head
            for i in range(1, len(insert_range)):
                new_element = Element(insert_range[i])
                iterator.next = new_element
                iterator = iterator.next
                iterator.prev = new_element

    def delete_at_start(self):
        """Deletes the first element in the list.
        """
        if self.head and self.head.next:
            self.head = self.head.next

    def delete_at_end(self):
        """Deletes the last element in the list.
        """
        if self.head and self.head.next:
            iterator = self.head
            while iterator.next.next:
                iterator = iterator.next
            iterator.next = None
        elif self.head:
            self.head.next = None

    def delete_at_index(self, index):
        """Deletes an element at the given index.

        :param index: Integer - index of element to be deleted.
        """
        if index < 0 or index > self.length() - 1:
            raise IndexError('Invalid index.')
        else:
            position = 0
            iterator = self.head
            while position != index - 1:
                iterator = iterator.next
                position += 1

            iterator.next.next.prev = iterator
            iterator.next = iterator.next.next

    def delete_by_value(self, element_value):
        """Deleted a provided element from the list based on it's value.

        :param element_value: Object - the element to be deleted.
        """
        if element_value in self.get_elements():
            position = 0
            iterator = self.head
            while iterator.next:
                if iterator.data == element_value:
                    self.delete_at_index(position)
                    break
                iterator = iterator.next
                position += 1

    def clear(self):
        """Clears the list.
        """
        self.head = None

    def get_elements(self):
        """Returns all elements in the list.

        :return: List - all elements in the list.
        """
        if self.head is None:
            return None
        else:
            list_of_elements = []
            iterator = self.head
            if iterator.next is None:
                list_of_elements.append(iterator.data)
            else:
                list_of_elements.append(iterator.data)
                while iterator.next:
                    iterator = iterator.next
                    list_of_elements.append(iterator.data)

            return list_of_elements

    def print_elements(self):
        """Prints all elements in the list.
        """
        if self.head is None:
            print('LinkedList is empty.')
        else:
            print(self.get_elements())


if __name__ == '__main__':

    ll = LinkedList()
    print('\nInsert at start: orange, mandarin')
    ll.insert_at_start('orange')
    ll.insert_at_start('mandarin')
    print('Insert at end: lemon, mango')
    ll.insert_at_end('lemon')
    ll.insert_at_end('mango')
    ll.print_elements()

    print('\nInsert at index 2 apple')
    ll.insert_at_index(2, 'apple')
    ll.print_elements()
    print('List length: {}'.format(ll.length()))

    print("\nInsert range: 'football', 'basketball', 'rugby', 'tennis', 'golf'")
    ll.insert_range(['football', 'basketball', 'rugby', 'tennis', 'golf'])
    ll.print_elements()
    print('List length: {}'.format(ll.length()))

    print('\nDelete at index 2')
    ll.delete_at_index(2)
    ll.print_elements()
    print('List length: {}'.format(ll.length()))

    print('\nGet element 1 twice')
    print(ll.get_element(1))
    print(ll[1])
    print('\nSet element 1 to hockey')
    ll[1] = 'hockey'
    print(ll[1])
    ll.print_elements()
    print('List length: {}'.format(ll.length()))

    print('\nInsert rugby before hockey')
    ll.insert_before_element('rugby', 'hockey')
    print('Insert basketball after tennis')
    ll.insert_after_element('basketball', 'tennis')
    ll.print_elements()
    print('List length: {}'.format(ll.length()))

    print('\nDelete basketball by value')
    ll.delete_by_value('basketball')
    ll.print_elements()
    print('List length: {}'.format(ll.length()))

    print('\nClear list')
    ll.clear()
    ll.print_elements()
