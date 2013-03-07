alphas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

dirname = "getty_data/"

with open("all_artists.json","w") as fh:
    fh.write("[\n")
    count = 0
    while count < 26:
        with open(dirname+"artist_" + alphas[count] +".json","r") as fe:
            prev_line = fe.readline().strip()
            for line in fe:
                if line.strip() != "":
                    fh.write(prev_line+","+"\n")
                    prev_line = line.strip()
            fh.write(prev_line)
            if count < 25 and prev_line != "":
                fh.write(",")
            fh.write("\n")
        count += 1
    fh.write("]")
    
with open("all_collections.json","w") as fc:
    fc.write("[\n")
    count = 0
    while count < 26:
        with open(dirname+"artwork_"+alphas[count] +".json","r") as fe:
            prev_line = fe.readline().strip()
            for line in fe:
                if line.strip() != "":
                    fc.write(prev_line+","+"\n")
                    prev_line = line.strip()
            fc.write(prev_line)
            if count < 25 and prev_line != "":
                fc.write(",")
            fc.write("\n")
        count += 1
    fc.write("]")
        
