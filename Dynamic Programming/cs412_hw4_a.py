'''
CS 412 -- HW 4 -- Rocket with part list constructed using backtracking and memoization

Molloy -- Feb 2023
Alex Karapetkov

'''
'''
def rocket_opt(part_list, target):
    full_part_list = sorted(part_list, reverse=True)
    memo = {} # initialize dictionary

    def rocket_opt_helper(part_list, target):
        # check if part list length and target length are already in memo
        if (len(part_list), target) in memo:
            return memo[(len(part_list), target)]

        # initialize part_count_opt to list of length of full_part_list; set each value to positive infinity
        # will use list to store min number of parts needed for each part size
        part_count_opt = [float("+inf")] * len(full_part_list)

        if len(part_list) == 1: # Base case; part must be length 1
            # create list using length of full_part_list and set first element equal to target
            # represents that we need target parts of first size to reach target length
            parts_qty = [0] * len(full_part_list)
            parts_qty[full_part_list.index(part_list[0])] = target
            return parts_qty

        # loop over all possible numbers of last part size in part_list that can fit in target length
        for piece_count in range(target // part_list[0] + 1):
            # call helper function on each possible number of last part size with remaining part sizes and length
            this_part_count = rocket_opt_helper(part_list[1:], target - piece_count * part_list[0])
            this_part_count[full_part_list.index(part_list[0])] = piece_count
            
            # if total num of parts in this_part_count is < current min in part_count_opt, updated part_count_opt w/ new min
            if sum(this_part_count) < sum(part_count_opt):
                part_count_opt = this_part_count

        # put part_count_opt entry in memo
        memo[(len(part_list), target)] = part_count_opt
        return part_count_opt

    return rocket_opt_helper(full_part_list, target)


def main():
    part_sizes = [int(x) for x in input().split()]
    target = int(input())

    part_qty_for_rocket = rocket_opt(part_sizes, target)
    for piece_count, piece_size in zip(part_qty_for_rocket, part_sizes):
        print(piece_count, 'of length', piece_size)

    print(sum(part_qty_for_rocket), 'rocket sections minimum')

if __name__ == "__main__":
    main()

'''

def rocket_opt(part_list, target):
    # sort list of part lengths in descending order to consider largest part first
    part_list.sort(reverse=True)

    # create empty dictionary to store results of subproblems
    memo = {}

    # helper function that takes index of current part length being considered and target which is remaining length to be reached
    def helper(index, target):
        # target length has been reached; return list of zeros
        if target == 0:
            return [0] * len(part_list)

        # if this case is reached, no valid solution can be found so return None
        if index == len(part_list) or target < 0:
            return None

        # if tuple (index, target) is already in memo, return that stored result
        if (index, target) in memo:
            return memo[(index, target)]

        # case where current part length is used; call helper with same index and target minus current part length
        current_part_count = helper(index, target - part_list[index])

        # if current_part_length is not None, valid solution has been found
        # increment count of current part length, store it in memo and return it
        if current_part_count is not None:
            current_part_count[index] += 1
            memo[(index, target)] = current_part_count
            return current_part_count

        # case where current part length is not being used; call helper with index + 1 and same target
        not_current_part = helper(index + 1, target)

        # if not None, valid solution found; store not current part in memo and return it
        if not_current_part is not None:
            memo[(index, target)] = not_current_part
            return not_current_part

        # return None if no solution can be found
        return None

    return helper(0, target)

def main():
    part_sizes = [int(x) for x in input().split()]
    target = int(input())

    part_qty_for_rocket = rocket_opt(part_sizes, target)
    for piece_count, piece_size in zip(part_qty_for_rocket, part_sizes):
        print(piece_count, 'of length', piece_size)

    print(sum(part_qty_for_rocket), 'rocket sections minimum')

if __name__ == "__main__":
    main()