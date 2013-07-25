imagemask
=========

PNG Image Mask generator


Description
-----------
A Python CLI tool to create an image mask on the fly through PIL (Python Image Library) from a PNG input file.


Opacity
-----------
PNG image files have the benefit of containing an Alpha Channel which specifies that certain parts of an image can be Opaque or Invisible.  This allows the user to have images display on top of other images while still being able to see the image underneath.


Mask Info
-----------
An Image Mask, like in Photoshop, contains only BLACK, WHITE, and GREY pixels.  BLACK pixels tell the system that this pixel should be displayed and WHITE pixels tell the system that this pixel should be hidden.  Pixels can also be partially visible by setting the Alpha Channel to a GREY color (i.e., 128 for 50% visible, 64 for 25% visible, etc.)


Operation
-----------
Local file is opened and its individual pixel contents are imported.  Each pixel is checked.  If the Alpha Channel was previously set to 255 (100% visible), the color of that pixel is converted to BLACK (0,0,0).  However if the Alpha Channel is not 255 (not fully visible), the color of the pixel is converted to WHITE if the original Alpha Channel was 0 (0% visible) or a the color of GREY based on the original opacity.


GPL
-----------
This code is released as GPL3 and is copyright 2013 by Modular Programming Systems Inc.
