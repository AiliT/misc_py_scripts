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

#get needed extension (file type to download)
ext = input("Give me an extension to limit downloads to (default: pdf): ")
if ext == "":
    ext = "pdf"

#open url
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

#define function that finds all pdf urls
def has_ext(tag):
    return tag.has_attr('href') and tag['href'].endswith(f".{ext}")

# fixes url
if not url.endswith("/"):
    x = url.split("/")
    url = "/".join(x[:len(x) - 1]) + "/"

# fixes target path
if not target.endswith(os.path.sep):
    target += os.path.sep

tries = 0
downloads = 0
names = set()

#find all pdfs
for i in soup.find_all(has_ext):

    #get the filename
    name = i['href']
    
    # skip duplicates
    if name in names:
        continue
    names.add(name)

    #inform user
    print("Downloading " + name)

    #save file to the target directory
    try:
        tries += 1

        # extract file name from download path
        tname_parts = name.split("/")
        tname = tname_parts[len(tname_parts) - 1]
        
        with open(target + tname, 'wb') as f:
            f.write(requests.get(url + name).content)

        downloads += 1
    except:
        print("Couldn't download " + name)


#inform user
print("\nProgram finished, " + str(downloads) + " files downloaded out of " + str(tries) + ".")
