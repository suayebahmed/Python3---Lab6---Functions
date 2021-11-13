
# taking input for street
def get_input_st():
    street = int(input('Street: '))
    while street < 0 or street % 2 == 0:
        street = int(input('Street must be a positive odd integer!  Try again: '))
    return street

# taking user input for avenue
def get_input_ave():
    ave = int(input('Avenue: '))
    while ave < 0 or ave % 2 == 1:
        ave = int(input('Avenue must be a positive even integer!  Try again: '))
    return ave

# Converting user input integer to ordinal number
ending_list = ['st', 'nd', 'rd', 'th']
def num_to_ordinal(n):
    if 11 <= int(str(n)[-2:]) <= 13:
        return str(n) + ending_list[3]
    elif int(str(n)[-1]) == 1:
        return str(n) + ending_list[0]
    elif int(str(n)[-1]) == 2:
        return str(n) + ending_list[1]
    elif int(str(n)[-1]) == 3:
        return str(n) + ending_list[2]
    else:
        return str(n) + ending_list[3]


def get_directions(start_st, start_ave, end_st, end_ave):
    print(f'Directions from {num_to_ordinal(start_st)} and {num_to_ordinal(start_ave)} to {num_to_ordinal(end_st)} and {num_to_ordinal(end_ave)}:')
    
    # Horizontal route
    if start_st < end_st:
        st_dir = 'east'
        st_len = (end_st - start_st) * 1000
        if start_ave < end_ave:
            turn = 'right'
        else:
            turn = 'left'
    else:
        st_dir = 'west'
        st_len = (start_st - end_st) * 1000
        if start_ave < end_ave:
            turn = 'right'
        else:
            turn = 'left'

    # Vertical Route
    if start_ave < end_ave:
        ave_dir = 'south'
        ave_len = (end_ave - start_ave) * 1000
    else:
        ave_dir = 'north'
        ave_len = (start_ave - end_ave) * 1000

    # # # #
    if start_st == end_st and start_ave == end_ave:
        print('You are in the right place.')
    
    elif start_st == end_st:
        print(f'Take {num_to_ordinal(start_st)} St. {ave_dir} for {ave_len // 2} ft until you get to {num_to_ordinal(end_ave)} Ave.')
        print("Yay, you've arrived!")
    elif start_ave == end_ave:
        print(f'Take {num_to_ordinal(start_ave)} Ave. {st_dir} for {st_len // 2} ft until you get to {num_to_ordinal(end_st)} St.')
        print("Yay, you've arrived!")
    else:
        print(f'Take {num_to_ordinal(start_ave)} Ave. {st_dir} for {st_len // 2} ft until you get to {num_to_ordinal(end_st)} St.')
        print(f'Turn {turn} onto {num_to_ordinal(end_st)} St.')
        print(f'Take {num_to_ordinal(end_st)} St. {ave_dir} for {ave_len // 2} ft until you get to {num_to_ordinal(end_ave)} Ave.')
        print("Yay, you've arrived!")

# taking input for two street and two avenue 
print('Starting Corner:')
st1 = get_input_st()
ave1 = get_input_ave()
print()
print('Ending Corner:')
st2 = get_input_st()
ave2 = get_input_ave()
print()

# final function call
get_directions(st1, ave1, st2, ave2)