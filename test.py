import os
import glob
directories = glob.glob("/Users/kristofferorum/Dropbox/projects/[0-9][0-9][0-9][0-9]*")
print directories
pNames = [ os.path.basename(os.path.normpath(element)).split(' ', 1 ) for element in directories]
print pNames