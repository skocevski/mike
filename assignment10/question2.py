import random
import json
import matplotlib.pyplot as plt
def generateChineseRestaurant(customers):
    # First customer always sits at the first table
        tables = [1]
        #for all other customers do
        for cust in range(2, customers+1):
                # rand between 0 and 1
                rand = random.random()
                # Total probability to sit at a table
                prob = 0
                # No table found yet
                table_found = False
                # Iterate over tables

                for table, guests in enumerate(tables):
                    # calc probability for actual table an add it to total probability
                    prob += float(guests) / float(cust)
                    # If rand is smaller than the current total prob., customer will sit down at current table
                    if rand < prob: 
                        # incr. #customers for that table
                        tables[table] += 1
                        # customer has found table
                        table_found = True
                        # no more tables need to be iterated, break out for loop
                        break
                # If table iteration is over and no table was found, open new table
                if not table_found:
                    tables.append(1)
        GPlot(tables)
        giniVal = gini(tables)
        print ("gini coefficient of %s Guest is = %s " % (customers, giniVal))

def GPlot(table_list):
    table_list = sorted(table_list)
    var_list = []
    plotList = []
    for x in table_list:
        var_list.append(x)
        g = gini(var_list)
        plotList.append(g)
    plt.plot(var_list,plotList)
    plt.ylabel('Gini coefficient')
    plt.xlabel('Guest')
    plt.show()

def gini(list_of_values):
    sorted_list = sorted(list_of_values)
    height, area = 0, 0
    for value in sorted_list:
        height += value
        area += height - value / 2.
    fair_area = height * len(list_of_values) / 2.
    return (fair_area - area) / fair_area
for i in range(0,5):
    allRestaurants = [1000,10000,100000,1000000,10000000]
    restaurants = allRestaurants[i]
    network = generateChineseRestaurant(restaurants)
    with open('network_' + str(restaurants) + '.json', 'w') as out:
        json.dump(network, out)
