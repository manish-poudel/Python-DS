# Example of defining custom iterator class

class SequenceIterator:

    def __init__(self, sequence):
        self._seq = sequence
        self._k = -1

    def __next__(self):
        self._k = self._k + 1
        if self._k < len(self._seq):
            return self._seq[self._k]
        else:
            return StopIteration()

    def __getitem__(self, item):
        return self._seq[item]

    def __len__(self):
        return len(self._seq)

    def __iter__(self):
        return self
