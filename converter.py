#!/usr/bin/python
import sys, getopt
from PIL import Image
def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofolder="])
        inputfile=outputfolder=''
        for opt, arg in opts:
            if opt == '-h':
                print 'converter.py -i <inputfile> -o <outputfolder>'
                sys.exit()
            elif opt in ("-i", "--ifile"):
                inputfile = arg
            elif opt in ("-o", "--ofolder"):
                outputfolder = arg
        if len(inputfile) and len(outputfolder):
            try:
                img = Image.open(inputfile)
                for i in range (img.n_frames):
                    img.seek(i)
                    img.save(outputfolder+'/'+inputfile+'_'+str(i)+'.png', format='PNG',optimize=True,quality=60)
            except:
                print "Unexpected error:", sys.exc_info()[0]
                sys.exit(0)
        else:
            print 'converter.py -i <inputfile> -o <outputfolder>'
            sys.exit()
    except getopt.GetoptError:
        print 'converter.py -i <inputfile> -o <outputfolder>'
        sys.exit(2)
if __name__ == "__main__":
    if len(sys.argv) >1:
        main(sys.argv[1:])
    else:
        print 'converter.py -i <inputfile> -o <outputfolder>'
        sys.exit()
