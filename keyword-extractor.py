import PyPDF2
import textract
import pandas as pd
from rake_nltk import Rake

filename = 'as_a_man_thinketh.pdf'

pdfObject = open(filename,'rb')
pdfReadable = PyPDF2.PdfReader(pdfObject)
numberOfPages = len(pdfReadable.pages)

count = 0
text = ""
                                                            
while count < numberOfPages:
    pageObject = pdfReadable.pages[count]
    count +=1
    text += pageObject.extract_text()

# because PyPDF2 cannot read scanned files, check if it returned words    
if text != "":
    text = text

# if not, run the textract to convert scanned/image based PDF files into text
else:
    text = textract.process(filename,method='tesseract',language='eng')

# execute the following two lines of code if using stopwords from the NLTK package for the first time
# import nltk 
# nltk.download('stopwords')

# to use the stopwords, load them from the package by executing the following line of code
# from nltk.corpus import stopwords
r = Rake()
r.extract_keywords_from_text(text)

phrases = r.get_ranked_phrases_with_scores()

table = pd.DataFrame(phrases,columns=['score','Phrase'])
table = table.sort_values('score',ascending=False)
print(table.head(50))