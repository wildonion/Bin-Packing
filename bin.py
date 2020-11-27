
import numpy as np

class Bin(object):
    def __init__(self):
        self.items = []
        self.sum = 0

    def append(self, item):
        self.items.append(item)
        self.sum += item

    def __str__(self):
        return f'Bin(sum={self.sum}, items={str(self.items)})'


def pack(values, capacity):
    values = sorted(values, reverse=True) # decreasing!
    bins = [] # a list of all bins

    for item in values:
        # Try to fit item into a bin
        for bin in bins:
            if bin.sum + item <= capacity:
                bin.append(item)
                break
        else:
            # item didn't fit into any bin, start a new bin
            bin = Bin()
            bin.append(item)
            bins.append(bin)

    return bins


# def packAndShow(objects, capacity):

#         print(f'[+] List with sum {sum(objects)} , requires at least {sum(objects)+capacity-1/capacity} bins')
#         bins = pack(objects, capacity)
#         print(f'[+] Solution using {len(bins)} bins')
#         for bin in bins:
#             print(bin)