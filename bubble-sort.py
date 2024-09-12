def compareToLeft(targetIndex, dictLst):
    # if the index is not already on the leftmost
    if targetIndex > 0:
        #set up counter
        counter = 0
        for _ in range(targetIndex):
            #traverse to the left of the targetIndex location
            counter -= 1
            if dictLst[targetIndex]["value"] < dictLst[targetIndex+counter]["value"]:
                #switch places with bigger number to the left
                dictLst[targetIndex], dictLst[targetIndex+counter] = dictLst[targetIndex+counter], dictLst[targetIndex]
                #record the new targetIndex
                targetIndex = targetIndex+counter
                #traverse to the left again
                compareToLeft(targetIndex, dictLst)
                break
        #eventually if no bigger number is found to the left, return the targetIndex
        return
    #if already on the left most, just return the index
    else:
        return
   
def compareToRight(targetIndex, dictLst):
    if targetIndex < len(dictLst)-1:
        counter = 0
        for _ in range(len(dictLst)-targetIndex-1):
            counter += 1
            if dictLst[targetIndex]["value"] > dictLst[targetIndex+counter]["value"]:
                dictLst[targetIndex], dictLst[targetIndex+counter] = dictLst[targetIndex+counter], dictLst[targetIndex]
                targetIndex = targetIndex+counter
                compareToRight(targetIndex, dictLst)
                break
        return
    else:
        return
           

userInput = ""
num_lst = []
while userInput != "Done":
    userInput = input("Please enter numbers to be sorted:(One at a time, when you're done enter anything other than a number)")
    try:
        num_lst.append(int(userInput))
    except ValueError:
        break

#create a list of dictionaries, each containing an id and a value that the user entered

dictionary_lst = []
id = 0
for num in num_lst:
    num_dict = {"id":id, "value":num}
    dictionary_lst.append(num_dict)
    id += 1
#create a duplicate of the newly created list
sortedDictionaryLst = dictionary_lst.copy()

#iterate each element from the original list, and sort the order inside the duplicated list

for num_dict_original in dictionary_lst:
    for num_dict_duplicate in sortedDictionaryLst:
        #find the current numberDict from the original list in the duplicated one
        if num_dict_duplicate["id"]==num_dict_original["id"]:
            #get its current position in the duplicated list
            targetDictIndex = sortedDictionaryLst.index(num_dict_duplicate)
            compareToLeft(targetDictIndex, sortedDictionaryLst)
            if num_dict_duplicate["id"]==num_dict_original["id"]:
                targetDictIndex = sortedDictionaryLst.index(num_dict_duplicate)
                compareToRight(targetDictIndex, sortedDictionaryLst)
                break

sorted_num_lst = []
#reconstruct a list consist of only the original numbers users have put in
for numberDict in sortedDictionaryLst:
    sorted_num_lst.append(numberDict["value"])

print("Sorted numbers:", sorted_num_lst)