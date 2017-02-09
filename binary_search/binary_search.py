class BinarySearch(list):



    def __init__(self, a, b, *args):
        """Initialise the list."""
        list.__init__(self, *args)
        self.items_length = a
        self.step = b

        end = self.items_length * self.step
        for i in range(self.step, end + 1, self.step):
            self.append(i)

    @property
    def length(self):

        return len(self)

    def search(self, element, low=0, high=None, count=0):
        
        if not high:
            high = self.length - 1

        if element == self[low]:
            return {'index': low, 'count': count}
        elif element == self[high]:
            return {'index': high, 'count': count}

        mid = (low + high) // 2
        if element == self[mid]:
            return {'index': mid, 'count': count}
        elif element > self[mid]:
            low = mid + 1
        elif element < self[mid]:
            high = mid - 1


        if low >= high:
            return {'index': -1, 'count': count}

        count += 1
        return self.search(element, low, high, count)
