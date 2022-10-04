#!/usr/bin/python3



class MyList(list):

    def print_sorted(self):
        rtn = self.copy()
        rtn.sort()
        print(rtn)
