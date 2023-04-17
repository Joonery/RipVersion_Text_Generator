from ripgen import *

if __name__ == "__main__" :
    PATH_ORIGINAL_TEXT = "data/original.txt"
    PATH_TARGET_TEXT = "data/target.txt"
    PATH_OUTPUT = "data/output.txt"
    MIN_CORPUS_SIZE = 5
    DELETE_RATE = 0.1
    TARGET_RATE = 0.3
    PER_LINE_SIZE = 100
    TOTAL_LINE = 8

    generator = RIPVERSION_TEXT_GENERATOR(PATH_ORIGINAL_TEXT, PATH_TARGET_TEXT, PATH_OUTPUT, MIN_CORPUS_SIZE, DELETE_RATE, TARGET_RATE, PER_LINE_SIZE, TOTAL_LINE)
    generator.run()