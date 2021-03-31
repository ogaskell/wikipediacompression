# wikipediacompression
 A program to test simple dictionary coding compression on a collection of wikipedia articles.
 
main.py will open source.xml, and attempt to read all wikipedia articles within it. It will iterate through each, compress it with a simple dictionary coding algorithm, and print the results to the console. After the collection has been fully compressed, the compression ratio of the entire collection is also printed.

Currently the compressed articles are not stored, and if they were the compression ratio would likely not be as good as reported since the printed values are based on rough estimates.

This is just a proof of concept for my CS class.

I ran the program on all articles in the `Computer science` category on wikipedia, and the results were as follows:

```
Total Source size:  562529 Bytes
Total Output size:  449213 Bytes

Compression Ratio: ~79%
```

Some articles did increase in size and had compression ratios over 100% so with some optimisiation the overall ratio could definitely be improved.

## Usage
To run the program, you need an XML file exported from wikipedia. Wikipedia has a page where you can download these [here](https://en.wikipedia.org/wiki/Special:Export). However I have included a few files which I have tested the program on, in the `source files` directory. The `source.xml` file in the root directory is simply a copy of the `computerscience(category).xml` file in this folder.

To run the program on an xml file, simply move it into the root directory of the repository and rename it to `source.xml`. The program will then operate on this file.
