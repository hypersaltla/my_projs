alphas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("getty_data_img/all_artists.json","w") as fh:
    count = 0
    while count < 26:
        with open("getty_data_img/artist_" + alphas[count] +".json","r") as fe:
            for line in fe:
                if line != "\n":
                    fh.write(line)
        count += 1
with open("getty_data_img/all_collections.json","w") as fc:
    count = 0
    while count < 26:
        with open("getty_data_img/artwork_"+alphas[count] +".json","r") as fe:
            for line in fe:
                if line != "\n":
                    fc.write(line)
        count += 1
        
