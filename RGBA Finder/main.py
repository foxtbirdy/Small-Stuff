from PIL import ImageColor
while True:
    def converter(text):
        try:
            text = text.lower()
            output = ImageColor.getcolor(text , "RGBA")
            print("RGBA color for %s is %s." % (text.title() , output))
        except ValueError:
            print("The color name didn't match our database")
    data = input("Color name? >")
    converter(data)
