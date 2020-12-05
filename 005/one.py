import math

seats = []
with open('input.txt') as f:
    for line in f:
        value = line.split()
        seats.append(value)
f.close()

row_start = 0
row_bound = 127
col_start = 0
col_bound = 7

def transform_bounds(seats, i, j):
    global total_f
    global row_bound
    global total_b
    global row_start
    global col_start
    global col_bound

    if seats[i][0][j] == 'F':
        # print("Found F at line " + str(i) + " char pos " + str(j))
        # print("row_bound before: " + str(row_bound))
        row_bound = math.floor(row_start + ((row_bound - row_start) / 2))
        # print("row_bound after: " + str(row_bound))

    if seats[i][0][j] == 'B':
    # if char == 'f':
        
        row_start = math.ceil(row_start + ((row_bound - row_start) / 2))
        # print("Found B at line " + str(i) + " char pos " + str(j))
        # print("New row start: " + str(row_start))
        # print("total b value after: " + str(total_b))

    if seats[i][0][j] == 'R':
        col_start = math.ceil(col_start + ((col_bound - col_start) / 2))

    if seats[i][0][j] == 'L':
        col_bound = math.floor(col_start + ((col_bound - col_start) / 2))

i=0
j=0

seat_ids = []
rows = []
col0 = []
col1 = []
col2 = []
col3 = []
col4 = []
col5 = []
col6 = []
col7 = []

while (i<len(seats)):
# while (i<20):

    # print(seats[i][0][0])

    while (j<len(seats[i][0])):
        transform_bounds(seats, i, j)
        j+=1

    if row_start == row_bound and col_start == col_bound:
        rows.append(row_start)
        if col_start == 0:
            col0.append(row_start)
        elif col_start == 1:
            col1.append(row_start)
        elif col_start == 2:
            col2.append(row_start)
        elif col_start == 3:
            col3.append(row_start)
        elif col_start == 4:
            col4.append(row_start)
        elif col_start == 5:
            col5.append(row_start)
        elif col_start == 6:
            col6.append(row_start)
        elif col_start == 7:
            col7.append(row_start)

        # print("Final seat: " + str(row_start) + ", " + str(col_start))
        seat_id = row_start * 8 + col_start
        # print("Seat ID: " + str(seat_id))
        seat_ids.append(seat_id)

    # print(seats[i][0])
    j=0
    row_bound = 127
    row_start = 0
    col_bound = 7
    col_start = 0
    i += 1

# print("# of seats: " + str(len(seat_ids)))
seat_ids.sort(reverse=True)
print("Highest seat ID: " + str(seat_ids[0]))

rows.sort()
print("Lowest row: " + str(rows[0]))
rows.sort(reverse=True)
print("Highest row: " + str(rows[0]))

col_lengths = {}
col_lengths[0] = len(col0)
col_lengths[1] = len(col1)
col_lengths[2] = len(col2)
col_lengths[3] = len(col3)
col_lengths[4] = len(col4)
col_lengths[5] = len(col5)
col_lengths[6] = len(col6)
col_lengths[7] = len(col7)

# print(col_lengths)
col_lengths = sorted(col_lengths, key=col_lengths.get)
print("My seat column: " + str(col_lengths[0]))

# col5.sort()
# k=4
# for seats in col5:
#     print(col5[k-4])
#     # if col5[k-4] != k:
#     #     print(str(col5[k-4]) + " does not equal " + str(k))
#     k += 1