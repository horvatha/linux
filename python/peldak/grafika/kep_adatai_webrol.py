#example2.py
import cStringIO # *much* faster than StringIO
import urllib
import Image


file = urllib.urlopen('http://freegee.sourceforge.net/FG_EN/src/teasers_en/t_gee-power_en.gif')
im = cStringIO.StringIO(file.read()) # constructs a StringIO holding the image
img = Image.open(im)

# now use PIL
print img.format, img.size, img.mode
img.save('my_copy.gif')
