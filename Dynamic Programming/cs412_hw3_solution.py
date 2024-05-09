'''
CS 412 -- HW 3 -- Rocket with part list constructed using backtracking

Molloy -- Feb 2023

'''

def rocket_opt(part_list, target):
    full_part_list = part_list

    def rocket_opt_helper(part_list, target):
        # initialize part_count_opt to list of length of full_part_list; set each value to positive infinity
        # will use list to store min number of parts needed for each part size
        part_count_opt = [float("+inf")] * len(full_part_list)

        if len(part_list) == 1: # Base case; part must be length 1
            # create list using length of full_part_list and set first element equal to target
            # represents that we need target parts of first size to reach target length
            parts_qty = [0] * len(full_part_list)
            parts_qty[0] = target
            return parts_qty

        # loop over all possible numbers of last part size in part_list that can fit in target length
        for piece_count in range(target // part_list[-1] + 1):
            # call helper function on each possible number of last part size with remaining part sizes and length
            this_part_count = rocket_opt_helper(part_list[:-1], target - piece_count * part_list[-1])
            this_part_count[len(part_list) - 1] = piece_count
            
            # if total num of parts in this_part_count is < current min in part_count_opt, updated part_count_opt w/ new min
            if sum(this_part_count) < sum(part_count_opt):
                part_count_opt = this_part_count

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