Forensics(??) Challenge

First, in your file explorer on windows, click View > Show > File name extensions
Then, change the pptx to a zip file since powerpoint presentations are basically fancy zip files. 
Extract the zip file to another folder and go ppt > media folder. This should show the files below.

![nice try](https://github.com/appeventuremoment/ctf_tools/blob/main/Past%20CTF%20Challenges/BlahajCTF/Meowerpoint/Solution/image.png)

Running the 3 images through the usual file stuff (grep, exiftool, binwalk, steghide, aperisolve.com) gave nothing.

Next, open the 2 glb files (3D Model File) in blender or glb file extractor to get the file meshes at https://products.aspose.app/3d/extractor/glb. For the latter method, you should find something like this in the zip folder:

![nice try](https://github.com/appeventuremoment/ctf_tools/blob/main/Past%20CTF%20Challenges/BlahajCTF/Meowerpoint/Solution/image2.png)

After this, looking through all of them we should find the flag written in texture.png blahaj{blahaj_hate_crime_;(}

Not bad, forensics/10