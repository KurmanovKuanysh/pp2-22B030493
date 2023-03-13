import os

fpath = '/PP2-22B030493/TSIS#7'
if not os.path.exists(fpath):
    print("path doesn't exist")


if os.path.exists(fpath):
    os.remove(fpath)