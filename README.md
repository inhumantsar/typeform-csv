task1
=====

# Install

setuptools will install the pre-requisites automagically.

    $ sudo python setup.py install

# Usage

    # dump to a file
    $ task1 -k somelongapikey -o /path/to/somefile.csv

    # dump to stdout
    $ task1 -k somelongapikey

    # specify form and apikey
    $ task1 -k somelongapikey -f formid 
