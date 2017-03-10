import argparse

from .grib import Grib

def gbdump():

    parser = argparse.ArgumentParser()
    parser.add_argument('inputfile', type=str)

    args = parser.parse_args()

    gb = Grib(args.inputfile)
    print(gb)
