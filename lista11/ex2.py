import time
import datetime
def quando(momento):

    difference = (momento - datetime.datetime.now())
    total_seconds = difference.total_seconds()
    return total_seconds
