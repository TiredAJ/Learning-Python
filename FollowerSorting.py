InDataLoc = 'C:/Users/.../Desktop/TwitterFollowing.txt'
OutDataLoc = 'C:/Users/.../Documents/Main-Remote/Misc/Old Twitter Following.md'

Following = []

with open(InDataLoc, 'r') as Reader:
    #print(Reader.readline())
    for Line in Reader:
        #print(Line)
        if Line.startswith('@'):
            Following.append(Line.strip())
            #print(Line.strip())
Reader.close()

with open (OutDataLoc, 'a') as Writer:
    for Follower in Following:
        Writer.write(Follower + '\n')
Writer.close()
print(Following[-1])
