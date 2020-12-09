bags = []
with open('sample-input.txt') as f:
    for line in f:
        value = line.split()
        bags.append(value)
f.close()

bag_registry = []

nothing = 0

found_int = 0

i=0
for items in bags:
    bag_name = bags[i][0] + " " + bags[i][1]
    # print(bag_name)
    bag_registry.append([{'name':bag_name}])
    bag_contents = bags[i][4:]
    # print(bag_contents[0])

    try:
        int(bag_contents[0])
        # print("We found an int: " + str(bag_contents[0]))
        found_int += 1
    except:
        nothing = 0
        # print("Nope not an int: " + str(bag_contents[0]))

    # print(bag_contents)

    if found_int == 1:
        bag_registry[i].append({'contents':[]})
        j=0
        number_of_bags = int(len(bag_contents) / 4)
        # print("Number of bag types in contents: " + str(number_of_bags))
        while(j<(number_of_bags * 4)):
            content_bag_name = bag_contents[j+1] + " " + bag_contents[j+2]
            new_dict = {content_bag_name:int(bag_contents[j+0])}
            # print(new_dict)
            bag_registry[i][1]['contents'].append(new_dict)
            # print(bag_name + " can hold " + str(bag_contents[j+0]) + " " + content_bag_name)
            j += 4


    
    found_int = 0
    i += 1

print(bag_registry)

bag_carriers = []
target_bag = 0
yes_contents = 0
k=0
for items in bag_registry:
    if len(bag_registry[k]) == 1:
        yes_contents += 0
        # print(bag_registry[k][0]['name'] + " only has one item. No contents.")
    else:
        yes_contents += 1

    # print("yes content: " + str(yes_contents))
    if yes_contents == 1:
        # name = bag_registry[k][0]['name']
        # Find 'name' in bag_registry[k][0]['name']
        # for length of contents in bag_name:
        #     Add ['contents'] to list of bag carriers
        #     For entries in bag carriers:
        #         name = bag_carrier[0] ++ 
        name = bag_registry[k][0]['name']
        m=0
        for items in bag_registry[k][1]['contents']:
            

        if 'shiny gold' in bag_registry[k][1]['contents'][0]:
            print("we found shiny gold")
            target_bag += 1
            bag_carriers.append(bag_registry[k][0]['name'])

    yes_contents = 0    
    k += 1


# l=0
# new_bag_carriers = []
# for items in bag_carriers:
#     try:
#         # print("Bag contents")
#         print(bag_registry[k][1]['contents'])
#         yes_contents += 1
#         # print("we found shiny gold")
#     except:
#         # print("No contents")
#         yes_contents += 0

#     # print("yes content: " + str(yes_contents))
#     if yes_contents == 1:
#         if 'shiny gold' in bag_registry[k][1]['contents'][0]:
#             # print("we found shiny gold")
#             target_bag += 1
#             new_bag_carriers.append(bag_registry[k][0]['name'])
#     yes_contents = 0    
#     l += 1

# print("Bag carriers: ")
print(bag_carriers)
# print("New bag carriers: ")
# print(new_bag_carriers)
print("# of possibilities for our target bag: " + str(target_bag))