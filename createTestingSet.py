import requests;
import json;
import unicodecsv as csv

movieCount = 1;
seedMovie = 180903;
maxCount = 300;

movieIdSuffix = seedMovie

fieldNames = ['imdbID', 'Title', 'Plot', 'Genre1', 'Genre2', 'Genre3'];


def getNewDict(data):
    newDict = {}
    newDict["imdbID"] = data["imdbID"]
    newDict["Title"] = data["Title"]
    newDict["Plot"] = data["Plot"]

    genres = data["Genre"].split(',')

    i=1;
    for genre in genres:
        newDict["Genre" + str(i)] = genre
        i=i+1;

    for j in range(i,4):
        newDict["Genre" + str(j)] = ""

    return newDict


with open('testingSet.csv','wb') as csvfile:
    csvwriter = csv.DictWriter(csvfile, fieldNames, extrasaction='ignore')
    csvwriter.writeheader()

    while movieCount <= maxCount:
        try:
            r = requests.get("http://www.omdbapi.com/?plot=full&i=tt0" + str(movieIdSuffix));
            data = json.loads(r.text);
            response = data['Response']
            if (response == "True"):
                plot = data['Plot']
                type = data['Type']
                genre = data['Genre']
                language = data['Language']
                country = data['Country']

                if (type == 'movie' and len(plot) > 10 and genre != 'N/A' and language == 'English' and country == 'USA'):
                    print "Processing movie no : %d" %(movieCount);
                    movieCount += 1;
                    finalData = getNewDict(data)
                    csvwriter.writerow(finalData);

            movieIdSuffix += 1

        except Exception:
            movieIdSuffix += 1
            continue

print movieIdSuffix