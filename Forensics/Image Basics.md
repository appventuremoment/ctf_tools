# CTF Image Steganography Checklist
---------------------------------

Each example image contains a flag.

_This checklist needs more work! Please contribute [here]({{ contributeSteps }})._

* * *

  

#### 1\. File

Just to be sure what file you are facing with, check its type with type filename.

  
  

#### 2\. Strings

View all strings in the file with strings -n 7 -t x filename.png.

We use \-n 7 for strings of length 7+, and \-t x to view- their position in the file.

Alternatively, you can view strings on this site once an image has been uploaded.

[Custom Example]({{ images.strings }})

  
  

#### 3\. Exif

Check all image metadata. I would recommend [Jeffrey's Image Metadata Viewer](http://exif.regex.info/exif.cgi) for in-depth analysis.

[Custom Example]({{ images.exif }})

  
  

#### 4\. Binwalk

We use binwalk to check image's for hidden embedded files.

My preferred syntax is binwalk -Me filename.png. \-Me is used to recursively extract any files.

[Custom Example]({{ images.binwalk }})

  
  

#### 5\. pngcheck

We can use pngcheck to look for optional/correct broken chunks. This is vital if the image appears corrupt.

Run pngcheck -vtp7f filename.png to view all info.

v is for verbose, t and 7 display tEXt chunks, p displays contents of some other optional chunks and f forces continuation after major errors are encountered.

Related write-ups:

*   [PlaidCTF 2015](https://github.com/ctfs/write-ups-2015/tree/master/plaidctf-2015/forensics/png-uncorrupt)
*   [SECCON Quals 2015](https://github.com/ctfs/write-ups-2015/tree/master/seccon-quals-ctf-2015/stegano/steganography-2)

  
  

#### 6\. Explore Colour & Bit Planes

Images can be hidden inside of the colour/bit planes. Upload your image to this site [here](upload). On the image menu page, explore all options in the top panel (i.e. Full Red, Inverse, LSB etc).

Go to "Browse Bit Planes", and browse through all available planes.

If there appears to be some static at the top of any planes, try extracting the data from them in the "Extract Files/Data" menu.

Related write-ups:

*   [MicroCTF 2017](https://www.doyler.net/security-not-included/image-steganography-microctf-2017)
*   [CSAW Quals 2016](https://github.com/krx/CTF-Writeups/blob/master/CSAW%2016%20Quals/for250%20-%20Watchword/jk_actual_writeup.md)
*   [ASIS Cyber Security Contest Quals 2014](https://github.com/ctfs/write-ups-2014/tree/master/asis-ctf-quals-2014/blocks)
*   [Cybersocks Regional 2016](https://mokhdzanifaeq.github.io/2016/12/14/cybersocks-regional-2016-color-writeup/)

  
  

#### 7\. Extract LSB Data

As mentioned in step 5, there could be some static in bit planes. If so, navigate to the "Extract Files/Data" page, and select the relevant bits.

[Custom Example]({{ images.lsb }})

  
  

#### 8\. Check RGB Values

ASCII Characters/other data can be hidden in the RGB(A) values of an image.

Upload your image [here](upload), and preview the RGBA values. Try converting them to text, and see if any flag is found. It might be worth looking at just the R/G/B/A values on their own.

Related write-ups:

*   [MMA-CTF-2015](https://github.com/ctfs/write-ups-2015/tree/master/mma-ctf-2015/stego/miyako-350)

  
  

#### 9\. Found a password? (Or not)

If you've found a password, the goto application to check should be [steghide](http://steghide.sourceforge.net/). Bear in mind that steghide can be used without a password, too.

You can extract data by running steghide extract -sf filename.png.

It might also be worth checking some other tools:

*   [OpenStego](https://www.openstego.com/)
*   [Stegpy](https://github.com/Baldanos/Stegpy)
*   [Outguess](https://outguess.rbcafe.com/)
*   [jphide](http://linux01.gwdg.de/~alatham/stego.html)

Related write-ups:

*   [Pragyan CTF 2017](http://blog.teambroast.com/2017/03/pragyan-star-wars-steganography-100.html)
*   [Xiomara 2019](https://github.com/mzfr/ctf-writeups/tree/master/xiomara-2019/Forensics/Steghide)
*   [CSAW Quals 2015](https://github.com/ctfs/write-ups-2015/tree/master/csaw-ctf-2015/forensics/airport-200)
*   [BlackAlps Y-NOT-CTF (JFK Challenge)](https://blog.compass-security.com/2017/11/write-up-blackalps-y-not-ctf/)

  
  

#### 10\. Browse Colour Palette

If the PNG is in [type 3 for type specs](https://www.w3.org/TR/PNG-Chunks.html), you should look through the colour palette.

This site has a feature for randomizing the colour palette, which may reveal the flag. You can also browse through each colour in the palette, if the flag is the same colour.

It may also be worth looking at the palette indexes themselves, as a string may be visible from there.

Related write-ups:

*   [Plain CTF 2014](https://github.com/ctfs/write-ups-2014/tree/master/plaid-ctf-2014/doge-stege)

  
  

##### 11\. Pixel Value Differencing (PVD/MPVD)

It would be rare to have a case of PVD where you're not explicitly told that this is the steganographic method, as it's very niche.

However, this is a method where the differences between pixel pairs are measured slightly adjusted in order to hide data.

A full paper on this process can be found [here](https://pdfs.semanticscholar.org/c893/fb37bda9cdffc12dcd1be33d01fed502ae32.pdf). A PVD feature to this site would be appreciated!

Related write-ups:

*   [TJCTF 2019](https://github.com/zst-ctf/tjctf-2019-writeups/tree/master/Writeups/Planning_Virtual_Distruction)
*   [MMA-CTF 2015](https://github.com/ctfs/write-ups-2015/tree/master/mma-ctf-2015/stego/miyako-350)

* * *

_Please contribute more steps [here]({{ contributeSteps }})._
