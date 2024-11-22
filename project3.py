# CPS121 Project 3
# Written: 11-21-24 Alida Grim alida.grim@gordon.edu
# 
# The purpose of this program is to take a variety of different pictures,
# apply functions to each image to transform them in different ways and put them
# into a collage. The program will then take that collage and put it into an
# html file where it can then be turned into a webpage for everyone to view. 

# Change each occurrence of "_" in the list below to be "Y" or "N" to indicate
# whether or not the given transformation is implemented in your program.
#
#   Can be done using just getPixels()
#   Y Altering colors of the image
#   Y Grayscale
#   Y Making darker or lighter
#   Y Sepia-toned
#   Y Posterized
#   Need nested loops
#   Y Mirrorizing
#   Y Edge detection
#   N Chromakey (change background)
#   N Blurring
#   Need nested loops and alter size or shape
#   Y Rotation
#   Y Cropping
#   N Shifting
#   Other transformations
#   N <description of transformation>
#   N <description of transformation>
#   N <description of transformation>
# ============================================================================

import GCPictureTools as pgt
import pygame as pg
import os, sys
import traceback

# ============================================================================
# ================ Start making changes after this comment ===================
# ============================================================================

def grayScale(picture):
    """Convert Image to grayscale
    Args:
    picture(picture): picture to be changed to greyscale (unchanged)
    Returns:
    picture: greyscaled picture
    """
    for x in range(0, picture.getWidth()):
        for y in range (0, picture.getHeight()):
            value = (picture.getRed(x,y) + picture.getGreen(x,y) + picture.getBlue(x,y))/3
            picture.setRed(x,y,value)
            picture.setGreen(x,y, value)
            picture.setBlue(x,y, value)


def edge(canvas):
    """Do edge detection in a picture
    Args: 
    canvas(picture): picture to be edge detected (unchanged)
    Returns:
    canvas: picture that has been edge detected. 
    """
    height= canvas.getHeight()
    width = canvas.getWidth()
    for p in canvas.getPixels():
        red = p.getRed()
        green = p.getGreen()
        blue = p.getBlue()
        x = p.getX()
        y = p.getY()
        p1= pgt.Pixel(p.getPicture(), p.getX()+1, p.getY()+1)
        if y < height-1 and x < width-1:
            sum = red+green+blue
            sum2 = p1.getRed()+p1.getGreen() + p1.getBlue()
            diff = min(255, abs(sum2-sum))
            canvas.setColor(p.getX(),p.getY(), (diff, diff, diff))


def cropIt(pic, newWidth, newHeight):
    """Crops a picture
    Args:
    pic(picture): picture to be cropped (unchanged)
    newWidth(width): desired new width of picture
    newHeight(height): desired new height of picture
    Returns:
    newPic: cropped picture
    """
    width = pic.getWidth()
    height = pic.getHeight()
    widthSpace= (width-newWidth)//2
    heightSpace= (height-newHeight)//2
    newPic = pgt.Picture(newWidth, newHeight)
    for col in range(0, newWidth):
        for row in range(0, newHeight):
            color = pic.getColor(col + widthSpace, row + heightSpace)
            newPic.setColor(col, row, color)
    return newPic


def inverse(picture):
    """Inverts the colors of a picture
    Args:
    picture(picture): picture to be inverted (unchanged)
    Returns:
    picture: inverted picture
    """
    for x in range(0, picture.getWidth()):
        for y in range(0, picture.getHeight()):
            newRed = picture.getRed(x,y) * 0.299
            newGreen = picture.getGreen(x,y) * 0.587
            newBlue = picture.getBlue(x,y) * 0.114
            color = 255 - (newRed + newGreen + newBlue)
            #set color of pix as (color, color, color)
            picture.setColor(x,y, (color, color, color))


def darken(picture):
    """Darkens the picture
    Args:
    picture: picture to be darkened (unchanged)
    Returns:
    picture: darkened picture
    """
    for x in range(0, picture.getWidth()):
        for y in range(0, picture.getHeight()):
            picture.setRed(x,y, picture.getRed(x,y)*0.3)
            picture.setGreen(x,y, picture.getGreen(x,y)*0.3)


def rotate90R(pic):
    """Rotate a picture 90 degrees to the right (clockwise).
    Args:
    pic (Picture): Picture to be rotated (unchanged).
    Returns:
    Picture: Rotated picture.
    """
    width = pic.getWidth()
    height = pic.getHeight()
    canvas = pgt.Picture(height,width)
    for col in range (0, width):
        for row in range(0, height):
            color = pic.getColor(col, row)
            canvas.setColor(height-1-row, col, color)
    return canvas


def makeRed(picture):
    """Increase the red color in an image. 
    Args: 
    picture: picture to be reddened (unchanged)
    Return:
    picture: reddened picture 
    """
    for x in range(0, picture.getWidth()):
        for y in range(0, picture.getHeight()):
            picture.setBlue(x,y, picture.getBlue(x,y)*0.5)
            picture.setGreen(x,y, picture.getGreen(x,y)*0.5)


def makeGreen(picture):
    """Increase the red color in an image. 
    Args: 
    picture: picture to be greened (unchanged)
    Return:
    picture: greened picture 
    """
    for x in range(0, picture.getWidth()):
        for y in range(0, picture.getHeight()):
            picture.setRed(x,y, picture.getRed(x,y)*0.5)
            picture.setBlue(x,y, picture.getBlue(x,y)*0.5)


def sepiaTint(picture):
    """Make picture look old
    Args: 
    picture: picture to be tinted/look old (unchanged)
    Returns:
    picture: tinted/looking old picture    
    """
    grayScale(picture)
    for x in range(0, picture.getWidth()):
        for y in range(0, picture.getHeight()):
            red = picture.getRed(x,y)
            blue = picture.getBlue(x,y)
            #tint shadows
            if(red < 63):
                red = red * 1.1
                blue = blue * 0.9
            #tint midtones
            if (red > 62 and red < 192):
                red = red * 1.15
                blue = blue * 0.85
            #tint highlights
            if (red > 191):
                red = red * 1.08
            if (red > 255):
                red = 255
                blue = blue * 0.93
            #set the new color values
            picture.setBlue(x,y,blue)
            picture.setRed(x,y,red)

def mirrorHorizontal(picture):
    """Mirrors a picture horizontally
    Args:
    picture: picture to be mirrored (unchanged)
    Returns:
    picture: mirrored picture
    """
    mirrorPoint = int(picture.getHeight() / 2)
    height = picture.getHeight()
    for x in range(0, picture.getWidth()):
        for y in range(0, mirrorPoint):
            topPixel = picture.getPixel(x, y)
            bottomPixel = picture.getPixel(x, height-y-1)
            color = topPixel.getColor()
            bottomPixel.setColor(color)

def mirrorVertical(picture):
    """Mirrors a picture vertically
    Args:
    picture: picture to be mirrored (unchanged)
    Returns:
    picture: mirrored picture
    """
    mirrorPoint = int(picture.getWidth()//2)
    width = picture.getWidth()
    for y in range(0, picture.getHeight()):
        for x in range(0, mirrorPoint):
            leftPixel = picture.getPixel(x, y)
            rightPixel = picture.getPixel(width-x-1, y)
            color = rightPixel.getColor()
            leftPixel.setColor(color)

def posterize(picture):
    """Reduce color resolution of picture to 4 levels.
    Args:
    picture: picture to be posterized (unchanged)
    Returns:
    picture: posterized picture
    """
    for x in range(0, picture.getWidth()):
        for y in range(0,picture.getHeight()):
            red = picture.getRed(x,y)
            green = picture.getGreen(x,y)
            blue = picture.getBlue(x,y)
            #red setting
            if red < 64:
                picture.setRed(x,y,31)
            if red > 63 and red < 128:
                picture.setRed(x,y,95)
            if red > 127 and red < 192:
                picture.setRed(x,y,159)
            if red > 191 and red < 256:
                picture.setRed(x,y,233)
            #green setting
            if green < 64:
                picture.setGreen(x,y,31)
            if green > 63 and green < 128:
                picture.setGreen(x,y,95)
            if green > 127 and green < 192:
                picture.setGreen(x,y,159)
            if green > 191 and green < 256:
                picture.setGreen(x,y,233)
            #blue setting
            if blue < 64:
                picture.setBlue(x,y,31)
            if blue > 63 and blue < 128:
                picture.setBlue(x,y,95)
            if blue > 127 and blue < 192:
                picture.setBlue(x,y,159)
            if blue > 191 and blue < 256:
                picture.setBlue(x,y,233)

def lighten(picture):
    """Lightens the colors of the image
    Args:
    picture: picture to be lightened(unchanged)
    Returns:
    picture: lightened picture
    """
    for x in range(0, picture.getWidth()):
        for y in range(0, picture.getHeight()):
            px = picture.getPixel(x,y)
            color = px.getColor()
            color = pgt.makeLighter(color, f = 1.55)
            px.setColor(color)

def makeLighter(color:pg.Color, f:float = 1.15):
    r = min(255, color.r*f)
    g = min(255, color.g*f)
    b = min(255, color.b*f)
    return pg.Color((r, g, b))


def createCollage():
    """Create a collage.
 
    Returns
    -------
    Picture
        the collage.
    """
    # create "canvas" on which to make a collage.  You may exchange the
    # width and height values if you prefer a landscape orientation.
    collage = pgt.Picture(700, 950)

    # ---- YOUR CODE TO BUILD THE COLLAGE GOES HERE ----
    # Notice that this is **inside** the createCollage() function.  Because
    # createCollage() should be a "one-and-only-one-thing" function, you
    # should use supporting functions to do transformations, etc.  These
    # supporting functions should be defined below, after the code for this
    # function.

    #Assign picture files
    pic1 = pgt.Picture('possum1.jpg')
    pic2 = pgt.Picture('possum2.jpg')
    pic3 = pgt.Picture('possum3.jpg')
    pic4 = pgt.Picture('possum4.jpg')
    pic5 = pgt.Picture('possum5.jpg')
    pic6 = pgt.Picture('possum6.jpg')
    pic7 = pgt.Picture('possum7.jpg')
    pic8 = pgt.Picture('possum8.jpg')
    pic9 = pgt.Picture('possum9.jpg')
    pic91 = pgt.Picture('possum9.jpg')
    pic10 = pgt.Picture('possum10.jpg')

    #transformations of picture 1
    posterize(pic1) 

    #transformations of picture 2
    edge(pic2)
    makeGreen(pic2)

    #transformations of picture 3
    mirrorHorizontal(pic3)
    pic3 = cropIt(pic3, 200, 200)

    #transformations of picture 4
    inverse(pic4)
    pic4 = cropIt(pic4, 150, 250)

    #transformations of picture 5
    darken(pic5)
    sepiaTint(pic5)
    pic5 = cropIt(pic5, 250, 200)

    #transformations of picture 6
    makeRed(pic6)
    pic6 = cropIt(pic6, 300, 200)
    pic6 = rotate90R(pic6)
    pic6 = rotate90R(pic6)

    #transformations of picture 7
    grayScale(pic7)
    posterize(pic7)

    #transformations of picture 8
    lighten(pic8)
    mirrorHorizontal(pic8)

    #transformations of picture 9
    pic9 = cropIt(pic9, 130, 130)
    pic9 = rotate90R(pic9)
    pic9 = rotate90R(pic9)
    pic9 = rotate90R(pic9)

    #transformations of picture 9(1)
    pic91 = cropIt(pic91, 130, 130)
    pic91 = rotate90R(pic91)

    #tranformations of picture 10
    pic10 = cropIt(pic10, 250, 250)
    mirrorVertical(pic10)

    #copys each of the images into the collage
    pic1.copyInto(collage, 300, 200)
    pic2.copyInto(collage, 0, 100)
    pic3.copyInto(collage, 500, 200)
    pic5.copyInto(collage, 420, 400)
    pic6.copyInto(collage, 120, 400)
    pic7.copyInto(collage, 270, 570)
    pic8.copyInto(collage, 540, 600)
    pic10.copyInto(collage, 20, 600)
    pic4.copyInto(collage, 0, 400)
    pic9.copyInto(collage, 340, 75)
    pic91.copyInto(collage, 460, 75)
    collage.save("collage.jpg")
    return collage

def createWebPage(imageFile, webPageFile):
    """Create web page that contains the collage.
    Parameter: imageFile - the image file name 
    Parameter: webPageFile - the filename of the output web page 
    Returns
    -------
    nothing
    """
    htmlFile = open(webPageFile, "w")
    htmlFile.write("<!DOCTYPE html>\n")
    htmlFile.write("<html>\n")
    htmlFile.write("<head>\n" + "<title>" + "da collage" + "</title>\n" + "</head>\n")
    htmlFile.write("<body bgcolor=4169E1 text=FFFFFF>")
    htmlFile.write("<h1>" + "Hey Look a Collage of Opossums" + "</h1>\n")
    htmlFile.write(f"<img src=\"{imageFile}\" alt=\"unfortunate\"/>\n")
    htmlFile.write("</body>\n")
    htmlFile.write("</html>")
    print("output file:", htmlFile.name)
    htmlFile.close()    
# ============================================================================
# ============== Do NOT make any changes below this comment ==================
# ============================================================================

if __name__ == '__main__':

    # first command line argument, if any, is name of image file for output
    # second command line argument, if any, is name of the output html file name
    collageFile = None
    htmlFileName = "webpage.html"  #Default name

    if len(sys.argv) > 1:
        collageFile = sys.argv[1]
    if len(sys.argv) > 2:
        htmlFile = sys.argv[2]    

    # temporarily set media path to project directory
    scriptDir = os.path.dirname(os.path.realpath(sys.argv[0]))

    # create the collage
    
    collage = createCollage()
    #collage.display()

    try:
        # either show collage on screen or write it to file
        if collageFile is None:
            collage.display()
            input('Press Enter to quit...')
        else:
            print(f'Saving collage to {collageFile}')
            collage.save(collageFile)
            createWebPage(collageFile, htmlFileName)
    except:
        print('Could not show or save picture')

