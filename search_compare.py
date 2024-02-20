import time
import random


def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    end = time.time()
    return found, end-start



def ordered_sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1

    end = time.time()
    return found, end-start


def binary_search_iterative(a_list,item):
    start = time.time()
    first = 0

    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    end = time.time()
    return found, end-start
    
    
def binary_search_recursive(a_list,item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)


if __name__ == "__main__":
    """Main entry point"""
    the_size1 = 500
    the_size2 = 1000
    the_size3 = 5000


    total_time = 0
    #average for sequential_search size 500
    for i in range(100):
        mylist = get_me_random_list(the_size1)
        # sorting is not needed for sequential search.
        time_list = []


        start = time.time()
        check = sequential_search(mylist, 99999999)
        time_spent = time.time() - start
        total_time += time_spent
        time_list.append(total_time)

    time_list_sum = sum(time_list)
    avg_time = time_list_sum / 100
    print(f"Sequential Search took {avg_time:10.7f} seconds to run, on average for a list of {the_size1} elements")

    # average for sequential_search size 1000
    for i in range(100):
        mylist = get_me_random_list(the_size2)
        time_list = []

        start = time.time()
        check = sequential_search(mylist, 99999999)
        time_spent = time.time() - start
        total_time += time_spent
        time_list.append(total_time)

    time_list_sum = sum(time_list)
    avg_time = time_list_sum / 100
    print(f"Sequential Search took {avg_time:10.7f} seconds to run, on average for a list of {the_size2} elements")

    # average for sequential_search size 5000
    for i in range(100):
        mylist = get_me_random_list(the_size3)
        time_list = []

        start = time.time()
        check = sequential_search(mylist, 99999999)
        time_spent = time.time() - start
        total_time += time_spent
        time_list.append(total_time)

    time_list_sum = sum(time_list)
    avg_time = time_list_sum / 100
    print(f"Sequential Search took {avg_time:10.7f} seconds to run, on average for a list of {the_size3} elements")

    # average for ordered_sequential_search size 500
    for i in range(100):
        mylist = get_me_random_list(the_size1)
        mylist = sorted(mylist)
        time_list = []

        start = time.time()
        check = ordered_sequential_search(mylist, 99999999)
        time_spent = time.time() - start
        total_time += time_spent
        time_list.append(total_time)

    time_list_sum = sum(time_list)
    avg_time = time_list_sum / 100
    print(f"Ordered Sequential Search took {avg_time:10.7f} seconds to run, on average for a list of {the_size1} elements")

    # average for ordered_sequential_search size 1000
    for i in range(100):
        mylist = get_me_random_list(the_size2)
        mylist = sorted(mylist)
        time_list = []

        start = time.time()
        check = ordered_sequential_search(mylist, 99999999)
        time_spent = time.time() - start
        total_time += time_spent
        time_list.append(total_time)

    time_list_sum = sum(time_list)
    avg_time = time_list_sum / 100
    print(f"Ordered Sequential Search took {avg_time:10.7f} seconds to run, on average for a list of {the_size2} elements")

    # average for ordered_sequential_search size 5000
    for i in range(100):
        mylist = get_me_random_list(the_size3)
        mylist = sorted(mylist)
        time_list = []

        start = time.time()
        check = ordered_sequential_search(mylist, 99999999)
        time_spent = time.time() - start
        total_time += time_spent
        time_list.append(total_time)

    time_list_sum = sum(time_list)
    avg_time = time_list_sum / 100
    print(f"Ordered Sequential Search took {avg_time:10.7f} seconds to run, on average for a list of {the_size3} elements")

    #average for binary_search_iterative size 500
    for i in range(100):
        mylist = get_me_random_list(the_size1)
        mylist = sorted(mylist)
        time_list = []


        start = time.time()
        check = binary_search_iterative(mylist, 99999999)
        time_spent = time.time() - start
        total_time += time_spent
        time_list.append(total_time)

    time_list_sum = sum(time_list)
    avg_time = time_list_sum / 100
    print(f"Binary Search Iterative took {avg_time:10.7f} seconds to run, on average for a list of {the_size1} elements")

    # average for binary_search_iterative size 1000
    for i in range(100):
        mylist = get_me_random_list(the_size2)
        mylist = sorted(mylist)
        time_list = []


        start = time.time()
        check = binary_search_iterative(mylist, 99999999)
        time_spent = time.time() - start
        total_time += time_spent
        time_list.append(total_time)

    time_list_sum = sum(time_list)
    avg_time = time_list_sum / 100
    print(f"Binary Search Iterative took {avg_time:10.7f} seconds to run, on average for a list of {the_size2} elements")

    # average for binary_search_iterative size 5000
    for i in range(100):
        mylist = get_me_random_list(the_size3)
        mylist = sorted(mylist)
        time_list = []


        start = time.time()
        check = binary_search_iterative(mylist, 99999999)
        time_spent = time.time() - start
        total_time += time_spent
        time_list.append(total_time)
    time_list_sum = sum(time_list)
    avg_time = time_list_sum / 100
    print(f"Binary Search Iterative took {avg_time:10.7f} seconds to run, on average for a list of {the_size3} elements")

    # average for binary_search_recursive size 500
    for i in range(100):
        mylist = get_me_random_list(the_size1)
        mylist = sorted(mylist)
        time_list = []


        start = time.time()
        check = binary_search_recursive(mylist, 99999999)
        time_spent = time.time() - start
        total_time += time_spent
        time_list.append(total_time)
    time_list_sum = sum(time_list)
    avg_time = time_list_sum / 100
    print(f"Binary Search Recursive took {avg_time:10.7f} seconds to run, on average for a list of {the_size1} elements")

    # average for binary_search_recursive size 1000
    for i in range(100):
        mylist = get_me_random_list(the_size2)
        mylist = sorted(mylist)
        time_list = []

        start = time.time()
        check = binary_search_recursive(mylist, 99999999)
        time_spent = time.time() - start
        total_time += time_spent
        time_list.append(total_time)
    time_list_sum = sum(time_list)
    avg_time = time_list_sum / 100
    print(f"Binary Search Recursive took {avg_time:10.7f} seconds to run, on average for a list of {the_size2} elements")

    # average for binary_search_recursive size 5000
    for i in range(100):
        mylist = get_me_random_list(the_size3)
        mylist = sorted(mylist)
        time_list = []

        start = time.time()
        check = binary_search_recursive(mylist, 99999999)
        time_spent = time.time() - start
        total_time += time_spent
        time_list.append(total_time)
    time_list_sum = sum(time_list)
    avg_time = time_list_sum / 100
    print(f"Binary Search Recursive took {avg_time:10.7f} seconds to run, on average for a list of {the_size3} elements")