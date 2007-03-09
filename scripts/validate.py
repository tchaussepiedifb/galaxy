#!/usr/bin/env python

"""
Validate a dataset based on extension a metadata passed in on the
command line.  Outputs a binhex'd representation of the exceptions.

usage: %prog input output
    -c, --cols=N,N,N,N: column metadata, in the case of GFF, BED, or intervals
    -x, --ext=N: extension as understood by galaxy
"""
from cookbook import doc_optparse
from galaxy import model
from fileinput import FileInput
from galaxy import util

def main():
    options, args = doc_optparse.parse( __doc__ )

    try:
        extension = options.ext
    except:
        doc_optparse.exception()

    # create datatype
    data = model.Dataset( extension=extension, id=int( args[0] ) )
    data.file_path = "/home/ian/trunk/database/files/"
    
    if options.cols:
        cols = options.cols.split(",")
        data.metadata.chromCol = cols[0]
        data.metadata.startCol = cols[1]
        data.metadata.endCol = cols[2]
        data.metadata.strandCol = cols[3]

    errors = data.datatype.validate( data )
    print util.object_to_string(errors)

if __name__ == "__main__":
    main()
