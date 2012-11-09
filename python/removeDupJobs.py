lines_seen = set() # holds lines already seen
outfile = open("jobTitles", "w")
for line in open("jobTitles.txt", "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
