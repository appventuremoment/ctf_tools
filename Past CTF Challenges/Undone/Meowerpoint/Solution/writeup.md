Forensics(??) Challenge

First, in your file explorer on windows, click View > Show > File name extensions
Then, change the pptx to a zip file since powerpoint presentations are basically fancy zip files. 
Extract the zip file to another folder and go ppt > media folder. This should show the files below.

![nice try]()

Running the 3 images through the usual file stuff (grep, exiftool, binwalk, steghide, aperisolve.com) gave nothing.

Next, open the 2 glb files (3D Model File) in blender or glb file extractor to get the file meshes at https://products.aspose.app/3d/extractor/glb. For the latter method, you should find something like this in the zip folder:

![nice try]()

After this, looking through all of them we should find the flag written in texture.png blahaj{blahaj_hate_crime_;(}