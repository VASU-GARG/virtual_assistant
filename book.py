import pyttsx3
import PyPDF2
import pyaudio


book = open('sample.pdf','rb')
Reader = PyPDF2.PdfFileReader(book)
pages = Reader.numPages
print(pages)


speaker = pyttsx3.init()
print("playing....")
page = Reader.getPage(0)
# 1st page is stored as 0 page
# 2nd page is stored as 1st page
# nth page -- (n-1) th page
text = page.extractText()
speaker.say(text)
speaker.runAndWait()
