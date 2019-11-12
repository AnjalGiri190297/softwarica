import unittest
from tp import *
class Test_tp(unittest.TestCase):
    def test_bubble_sort(self):
        sort_by = 0
        list = [("2","Amrit","Pangeni","Eth Hacking","Nawalparasi","9847095399"),
                    ("1","Anjal","Giri","B.Computing","Kathmandu","9847095398"),
                    ("3","David","Joshi","B.Commerce","Dhangadi","9847095397")]
        ex_result=[("1","Anjal","Giri","B.Computing","Kathmandu","9847095398"),
                   ("2", "Amrit", "Pangeni", "Eth Hacking", "Nawalparasi", "9847095399"),
                   ("3", "David", "Joshi", "B.Commerce", "Dhangadi", "9847095397")]
        ac_result=Softwarica.bubble_sort(list,sort_by)
        self.assertEqual(ex_result,ac_result)

    def test_search(self):
            search_by = 1  # searching by First Name, Change values accordance to index value to searching by different parameters.
            search_for = "Amrit"
            array_test =[("2","Amrit","Pangeni","Eth Hacking","Nawalparasi","9847095399"),
                    ("1","Anjal","Giri","B.Computing","Kathmandu","9847095398"),
                    ("3","David","Joshi","B.Commerce","Dhangadi","9847095397")]

            expected_result = [("2","Amrit","Pangeni","Eth Hacking","Nawalparasi","9847095399")]
            mylist = Softwarica.search(array_test,search_by ,search_for)
            self.assertEqual(mylist, expected_result)


import unittest
# from tp import *

# class TestNewAlgorithm(unittest.TestCase):
#     def test_sort(self):
#             array_test=[('102', 'david', 'joshi','Ethical Hacking','rajgadh' ,'982433242'),
#                         ('123','subash','rimal','Bsc(Hons)computing','naxal','980605348')]
#             expected_result =[('102', 'david', 'joshi','Ethical Hacking', 'rajgadh','982433242'),
#                               ('123','subash','rimal','Bsc(Hons)computing','naxal','980605348')]
#             sort_by = 0 # sorting by Id, Change values accordance to index value to sort by different parameters.
#             self.bubble_sort(array_test,sort_by)
#             self.assertEqual(array_test, expected_result)
#
#     def test_search(self):
#         search_by = 1 # searching by First Name, Change values accordance to index value to searching by different parameters.
#         search_for = "subash"
#         array_test = [('102', 'david', 'joshi', 'Ethical Hacking', '982433242'),
#                   ('123', 'subash', 'rimal', 'Bsc(Hons)computing', 'naxal', '980605348')]
#
#         expected_result=[('123', 'subash', 'rimal', 'Bsc(Hons)computing', 'naxal', '980605348')]
#         mylist = self.search(array_test,search_by,search_for)
#         self.assertEqual(mylist, expected_result)
#
# if __name__ == '__main__':
#     unittest.main()
# root.mainloop()


