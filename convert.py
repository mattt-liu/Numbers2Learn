## Matthew Liu
## convert 'degradedpoints.txt' to csv

########## MODULES ##########
def main():
    import csv

    infile  = open("degradedPoints.txt", "r")
    outfile = open("dPoints.csv", 'w')

    ## take in points
    points = []
    for line in infile.readlines():
        for p in line.strip().split(" "):
            a = int(float(p)*255)
            points.append(a)

    ## write row of labels
    labels = []
    for i in range(len(points)):
        labels.append("pixel"+str(i))
    
    ## write to csv
    with open('dPoints.csv', 'w') as csvFile:
        wr = csv.writer(outfile)
        wr.writerow(labels)
        wr = csv.writer(outfile)
        wr.writerow(points)

    ##row = ['4', ' Danny', ' New York']
    ##with open('test.csv', 'w') as csvFile:
    ##    writer = csv.writer(csvFile)
    ##    writer.writerow(row)

    infile.close()
    outfile.close()


if __name__ == "__main__":
    main()
