#Gabe Ryan
#Edit Distance Algorithm Implementation


#X - String 1, Y - String 2
#d - penalty for instert/delete
#a1 - penalty for cv,vc swap
#a2 - penatly for vv,cc swap


def editDistance(X,Y,d,a1,a2):

    m = len(X)
    n = len(Y)
    
    A = [[0 for y in range(n+1)] for x in range(m+1)] #2D Matrix to hold string values

    finaloutput = X + " " + Y+"\n"
    finaloutput += str(d) + " " + str(a1) + " " + str(a2)+"\n"
    
    X.lower()
    Y.lower()

    for i in range(m+1): #### Initialize first column ####
        A[i][0] = i*d

    for j in range(n+1): #### Initialize first row #######
        A[0][j] =j*d
        
    for i in range(1,m+1):          ######## Populate Matrix A #########
        for j in range(1,n+1):
            
            swapPen = getPenVal(X[i-1],Y[j-1],a1,a2) ### Penalty for swapping ###
        
            A[i][j] = min(swapPen + A[i-1][j-1],
                          d + A[i-1][j],
                          d + A[i][j-1])
            
    
    finaloutput += "Start!\t\t\t\t"+X+"\n"
    
    s1,s2,final = findPath(A,X,Y,i,j,"","",d,a1,a2,[]) ###### Call Trace Back Function ######
    
    final.reverse()

    output =""
    for string in final:
        output += string
    
            
    output += "\n\nEdit Distance\t\t\t"+str(A[i][j])+"\n\n"
    output += "******************* MATRIX ************************\n"

    A.reverse()
    for k in A:
        output += str(k) +"\n"

    output += "****************** END MATRIX *********************\n\n"

    output += "****************** ALIGNMENT **********************\n\n"

    output += "\t\tString A: "+s1+"\n"
    output += "\t\tString B: "+s2+"\n\n"
    output += "***************** END ALIGNMENT *******************\n\n\n-----------------------------------------------------------\n\n"
    finaloutput+=output
    return finaloutput
    

#returns swap penalty value c->c, v->v, c->v, v->c
def getPenVal(x,y,a1,a2):
    
    vowels = ("a","e","i","o","u")
    penVal = 0
    
    #Check to see how values compare
    if x == y:
        return penVal
    
    elif x in vowels: 
        if y in vowels:
            penVal = a2
        else:
            penVal = a1
            
    else:
        if y in vowels:
            penVal = a1
        else:
            penVal = a2

    return penVal


###################### TRACE BACK THROUGH PATH #########################

def findPath(A,X,Y,i,j,s1,s2,d,a1,a2,final):

    if i>0 or j>0:

        
        swapPen = getPenVal(X[i-1],Y[j-1],a1,a2)
        
        penVal = min(swapPen + A[i-1][j-1], ##Swamp/match
                         d + A[i-1][j],     ##Delete
                         d + A[i][j-1])     ##Insert
        
    
        if swapPen == 0: ### LETTERS ARE THE SAME ###
            s1 = X[i-1]+s1
            s2 = Y[j-1]+s2
            final.append("Ignore \'"+Y[j-1]+"\'.\t\t\t"+Y[:j-1]+X[i-1:]+"\n")
            return findPath(A,X,Y,i-1,j-1,s1,s2,d,a1,a2,final)

        elif penVal == swapPen + A[i-1][j-1]: ### SWAP ###
            s1 = X[i-1]+s1
            s2 = Y[j-1]+s2
            final.append("Change \'"+X[i-1]+"\' to \'"+Y[j-1]+"\'.\t\t"+Y[:j]+X[i:]+"\n")
            return findPath(A,X,Y,i-1,j-1,s1,s2,d,a1,a2,final)

        elif penVal == d + A[i-1][j]:         ### DELETE ###
            s1 = '_' +s1
            s2 = '_' +s2
            final.append("Delete \'"+X[i-1]+"\'.\t\t\t"+Y[:j]+X[i:]+"\n")
            return findPath(A,X,Y,i-1,j,s1,s2,d,a1,a2,final)
        
        

        elif penVal == d + A[i][j-1]:         ### INSERT ###
            s1 = '_' +s1
            s2 = Y[j-1]+s2
            final.append("Insert \'"+Y[j-1]+"\'.\t\t\t"+Y[:j] + X[i:]+"\n")
            return findPath(A,X,Y,i,j-1,s1,s2,d,a1,a2,final)


        
    return s1,s2,final
    
def main():
    userIn = input("Please enter text file name with \'.txt\' extension or two seperate strings to compare: ")
    

    if userIn[-4:] == ".txt":
        infile = open(userIn, 'r',encoding='UTF-8').read()
        file = infile.split()
        output = ""
        for i in range(0,len(file),5):
            X = file[i]
            Y = file[i+1]
            d = int(file[i+2])
            a1 = int(file[i+3])
            a2 = int(file[i+4])

            output += editDistance(X,Y,d,a1,a2)

        outfile = open("EditOutPut.txt",'w')
        outfile.write(output)
        outfile.close()
        
        print("Your output has been save to \'EditOutPut.txt\'.")
        
    else:
        userIn = userIn.split()
        X = userIn[0]
        Y = userIn[1]
        
        userIn2 = input("Please enter the penalty for misatches between strings seperated by commas\n"
                         "(insert/delete, vowel<->consonant, vowel->vowel/consonant->consonant: ")

        userIn2 = userIn2.split(',')
        
        d = int(userIn2[0])
        a1 = int(userIn2[1])
        a2 = int(userIn2[2])

        output = editDistance(X,Y,d,a1,a2)
        print("\n\n\n"+output)

main()
