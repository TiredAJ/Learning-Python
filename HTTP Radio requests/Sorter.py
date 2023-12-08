import requests

InDataLoc = "Data.txt"
GoodData = "Working.txt"
BadData = "NonWorking.txt"

#declares dictionary
MainList = {}
#declares list
TempList = []

#opens Data.txt for writing
with open(InDataLoc, 'r') as Reader:
    Title = ""

    #loops through every line in the file
    for Line in Reader:
        #print(Line)

        #checks if it starts with 'h' (for "http"/"https")
        if not Line.startswith('h'):
            #checks if the sublist actually has data
            if len(TempList) != 0:
                #if so, creates a new key with the title
                #and copies the list as it's value
                MainList[Title] = TempList.copy()
                #empties the list
                TempList.clear()

            #assigns the title
            Title = Line.strip()
        else:
            #if it's not a title, copy the url into the list
            TempList.append(Line.strip())

#closes the file
Reader.close()

#opens both files for writing (idk how to do this without nesting)
with open(GoodData, 'w') as GWriter:
    with open(BadData, 'w') as BWriter:
        #declares int to hold status codes
        Status = 0

        #loops through the keys in the dictionary
        for Key in MainList:
            #makes a title in the files
            GWriter.write(Key + "---\n")
            BWriter.write(Key + "---\n")

            #gets the value (which is a list) for the key and loops through it
            for SubItem in MainList[Key]:
                #sends a request and records the status code
                Status = requests.get(SubItem, stream=True).status_code

                #checks if it's a good or bad status
                if Status >= 300:
                    #bad status, goes in non-working
                    BWriter.write("%s - %s\n"%(Status, SubItem))
                else:
                    #good status, goes in working
                    GWriter.write("%s - %s\n"%(Status, SubItem))

#closes files
GWriter.close()
BWriter.close()

#lets the user know it's finished
print("Finished!")