import requests;
import json;
import unicodecsv as csv
import pandas as pd

movieCount = 0;
# seedMovie = 120903;
# maxCount = 500;
# movieIndex = 0
movies = pd.read_csv('links.csv')

# movieIdSuffix = movies['imdbId'][movieIndex]

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


with open('trainingSet.csv','wb') as csvfile:
    csvwriter = csv.DictWriter(csvfile, fieldNames, extrasaction='ignore')
    csvwriter.writeheader()

    for movieIdSuffix in movies['imdbId']:
        try:
            r = requests.get("http://www.omdbapi.com/?plot=full&i=tt0" + str(movieIdSuffix));
            data = json.loads(r.text);
            response = data['Response']
            if (response == "True"):
                plot = data['Plot']
                type = data['Type']
                genre = data['Genre']
                # language = data['Language']
                # country = data['Country']

                if (type == 'movie' and len(plot) > 50 and genre != 'N/A'):
                    movieCount += 1;
                    print "Processing movie no : %d" %(movieCount);
                    finalData = getNewDict(data)
                    csvwriter.writerow(finalData);

            # movieIndex += 1
            # movieIdSuffix = movies['imdbId'][movieIndex]

        except Exception:
            # movieIndex += 1
            # movieIdSuffix = movies['imdbId'][movieIndex]
            continue

print movieIdSuffix