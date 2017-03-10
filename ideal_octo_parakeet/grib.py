import struct

class Grib(object):
    def __init__(self, inputfile):
        self.file = inputfile

        self.parse()

    def parse(self):
        with open(self.file, 'rb') as f:

            buffer = f.read(16)
            indicator_section = struct.unpack('>4sHBBQ', buffer)
            magic, reserved, discipline, edition, length = indicator_section

            # assert magic == b'GRIB'

            self.discipline = discipline
            self.edition = edition
            self.grib_message_length = length

    def __str__(self):
        return "blah"
