#!/usr/bin/python

class AsciiEditor:
    imageRows = []

    def initializeImage(self, columns, rows):
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

        xStart = self.getRegionXStart(column, row)
        xEnd = self.getRegionXEnd(column, row)
        yStart = self.getRegionYStart(column, row)
        yEnd = self.getRegionYEnd(column, row)

        for row in range(yStart, yEnd + 1):
            self.drawHorizontalSegment(xStart, xEnd, row, drawLetter)

    def getRegionXStart(self, column, row):
        letter = self.getPixel(column, row)

        while (self.getPixel(column, row) == letter and column != 0):
            column = column - 1

        return column + 1

    def getRegionYStart(self, column, row):
        letter = self.getPixel(column, row)

        while (self.getPixel(column, row) == letter and row != 0):
            row = row - 1

        return row + 1

    def getRegionXEnd(self, column, row):
        letter = self.getPixel(column, row)

        while (self.getPixel(column, row) == letter and column != len(self.imageRows[row]) + 1):
            column = column + 1

        return column - 1

    def getRegionYEnd(self, column, row):
        letter = self.getPixel(column, row)

        while (self.getPixel(column, row) == letter and row != len(self.imageRows) + 1):
            row = row + 1

        return row - 1

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
