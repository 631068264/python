# pipeline.py
#
# An example of setting up a processing pipeline with generators
from coroutines.lesson1.follow import follow


def grep(pattern, lines):
    for line in lines:
        if pattern in line:
            yield line


if __name__ == '__main__':

    # Set up a processing pipe : tail -f | grep python
    logfile = open("../access-log")
    loglines = follow(logfile)
    pylines = grep("python", loglines)

    # Pull results out of the processing pipeline
    for line in pylines:
        print line,
