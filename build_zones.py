#!/usr/bin/env python
import shutil
import subprocess

# produce multiple .pbw with varying time offsets

if __name__ == "__main__":
    # first save the orignal c file
    shutil.copyfile('src/DblTime.c', 'src/DblTime.c.orig')
    
    startingTimeOffset = 24
    endingTimeOffset = 32

    for curTimeOffset in xrange( startingTimeOffset, endingTimeOffset+1):
        # copy the original file as we edit in place
        shutil.copyfile('src/DblTime.c.orig', 'src/DblTime.c')
        sedString = "sed -i.bak 's:DEFAULT_TIME_OFFSET 30:DEFAULT_TIME_OFFSET "
        sedString += str(curTimeOffset)
        sedString += ":' src/DblTime.c"
        print sedString
        sub = subprocess.call(sedString, shell=True )

        # next build it
        sub = subprocess.call("./waf build", shell =True)

        # next copy the DblTime.pbw to descriptive filenames
        destFileName = "build/UsaMnlTime_"
        destFileName += "plus_"
        if ( curTimeOffset < 0):
            destFilename = "minus_"
        destFileName += str (curTimeOffset) + ".pbw"
        shutil.copy ("build/DblTime.pbw", destFileName)


    # copy the usa time zones
    shutil.copy("build/UsaMnlTime_plus_32.pbw","build/UsaMnlTime_PST.pbw");
    shutil.copy("build/UsaMnlTime_plus_30.pbw","build/UsaMnlTime_PDT.pbw");
    shutil.copy("build/UsaMnlTime_plus_30.pbw","build/UsaMnlTime_MST.pbw");
    shutil.copy("build/UsaMnlTime_plus_28.pbw","build/UsaMnlTime_CST.pbw");
    shutil.copy("build/UsaMnlTime_plus_28.pbw","build/UsaMnlTime_MDT.pbw");
    shutil.copy("build/UsaMnlTime_plus_26.pbw","build/UsaMnlTime_CDT.pbw");
    shutil.copy("build/UsaMnlTime_plus_26.pbw","build/UsaMnlTime_EST.pbw");
    shutil.copy("build/UsaMnlTime_plus_24.pbw","build/UsaMnlTime_EDT.pbw");

    # copy the original file again
    shutil.copyfile('src/DblTime.c.orig', 'src/DblTime.c')
