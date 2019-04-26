# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 14:37:54 2019

@author: pabde
"""

import webbrowser
import requests
import bs4
import urllib

#Define your keyword of interest
keyword = "influenza"

#Define the string indicator for a PDF in the source code
PDFstring = "/track/pdf"

#Create empty global array to hold PDF references from all multiple pages
PDFList = []

#Define the page of interest (here it is from BMC Public Health, searching on the keyword)
BMCPH = "https://bmcpublichealth.biomedcentral.com/articles?query=" +keyword

#Open the page in a browser to check it
#webbrowser.open(BMCPH)

#Put the text of the defined page into the variable 'res'
res = requests.get(BMCPH)
type(res)
res.status_code == requests.codes.ok
len(res.text)
#print(res.text[:250])

#Get the number of pages
pageText = "Page 1 of "
startPages = res.text.find(pageText) + len(pageText)
endPages = res.text.find("<",startPages)
numPages = int(res.text[startPages:endPages])

#Page string in URL is &page=
#print(numPages)

def getPDFList():
    failsafe = 9999
    for i in range (1,numPages+1):
        sanityCheck = 0
        linkStart = 0
        nextPosition = 0
        PDFSource = BMCPH+"&page=%s"%(i)   #the %s is like a pointer which is replaced by i; done here because cannot concatenate integer to string  
        print ("Getting Page ",i," of ",numPages)
        res = requests.get(PDFSource)
        while linkStart != -1:
            sanityCheck = sanityCheck + 1
            linkStart = res.text.find(PDFstring, nextPosition)
            if sanityCheck > failsafe or linkStart == -1:  
                break   
            linkEnd = res.text.find('"',linkStart)
            PDFList.append (res.text[linkStart:linkEnd]) 
            nextPosition = linkEnd
                        
        #PDFList.extend (getPDFList(res.text))
        #print (PDFSource)

    #return PDFList

getPDFList()

#,"status","DLC","PDFDate"] #DLC is the Date Last Checked

#Save the PDF list to a CSV file
filename = "PDF_List_" + keyword + ".csv"
thisFile = open(filename,"w+")

with thisFile as f:
    for item in PDFList:
        f.write(item+"\n")
        #f.write(",".join(map(str, item))+"\n")
        
print ("Total PDFs in list: ",len(PDFList),". File has been written to ",filename)

#print (PDFList)

#def getPDFs(PDFList):
#    testfile = urllib.URLopener()
#   
#   testfile.retrieve("http://randomsite.com/file.gz", "file.gz")


#folder_location = r'E:\webscraping'
#if not os.path.exists(folder_location):os.mkdir(folder_location)    

#STEPS
# Change the keyword from a variable to a list
# Change the journal URL from a variable to a list
#
# Check if a CSV file already exists for the journal and keyword being mined
# If a file doe not exist:
#   - Create an empty CSV 
#   - Fetch the PDF list
#   - Add Status and Date to each record
#   - Write the PDF list to the CSV
# If a CSV file does exist
#   - Read the CSV file into Python (let this be "old")
#   - Create PDF list from the site (let this be "new")
#   - Compare the two lists (each item in "old" against all items in "new")
#   - For each record, add if new and set status (e.g. new, old, archived)
#   - Update other variables as appropriate (e.g. date)
#   - Overwrite CSV 
# Downloading PDFS
#   - For each status = "new", download the PDF
#   - For each status = "archived" do nothing
#   - For each status = "old" check if the PDF online is different from the one previously downloaded
 






















