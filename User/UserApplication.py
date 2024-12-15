
import os
from .Font import Font as Font
from .Font.StandardFont import StandardFont as StandardFont


class ApplicationSettings:
    # def __init__(self, width, height):
    #     self.m_width = width
    #     self.m_height = height
    def __init__(self):
        pass
        # self.m_width = width
        # self.m_height = height

    m_width = 0
    m_height = 0

    def start(self, width, height):
        self.m_width = width
        self.m_height = height

class Border:
    def __init__(self):
        self.m_width = 1
        self.m_shown = True

    m_width = 0
    m_shown = False

class Pixels:
    def __init__(self):
        pass

    def start(self, width, height):
        for i in range(0, height):
            self.m_screenPixels.append([])
            for j in range(0, width):
                self.m_screenPixels[i].append(" ")
                # self.m_screenPixels[i].append(" ")

    def setPixel(self, x, y, character):
        self.m_screenPixels[y][x] = character

    def pixel(self, x, y):
        return self.m_screenPixels[y][x]


    m_screenPixels = [[]]

class CharaterBox:
    def __init__(self, countInList):
        self.m_width = 0
        self.m_height = 0
        self.m_countInList = countInList
        self.m_text = [[]]

    def start(self, boxWidth, boxHeight):
        self.m_width = boxWidth
        self.m_height = boxHeight

        for i in range(0, boxHeight):
            self.m_text.append([])
            for j in range(0, boxWidth):
                # self.m_text[i].append('=')
                self.m_text[i].append(" ")

    def setBoxToSource(self, sources = []):
        for i in range(0, len(sources)):
            for j in range(0, len(sources[i])):
                for k in range(0, len(sources[i][j])):
                    self.m_text[j][k] = sources[i][j][k]


    def fillBox(self, character):
        for i in range(0, self.m_height):
            for j in range(0, self.m_width):
                self.m_text[i][j] = character

    def setFirstBox(self, character):
        self.m_text[0][0] = character

    def box(self, x, y):
        return self.m_text[y][x]


    m_countInList = 0
    m_width = 0
    m_height = 0
    m_text = [[]]

class BoxSettings:
    def __init__(self, width, height):
        self.m_width = width
        self.m_height = height

    m_width = 0
    m_height = 0

class Window:
    def __init__(self):
        self.m_posX = 0
        self.m_posY = 0
        self.m_width = 0 
        self.m_height = 0 
        self.m_border = Border()
        self.m_cursorPosition = 0
        self.m_pixels = Pixels()
   

    def start(self, applicationSettings):
        self.m_width = applicationSettings.m_width
        self.m_height = applicationSettings.m_height
        self.m_pixels.start(applicationSettings.m_width, applicationSettings.m_height)
        # for i in range(0, applicationSettings.m_height):
        #     self.m_pixels.append([])
        #     for j in range(0, applicationSettings.m_width):
        #         self.m_pixels[i].append('=')

        self.loadCharacterBoxes(applicationSettings, BoxSettings(6,6))

        self.drawWindow()


    def update(self, characters, font):
        self.configureCharacterBoxes(characters, font)
        self.setCharacterBoxes()

        self.drawWindow()

    def loadCharacterBoxes(self, applicationSettings, boxSettings):
        i = 0
        j = 0
        s = ""
        while i < applicationSettings.m_height:
            while j < applicationSettings.m_width:
                j += boxSettings.m_width

                characterBox = CharaterBox(len(self.m_characterBoxes))
                characterBox.start(boxSettings.m_width, boxSettings.m_height)
                self.m_characterBoxes.append(characterBox)
                # s += f"Pos X Y {j:10} {i:10}\n"
            i += boxSettings.m_height
            j = 0
        # f = open("characterPositionStart.txt", "w")
        # f.write(s)

    def configureCharacterBoxes(self, characters, font):
        if len(self.m_characterBoxes) == 0:
            return

        if self.m_cursorPosition == len(self.m_characterBoxes):
            return

        # if font.m_fontWidth == 6:
        #     print("font set standard")

        # Use character boxes own width with its class
        if (font.m_fontWidth != self.m_characterBoxes[0].m_width) | (font.m_fontHeight != self.m_characterBoxes[0].m_height):
            print("Incompatible font sizes and can't draw")
            return



        for i in range(0, len(characters)):
            matchedSources = font.matchCharacter(characters[i])
            self.m_characterBoxes[self.m_cursorPosition].setBoxToSource(sources = matchedSources)
            if self.m_cursorPosition != len(self.m_characterBoxes):
                self.m_cursorPosition += 1


    def setCharacterBoxes(self):
        characterCount = 0
        i = 0
        j = 0
        s = ""
        while i < self.m_height:
            while j < self.m_width:
                startX = j
                startY = i
                for iterateCharacterY in range(0, self.m_characterBoxes[characterCount].m_height):
                    for iterateCharacterX in range(0, self.m_characterBoxes[characterCount].m_width):
                        self.m_pixels.setPixel(startX + iterateCharacterX, startY + iterateCharacterY, self.m_characterBoxes[characterCount].box(iterateCharacterX, iterateCharacterY))
                        # s += f"Pos X Y {startX + iterateCharacterX:10} {startY + iterateCharacterY:10}\n"

                j += self.m_characterBoxes[characterCount].m_width
                if characterCount < len(self.m_characterBoxes) - 1:
                    characterCount += 1
            i += self.m_characterBoxes[characterCount].m_height
            j = 0
        # file = open("positions.txt", "w")
        # file.write(s)


    def drawWindow(self):
        os.system("clear")
        os.system("clear")

        # self.m_window.reloadCharacterBoxes()

        if self.m_border.m_shown == True:
            s = ""
            for i in range(0, self.m_border.m_width):
                s += '+'
                for j in range(0, self.m_width):
                    s += '-'
                s += '+'
                print(s)

      
        for i in range(0, self.m_height):
            s = ""
            if self.m_border.m_shown == True:
                for k in range(0, self.m_border.m_width):
                    s += "|"
            for j in range(0, self.m_width):
                # s += self.m_pixels[i][j]
                s += self.m_pixels.pixel(j,i)
            if self.m_border.m_shown == True:
                for k in range(0, self.m_border.m_width):
                    s += "|"
            print(s)


        if self.m_border.m_shown == True:
            s = ""
            for i in range(0, self.m_border.m_width):
                s += '+'
                for j in range(0, self.m_width):
                    s += '-'
                s += '+'
                print(s)


    m_posX = 0
    m_posY = 0
    m_width = 0
    m_height = 0

    m_border = Border

    m_cursorPosition = 0
    m_characterBoxes = []

    m_pixels = Pixels

class Command:
    def __init__(self):
        self.m_message = []

    def readCommand(self):
        s = input()
        for i in range(0, len(s)):
            self.m_message.append(s[i])

    def clearMessage(self):
        self.m_message = []

    def messageToString(self):
        s = ""
        for i in range(0, len(self.m_message)):
            s += self.m_message[i]
        return s

    def message(self):
        return self.m_message
        

    m_message = []


class UserApplication:
    def __init__(self):
        self.m_isOver = False
        self.m_window = Window()
        self.m_command = Command()
        self.m_font = StandardFont.StandardFont()

    def onDestroy(self):
        pass

    def start(self, applicationSettings):
        self.m_window.start(applicationSettings)

    def run(self):
        while self.m_isOver != True:
            self.m_command.readCommand()
            self.m_window.update(self.m_command.message(), self.m_font)
            if self.m_command.messageToString() == "exit":
                self.m_isOver = True
            self.m_command.clearMessage()


        
    m_font = Font.Font
    m_window = Window
    m_command = Command
    m_isOver = False






