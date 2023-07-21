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
    
if text != "":
    text = text

else:
    text = textract.process(filename,method='tesseract',language='eng')

r = Rake()
r.extract_keywords_from_text(text)

phrases = r.get_ranked_phrases_with_scores()

table = pd.DataFrame(phrases,columns=['score','Phrase'])
table = table.sort_values('score',ascending=False)
print(table.head(50))