def Line(file_count,count_Line) :
    print('Line :',(len(file_count.split('\n'))))

def Sentence(file_count,count_Sentences):
    Sentences = file_count.split('.')
    print('Sentence :',(len(Sentences) - 1 ))

def Word(file_count) :
    print('Word :',(len(file_count.split())))

def Letter(file_count,count_Letter) :
    for i in file_count :
        if i.isalpha() == True :
            count_Letter += 1
    print('Character :',(count_Letter))

def Upper(file_count,count_Upper) :
    for i in file_count :
        if i.isupper() is True :
            count_Upper += 1
    print('Upper :',count_Upper)

def Lower(file_count,count_Lower) :
    for i in file_count :
        if i.islower() is True :
            count_Lower += 1
    print('Lower :',count_Lower)

def Special(file_count,count_Special) :
    for i in file_count :
        if i == '.' or i == ',' or i == ':' or i == ';' or i == '/' or i == '(' or i == ')' or i =='-'  :
            count_Special += 1
    print('Special :',count_Special)

def main() :
    count_Sentences = 0
    count_Letter = 0
    count_Line = 0
    count_Upper = 0
    count_Lower = 0
    count_Special = 0
    infile = open('Loop.txt','r+')
    file_count = infile.read()
    list(file_count)
    print('---Program Structure---')
#Count Line
    Line(file_count,count_Line)
#Count Sentence
    Sentence(file_count,count_Sentences)
#Count Word
    Word(file_count)
#Count Letter
    Letter(file_count,count_Letter)
#Count Upper
    Upper(file_count,count_Upper)
#Count Lower
    Lower(file_count,count_Lower)
#Count Special alphabet 
    Special(file_count,count_Special)
    print('-----------------------')

main()