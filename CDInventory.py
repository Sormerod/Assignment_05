#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# SOrmerod, 2020-Aug-10, Modified 2D data structure to use dictionaries as the inner data type
# SOrmerod, 2020-Aug-11, Implemented the delete ability
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break

    if strChoice == 'l':
        # TODO Add the functionality of loading existing data
        lstTbl.clear()
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dicRow = {'ID': lstRow[0], 'CD Title': lstRow[1], 'Artist': lstRow[2]}
            lstTbl.append(dicRow)
        objFile.close()

    elif strChoice == 'a':
        # 2. Add data to the table (2d-list) each time the user wants to add data
        while True:
            print('\nAdding CD\'s: [x] exit')
            strID = input('Enter an ID: ')
            if strID.lower() == 'x': break
            strTitle = input('Enter the CD\'s Title: ')
            if strTitle.lower() == 'x': break
            strArtist = input('Enter the Artist\'s Name: ')
            if strArtist.lower() == 'x': break
            dicRow = {'ID': strID,'CD Title': strTitle,'Artist': strArtist}
            lstTbl.append(dicRow)

    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ', ')

    elif strChoice == 'd':
        # TODO Add functionality of deleting an entry
        iDRow = (input('\nEnter the ID for the CD you would like to delete: '))
        for idx in range(len(lstTbl)):
            if lstTbl[idx]['ID'] == iDRow:
                del lstTbl[idx]
                break

    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        strRow = ''
        for row in lstTbl:
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
        objFile = open(strFileName, 'w')
        objFile.write(strRow)
        objFile.close()

    else:
        print('Please choose either l, a, i, d, s or x!')

