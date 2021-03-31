from wiki_dump_reader import Cleaner, iterate
from sys import getsizeof
from math import floor

totssize = 0
totcsize = 0

cleaner = Cleaner()
for title, text in iterate("source.xml"):
    print("Compressing '",title,"'",sep="")
    text = cleaner.clean_text(text)
    source, links = cleaner.build_links(text)

    source += "\n"
    compsource = []
    currentword = ""
    whitespace = [" ","\n",".",";"]
    dictionary = whitespace.copy()

    for x in source:
        if x in whitespace and currentword != "":
            if not currentword in dictionary:
                dictionary.append(currentword)
            
            compsource.append(dictionary.index(currentword))
            compsource.append(dictionary.index(x))
            currentword = ""
        elif x in whitespace:
            compsource.append(dictionary.index(x))
        else:
            currentword += x

    recompsource = ""
    for n in compsource:
        recompsource += dictionary[n]

    if recompsource == source: print("Success!")
    else: print("Recompiled source doesn't match original")

    print("== Approx Sizes ==")
    ssize = len(source) # source size
    dsize = len(" ".join(dictionary)) # dictionary size
    osize = len(compsource) # compsource size
    csize = dsize + osize # compressed size

    totssize += ssize
    totcsize += csize
    
    print("Source size: ",ssize,"Bytes")
    print("Output size: ",csize,"Bytes")
    print("  Dict size: ",dsize,"Bytes")
    print("  Key size:  ",osize,"Bytes (using 8bit unsigned ints)\n")

    print("Compression Ratio: ~",floor(csize*100 / ssize),"%",sep="")

print("==== FINAL RESULTS ====")
print("Total Source size: ",totssize,"Bytes")
print("Total Output size: ",totcsize,"Bytes\n")

print("Compression Ratio: ~",floor(totcsize*100 / totssize),"%",sep="")
