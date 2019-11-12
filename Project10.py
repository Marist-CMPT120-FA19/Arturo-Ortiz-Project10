#Arturo Ortiz arturo.ortiz@marist.edu

#This is an automated censor program that reads in text from a file and
#creates a new file where all the censored words are replaced by a string of asterisks (*)

def main():
    fname=input("Enter filename of sentence that needs to be censored: ")
    cname=input("Enter filename of censored words: ")
    
    infilef=open(fname, 'r')
    infilec=open(cname, 'r')

    
    dataf=infilef.read()
    datac=infilec.read()
    outfile=open("output.txt","w")
    

    datalst=dataf.split()
    datalst2=datac.split()
    
        
    censorlst=dataf.split()
    uncensorlst=datac.split()
    #censorlst holds all the censored words
    #uncensorlst holds all uncensored sentence

    for data in datalst2:
        for i in range(0,len(datalst)):
            if data.lower()==datalst[i].lower():
                datalst[i]="*" *len(data)

    output= open("Output.txt", 'w+')

    for d in datalst:
        output.write(d + " ")



    infilef.close()
    infilec.close()
    outfile.close()

main()

