import numpy as np
import itertools
import time

# This fills the dictionary as wished
def fillRight(dictionary, example_list):
    to_strings1 = ['a', 'b', 'c']
    to_strings2 = ['a2', 'b2', 'c2']
    for idx in range(0, len(example_list)):
        element = example_list[idx]

        if(idx%18 < 6):
            if(idx%18 < 3):
                from_string = 'a_to'
            else:
                from_string = 'b_to'
            to_string = to_strings1[idx%3]
            dictionary[from_string][to_string].append(element)

        if(idx%18 > 8 and idx%18 < 15):
            if(idx%18 < 12):
                from_string = 'a2_to'
            else:
                from_string = 'b2_to'
            to_string = to_strings2[idx%3]
            dictionary[from_string][to_string].append(element)
    
# Faster/easier to read filling. Not memory efficient for large lists but very fast
def fillFast1(dictionary, example_list):
    dictionary['a_to']['a'] = example_list[0::18]
    dictionary['a_to']['b'] = example_list[1::18]
    dictionary['a_to']['c'] = example_list[2::18]
    dictionary['b_to']['a'] = example_list[3::18]
    dictionary['b_to']['b'] = example_list[4::18]
    dictionary['b_to']['c'] = example_list[5::18]
    dictionary['a2_to']['a2'] = example_list[9::18]
    dictionary['a2_to']['b2'] = example_list[10::18]
    dictionary['a2_to']['c2'] = example_list[11::18]
    dictionary['b2_to']['a2'] = example_list[12::18]
    dictionary['b2_to']['b2'] = example_list[13::18]
    dictionary['b2_to']['c2'] = example_list[14::18]
    
# Works
def fillFast2(dictionary, example_list):
    dictionary['a_to']['a'] = [example_list[i] for i in xrange(0, len(example_list), 18)]
    dictionary['a_to']['b'] = [example_list[i] for i in xrange(1, len(example_list), 18)]
    dictionary['a_to']['c'] = [example_list[i] for i in xrange(2, len(example_list), 18)]
    dictionary['b_to']['a'] = [example_list[i] for i in xrange(3, len(example_list), 18)]
    dictionary['b_to']['b'] = [example_list[i] for i in xrange(4, len(example_list), 18)]
    dictionary['b_to']['c'] = [example_list[i] for i in xrange(5, len(example_list), 18)]
    dictionary['a2_to']['a2'] = [example_list[i] for i in xrange(9, len(example_list), 18)]
    dictionary['a2_to']['b2'] = [example_list[i] for i in xrange(10, len(example_list), 18)]
    dictionary['a2_to']['c2'] = [example_list[i] for i in xrange(11, len(example_list), 18)]
    dictionary['b2_to']['a2'] = [example_list[i] for i in xrange(12, len(example_list), 18)]
    dictionary['b2_to']['b2'] = [example_list[i] for i in xrange(13, len(example_list), 18)]
    dictionary['b2_to']['c2'] = [example_list[i] for i in xrange(14, len(example_list), 18)]

# 
def fillFast3(dictionary, example_list):
    dictionary['a_to']['a'] = list(itertools.islice(example_list, 0, None, 18))
    dictionary['a_to']['b'] = list(itertools.islice(example_list, 1, None, 18))
    dictionary['a_to']['c'] = list(itertools.islice(example_list, 2, None, 18))
    dictionary['b_to']['a'] = list(itertools.islice(example_list, 3, None, 18))
    dictionary['b_to']['b'] = list(itertools.islice(example_list, 4, None, 18))
    dictionary['b_to']['c'] = list(itertools.islice(example_list, 5, None, 18))
    dictionary['a2_to']['a2'] = list(itertools.islice(example_list, 9, None, 18))
    dictionary['a2_to']['b2'] = list(itertools.islice(example_list, 10, None, 18))
    dictionary['a2_to']['c2'] = list(itertools.islice(example_list, 11, None, 18))
    dictionary['b2_to']['a2'] = list(itertools.islice(example_list, 12, None, 18))
    dictionary['b2_to']['b2'] = list(itertools.islice(example_list, 13, None, 18))
    dictionary['b2_to']['c2'] = list(itertools.islice(example_list, 14, None, 18))

# For the next functions, see http://stackoverflow.com/questions/8865878/skipping-every-other-element-after-the-first
# List comprehension: Range with conditional
def fillFast4(dictionary, example_list):
    dictionary['a_to']['a'] = [example_list[idx] for 
                               idx in range(0, len(example_list)) if idx%18 == 0]
    dictionary['a_to']['b'] = [example_list[idx] for 
                               idx in range(1, len(example_list)) if idx%18 == 1]
    dictionary['a_to']['c'] = [example_list[idx] for 
                               idx in range(2, len(example_list)) if idx%18 == 2]
    dictionary['b_to']['a'] = [example_list[idx] for 
                               idx in range(3, len(example_list)) if idx%18 == 3]
    dictionary['b_to']['b'] = [example_list[idx] for 
                               idx in range(4, len(example_list)) if idx%18 == 4]
    dictionary['b_to']['c'] = [example_list[idx] for 
                               idx in range(5, len(example_list)) if idx%18 == 5]
    dictionary['a2_to']['a2'] = [example_list[idx] for 
                                 idx in range(9, len(example_list)) if idx%18 == 9]
    dictionary['a2_to']['b2'] = [example_list[idx] for 
                                 idx in range(10, len(example_list)) if idx%18 == 10]
    dictionary['a2_to']['c2'] = [example_list[idx] for 
                                 idx in range(11, len(example_list)) if idx%18 == 11]
    dictionary['b2_to']['a2'] = [example_list[idx] for 
                                 idx in range(12, len(example_list)) if idx%18 == 12]
    dictionary['b2_to']['b2'] = [example_list[idx] for 
                                 idx in range(13, len(example_list)) if idx%18 == 13]
    dictionary['b2_to']['c2'] = [example_list[idx] for 
                                 idx in range(14, len(example_list)) if idx%18 == 14]
  
# List comprehension: Range with step
def fillFast5(dictionary, example_list):
    dictionary['a_to']['a'] = [example_list[idx] for idx in range(0, len(example_list), 18)]
    dictionary['a_to']['b'] = [example_list[idx] for idx in range(1, len(example_list), 18)]
    dictionary['a_to']['c'] = [example_list[idx] for idx in range(2, len(example_list), 18)]
    dictionary['b_to']['a'] = [example_list[idx] for idx in range(3, len(example_list), 18)]
    dictionary['b_to']['b'] = [example_list[idx] for idx in range(4, len(example_list), 18)]
    dictionary['b_to']['c'] = [example_list[idx] for idx in range(5, len(example_list), 18)]
    dictionary['a2_to']['a2'] = [example_list[idx] for idx in range(9, len(example_list), 18)]
    dictionary['a2_to']['b2'] = [example_list[idx] for idx in range(10, len(example_list), 18)]
    dictionary['a2_to']['c2'] = [example_list[idx] for idx in range(11, len(example_list), 18)]
    dictionary['b2_to']['a2'] = [example_list[idx] for idx in range(12, len(example_list), 18)]
    dictionary['b2_to']['b2'] = [example_list[idx] for idx in range(13, len(example_list), 18)]
    dictionary['b2_to']['c2'] = [example_list[idx] for idx in range(14, len(example_list), 18)]

# List comprehension: Enumerate with conditional
def fillFast6(dictionary, example_list):
    dictionary['a_to']['a'] = [item for idx, item in enumerate(example_list) if idx%18 == 0]
    dictionary['a_to']['b'] = [item for idx, item in enumerate(example_list) if idx%18 == 1]
    dictionary['a_to']['c'] = [item for idx, item in enumerate(example_list) if idx%18 == 2]
    dictionary['b_to']['a'] = [item for idx, item in enumerate(example_list) if idx%18 == 3]
    dictionary['b_to']['b'] = [item for idx, item in enumerate(example_list) if idx%18 == 4]
    dictionary['b_to']['c'] = [item for idx, item in enumerate(example_list) if idx%18 == 5]
    dictionary['a2_to']['a2'] = [item for idx, item in enumerate(example_list) if idx%18 == 9]
    dictionary['a2_to']['b2'] = [item for idx, item in enumerate(example_list) if idx%18 == 10]
    dictionary['a2_to']['c2'] = [item for idx, item in enumerate(example_list) if idx%18 == 11]
    dictionary['b2_to']['a2'] = [item for idx, item in enumerate(example_list) if idx%18 == 12]
    dictionary['b2_to']['b2'] = [item for idx, item in enumerate(example_list) if idx%18 == 13]
    dictionary['b2_to']['c2'] = [item for idx, item in enumerate(example_list) if idx%18 == 14]
    
# List filter: Index in range (garbage, only the indices are saved here)
def fillFast7(dictionary, example_list):
    dictionary['a_to']['a'] = filter(lambda idx: idx%18 == 0, range(len(example_list)))
    dictionary['a_to']['b'] = filter(lambda idx: idx%18 == 1, range(len(example_list)))
    dictionary['a_to']['c'] = filter(lambda idx: idx%18 == 2, range(len(example_list)))
    dictionary['b_to']['a'] = filter(lambda idx: idx%18 == 3, range(len(example_list)))
    dictionary['b_to']['b'] = filter(lambda idx: idx%18 == 4, range(len(example_list)))
    dictionary['b_to']['c'] = filter(lambda idx: idx%18 == 5, range(len(example_list)))
    dictionary['a2_to']['a2'] = filter(lambda idx: idx%18 == 9, range(len(example_list)))
    dictionary['a2_to']['b2'] = filter(lambda idx: idx%18 == 10, range(len(example_list)))
    dictionary['a2_to']['c2'] = filter(lambda idx: idx%18 == 11, range(len(example_list)))
    dictionary['b2_to']['a2'] = filter(lambda idx: idx%18 == 12, range(len(example_list)))
    dictionary['b2_to']['b2'] = filter(lambda idx: idx%18 == 13, range(len(example_list)))
    dictionary['b2_to']['c2'] = filter(lambda idx: idx%18 == 14, range(len(example_list)))

def createData(length):

    example_list = []
    for i in range(0,length):
        value = float(i%18)
        example_list.append(value)
    a_abc = {'a' : [], 'b' : [], 'c' : [] }
    b_abc = {'a' : [], 'b' : [], 'c' : [] }
    a2_abc = {'a2' : [], 'b2' : [], 'c2' : [] }
    b2_abc = {'a2' : [], 'b2' : [], 'c2' : [] }
    dictionary = {'a_to': a_abc, 'b_to': b_abc, 'a2_to': a2_abc, 'b2_to': b2_abc}
    return example_list, dictionary

number_of_elements = 936 # Most interesting for me is 936000
iterations = 10
time_right = 0.0
time_1 = 0.0
time_2 = 0.0
time_3 = 0.0
time_4 = 0.0
time_5 = 0.0
time_6 = 0.0

for j in range(0,5):
    for i in range(iterations):
        example_list, dictionary = createData(number_of_elements)
        start = time.clock()
        fillRight(dictionary, example_list)
        t0 = time.clock()
        time_right = time_right + t0-start

        example_list, dictionary = createData(number_of_elements)
        t0 = time.clock()
        fillFast1(dictionary, example_list)
        t1 = time.clock()
        time_1 = time_1 + t1-t0

        example_list, dictionary = createData(number_of_elements)
        t0 = time.clock()
        fillFast2(dictionary, example_list)
        t1 = time.clock()
        time_2 = time_2 + t1-t0

        example_list, dictionary = createData(number_of_elements)
        t0 = time.clock()
        fillFast3(dictionary, example_list)
        t1 = time.clock()
        time_3 = time_3 + t1-t0

        example_list, dictionary = createData(number_of_elements)
        t0 = time.clock()
        fillFast4(dictionary, example_list)
        t1 = time.clock()
        time_4 = time_4 + t1-t0

        example_list, dictionary = createData(number_of_elements)
        t0 = time.clock()
        fillFast5(dictionary, example_list)
        t1 = time.clock()
        time_5 = time_5 + t1-t0

        example_list, dictionary = createData(number_of_elements)
        t0 = time.clock()
        fillFast6(dictionary, example_list)
        t1 = time.clock()
        time_6 = time_6 + t1-t0
    print "Number of elements: ", number_of_elements
    print "0 time: ", time_right/iterations
    print "1 time: ", time_1/iterations
    print "2 time: ", time_2/iterations
    print "3 time: ", time_3/iterations
    print "4 time: ", time_4/iterations
    print "5 time: ", time_5/iterations
    print "6 time: ", time_6/iterations
    number_of_elements = number_of_elements*10