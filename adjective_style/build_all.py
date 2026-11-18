import sys
from adjgen import build
import errors_13_to_18 as a, errors_19_to_32 as b
if __name__ == '__main__':
    build(sys.argv[1], a.story + [a.PageBreak()] + b.story)
