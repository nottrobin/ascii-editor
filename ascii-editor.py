#!/usr/bin/python

class AsciiEditor:
    imageRows = []

    def initializeImage(self, columns, rows):
        self.imageRows = []

        columns = int(columns)
        rows = int(rows)

        for rowNumber in range(0, rows):
            row = ['O'] * columns

            self.imageRows.append(row)

    def clearImage(self):
        self.imageRows = [['O'] * len(row) for row in self.imageRows]

    def getPixel(self, column, row):
        return self.imageRows[int(row) - 1][int(column) - 1]

    def drawPixel(self, column, row, drawLetter):
        self.imageRows[int(row) - 1][int(column) - 1] = drawLetter

    def drawVerticalSegment(self, column, rowStart, rowEnd, drawLetter):
        for row in range(int(rowStart), int(rowEnd) + 1):
            self.drawPixel(column, row, drawLetter)

    def drawHorizontalSegment(self, columnStart, columnEnd, row, drawLetter):
        for column in range(int(columnStart), int(columnEnd) + 1):
            self.drawPixel(column, row, drawLetter)

    def fillRegion(self, column, row, drawLetter):
        column = int(column)
        row = int(row)

        self.drawMatchingSiblings(column, row, self.getPixel(column, row), drawLetter)

    def drawMatchingSiblings(self, column, row, oldLetter, newLetter):
        if (column < 1 or row < 1 or row > len(self.imageRows) or column > len(self.imageRows[row - 1]) or self.getPixel(column, row) != oldLetter):
            return

        self.drawPixel(column, row, newLetter)

        self.drawMatchingSiblings(column + 1, row, oldLetter, newLetter)
        self.drawMatchingSiblings(column - 1, row, oldLetter, newLetter)
        self.drawMatchingSiblings(column, row + 1, oldLetter, newLetter)
        self.drawMatchingSiblings(column, row - 1, oldLetter, newLetter)
        self.drawMatchingSiblings(column + 1, row + 1, oldLetter, newLetter)
        self.drawMatchingSiblings(column + 1, row - 1, oldLetter, newLetter)
        self.drawMatchingSiblings(column - 1, row + 1, oldLetter, newLetter)
        self.drawMatchingSiblings(column - 1, row - 1, oldLetter, newLetter)

    def showImage(self):
        for row in self.imageRows:
            print "".join(row)

editor = AsciiEditor()

actions = {
    'I': editor.initializeImage,
    'C': editor.clearImage,
    'L': editor.drawPixel,
    'V': editor.drawVerticalSegment,
    'H': editor.drawHorizontalSegment,
    'F': editor.fillRegion,
    'S': editor.showImage,
    'X': exit
}

while True:
    commands = raw_input('> ').upper().split()
    action = commands.pop(0)
    actions[action](*commands)
