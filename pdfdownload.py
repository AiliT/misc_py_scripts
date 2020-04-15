from bs4 import BeautifulSoup
import requests
import os.path


#get path to save files to
target = input("Give me a path to save files to: ")

while (not os.path.exists(target)):   
    print("Invalid filename. Please try again (or hit CTRL+C to exit).")
    target = input("Give me a path to save files to: ")


#get url to download from
url = input("Give me a URL to download files from: ")

while (True):
    try:
        if requests.get(url).status_code == requests.codes.ok:
            break
        else:
            raise Exception
    except:
        print("Couldn't open URL. Please try again (or hit CTRL+C to exit).")
        url = input("Give me a URL to download files from: ")

#open url
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

#define function that finds all pdf urls
def is_pdf_file(tag):
    return tag.has_attr('href') and tag['href'].endswith('.pdf')


tries = 0
downloads = 0

#find all pdfs
for i in soup.find_all(is_pdf_file):

    #get the filename
    name = i['href']

    #inform user
    print("Downloading " + name)

    #save file to the target directory
    try:
        tries += 1
        
        with open(target + name, 'wb') as f:
            f.write(requests.get(url + name).content)

        downloads += 1
    except:
        print("Couldn't download " + name)


#inform user
print("\nProgram finished, " + str(downloads) + " files downloaded out of " + str(tries) + ".")
