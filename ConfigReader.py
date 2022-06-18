class Configreader:
    def __init__(self, splitwith="="):
        self.splitwith = splitwith

    def readfile(self, filepath):
        with open(filepath, 'r') as f:
            filecontents = [i.strip('\n') for i in f.readlines()]

        out = {}
        for line in filecontents:
            try:
                out[line.split('=')[0]] = line.split('=')[1]
            except IndexError:
                pass

        return out
