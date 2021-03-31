# wikipediacompression
 A program to test simple dictionary coding compression on a collection of wikipedia articles.
 
main.py will open source.xml, and attempt to read all wikipedia articles within it. It will iterate through each, compress it with a simple dictionary coding algorithm, and print the results to the console. After the collection has been fully compressed, the compression ratio of the entire collection is also printed.

Currently the compressed articles are not stored, and if they were the compression ratio would likely not be as good as reported since the printed values are based on rough estimates.

This is just a proof of concept for my CS class.
