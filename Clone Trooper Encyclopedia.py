from pygame import mixer
from cmu_graphics import *
mixer.init()

app.background = 'darkSlateGray'
app.decal = 'shiny'

### Backgrounds
Coruscant = Image(r"Image\Cropped\Coruscant_at_night.png", 0, 0, opacity = 0)
Christophsis = Image(r"Image\Cropped\databank_christophsis.png", 0, 0, opacity = 0)
Geonosis = Image(r"Image\Cropped\databank_geonosis.png", 0, 0, opacity = 0)
Jedi_Temple = Image(r"Image\Cropped\JediTemple.png", 0, 0, opacity = 0)
Kashyyyk = Image(r"Image\Cropped\kachirho_1113a1d6.png", 0, 0, opacity = 0)
Kamino = Image(r"Image\Cropped\TipocaCity.png", 0, 0, opacity = 0)
Umbara = Image(r"Image\Cropped\umbara.png", 0, 0, opacity = 0)
backgrounds = [Coruscant, Christophsis, Geonosis, Jedi_Temple, Kashyyyk, Kamino, Umbara]
for image in backgrounds:
    image.shown = False

changeSound = mixer.Sound(r"Sound\purchase_success.mp3")
errorSound = mixer.Sound(r"Sound\purchase_failure.mp3")
listSound = mixer.Sound(r"Sound\menu_enter.mp3")


### Music
theClonesTheme = mixer.Sound(r"Sound\The Clones - Theme.mp3")
theClonesTheme2 = mixer.Sound(r"Sound\The Clones - Theme 2.mp3")
padawanIntroduction = mixer.Sound(r"Sound\Padawan Introduction.mp3")
meetingTheRookiesAndRetakingTheBase = mixer.Sound(r"Sound\Meeting the Rookies and Retaking the base.mp3")
theClonesTheme2StepsFromHellStyle = mixer.Sound(r"Sound\The Clones Theme - TWO STEPS FROM HELL STYLE.mp3")
battleOverCoruscant = mixer.Sound(r"Sound\Battle over Coruscant.mp3")
theArena = mixer.Sound(r"Sound\The Arena.mp3")
music = {theClonesTheme, theClonesTheme2, padawanIntroduction, meetingTheRookiesAndRetakingTheBase, theClonesTheme2StepsFromHellStyle, battleOverCoruscant, theArena}
theClonesTheme.play(-1)

### Logos   
logo187th = Image(r"Image\1691624715925.png", 330, 330, opacity = 0)
logo212th = Image(r"Image\1691624790595.png", 330, 330, opacity = 0)
logo332nd = Image(r"Image\1691624832191.png", 330, 330, opacity = 0)
logo41st = Image(r"Image\1691625082198.png", 330, 330, opacity = 0)
logo501st = Image(r"Image\1691624958087.png", 330, 330, opacity = 0)
logo442nd = Image(r"Image\1691624995599.png", 330, 330, opacity = 0)
logo327th = Image(r"Image\1691625023492.png", 330, 330, opacity = 0)
logoCoruscantGuard = Image(r"Image\1691625150133.png", 330, 330, opacity = 0)
logo91st = Image(r"Image\1691625182759.png", 330, 330, opacity = 0)
logo104th = Image(r"Image\1691624920960.png", 330, 330, opacity = 0)
logoRancor = Image(r"Image\1691625255922.png", 330, 330, opacity = 0)
logoKeeli = Image(r"Image\1691636634959_64x64.png", 330, 330, opacity = 0)
logoRepublic = Image(r"Image\Republic_Emblem_64x64.png", 330, 330)
logos = {logoRepublic, logo187th, logo212th, logo332nd, logo41st, logo501st, logo442nd, logo327th, logoCoruscantGuard, logo91st, logo104th, logoRancor, logoKeeli}
for image in logos:
    image.shown = False
logoRepublic.shown = True

############### Phase I Helmet #####################################################################################################################################################################################################

phaseIBase = Arc(200, 146, 262, 262, -76, 152, fill=gradient('lightGrey', 'white', 'white', start='top'))
    
phaseIBase2 = Polygon(84, 115, 87, 146, 200, 146, 313, 146, 316, 115, 200, 146, fill = 'white')

phaseIHelmet = Group(    
    
### Lower Half
    Oval(200, 310, 290, 120, fill=rgb(210, 210, 210)),
    
    Rect(90, 210, 90, 65, fill=rgb(220, 220, 220)),
    Rect(220, 210, 90, 65, fill=rgb(220, 220, 220)),
    
### Upper half details
    Polygon(73, 146, 87, 146, 84, 118, 78, 117, fill=rgb(75, 81, 85)),
    Polygon(327, 146, 313, 146, 316, 118, 322, 117, fill=rgb(75, 81, 85)),

### Sides
    Polygon(68, 150, 75, 195, 150, 260, 150, 300, 190, 245, 194, 240, 206, 240, 210, 245, 250, 300, 250, 260, 325, 195, 332, 150, fill=gradient(rgb(220, 220, 220), 'white', 'white', 'white', 'white', 'white', 'white', 'white', rgb(220, 220, 220), start='left'), border=rgb(200, 200, 200)),
)

phaseILower = Oval(200, 300, 290, 120, fill=gradient('white', 'white','white','white', 'grey', start='bottom'))

phaseISides = Group(
    Rect(90, 210, 90, 65, fill=rgb(220, 220, 220)),
    Rect(220, 210, 90, 65, fill=rgb(220, 220, 220)),
    Polygon(75, 127, 55, 135, 60, 295, 100, 275, 100, 220, 75, 146, fill=rgb(240, 240, 240)),
    Polygon(325, 127, 345, 135, 340, 295, 300, 275, 300, 220, 325, 146, fill=rgb(240, 240, 240)),
)

phaseICover = Polygon(68, 150, 75, 195, 150, 260, 150, 300, 190, 245, 194, 240, 206, 240, 210, 245, 250, 300, 250, 260, 325, 195, 332, 150, fill=gradient(rgb(220, 220, 220), 'white', 'white', 'white', 'white', 'white', 'white', 'white', rgb(220, 220, 220), start='left'), border=rgb(200, 200, 200))

phaseIVisor = Polygon(198, 242, 190, 245, 170, 185, 160, 180, 95, 170, 90, 160, 310, 160, 305, 170, 240, 180, 230, 185, 210, 245, 202, 242)

phaseIMouthPiece = Group(
    Polygon(190, 245, 198, 242, 202, 242, 210, 245, 250, 300, 246, 300, 210, 265, 200, 260, 190, 265, 154, 300, 150, 300, fill=rgb(50, 50, 50)),
    Line(248, 299, 295, 345, lineWidth=4, fill=rgb(50, 50, 50)),
    Line(152, 299, 105, 345, lineWidth=4, fill=rgb(50, 50, 50)),

    Line(195, 262, 190, 245, lineWidth=5),
    Line(205, 262, 210, 245, lineWidth=5),
    Line(185, 268, 180, 260, lineWidth=5),
    Line(215, 268, 220, 260, lineWidth=5),
    Line(170, 274, 178, 275, lineWidth=5),
    Line(230, 274, 222, 275, lineWidth=5),
    
    Rect(182, 335, 36, 35, fill='grey', border=rgb(210, 210, 210), borderWidth=3),
    Line(200, 338, 200, 363, lineWidth=10, fill=rgb(20, 20, 20)),
    Rect(187, 338, 7, 28),
    Rect(206, 338, 7, 28),
)


phaseIMowhawk = Rect(180, 4, 40, 83, fill=gradient('lightGrey', 'lightGrey', 'white', 'white', 'white', start='top'))

phaseIMowhawkLines = Group(
    Line(189, 7, 189, 85, opacity=5),
    Line(211, 7, 211, 85, opacity=5),
    Line(180, 85, 220, 85, opacity=25),
)

phaseILine = Line(65, 149, 335, 149, lineWidth=9)

############### Phase II Helmet ##################################################################################################################################################################################################

phaseIIBase = Arc(200, 146, 262, 262, -76, 152, fill=gradient('lightGrey', 'white', 'white', start='top'))
    
phaseIIBase2 = Polygon(84, 115, 87, 146, 200, 146, 313, 146, 316, 115, 200, 146, fill = 'white')

phaseIIHelmet = Group( 
    
### Side Details
    Line(63, 260, 62, 160, fill=rgb(220, 220, 220), lineWidth=8),
    Polygon(58, 158, 59, 205, 50, 195, 49, 165, fill='white'),
    Line(60, 154, 62, 210, fill=rgb(217, 213, 215), lineWidth=9),
    Line(45, 175, 45, 190, lineWidth=4, fill='grey'),
    Line(48, 175, 48, 190, lineWidth=4),

    Line(337, 260, 338, 160, fill=rgb(221, 221, 224), lineWidth=8),
    Polygon(342, 158, 341, 205, 350, 195, 351, 165, fill=rgb(225, 229, 233)),
    Line(340, 154, 338, 210, fill=rgb(234, 234, 237), lineWidth=9),
    Line(355, 175, 355, 190, lineWidth=4, fill='grey'),
    Line(352, 175, 352, 190, lineWidth=4),

### Lower Half
    Circle(150, 305, 20, fill=rgb(245, 245, 245)),
    Circle(250, 305, 20, fill=rgb(245, 245, 245)),
    
### Upper half details
    Rect(180, 4, 40, 83, fill=gradient('lightGrey', 'lightGrey', 'white', 'white', 'white', start='top')),
    Line(189, 7, 189, 85, opacity=5),
    Line(211, 7, 211, 85, opacity=5),
    Line(180, 85, 220, 85, opacity=25),
    Polygon(73, 146, 87, 146, 84, 118, 78, 117, fill=rgb(75, 81, 85)),
    Polygon(327, 146, 313, 146, 316, 118, 322, 117, fill=rgb(75, 81, 85)),
)

phaseIILeftLowerHalf = Circle(95, 290, 45, fill=gradient('grey', rgb(245, 245, 245), rgb(245, 245, 245), rgb(245, 245, 245), start='left-bottom'), border='grey')
phaseIIRightLowerHalf = Circle(305, 290, 45, fill=gradient('grey', rgb(245, 245, 245), rgb(245, 245, 245), rgb(245, 245, 245), start='right-bottom'), border='grey')

phaseIIInner = Polygon(64, 150, 63, 260, 95, 250, 140, 285, 260, 285, 305, 250, 337, 260, 337, 150, fill=rgb(240, 240, 240), border='grey')
    
phaseIILowerDetails = Group(
    
    Line(95, 250, 95, 200, fill='grey'),
    Line(305, 250, 305, 200, fill='grey'),

### Blue Stripes
    Line(61, 261, 51, 279, fill=rgb(22, 67, 152), lineWidth=1),
    Line(62, 260, 53, 280, fill=rgb(22, 67, 152), lineWidth=2),
    Line(66, 264, 57, 281, fill=rgb(22, 67, 152), lineWidth=2),
    Line(71, 268, 61, 284, fill=rgb(22, 67, 152), lineWidth=3),
    Line(76, 272, 65, 287, fill=rgb(22, 67, 152), lineWidth=3),
    Line(81, 276, 69, 291, fill=rgb(22, 67, 152), lineWidth=3),
    Line(86, 280, 73, 295, fill=rgb(22, 67, 152), lineWidth=3),

    Line(339, 261, 349, 279, fill=rgb(22, 67, 152), lineWidth=1),
    Line(338, 260, 347, 280, fill=rgb(22, 67, 152), lineWidth=2),
    Line(334, 264, 343, 281, fill=rgb(22, 67, 152), lineWidth=2),
    Line(329, 268, 339, 284, fill=rgb(22, 67, 152), lineWidth=3),
    Line(324, 272, 335, 287, fill=rgb(22, 67, 152), lineWidth=3),
    Line(319, 276, 331, 291, fill=rgb(22, 67, 152), lineWidth=3),
    Line(314, 280, 327, 295, fill=rgb(22, 67, 152), lineWidth=3),
)

phaseIIMouthPiece = Group(
    Rect(190, 240, 20, 50, fill=rgb(108, 120, 131)),

    Rect(210, 240, 12, 50),
    Rect(222, 240, 12, 50, fill=rgb(108, 120, 131)),
    Rect(234, 240, 8, 50),
    Rect(242, 240, 10, 50, fill=rgb(108, 120, 131)),
    Rect(252, 240, 8, 50),
    Rect(260, 240, 10, 50, fill=rgb(108, 120, 131)),
    Rect(270, 280, 4, 10),

    Rect(178, 240, 12, 50),
    Rect(166, 240, 12, 50, fill=rgb(108, 120, 131)),
    Rect(158, 240, 8, 50),
    Rect(148, 240, 10, 50, fill=rgb(108, 120, 131)),
    Rect(140, 240, 8, 50),
    Rect(130, 240, 10, 50, fill=rgb(108, 120, 131)),
    Rect(126, 280, 4, 10),
    
    Line(274, 288, 290, 295, fill='darkGrey'),
    Line(126, 288, 110, 295, fill='darkGrey'),
)

phaseIICover = Group( 
    Polygon(66, 150, 65, 190, 130, 250, 125, 287, 195, 245, 194, 240, 206, 240, 205, 245, 275, 287, 270, 250, 335, 190, 335, 150, fill=gradient(rgb(220, 220, 220), 'white', 'white', 'white', 'white', 'white', 'white', 'white', rgb(220, 220, 220), start='left'), border=rgb(200, 200, 200)),
    Polygon(185, 350, 215, 350, 220, 353, 230, 345, 220, 330, 180, 330, 170, 345, 180, 353, fill=rgb(230, 230, 230)),
    Rect(185, 332, 30, 12),
    Rect(190, 344, 20, 3),
    Rect(193, 331, 15, 3, fill=rgb(230, 230, 230)),
)    

phaseIIVisor = Polygon(85, 160, 200, 161, 315, 160, 312, 202, 308, 203, 295, 200, 235, 180, 225, 177, 220, 180, 205, 240, 195, 240, 180, 180, 175, 177, 165, 180, 105, 200, 98, 203, 90, 202)

phaseIILine = Line(61, 149, 339, 149, lineWidth=9)

phaseIILeftBottom = Oval(130, 342, 110, 90, fill=gradient('grey', rgb(245, 245, 245), rgb(245, 245, 245), rgb(245, 245, 245), start='left-bottom'))

phaseIIRightBottom = Oval(270, 342, 110, 90, fill=gradient('grey', rgb(245, 245, 245), rgb(245, 245, 245), rgb(245, 245, 245), start='right-bottom'))

phaseIILowerCover = Group(
    Oval(200, 302, 90, 80, fill=rgb(245, 245, 245)),
    Line(222, 277, 235, 285, fill=rgb(245, 245, 245), lineWidth=20),
    Line(220, 277, 275, 300, fill=rgb(245, 245, 245), lineWidth=20),
    Line(178, 277, 165, 285, fill=rgb(245, 245, 245), lineWidth=20),
    Line(180, 277, 125, 300, fill=rgb(245, 245, 245), lineWidth=20),
    Polygon(130, 310, 170, 345, 180, 330, 220, 330, 230, 345, 270, 310, 278, 295, 122, 295, fill = rgb(245, 245, 245))
)

phaseIIAeroators = Group(
    Polygon(185, 350, 215, 350, 220, 353, 230, 345, 220, 330, 180, 330, 170, 345, 180, 353, fill='lightgrey', border='grey', borderWidth=1),
    Rect(185, 332, 30, 12),
    Rect(190, 344, 20, 3),
    Rect(193, 331, 15, 3, fill=rgb(230, 230, 230)),
    
    Circle(260, 360, 20, fill=rgb(20, 20, 20)),
    Rect(240, 340, 20, 20, fill=rgb(20, 20, 20)),
    Oval(260, 360, 35, 27, fill=rgb(70, 70, 70)),
    Circle(260, 360, 12),
    Circle(260, 360, 8, fill=rgb(90, 90, 90)),

    Circle(140, 360, 20, fill=rgb(20, 20, 20)),
    Rect(140, 340, 20, 20, fill=rgb(20, 20, 20)),
    Oval(140, 360, 35, 27, fill=rgb(70, 70, 70)),
    Circle(140, 360, 12),
    Circle(140, 360, 8, fill=rgb(90, 90, 90)),
)

phaseIIHelmet.visible = False
phaseIIVisor.visible = False
phaseIIMouthPiece.visible = False
phaseIICover.visible = False
phaseIILowerCover.visible = False
phaseIILine.visible = False
phaseIIAeroators.visible = False
phaseIILeftBottom.visible = False
phaseIIRightBottom.visible = False
phaseIIBase.visible = False
phaseIIBase2.visible = False
phaseIILeftLowerHalf.visible = False
phaseIIRightLowerHalf.visible = False
phaseIILowerDetails.visible = False
phaseIIInner.visible = False


############### Decals ##################################################################################################################################################################################################

### Numbers / Grunts

shiny = Polygon()

grunt187thP1 = Group(
    Polygon(187, 335, 184, 245, 160, 188, 73, 172, 71, 153, 331, 153, 328, 172, 240, 188, 216, 245, 213, 335, fill = rgb(135, 75, 150)),
    Polygon(182, 85, 185, 144, 215, 144, 218, 85, fill = rgb(135, 75, 150))
)

stripedP2 = Group(
    Rect(90, 104, 10, 40),
    Rect(108, 104, 10, 40),   
    Rect(128, 104, 10, 40),
    Rect(150, 104, 10, 40),
    Rect(168, 104, 10, 40),
    Rect(186, 104, 10, 40),
    Rect(204, 104, 10, 40),
    Rect(222, 104, 10, 40),
    Rect(240, 104, 10, 40),
    Rect(258, 104, 10, 40),
    Rect(276, 104, 10, 40),
    Rect(298, 104, 10, 40),
    Polygon(273, 275, 270, 250, 337, 190, 337, 260, 305, 250, 305, 200, 305, 250, border = 'gray'),
    Polygon(127, 275, 130, 250, 63,  190, 63,  260, 95,  250, 95,  200, 95, 250, border = 'gray'),
    Line(115, 305, 140, 335, lineWidth=7),
    Line(105, 315, 130, 345, lineWidth=7),
    Line(95, 325, 120, 355, lineWidth=7),
    Line(85, 335, 110, 365, lineWidth=7),
    Line(285, 305, 260, 335, lineWidth=7),
    Line(295, 315, 270, 345, lineWidth=7),
    Line(305, 325, 280, 355, lineWidth=7),
    Line(315, 335, 290, 365, lineWidth=7),    
)

grunt212thP1 = Group(
    Polygon(187, 335, 184, 250, 216, 250, 213, 335, fill = 'orange'),
    Polygon(73, 165, 71, 153, 331, 153, 328, 165, fill = 'orange')
)

gruntTriangle = Polygon(200, 144, 297, 60, 280, 45, 260, 29, 220, 15, 180, 15,140, 29, 120, 45, 103, 60, fill = 'orange')

grunt332ndP2 = Group(
    Polygon(95, 145, 120, 120, 165, 130, 165, 120, 145, 100, 160, 85, 180, 40, 220, 40, 240, 85, 255, 100, 235, 120, 235, 130, 280, 120, 305, 145, 220, 145, 220, 115, 235, 100, 220, 85, 180, 85, 165, 100, 180, 115, 180, 145,  fill = 'white'),
    Polygon(140, 100, 125, 85, 140, 65, 155, 85, fill = 'white'),
    Polygon(260, 100, 275, 85, 260, 65, 245, 85, fill = 'white'),
)

grunt41stP1 = Polygon(187, 335, 184, 245, 160, 188, 73, 172, 71, 153, 331, 153, 328, 172, 240, 188, 216, 245, 213, 335, fill = 'darkGreen')

grunt41stP2 = Polygon(115, 145, 285, 145, 200, 30, fill = 'darkGreen')

grunt501stP1 = Group(
    Polygon(187, 335, 180, 250 , 220, 250, 213, 335, fill = rgb(48, 127, 186)),
    Polygon(260, 29, 220, 15, 180, 15,140, 29, 120, 45, 165, 180, 180, 255, 195, 245, 195, 240, 205, 240, 205, 245, 220, 255, 235, 180, 280, 45, fill = rgb(48, 127, 186))
)

grunt501stP2 = Group( 
    Polygon(180, 330, 220, 330, 220, 265, 200, 260, 180, 265, fill = rgb(48, 127, 186)),
    Polygon(260, 29, 220, 15, 180, 15,140, 29, 120, 45, 165, 180, 180, 255, 195, 245, 195, 240, 205, 240, 205, 245, 220, 255, 235, 180, 280, 45, fill = rgb(48, 127, 186))
)    

grunt442ndP1 = Group(
    Polygon(100, 275, 100, 217, 150, 260, 150, 275, fill = 'yellowGreen'),
    Polygon(300, 275, 300, 217, 250, 260, 250, 275, fill = 'yellowGreen'),    
    Polygon(200, 144, 297, 60, 280, 45, 260, 29, 220, 15, 180, 15,140, 29, 120, 45, 103, 60, fill = 'yellowGreen')
)
    
grunt327thP1 = Polygon(187, 335, 175, 250, 140, 30, 180, 15, 220, 15, 260, 30, 225, 250, 213, 335, fill = 'gold')

grunt327thP2 = Group(
    Polygon(180, 330, 220, 330, 220, 265, 200, 260, 180, 265, fill = 'gold'),
    Polygon(260, 30, 220, 15, 180, 15,140, 30, 165, 180, 180, 255, 195, 245, 195, 240, 205, 240, 205, 245, 220, 255, 235, 180, fill = 'gold')
)

gruntCoruscantGuardP1 = Group(
    Polygon(182, 335, 175, 305, 182, 270, 200, 259, 218, 270, 225, 305, 218, 335, fill = 'maroon'),
    Polygon(72, 117, 84, 118, 87, 146, 313, 146, 316, 118, 328, 117, 322, 100, 305, 110, 300, 140, 210, 140, 220, 110, 200, 90, 180, 110, 190, 140, 100, 140, 95, 110, 78, 100, fill = 'maroon')
)

grunt91st = Group(
    Circle(135, 100, 36, fill = 'maroon'),
    Line(135, 136, 135, 64, fill = 'white', lineWidth = 7),
    Circle(135, 85, 10, fill = 'white'),
)

grunt104thP1 = Group(
    Polygon(170, 145, 160, 120, 140, 95, 80, 95, 71, 117, 84, 118, 87, 145, fill = 'lightSlateGray'),
    Polygon(230, 145, 240, 120, 260, 95, 320, 95, 329, 117, 316, 118, 313, 145, fill = 'lightSlateGray'),
    
    Oval(175, 107, 37, 25, rotateAngle=50, fill = None, border='lightSlateGray', borderWidth = 4),
    Oval(225, 107, 37, 25, rotateAngle=-50, fill = None, border='lightSlateGray', borderWidth = 4),
    Oval(170, 90, 20, 15, rotateAngle = 25, fill=None, border='lightSlateGray', borderWidth = 5),
    Circle(165, 90, 4, fill = 'white'),
    Oval(230, 90, 20, 15, rotateAngle = -25, fill=None, border='lightSlateGray', borderWidth = 5),
    Circle(235, 90, 4, fill = 'white'),
    Polygon(190, 142, 193, 142, 194, 138, 206, 138, 207, 142, 210, 142, 220, 110, 235, 100, 235, 93, 200, 100, 165, 93, 165, 100, 180, 110, fill = 'lightSlateGray'),

    Line(200, 132, 200, 100, fill = 'white', lineWidth = 3),
    Line(200, 110, 175, 100, fill = 'white'),
    Line(200, 110, 225, 100, fill = 'white'),
    Circle(200, 132, 3, fill = 'white'),
    Circle(211, 107, 3, fill = 'lightSlateGray'),
    Circle(189, 107, 3, fill = 'lightSlateGray'),    
)

grunt104thP2 = Group(
    Polygon(170, 145, 160, 120, 140, 95, 80, 95, 71, 117, 84, 118, 87, 145, fill = 'lightSlateGray'),
    Polygon(230, 145, 240, 120, 260, 95, 320, 95, 329, 117, 316, 118, 313, 145, fill = 'lightSlateGray'),
    
    Oval(175, 107, 37, 25, rotateAngle=50, fill = None, border='lightSlateGray', borderWidth = 4),
    Oval(225, 107, 37, 25, rotateAngle=-50, fill = None, border='lightSlateGray', borderWidth = 4),
    Oval(170, 90, 20, 15, rotateAngle = 25, fill=None, border='lightSlateGray', borderWidth = 5),
    Circle(165, 90, 4, fill = 'white'),
    Oval(230, 90, 20, 15, rotateAngle = -25, fill=None, border='lightSlateGray', borderWidth = 5),
    Circle(235, 90, 4, fill = 'white'),
    Polygon(190, 142, 193, 142, 194, 138, 206, 138, 207, 142, 210, 142, 220, 110, 235, 100, 235, 93, 200, 100, 165, 93, 165, 100, 180, 110, fill = 'lightSlateGray'),

    Line(200, 132, 200, 100, fill = 'white', lineWidth = 3),
    Line(200, 110, 175, 100, fill = 'white'),
    Line(200, 110, 225, 100, fill = 'white'),
    Circle(200, 132, 3, fill = 'white'),
    Circle(211, 107, 3, fill = 'lightSlateGray'),
    Circle(189, 107, 3, fill = 'lightSlateGray'),
)

### Letters / Commanders and Captains

appoP1 = Group(
    Polygon(187, 335, 180, 250 , 220, 250, 213, 335, fill = rgb(48, 127, 186)),
    Polygon(260, 29, 220, 15, 180, 15,140, 29, 120, 45, 165, 180, 180, 255,   195, 245, 195, 240, 205, 240, 205, 245,   220, 255, 235, 180, 280, 45, fill = rgb(48, 127, 186)),
    Polygon(220, 87, 220, 110, 255, 110, 200, 146, 145, 110, 180, 110, 180, 87, fill='white')
)

appoP2 = Group(
    Polygon(180, 330, 220, 330, 220, 265, 200, 260, 180, 265, fill = rgb(48, 127, 186)),
    Polygon(260, 29, 220, 15, 180, 15,140, 29, 120, 45, 165, 180, 180, 255,   195, 245, 195, 240, 205, 240, 205, 245,   220, 255, 235, 180, 280, 45, fill = rgb(48, 127, 186)),
    Polygon(220, 87, 220, 110, 255, 110, 200, 146, 145, 110, 180, 110, 180, 87, fill='white')
)

blyP1 = Group(
    Polygon(187, 335, 175, 250, 140, 30, 180, 15, 220, 15, 260, 30, 225, 250, 213, 335, fill = 'gold'),
    Polygon(170, 185, 230, 185, 210, 245, 190, 245),
    Polygon(75, 195, 325, 195, 345, 135, 55, 135, fill = rgb(245, 240, 240) ),
    Polygon(80, 190, 320, 190, 340, 140, 60, 140, fill = rgb(245, 245, 245), border='gold', borderWidth=1 ),
    Rect(95, 140, 15, 50, fill='gold'),
    Line(75, 165, 325, 165, lineWidth=8),
)
    
blyP2 = Group(
    Polygon(180, 330, 220, 330, 220, 265, 200, 260, 180, 265, fill = 'saddleBrown'),
    Polygon(260, 30, 220, 15, 180, 15,140, 30, 165, 180, 180, 255, 195, 245, 195, 240, 205, 240, 205, 245, 220, 255, 235, 180, fill = 'saddleBrown'),
    Polygon(195, 240, 205, 240, 220, 180, 180, 180),
    Polygon(75, 205, 325, 205, 345, 145, 55, 145, fill = rgb(245, 240, 240) ),
    Polygon(80, 200, 320, 200, 340, 150, 60, 150, fill = rgb(245, 245, 245), border='gold', borderWidth=1 ),
    Rect(95, 150, 15, 50, fill='gold'),
    Line(75, 170, 325, 170, lineWidth=8),
)

codyP1 = Group(
    Polygon(200, 310, 195, 333, 205, 333, fill = 'orange'),
    Polygon(225, 315, 215, 333, 220, 335, fill = 'orange'),
    Polygon(175, 315, 185, 333, 180, 335, fill = 'orange'),
    Polygon(150, 335, 175, 345, 177, 340, fill = 'orange'),
    Polygon(250, 335, 225, 345, 223, 340, fill = 'orange'),
    
    Circle(330, 105, 20, fill = 'gainsboro'),
    Circle(330, 105, 15, fill = 'red'),
    Line(53, 150, 53, 4, fill = 'orange', lineWidth=8),
    
    Polygon(315, 230, 340, 200, 340, 120, 60, 120, 60, 200, 85, 230, 85, 155, 315, 155, fill = 'orange'),
    Polygon(85, 230, 85, 155, 60, 120, 60, 200, fill = 'darkOrange'),
    Polygon(315, 230, 315, 155, 340, 120, 340, 200, fill = 'darkOrange'),
    Rect(185, 120, 30, 30, fill = rgb(240, 240, 240)),
)

codyP2 = Group(
    Polygon(195, 330, 190, 280, 180, 265, 200, 260, 220, 265, 210, 280, 205, 330),   # Lower mouth piece design
    Line(200, 315, 180, 320, lineWidth = 7),
    Line(200, 315, 220, 320, lineWidth = 7),
    Line(200, 300, 175, 305, lineWidth = 7),
    Line(200, 300, 225, 305, lineWidth = 7),
    Line(200, 285, 170, 290, lineWidth = 7),
    Line(200, 285, 230, 290, lineWidth = 7),
    
    Polygon(160, 320, 155, 340, 165, 340, fill = 'orange'),
    Polygon(240, 320, 245, 340, 235, 340, fill = 'orange'),
    
    Line(115, 353, 150, 335, fill = 'orange',dashes=(3, 5), lineWidth = 10),
    Line(285, 353, 250, 335, fill = 'orange',dashes=(3, 5), lineWidth = 10),
    
    Line(72, 115, 328, 115, fill = 'fireBrick', lineWidth = 8),
    
    Polygon(175, 90, 175, 10, 165, 15, 165, 80, 155, 80, 155, 15, 135, 25, 135, 80, 125, 80, 125, 30, 115, 40, 115, 90, fill = 'tan'), #Upper helmet pads
    Polygon(225, 90, 225, 10, 235, 15, 235, 80, 245, 80, 245, 15, 265, 25, 265, 80, 275, 80, 275, 30, 285, 40, 285, 90, fill = 'tan'), 
    Polygon(125, 35, 125, 80, 135, 80, 135, 30, fill = rgb(170, 150, 120)),
    Polygon(155, 20, 155, 80, 165, 80, 165, 18, fill = rgb(170, 150, 120)),
    Polygon(235, 18, 235, 80, 245, 80, 245, 20, fill = rgb(170, 150, 120)),
    Polygon(265, 30, 265, 80, 275, 80, 275, 35, fill = rgb(170, 150, 120)),
    
    Polygon(310, 270, 340, 240, 340, 125, 220, 120, 180, 120, 60, 125, 60, 240, 90, 270, 80, 155, 320, 155,  fill = 'orange', border='darkOrange'), # Visor
    Polygon(90, 270, 60, 240, 60, 125, 80, 155, fill = 'darkOrange'),
    Polygon(310, 270, 340, 240, 340, 125, 320, 155, fill = 'darkOrange'),
    Line(325, 255, 330, 135, fill = 'white'),
    Line(330, 135, 70, 135, fill = 'white'),
    Line(75, 255, 70, 135, fill = 'white'),
    Line(180, 135, 180, 150, fill = 'white'),
    Line(220, 135, 220, 150, fill = 'white'),
    Line( 170, 135, 170, 145, fill = 'white'),
    Line( 230, 135, 230, 145, fill = 'white'),
    Line( 170, 145, 155, 145, fill = 'white'),
    Line( 230, 145, 245, 145, fill = 'white'),
    
    Rect(355, 155, 7, 70, fill = 'darkgrey'),
    Line(358, 155, 358, 35, fill = 'silver', lineWidth = 4),
    Polygon(358, 35, 358, 48, 337, 40, fill = 'silver'),
    
    Line(45, 225, 45, 10, fill = gradient('dimgrey', 'dimgrey', 'darkgrey', start='right'), lineWidth=10),
    
    Circle(307, 80, 18, fill = 'white'),
    Circle(310, 80, 18, fill = 'gainsboro'),
    Circle(310, 80, 12),
    
    Polygon(193, 330, 208, 330, 208, 375, 193, 375, fill = 'darkgrey'),
)

doomP2 = Group(
    Polygon(310, 270, 340, 240, 340, 125, 220, 120, 180, 120, 60, 125, 60, 240, 90, 270, 80, 155, 320, 155,  fill = 'oliveDrab', border='darkOliveGreen'), # Visor
    Polygon(90, 270, 60, 240, 60, 125, 80, 155, fill = 'darkOliveGreen'),
    Polygon(310, 270, 340, 240, 340, 125, 320, 155, fill = 'darkOliveGreen'),
    Line(325, 255, 330, 135, fill = 'yellow'),
    Line(200, 125, 70, 135, fill = 'yellow'),
    Line(330, 135, 200, 125, fill = 'yellow'),
    Line(75, 255, 70, 135, fill = 'yellow'),
    RegularPolygon(200, 140, 14, 3, fill = 'yellow', rotateAngle = 60),
    Line(180, 138, 220, 138, fill = 'yellow'),
    Line(185, 144, 215, 144, fill = 'yellow'),
    Line(188, 130, 212, 130, fill = 'yellow', dashes=(3, 4), lineWidth = 5),
    
    Line(45, 225, 45, 10, fill = gradient('dimgrey', 'dimgrey', 'darkgrey', start='right'), lineWidth=10),
    
    Circle(287, 105, 18, fill = 'grey'),
    Circle(290, 105, 18, fill = 'darkGrey'),
    Circle(290, 105, 12),
)    

echoP1 = Group(
    Polygon(100, 275, 100, 217, 150, 260, 150, 275, fill = 'steelBlue'),
    Polygon(300, 275, 300, 217, 250, 260, 250, 275, fill = 'steelBlue'),
    Polygon(130, 145, 130, 35, 160, 20, 160, 145, fill = 'steelBlue'),
    Polygon(270, 145, 270, 35, 240, 20, 240, 145, fill = 'steelBlue'),
)

echoP2 = Group(
    Polygon(273, 275, 270, 250, 305, 220,305, 250,  fill = 'steelBlue', border = 'gray'),
    Polygon(127, 275, 130, 250, 95,  220, 95,  250, fill = 'steelBlue', border = 'gray'),
    Polygon(130, 145, 130, 35, 160, 20, 160, 145, fill = 'lightSkyBlue'),
    Polygon(270, 145, 270, 35, 240, 20, 240, 145, fill = 'lightSkyBlue'),
    Line(145, 145, 145, 29, fill = 'steelBlue', lineWidth=10),
    Line(255, 145, 255, 29, fill = 'steelBlue', lineWidth=10),
    Line(42, 190, 42, 7, fill = 'darkGrey', lineWidth=8),
    Polygon(42, 25, 60, 15, 100, 10, 105, 2, 60, 2, 60, 1, 24, 1, 20, 10, 24, 15, fill='grey'),
)

fivesP1 = Group(
    Polygon(100, 275, 100, 217, 150, 260, 150, 275, fill = 'steelBlue'),
    Polygon(300, 275, 300, 217, 250, 260, 250, 275, fill = 'steelBlue'),
    Circle(200, 100, 40, fill = 'steelBlue'),
    RegularPolygon(200, 95, 8, 4, fill = 'white'),
    Line(200, 100, 200, 150, fill = 'white', lineWidth=5),
    Polygon(200, 120, 255, 140, 145, 140, fill = 'white'),
    RegularPolygon(200, 130, 13, 3, fill='red',rotateAngle=180),
    Polygon(280, 145, 230, 115, 225, 129, fill = 'steelBlue'),
    Polygon(120, 145, 170, 115, 175, 129, fill = 'steelBlue'),
    Oval(170, 105, 12, 15, rotateAngle=135, fill = 'white'),
    Oval(230, 105, 12, 15, rotateAngle=45, fill = 'white')
)    

fivesP2 = Group(
    Polygon(273, 275, 270, 250, 305, 218, 305, 250,  fill = 'steelBlue', border = 'gray'),
    Polygon(127, 275, 130, 250, 95,  218, 95,  250, fill = 'steelBlue', border = 'gray'),
    RegularPolygon(200, 130, 13, 3, fill='red',rotateAngle=180),
    Line(42, 190, 42, 7, fill = 'darkGrey', lineWidth=8),
    Polygon(42, 25, 60, 15, 100, 10, 105, 2, 60, 2, 60, 1, 24, 1, 20, 10, 24, 15, fill='grey'),
    Polygon(160, 20, 160, 55, 150, 75, 155, 80, 152, 90, 160, 85, 175, 105, 225, 105, 240, 85, 248, 90, 245, 80, 250, 75, 240, 55, 240, 20, 200, 13, fill = 'steelBlue'),
    Circle(152, 100, 4, fill = 'red'),
    Circle(248, 100, 4, fill = 'red'),
    Polygon(145, 100, 100, 145, 150, 105, 160, 110, 170, 100, 230, 100, 240, 110, 250, 105, 300, 145, 265, 130, 210, 115, 205, 120, 195, 120, 190, 115, 135, 130, 100, 145, fill = 'steelBlue'),
    Line(200, 120, 200, 100, fill = 'white', lineWidth = 4),
    Polygon(200, 90, 205, 110, 195, 110, fill = 'white'),
)

greeP1 = Group(
    Polygon(100, 275, 100, 217, 150, 260, 150, 275, fill = 'darkGreen'),
    Polygon(300, 275, 300, 217, 250, 260, 250, 275, fill = 'darkGreen'),
    Polygon(187, 335, 175, 250, 160, 100, 91, 75, 114, 47, 140, 30, 180, 14, 220, 14, 260, 30, 285, 47, 309, 75, 240, 100, 225, 250, 213, 335, fill = 'darkGreen'),
)

greeP2 = Group(
    Polygon(130, 310, 170, 345, 180, 330, 220, 330, 230, 345, 270, 310, 278, 295, 122, 295, fill = gradient('gainsboro', 'silver', start = 'top')),
    Polygon(180, 330, 220, 330, 220, 265, 200, 260, 180, 265, fill = 'darkGreen'),
    Polygon(180, 255, 160, 100, 91, 75, 114, 47, 140, 30, 180, 14, 220, 14, 260, 30, 285, 47, 309, 75, 240, 100, 220, 255, 205, 245, 205, 240, 195, 240, 195, 245, fill = 'darkGreen'),
    Polygon(273, 275, 270, 250, 305, 218, 305, 250,  fill = 'oliveDrab', border = 'gray'),
    Polygon(127, 275, 130, 250, 95,  218, 95,  250, fill = 'oliveDrab', border = 'gray'),
)

hammerP1 = Group(
    Polygon(100, 275, 100, 217, 150, 260, 150, 275, fill = 'darkRed'),
    Polygon(300, 275, 300, 217, 250, 260, 250, 275, fill = 'darkRed'),
        
    Circle(95, 128, 8, fill = 'darkRed'),
    Circle(90, 105, 8, fill = 'darkRed'),
    Circle(305, 128, 8, fill = 'darkRed'),
    Circle(310, 105, 8, fill = 'darkRed'),
    
    Line(60, 140, 60, 7, fill = 'darkGrey', lineWidth=8),
    Polygon(60, 25, 78, 15, 118, 10, 123, 2, 78, 2, 78, 1, 42, 1, 38, 10, 42, 15, fill='grey'),
    
    Polygon(100, 345,   200, 255,   295, 345,   259, 356,   218, 361,   218,335,   182, 335,   181, 361,   144, 356, fill = 'darkGrey'),
)

hammerP2 = Group(
    Polygon(273, 275, 270, 250, 305, 218, 305, 250,  fill = 'darkRed', border = 'gray'),
    Polygon(127, 275, 130, 250, 95,  218, 95,  250, fill = 'darkRed', border = 'gray'),

    Circle(95, 128, 8, fill = 'darkRed'),
    Circle(90, 105, 8, fill = 'darkRed'),
    Circle(305, 128, 8, fill = 'darkRed'),
    Circle(310, 105, 8, fill = 'darkRed'),
    
    Line(42, 190, 42, 7, fill = 'darkGrey', lineWidth=8),
    Polygon(42, 25, 60, 15, 100, 10, 105, 2, 60, 2, 60, 1, 24, 1, 20, 10, 24, 15, fill='grey'),
)
    
jesseP1 = Group(
    Polygon(87, 145,  92, 75, 115, 49, 140, 30, 180, 15, 220, 15, 260, 30, 285, 49, 308, 75, 313, 145, border = 'darkGrey', fill = None, borderWidth=12),
    Rect(100, 130, 200, 15, fill = 'white'),
    Polygon(187, 335, 184, 245, 160, 188, 73, 172, 71, 153, 331, 153, 328, 172, 240, 188, 216, 245, 213, 335, fill = 'steelBlue'),
    Circle(200, 100, 32, fill = 'darkGrey'),
    Line(200, 125, 200, 145, fill = 'darkGrey', lineWidth=10),
    Line(225, 115, 250, 130, fill = 'darkGrey', lineWidth=10),
    Line(175, 115, 150, 130, fill = 'darkGrey', lineWidth=10),
    Line(175, 115, 150, 130, fill = 'darkGrey', lineWidth=10),
    Line(140, 100, 175, 100, fill = 'darkGrey', lineWidth=10),
    Line(175, 85, 150, 70, fill = 'darkGrey', lineWidth=10),
    Line(225, 85, 250, 70, fill = 'darkGrey', lineWidth=10),
    Line(260, 100, 225, 100, fill = 'darkGrey', lineWidth=10),
    Line(110, 145, 110, 115, fill = 'darkGrey', lineWidth=10),
    Line(115, 90, 120, 80, fill = 'darkGrey', lineWidth=10),
    Line(120, 80, 135, 60, fill = 'darkGrey', lineWidth=10),
    Line(160, 50, 180, 40, fill = 'darkGrey', lineWidth=10),
    Line(285, 90, 280, 80, fill = 'darkGrey', lineWidth=10),
    Line(280, 80, 265, 60, fill = 'darkGrey', lineWidth=10),
    Line(240, 50, 220, 40, fill = 'darkGrey', lineWidth=10),
    Line(290, 145, 290, 115, fill = 'darkGrey', lineWidth=10),
)

jesseP2 = Group(
    Polygon(87, 145,  92, 75, 115, 49, 140, 30, 180, 15, 220, 15, 260, 30, 285, 49, 308, 75, 313, 145, border = 'darkGrey', fill = 'white', borderWidth=12),
    Rect(100, 130, 200, 15, fill = 'white'),
    Circle(200, 100, 32, fill = 'darkGrey'),
    Line(200, 125, 200, 145, fill = 'darkGrey', lineWidth=10),
    Line(225, 115, 250, 130, fill = 'darkGrey', lineWidth=10),
    Line(175, 115, 150, 130, fill = 'darkGrey', lineWidth=10),
    Line(175, 115, 150, 130, fill = 'darkGrey', lineWidth=10),
    Line(140, 100, 175, 100, fill = 'darkGrey', lineWidth=10),
    Line(175, 85, 150, 70, fill = 'darkGrey', lineWidth=10),
    Line(225, 85, 250, 70, fill = 'darkGrey', lineWidth=10),
    Line(260, 100, 225, 100, fill = 'darkGrey', lineWidth=10),
    Line(110, 145, 110, 115, fill = 'darkGrey', lineWidth=10),
    Line(115, 90, 120, 80, fill = 'darkGrey', lineWidth=10),
    Line(120, 80, 135, 60, fill = 'darkGrey', lineWidth=10),
    Line(160, 50, 180, 40, fill = 'darkGrey', lineWidth=10),
    Line(285, 90, 280, 80, fill = 'darkGrey', lineWidth=10),
    Line(280, 80, 265, 60, fill = 'darkGrey', lineWidth=10),
    Line(240, 50, 220, 40, fill = 'darkGrey', lineWidth=10),
    Line(290, 145, 290, 115, fill = 'darkGrey', lineWidth=10),
    
    Polygon(200, 241, 180, 255, 165, 200, 98, 220, 65, 190, 65, 153, 335, 153, 335, 190, 302, 220, 235, 200, 220, 255, fill = 'steelBlue'),
)

keeliP1 = Group(
    Polygon(100, 145, 105, 120, 160, 130, 165, 145, fill = 'brown'),
    Polygon(105, 117, 105, 105, 160, 98, 160, 127, fill = 'brown'),
    Polygon(105, 102, 100, 80, 145, 65, 160, 95, fill = 'brown'),
    Polygon(100, 77, 94, 71, 120, 43, 145, 62, fill = 'brown'),
    
    Polygon(300, 145, 295, 120, 240, 130, 235, 145, fill = 'brown'),
    Polygon(295, 117, 295, 105, 240, 98, 240, 127, fill = 'brown'),
    Polygon(295, 102, 300, 80, 255, 65, 240, 95, fill = 'brown'),
    Polygon(300, 77, 306, 71, 280, 43, 255, 62, fill = 'brown'),
    
    Polygon(100, 240, 135, 275, 115, 275, 100, 265, fill = 'brown'),
    Circle(117, 289, 23, fill = 'brown'),
    Circle(103, 284, 15, fill = 'white'),
    
    Polygon(300, 240, 265, 275, 285, 275, 300, 265, fill = 'brown'),
    Circle(283, 289, 23, fill = 'brown'),
    Circle(297, 284, 15, fill = 'white'),
    
    Polygon(172, 282, 200, 255, 228, 282, 217, 305, 235, 323, 230, 330, 170, 330, 165, 323, 183, 305, fill = 'brown'),
    Polygon(155, 300, 170, 285, 180, 305, 165, 320, fill = 'brown'),
    Polygon(245, 300, 230, 285, 220, 305, 235, 320, fill = 'brown'),
    
    Line(60, 140, 60, 7, fill = 'darkGrey', lineWidth=8),
    Polygon(60, 25, 78, 15, 118, 10, 123, 2, 78, 2, 78, 1, 42, 1, 38, 10, 42, 15, fill='grey'),
)

lockP1 = Group(
    Polygon(160, 20, 200, 14, 240, 20, 240, 145, 160, 145, fill = 'oliveDrab'),
    Line(160, 20, 160, 145, fill = 'yellow', lineWidth = 5),
    Line(240, 20, 240, 145, fill = 'yellow', lineWidth = 5),
    
    Polygon(315, 230, 340, 200, 340, 120, 60, 120, 60, 200, 85, 230, 85, 155, 315, 155, fill = 'oliveDrab'),
    Polygon(85, 230, 85, 155, 60, 120, 60, 200, fill = 'darkOliveGreen'),
    Polygon(315, 230, 315, 155, 340, 120, 340, 200, fill = 'darkOliveGreen'),
)

lockP2 = Group(
    Polygon(160, 20, 200, 14, 240, 20, 240, 145, 160, 145, fill = 'oliveDrab'),
    Line(160, 20, 160, 145, fill = 'yellow', lineWidth = 5),
    Line(240, 20, 240, 145, fill = 'yellow', lineWidth = 5),
    
    Polygon(310, 270, 340, 240, 340, 125, 220, 120, 180, 120, 60, 125, 60, 240, 90, 270, 80, 155, 320, 155,  fill = 'oliveDrab', border='darkOliveGreen' ),
    Polygon(90, 270, 60, 240, 60, 125, 80, 155, fill = 'darkOliveGreen'),
    Polygon(310, 270, 340, 240, 340, 125, 320, 155, fill = 'darkOliveGreen'),
)    

neyoP2 = Group(
    Circle(135, 100, 36, fill = 'maroon'),
    Line(135, 136, 135, 64, fill = 'white', lineWidth = 7),
    Circle(135, 85, 10, fill = 'white'),
    
    Polygon(70, 153,70, 170, 175, 195, 200, 175, 225, 195, 330, 170, 330, 153, fill = 'white', border='lightgrey'),
    Polygon(75, 160, 75, 165, 170, 185, 200, 168, 230, 185, 325, 165, 325, 160,),
    Polygon(200, 175, 210, 180, 190, 180),
    Line(200, 235, 130, 285, fill = 'grey', dashes=(10, 12,), lineWidth = 5),
    Line(200, 235, 270, 285, fill = 'grey', dashes=(10, 12,), lineWidth = 5),

    Polygon(167, 345, 150, 385, 250, 385, 233, 345, fill = 'white'),
    Polygon(167, 345, 160, 385, 240, 385, 233, 345, fill = rgb(240, 240, 240), border='black'),
    Rect(185, 348, 30, 12),
    Rect(190, 360, 20, 3),
    Rect(175, 370, 50, 15)    
) 

pondsP1 = Group(
    Polygon(73, 165, 71, 153, 331, 153, 328, 165, fill = 'brown'),
    Polygon(100, 275, 105, 346, 80, 334, 67, 325, 57, 312, 56, 295, fill = 'brown'),
    Polygon(300, 275, 295, 346, 320, 334, 333, 325, 343, 312, 344, 295, fill = 'brown'),
    Polygon(100, 145, 140, 100, 160, 22, 180, 16, 180, 87, 220, 87, 220, 16, 240, 22, 260, 100, 300, 145, fill = 'white'),
)    

rexP1 = Group(
    Polygon(187, 335, 184, 245, 160, 188, 73, 172, 71, 153, 331, 153, 328, 172, 240, 188, 216, 245, 213, 335, fill = 'steelBlue'),
    Polygon(210, 130, 260, 35, 290, 80, 285, 125, 245, 135, 260, 125, 265, 100, 260, 80, fill = 'steelBlue'),
    Polygon(190, 130, 140, 35, 110, 80, 115, 125, 155, 135, 140, 125, 135, 100, 140, 80, fill = 'steelBlue'),
    Polygon(210, 125, 220, 95, 210, 90, 205, 95, fill = 'steelBlue'),
    Polygon(190, 125, 180, 95, 190, 90, 195, 95, fill = 'steelBlue'),
    Line(85, 135, 115, 135, fill = 'yellow', dashes=True, lineWidth=20),
    Line(315, 135, 285, 135, fill = 'yellow', dashes=True, lineWidth=20),
    Line(60, 140, 60, 7, fill = 'darkGrey', lineWidth=8),
    Polygon(60, 25, 78, 15, 118, 10, 123, 2, 78, 2, 78, 1, 42, 1, 38, 10, 42, 15, fill='grey'),
)

rexP2 = Group(
    Polygon(200, 241, 180, 255, 170, 205, 65, 175, 65, 153, 335, 153, 335, 175, 230, 205, 220, 255, fill = 'steelBlue'),
    Polygon(210, 130, 260, 35, 290, 80, 285, 125, 245, 135, 260, 125, 265, 100, 260, 80, fill = 'steelBlue'),
    Polygon(190, 130, 140, 35, 110, 80, 115, 125, 155, 135, 140, 125, 135, 100, 140, 80, fill = 'steelBlue'),
    Polygon(210, 125, 220, 95, 210, 90, 205, 95, fill = 'steelBlue'),
    Polygon(190, 125, 180, 95, 190, 90, 195, 95, fill = 'steelBlue'),

    Polygon(195, 240, 205, 240, 220, 180, 180, 180),
    Polygon(210, 195, 320, 170, 320, 160, 80, 160, 80, 170, 190, 195),
    
    Line(87, 143, 313, 143, fill = 'darkGoldenRod', lineWidth=5),
    Line(87, 143, 313, 143, fill = 'lightBlue', lineWidth=2),
    Line(230, 205, 274, 280, fill = 'darkGoldenRod', lineWidth=5),
    Line(230, 205, 274, 280, fill = 'lightBlue', lineWidth=2),
    Line(170, 205, 126, 280, fill = 'darkGoldenRod', lineWidth=5),
    Line(170, 205, 126, 280, fill = 'lightBlue', lineWidth=2),
    
    Line(42, 190, 42, 7, fill = 'darkGrey', lineWidth=8),                                       # Antenna 
    Polygon(42, 25, 60, 15, 100, 10, 105, 2, 60, 2, 60, 1, 24, 1, 20, 10, 24, 15, fill='grey'),
    
    Oval(125, 340, 108, 90, fill = 'darkGoldenRod'),
    Oval(275, 340, 108, 90, fill = 'darkGoldenRod'),
    Oval(127, 340, 108, 90, fill = None, border = 'lightBlue'),
    Oval(273, 340, 108, 90, fill = None, border = 'lightBlue'),
    Line(110, 297, 138, 295, fill = 'white'),
    Line(290, 297, 262, 295, fill = 'white'),
    Oval(130, 342, 110, 90, fill=gradient('grey', rgb(245, 245, 245), rgb(245, 245, 245), rgb(245, 245, 245), start='left-bottom')),
    Oval(270, 342, 110, 90, fill=gradient('grey', rgb(245, 245, 245), rgb(245, 245, 245), rgb(245, 245, 245), start='right-bottom')),
    
    Line(300, 107, 316, 102, dashes=(1, 4), lineWidth=12),
    Line(298, 102, 318, 107, lineWidth = 1),
    Line(300, 87, 313, 82, dashes=(1, 4), lineWidth=12),
    Line(298, 82, 315, 87, lineWidth = 1),
    
    Line(84, 102, 100, 107, dashes=(1, 4), lineWidth=12),
    Line(82, 107, 102, 102, lineWidth = 1),
    Line(87, 82, 100, 87, dashes=(1, 4), lineWidth=12),
    Line(85, 87, 102, 82, lineWidth = 1),
    
    Polygon(130, 310, 170, 345, 180, 330, 220, 330, 230, 345, 270, 310, 278, 295, 122, 295, fill = rgb(240, 240, 240)),
    Polygon(180, 330, 220, 330, 220, 265, 200, 260, 180, 265, fill = 'steelBlue'),
)

stoneP1 = Group(
    Polygon(140, 145, 140, 29, 160, 22, 180, 16, 180, 87, 220, 87, 220, 16, 240, 22, 260, 29, 260, 145, fill = 'brown'),
    
    Polygon(75, 127, 55, 135, 60, 295, 100, 275, 100, 216, 75, 195, 68, 150, 63, 146, 75, 146, fill = 'brown'),
    Polygon(325, 127, 345, 135, 340, 295, 300, 275, 300, 216, 325, 195, 332, 150, 337, 146, 325, 146, fill = 'brown'),
    Polygon(100, 275, 100, 295, 64, 320, 56, 311,56, 297, fill = 'brown'),
    Polygon(300, 275, 300, 295, 336, 320, 344, 311, 344, 297, fill = 'brown'),
    
    Polygon(70, 119, 80, 96, 90, 78, 100, 145, 87, 146, 84, 118, fill = 'brown'),
    Polygon(330, 119, 320, 96, 310, 78, 300, 145, 313, 146, 316, 118, fill = 'brown'),
)

stoneP2 = Group(
    Polygon(140, 145, 140, 29, 160, 22, 180, 16, 180, 87, 220, 87, 220, 16, 240, 22, 260, 29, 260, 145, fill = 'crimson'),
    
    Polygon(70, 119, 80, 96, 90, 78, 100, 145, 87, 146, 84, 118, fill = 'crimson'),
    Polygon(330, 119, 320, 96, 310, 78, 300, 145, 313, 146, 316, 118, fill = 'crimson'),    
    
    Polygon(305, 215, 337, 190, 337, 260, 305, 250, 305, 200, 305, 250, fill = 'crimson', border = 'gray'),
    Polygon(95, 215, 63,  190, 63,  260, 95,  250, 95,  200, 95, 250, fill = 'crimson', border = 'gray'),
)    

thornP1 = Group(
    Polygon(75, 195, 155, 200, 145, 160, 140, 154, 170, 154, 175, 160, 225, 160, 230, 154, 260, 154, 255, 160, 245, 200, 325, 195, 250, 260, 250, 300, 206, 240, 194, 240, 150, 300, 150, 260, fill = 'crimson'),
    
    Polygon(165, 145, 150, 110, 150, 80, 160, 60, 168, 19,   150, 25, 150, 60, 135, 60, 130, 80, 120, 90,  125, 120, 137, 145, fill = 'crimson'),
    Polygon(147, 57, 147, 27, 135, 33, 135, 57, fill = 'crimson'),
    Polygon(132, 60, 132, 36,  120, 45, 125, 80, fill = 'crimson'),
    Polygon(123, 82, 114, 48, 102, 60, 120, 87, fill = 'crimson'),
    Polygon(117, 90, 100, 65, 93, 75, 115, 95, fill = 'crimson'),
    Polygon(116, 100, 122, 120, 85, 91, 90, 80, fill = 'crimson'),
    
    Polygon(235, 145, 250, 110, 250, 80, 240, 60, 232, 19,   250, 25, 250, 60, 265, 60, 270, 80, 280, 90,  275, 120, 263, 145, fill = 'crimson'),
    Polygon(253, 57, 253, 27, 265, 33, 265, 57, fill = 'crimson'),
    Polygon(268, 60, 268, 36,  280, 45, 275, 80, fill = 'crimson'),
    Polygon(278, 82, 286, 48, 298, 60, 280, 87, fill = 'crimson'),
    Polygon(283, 90, 300, 65, 307, 75, 285, 95, fill = 'crimson'),
    Polygon(284, 100, 278, 120, 315, 91, 310, 80, fill = 'crimson'),
    
    Polygon(100, 345,   200, 255,   295, 345,   259, 356,   218, 361,   218,335,   182, 335,   181, 361,   144, 356, fill = 'crimson'),
    
    Line(130, 330, 155, 350, fill = 'white', dashes=(4, 4), lineWidth = 35),
    Line(270, 330, 245, 350, fill = 'white', dashes=(4, 4), lineWidth = 35),
    Polygon(105, 308, 127, 320, 110, 335, 95, 325, fill = 'crimson'),
    Polygon(295, 308, 273, 320, 290, 335, 305, 325, fill = 'crimson'),
    Polygon(150, 300, 115, 285, 125, 275, 125, 255, 128, 252, 135, 275, 150, 260, fill = 'crimson'),
    Polygon(250, 300, 285, 285, 275, 275, 275, 255, 272, 252, 265, 275, 250, 260, fill = 'crimson'),
    
    Polygon(315, 230, 340, 200, 340, 120, 60, 120, 60, 200, 85, 230, 85, 155, 315, 155, fill = 'grey'),
    Polygon(85, 230, 85, 155, 60, 120, 60, 200, fill = 'dimgrey'),
    Polygon(315, 230, 315, 155, 340, 120, 340, 200, fill = 'dimgrey'),
    Rect(185, 120, 30, 30, fill = rgb(240, 240, 240)),
)    

thornP2 = Group(
    Polygon(145, 160, 140, 154, 64, 154, 65, 190, 98, 221, 155, 200, fill = rgb(240, 240, 240)),
    Polygon(255, 165, 260, 154, 336, 154, 335, 190, 302, 221, 245, 200, fill = rgb(240, 240, 240)),
    Polygon(175, 160, 170, 154, 230, 154, 225, 160, fill = 'white'),
    Oval(130, 342, 110, 90, fill=gradient('grey', 'crimson', 'crimson', 'crimson', start='left-bottom')),
    Oval(270, 342, 110, 90, fill=gradient('grey', 'crimson', 'crimson', 'crimson', start='right-bottom')),
    
    Polygon(165, 145, 150, 110, 150, 80, 160, 60, 168, 19,   150, 25, 150, 60, 135, 60, 130, 80, 120, 90,  125, 120, 137, 145, fill = 'crimson'),
    Polygon(147, 57, 147, 27, 135, 33, 135, 57, fill = 'crimson'),
    Polygon(132, 60, 132, 36,  120, 45, 125, 80, fill = 'crimson'),
    Polygon(123, 82, 114, 48, 102, 60, 120, 87, fill = 'crimson'),
    Polygon(117, 90, 100, 65, 93, 75, 115, 95, fill = 'crimson'),
    Polygon(116, 100, 122, 120, 85, 91, 90, 80, fill = 'crimson'),
    
    Polygon(235, 145, 250, 110, 250, 80, 240, 60, 232, 19,   250, 25, 250, 60, 265, 60, 270, 80, 280, 90,  275, 120, 263, 145, fill = 'crimson'),
    Polygon(253, 57, 253, 27, 265, 33, 265, 57, fill = 'crimson'),
    Polygon(268, 60, 268, 36,  280, 45, 275, 80, fill = 'crimson'),
    Polygon(278, 82, 286, 48, 298, 60, 280, 87, fill = 'crimson'),
    Polygon(283, 90, 300, 65, 307, 75, 285, 95, fill = 'crimson'),
    Polygon(284, 100, 278, 120, 315, 91, 310, 80, fill = 'crimson'),
    
    Polygon(300, 253, 273, 272, 275, 287, 275, 300, 285, 300, 305, 277, 300, 270, 308, 261,  fill = 'crimson'),
    Polygon(302, 307, 320, 285, 312, 275, 320, 265, 335, 285, 315, 315, fill = 'crimson'),
    
    Polygon(100, 253, 127, 272, 125, 287, 125, 300, 115, 300, 95, 277, 100, 270, 92, 261,  fill = 'crimson'),
    Polygon(98, 307, 80, 285, 88, 275, 80, 265, 65, 285, 85, 315, fill = 'crimson'),

    Polygon(140, 290, 135, 300, 110, 310, 80, 335, 75, 350, 75, 335, 85, 320, 100, 307,  fill = 'white'),
    Polygon(140, 315, 145, 302,  115, 312, 90, 332, 82, 345, 80, 360, 85, 370, 87, 355, 95, 340, 120, 323,  fill = 'white'),
    Polygon(160, 332, 160, 317, 140, 323, 115, 332, 105, 340, 95, 350, 90, 375, 95, 377, 105, 355, 130, 338,  fill = 'white'),
    
    Polygon(260, 290, 265, 300, 290, 310, 320, 335, 325, 350, 325, 335, 315, 320, 300, 307,  fill = 'white'),
    Polygon(260, 315, 255, 302,  285, 312, 310, 332, 318, 345, 320, 360, 315, 370, 313, 355, 305, 340, 280, 323,  fill = 'white'),
    Polygon(240, 332, 240, 317, 260, 323, 285, 332, 295, 340, 305, 350, 310, 375, 305, 377, 295, 355, 270, 338,  fill = 'white'),

    Polygon(310, 270, 340, 240, 340, 125, 220, 120, 180, 120, 60, 125, 60, 240, 90, 270, 80, 155, 320, 155,  fill = 'grey'),
    Polygon(90, 270, 60, 240, 60, 125, 80, 155, fill = 'dimgrey'),
    Polygon(310, 270, 340, 240, 340, 125, 320, 155, fill = 'dimgrey'),
    Line(325, 255, 330, 135, fill = 'white'),
    Line(330, 135, 70, 135, fill = 'white'),
    Line(75, 255, 70, 135, fill = 'white'),
    Line(180, 135, 180, 150, fill = 'white'),
    Line(220, 135, 220, 150, fill = 'white'),
    Line( 170, 135, 170, 145, fill = 'white'),
    Line( 230, 135, 230, 145, fill = 'white'),
    Line( 170, 145, 155, 145, fill = 'white'),
    Line( 230, 145, 245, 145, fill = 'white'),
)

vaughnP2 = Group(
    Polygon(175, 90, 175, 10, 165, 15, 165, 80, 155, 80, 155, 15, 135, 25, 135, 80, 125, 80, 125, 30, 115, 40, 115, 90, fill = rgb(255, 90, 20)), #Upper helmet pads
    Polygon(225, 90, 225, 10, 235, 15, 235, 80, 245, 80, 245, 15, 265, 25, 265, 80, 275, 80, 275, 30, 285, 40, 285, 90, fill = rgb(255, 90, 20)), 
    
    Polygon(95, 145, 120, 120, 165, 130, 165, 120, 145, 100, 160, 85, 180, 40, 220, 40, 240, 85, 255, 100, 235, 120, 235, 130, 280, 120, 305, 145, 220, 145, 220, 115, 235, 100, 220, 85, 180, 85, 165, 100, 180, 115, 180, 145,  fill = 'white'),
    Polygon(140, 100, 125, 85, 140, 65, 155, 85, fill = 'white'),
    Polygon(260, 100, 275, 85, 260, 65, 245, 85, fill = 'white'),
    
    Polygon(310, 270, 340, 240, 340, 125, 220, 120, 180, 120, 60, 125, 60, 240, 90, 270, 80, 155, 320, 155,  fill = 'crimson', border='firebrick'), # Visor
    Polygon(90, 270, 60, 240, 60, 125, 80, 155, fill = 'firebrick'),
    Polygon(310, 270, 340, 240, 340, 125, 320, 155, fill = 'firebrick'),
    
    Polygon(220, 120, 220, 155, 250, 145, 300, 140, 327, 146, 325, 205, 315, 230, 330, 210, 333, 135, 300, 125, 235, 140, 235, 120, fill = 'white'),
    Polygon(180, 120, 180, 155, 150, 145, 100, 140, 73, 146, 75, 205, 85, 230, 70, 210, 67, 135, 100, 125, 165, 140, 165, 120, fill = 'white'),
    Polygon(310, 270, 340, 240, 340, 190, 330, 225, fill = 'white', border = 'firebrick', borderWidth = 1),
    Polygon(90, 270, 60, 240, 60, 190, 70, 225, fill = 'white', border = 'firebrick', borderWidth = 1),
    
    Rect(355, 155, 7, 70, fill = 'darkgrey'),
    Line(358, 155, 358, 35, fill = 'silver', lineWidth = 4),
    Polygon(358, 35, 358, 48, 337, 40, fill = 'silver'),
    
    Line(45, 225, 45, 10, fill = gradient('dimgrey', 'dimgrey', 'darkgrey', start='right'), lineWidth=10),
    
    Circle(287, 105, 18, fill = 'white'),
    Circle(290, 105, 18, fill = 'gainsboro'),
    Circle(290, 105, 12, fill = 'red'),
    
    Polygon(193, 330, 208, 330, 208, 385, 193, 385, fill = 'darkOrange', border = 'white', borderWidth = 5),
)    

wolffeP1 = Group(
    Polygon(175, 160, 160, 100, 115, 48, 140, 29, 180, 15, 220, 15, 260, 29, 285, 48, 240, 100, 225, 160, fill = 'lightSlateGray'),
    RegularPolygon(200, 115, 20, 3, fill = 'red', rotateAngle = 60),
    Line(85, 135, 115, 135, fill = 'yellow', dashes=True, lineWidth=20),
    Line(315, 135, 285, 135, fill = 'yellow', dashes=True, lineWidth=20),
    
    Polygon(200, 255, 155, 300, 165, 320, 170, 300, 185, 315, 190, 295, 200, 310, 210, 295, 215, 315, 230, 300, 235, 320, 245, 300, fill = 'white'),
    
    Polygon(75, 127, 55, 135, 75, 195, 65, 149, 75, 146, fill = 'lightSlateGray'),
    Polygon(325, 127, 345, 135, 325, 195, 335, 149, 325, 146, fill = 'lightSlateGray'),
    
    Polygon(55, 175, 85, 240, 100, 217, 108, 240, 118, 228, 125, 250, 135, 244, 140, 270, 130, 260, 120, 270, 115, 255, 105, 260, 100, 250 , 85, 260,  56, 220,  fill = 'lightSlateGray'),
    Polygon(345, 175, 315, 240, 300, 217, 292, 240, 282, 228, 275, 250, 265, 244, 260, 270, 270, 260, 280, 270, 285, 255, 295, 260, 300, 250 , 315, 260,  344, 220,  fill = 'lightSlateGray'),
    Polygon(59, 258, 80, 275, 100, 260, 100, 275, 60, 295, fill = 'lightSlateGray'),
    Polygon(341, 258, 320, 275, 300, 260, 300, 275, 340, 295, fill = 'lightSlateGray'),
    Polygon(135, 275, 105, 300, 110, 275, fill = rgb(245, 245, 245)),
    Polygon(265, 275, 295, 300, 290, 275, fill = rgb(245, 245, 245)),
)    

wolffeP2 = Group(
    Line(42, 190, 42, 7, fill = 'darkGrey', lineWidth=8),
    Polygon(42, 25, 60, 15, 100, 10, 105, 2, 60, 2, 60, 1, 24, 1, 20, 10, 24, 15, fill='grey'),
    
    Polygon(180, 162, 180, 100, 115, 48, 140, 29, 180, 15, 220, 15, 260, 29, 285, 48, 220, 100, 220, 162, fill = 'lightSlateGray'),
    RegularPolygon(200, 125, 17, 3, fill = 'red', rotateAngle = 60),
    Line(95, 130, 125, 130, fill = 'yellow', dashes=True, lineWidth=25),
    Line(305, 130, 275, 130, fill = 'yellow', dashes=True, lineWidth=25),
    
    Polygon(70, 153,70, 170, 175, 195, 200, 175, 225, 195, 330, 170, 330, 153, fill = 'white', border='lightgrey'),
    Polygon(220, 168, 180, 168, 180, 255, 195, 245, 195, 240, 205, 240, 205, 245, 220, 255, fill = 'lightSlateGray'),
    
    Polygon(75, 160, 75, 163, 170, 185, 200, 168, 230, 185, 325, 163, 325, 160),
    Polygon(110, 165, 150, 182, 105, 175, fill = 'white'),
    Polygon(290, 165, 250, 182, 295, 175, fill = 'white'),
    Polygon(200, 175, 210, 180, 190, 180),
    
    Oval(130, 342, 110, 90, fill=gradient('grey', 'lightSlateGray', 'lightSlateGray', 'lightSlateGray', start='left-bottom')),
    Oval(270, 342, 110, 90, fill=gradient('grey', 'lightSlateGray', 'lightSlateGray', 'lightSlateGray', start='right-bottom')),
    
    Polygon(130, 310, 170, 345, 180, 330, 220, 330, 230, 345, 270, 310, 278, 295, 122, 295, fill = rgb(240, 240, 240)),
    
    Polygon(220, 265, 200, 260, 180, 265, 160, 275, 180, 300, 180, 325, 170, 320, 178, 337, 167, 330, 165, 360, 235, 360,  233, 330, 222, 337, 230, 320, 220, 325, 220, 300, 240, 275, fill = 'lightSlateGray'),
    Polygon(75, 200, 65, 250, 80, 245, 90, 235, 105, 250, 115, 245, 130, 260, 115, 235, 105, 240, 100, 220, 100, 220, 90, 225, 90, 210, 80, 220, 80, 202,  fill = 'lightSlateGray'),
    Polygon(325, 200, 335, 250, 320, 245, 310, 235, 295, 250, 285, 245, 270, 260, 285, 235, 295, 240, 300, 220, 300, 220, 310, 225, 310, 210, 320, 220, 320, 202,  fill = 'lightSlateGray'),
    Polygon(95, 250, 85, 265, 105, 262, 105, 280, 125, 275,130, 277,  fill = rgb(240, 240, 240)),
    Polygon(305, 250, 315, 265, 295, 262, 295, 280, 275, 275,270, 277,  fill = rgb(240, 240, 240)),
    
    
    Polygon(167, 345, 150, 385, 250, 385, 233, 345, fill = 'lightSlateGray'),
    Polygon(167, 345, 160, 385, 240, 385, 233, 345, fill = 'slateGray', border='black'),
    Rect(185, 348, 30, 12),
    Rect(190, 360, 20, 3),
    Rect(175, 370, 50, 15)
)

decals = {
    "shiny": shiny,
    "grunt187thP1": grunt187thP1,
    "stripedP2": stripedP2,
    "grunt212thP1": grunt212thP1,
    "gruntTriangle": gruntTriangle,
    "grunt332ndP2": grunt332ndP2,
    "grunt41stP1": grunt41stP1,
    "grunt41stP2": grunt41stP2,
    "grunt501stP1": grunt501stP1,
    "grunt501stP2": grunt501stP2,
    "grunt442ndP1": grunt442ndP1,
    "grunt327thP1": grunt327thP1,
    "grunt327thP2": grunt327thP2,
    "grunt104thP1": grunt104thP1,
    "grunt104thP2": grunt104thP2,
    "gruntCoruscantGuardP1": gruntCoruscantGuardP1,
    "grunt91st": grunt91st,
    "appoP1": appoP1,
    "appoP2": appoP2,
    "blyP1": blyP1,
    "blyP2": blyP2,
    "codyP1": codyP1,
    "codyP2": codyP2,
    "doomP2": doomP2,
    "echoP1": echoP1,
    "echoP2": echoP2,
    "fivesP1": fivesP1,
    "fivesP2": fivesP2,
    "greeP1": greeP1,
    "greeP2": greeP2,
    "hammerP1": hammerP1,
    "hammerP2": hammerP2,
    "jesseP1": jesseP1,
    "jesseP2": jesseP2,
    "keeliP1": keeliP1,
    "lockP1": lockP1,
    "lockP2": lockP2,
    "neyoP2": neyoP2,
    "pondsP1": pondsP1,
    "rexP1": rexP1,
    "rexP2": rexP2,
    "stoneP1": stoneP1,
    "stoneP2": stoneP2,
    "thornP1": thornP1,
    "thornP2": thornP2,
    "vaughnP2": vaughnP2,
    "wolffeP1": wolffeP1,
    "wolffeP2": wolffeP2
}

for name, decal in decals.items():
    decal.visible = False
    
############### Other Shapes / Objects #####################################################################################################################################################################################################

labelP = Label('Phase I', 32, 375, size=11, font='orbitron', fill = 'aliceBlue', border='aliceBlue', borderWidth=.5)
labelDecal = Label('Grunt', 35, 390, size=11, font='orbitron', fill = 'aliceBlue', border='aliceBlue', borderWidth=.5)

startInfo = Group(
    Rect(10, 140, 380, 100, border=gradient('darkgrey', 'gainsboro', start='right'), borderWidth=10, visible=False, fill=gradient('deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue', start='top')),
    Label('Click different keys to show different Clone Trooper styles. Click the',  200, 165, size=10, fill='lightCyan', font='montserrat', bold=True),
    Label('space key to switch between Phase I and Phase II. Click the',  182, 180, size=10, fill='lightCyan', font='montserrat', bold=True),
    Label('backspace key to revert to a blank helmet. Hold the enter key to',  192, 195, size=10, fill='lightCyan', font='montserrat', bold=True),
    Label('show a list of all the possible styles. Click the screen to continue.',  192, 210, size=10, fill='lightCyan', font='montserrat', bold=True),
)
startInfo.shown = True
    
holoPad = Rect(10, 140, 380, 100, border='silver', borderWidth=10, opacity=95, visible=False, fill=gradient( 'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue', start='top'))
invalidLabel = Label('', 200, 190, size=13, fill='lightCyan', font='montserrat', bold=True)    

binocsShadowP1 = Polygon(75, 195, 150, 370, 250, 370, 325, 195, opacity=7, visible = False) 
binocsShadowP2 = Polygon(75, 205, 150, 380, 185, 350, 215, 350, 250, 380, 325, 205, opacity=7, visible = False)
visorShadowP1 = Polygon(85, 155, 315, 155, 315, 230, 270, 243, 200, 243, 130, 243, 85, 230, fill = gradient('black', 'black', 'gainsboro', start = 'top'), opacity=20, visible = False)
visorShadowThorn = Polygon(85, 155, 315, 155, 315, 230, 270, 243, 200, 243, 130, 243, 85, 230, fill = gradient('black', 'black', rgb(200, 0, 40), start = 'top'), opacity=20, visible = False)
visorShadowP2 = Polygon(80, 155, 320, 155, 315, 205, 310, 270, 274, 284, 200, 245, 126, 284, 90, 270, 85, 205, fill = gradient('black', 'black', 'gainsboro', start = 'top'), opacity=20, visible = False)
visorShadowDoom = Polygon(80, 155, 320, 155, 315, 205, 310, 270, 274, 284, 200, 245, 126, 284, 90, 270, 85, 205, fill = gradient('black', 'black', 'grey', start = 'top'), opacity=20, visible = False)

list = Group(        
    Rect(10, 95, 380, 190, border=gradient('darkgrey', 'gainsboro', start='right'), borderWidth=10, visible=False, fill=gradient('deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue', start='top')),
    Label('1 = 187th    A = Commander Appo       L = Captain Lock              ', 200, 115, size = 11, fill='lightCyan', font='montserrat', bold=True),
    Label('2 = 212th     B = Commander Bly           N = Commander Neyo     ', 200, 130, size = 11, fill='lightCyan', font='montserrat', bold=True),
    Label('3 = 332nd   C = Commander Cody        P = Commander Ponds  ', 200, 145, size = 11, fill='lightCyan', font='montserrat', bold=True),
    Label('4 = 41st      D = Commander Doom      R = Captain Rex               ', 200, 160, size = 11, fill='lightCyan', font='montserrat', bold=True),
    Label('5 = 501st    E = Arc Trooper Echo          S = Commander Stone   ', 200, 175, size = 11, fill='lightCyan', font='montserrat', bold=True),
    Label('6 = 442nd  F = Arc Trooper Fives          T = Commander Thorn   ', 200, 190, size = 11, fill='lightCyan', font='montserrat', bold=True),
    Label('7 = 327th   G = Commander Gree         V = Captain Vaughn        ', 200, 205, size = 11, fill='lightCyan', font='montserrat', bold=True),
    Label('8 = CG        H = Arc Trooper Hammer  W = Commander Wolffe', 200, 220, size = 11, fill='lightCyan', font='montserrat', bold=True),
    Label('9 = 91st      J = Commander Jesse                                                     ', 200, 235, size = 11, fill='lightCyan', font='montserrat', bold=True),
    Label('0 = 104th   K = Captain Keeli                                                             ', 200, 250, size = 11, fill='lightCyan', font='montserrat', bold=True),
)
list.visible = False
list.shown = False

backgroundIcon = Group(
    Circle(380, 20, 12, fill=gradient( 'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue', start='top'), border = 'silver'),
    Rect(373, 13, 14, 14, fill = None, border='lightCyan', borderWidth=2),
    Polygon(373, 27, 373, 26, 378, 20, 381, 23, 383, 23, 387, 27, 387, 26, fill = 'lightCyan'),
    Circle(382, 18, 2, fill = 'lightCyan')
    )
backgroundUILabel = Label('None', 200, 200, size=14, fill ='lightCyan', font='montserrat', bold=True, opacity = 0)
backgroundUIX = Group(
    Line(340, 140, 350, 150, fill = 'lightCyan'),
    Line(350, 140, 340, 150, fill = 'lightCyan')    
    )
backgroundUILeft = Rect(70,185 ,20, 30, fill='lightCyan', opacity=1)
backgroundUIRight = Rect(310,185 ,20, 30, fill='lightCyan', opacity=1)
backgroundUI = Group(
    Rect(50, 140, 300, 100, border=gradient('darkgrey', 'gainsboro', start='right'), borderWidth=10, visible=False, fill=gradient('deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue', start='top')),
    Label('Background', 200, 160, size = 25, fill ='lightCyan', font='montserrat', bold=True),
    Label('<', 80, 200, fill = 'lightCyan', bold=True, size = 24),
    Label('>', 320, 200, fill = 'lightCyan', bold=True, size = 24),
    Rect(70,185 ,20, 30, fill=None, border='lightCyan'),
    Rect(310,185 ,20, 30, fill=None, border='lightCyan'),
    backgroundUIX,
    )
backgroundUI.opacity=0
backgroundUI.shown=False
backgroundUILabel.shown=False
backgroundUILabel.image = 0

musicIcon = Group(
    Circle(380, 50, 12, fill=gradient( 'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue', start='top'), border = 'silver'),
    Circle(375, 54, 3, fill = 'lightCyan'),
    Line(377, 54, 377, 45, fill = 'lightCyan'),
    Line(376, 45, 387, 44, fill = 'lightCyan', lineWidth=3),
    Line(386, 52, 386, 45, fill = 'lightCyan'),
    Circle(384, 53, 3, fill = 'lightCyan'),
    )
musicUILabel = Label('The Clones - Theme', 200, 200, size=14, fill ='lightCyan', font='montserrat', bold=True, opacity = 0)
musicUIX = Group(
    Rect(340, 140, 10, 10, fill = 'lightCyan', opacity = 1),
    )
musicUILeft = Rect(70,185 ,20, 30, fill='lightCyan', opacity=1)
musicUIRight = Rect(310,185 ,20, 30, fill='lightCyan', opacity=1)
musicUI = Group(
    Rect(50, 140, 300, 100, border=gradient('darkgrey', 'gainsboro', start='right'), borderWidth=10, visible=False, fill=gradient('deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue', start='top')),
    Label('Music', 200, 160, size = 25, fill ='lightCyan', font='montserrat', bold=True),
    Label('<', 80, 200, fill = 'lightCyan', bold=True, size = 24),
    Label('>', 320, 200, fill = 'lightCyan', bold=True, size = 24),
    Rect(70,185 ,20, 30, fill=None, border='lightCyan'),
    Rect(310,185 ,20, 30, fill=None, border='lightCyan'),
    Line(340, 140, 350, 150, fill = 'lightCyan'),
    Line(350, 140, 340, 150, fill = 'lightCyan'),
    )
musicUI.opacity=0
musicUI.shown=False
musicUILabel.shown=False
musicUILabel.song = 1

infoIcon = Group(
    Circle(380, 80, 12, fill=gradient( 'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue', start='top'), border = 'silver'),
    Line(380, 79, 380, 88, fill = 'lightCyan', lineWidth = 5),
    Circle(380, 75, 3, fill = 'lightCyan')
    )
infoLabel1 = Label('Label 1', 200, 150, fill ='lightCyan', font='montserrat', bold=True, opacity = 0)
infoLabel2 = Label('Label 2', 200, 170, fill ='lightCyan', font='montserrat', bold=True, opacity = 0)
infoLabel3 = Label('Label 3', 200, 190, fill ='lightCyan', font='montserrat', bold=True, opacity = 0)
infoLabel4 = Label('Label 4', 200, 210, fill ='lightCyan', font='montserrat', bold=True, opacity = 0)
infoLabel5 = Label('Label 5', 200, 230, fill ='lightCyan', font='montserrat', bold=True, opacity = 0)
infoUIX = Group(
    Line(340, 130, 350, 140, fill = 'lightCyan'),
    Line(350, 130, 340, 140, fill = 'lightCyan')    
    )
infoUI = Group(
    Rect(50, 130, 300, 130, border=gradient('darkgrey', 'gainsboro', start='right'), borderWidth=10, visible=False, fill=gradient('deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue',  'deepSkyBlue', 'dodgerBlue', start='top')),
    infoUIX,
    )
infoUI.opacity = 0
infoUI.shown = False

cursorLabelLabel = Label('Background', 24, 3, size = 9, fill = 'white', opacity = 0)
cursorLabel = Group(
    Rect(0, 0, 50, 10, opacity = 0),
    cursorLabelLabel
    )
cursorLabel.shown = False

vignette = Rect(0, 0, 400, 400, opacity = 0)
vignette.shown = False

############### Functions ###################################################################################################################################################################################################

app.fadeObjectsList = [startInfo, list, backgroundUI, backgroundUILabel, musicUI, musicUILabel, infoUI, cursorLabel]
app.stepsPerSecond = 70
def onStep():
    
    if app.decal in decals:
        poly = decals[app.decal]
        if (poly.opacity < 100):
            poly.opacity += 5 
            
    for object in app.fadeObjectsList:
        if object.shown == False and object.opacity > 0:
            object.opacity -= 5
        elif object.shown == True and object.opacity < 100:
            object.opacity += 5

    # if ((infoUI.shown == False) and (infoUI.opacity > 0)):
    #     infoUI.opacity -= 5
    #     infoLabel1.opacity -=5
    #     infoLabel2.opacity -=5
    #     infoLabel3.opacity -=5
    #     infoLabel4.opacity -=5
    #     infoLabel5.opacity -=5
    # elif ((infoUI.shown == True) and (infoUI.opacity < 100)):
    #     infoUI.opacity += 5
    #     infoLabel1.opacity +=5
    #     infoLabel2.opacity +=5
    #     infoLabel3.opacity +=5
    #     infoLabel4.opacity +=5
    #     infoLabel5.opacity +=5
        
    if ((vignette.shown == False) and (vignette.opacity > 0)):
        vignette.opacity -= 2
    elif ((vignette.shown == True) and (vignette.opacity < 50)):
        vignette.opacity += 2

    for image in backgrounds:
        if ((image.shown == False) and (image.opacity > 0)):
            image.opacity -= 5
        elif ((image.shown == True) and (image.opacity < 100)):
            image.opacity += 5

    for image in logos:
        if ((image.shown == False) and (image.opacity > 0)):
            image.opacity -= 5
        elif ((image.shown == True) and (image.opacity < 100)):
            image.opacity += 5

def showDecal(decal):                   ### Shows the decal that was called and hides other decals
    for name, poly in decals.items():
        if (name == decal):
            poly.visible = True
        else: 
            poly.visible = False

def opacity(decal):                    
    for name, poly in decals.items():
        if (name == decal):
            app.decal = decal
            poly.opacity = 0

def invalid(size, text):                      ### Show and invalid message or reset the invalid message
    holoPad.visible = True
    invalidLabel.visible = True
    invalidLabel.value = text
    labelP.toFront()
    labelDecal.toFront()
    invalidLabel.toFront()
    changeLogo(logoRepublic)
    if (size == ""):
        invalidLabel.size = 13
    else: 
        invalidLabel.size = size
    if (text == ""):
        holoPad.visible = False
        invalidLabel.visible = False
        changeSound.stop()
        changeSound.play()
    else:
        errorSound.stop()
        errorSound.play()

def showShadow(phase, gear):                ### Shows the shadow for binocs or visors
    if (phase == 'p1'):
        if (gear == 'binocs'):
            binocsShadowP1.visible = True
        elif (gear == 'visor'):
            visorShadowP1.visible = True
        elif (gear == 'thorn'):
            visorShadowThorn.visible = True
            
    elif (phase == 'p2'):
        if (gear == 'binocs'):
            binocsShadowP2.visible = True
        elif (gear == 'visor'):
            visorShadowP2.visible = True
        elif (gear == 'doom'):
            visorShadowDoom.visible = True
        
    elif (phase == ''):
        binocsShadowP1.visible = False
        binocsShadowP2.visible = False
        visorShadowP1.visible = False
        visorShadowThorn.visible = False
        visorShadowP2.visible = False
        visorShadowDoom.visible = False

def reset():                                        ### Reset
    phaseIIVisor.fill = 'black'
    phaseIILowerCover.fill = rgb(240, 240, 240)
    phaseIMowhawk.fill = gradient('lightGrey', 'lightGrey', 'white', 'white', 'white', start='top')
    phaseIICover.fill = gradient(rgb(220, 220, 220), 'white', 'white', 'white', 'white', 'white', 'white', 'white', rgb(220, 220, 220), start='left')
    phaseICover.fill = gradient(rgb(220, 220, 220), 'white', 'white', 'white', 'white', 'white', 'white', 'white', rgb(220, 220, 220), start='left')
    phaseILower.fill = gradient('white', 'white','white','white', 'grey', start='bottom')
    phaseIIBase.fill = gradient('lightGrey', 'white', 'white', start='top')
    phaseIIBase2.fill = 'white'
    phaseIBase2.fill = 'white'
    phaseIBase.fill = gradient('lightGrey', 'white', 'white', start='top')
    phaseIILeftLowerHalf.fill = gradient('grey', rgb(245, 245, 245), rgb(245, 245, 245), rgb(245, 245, 245), start='left-bottom')
    phaseIIRightLowerHalf.fill = gradient('grey', rgb(245, 245, 245), rgb(245, 245, 245), rgb(245, 245, 245), start='right-bottom')
    phaseIILeftBottom.fill = gradient('grey', rgb(245, 245, 245), rgb(245, 245, 245), rgb(245, 245, 245), start='left-bottom')
    phaseIIRightBottom.fill = gradient('grey', rgb(245, 245, 245), rgb(245, 245, 245), rgb(245, 245, 245), start='right-bottom')
    phaseIIInner.fill = rgb(240, 240, 240)
    showShadow('', '')
    if (labelP.value == 'Phase II'):
        phaseIIVisor.visible = True
        phaseIIMouthPiece.visible = True
        phaseIIAeroators.visible = True
        phaseIIAeroators.toFront()
    for name, poly in decals.items():
        poly.toFront()
         
#def changeHelmet(label, decal, logo, mowhawkFill='', ):
 #   labelDecal.value = label
  #  invalid("", "")
   #showDecal(decal)
    #changeLogo(logo)
    #phaseIMowhawk.toFront()
    #opacity(decal)

def changeLogo(logo):
    for image in logos:
        image.shown = False
    logo.shown = True

def changeBackground():
    for image in backgrounds:
        image.shown = False

    if backgroundUILabel.image < 0:
        backgroundUILabel.image = 7
    elif backgroundUILabel.image > 7:
        backgroundUILabel.image = 0

    backgrounds[backgroundUILabel.image].shown = True
    backgroundUILabel.value = str(backgrounds[backgroundUILabel.image])

def changeMusic():
    for sound in music:
        sound.stop()
    if musicUILabel.song < 0:
        musicUILabel.song = 7
    if musicUILabel.song > 7:
        musicUILabel.song = 0

    if musicUILabel.song == 0:
        musicUILabel.value = 'Off'
    elif musicUILabel.song == 1:
        musicUILabel.value = 'The Clones - Theme'
        theClonesTheme.play(-1)
    elif musicUILabel.song == 2:
        musicUILabel.value = 'The Clones - Theme 2'
        theClonesTheme2.play(-1)
    elif musicUILabel.song == 3:
        musicUILabel.value = 'Padawan Introduction'
        padawanIntroduction.play(-1)
    elif musicUILabel.song == 4:
        musicUILabel.size = 10
        musicUILabel.value = 'Meeting the Rookies / Retaking the Base'
        meetingTheRookiesAndRetakingTheBase.play(-1)
    elif musicUILabel.song == 5:
        musicUILabel.size = 9
        musicUILabel.value = 'The Clones Theme - 2 Steps From Hell Style'
        theClonesTheme2StepsFromHellStyle.play(-1)
    elif musicUILabel.song == 6:
        musicUILabel.value = 'Battle Over Coruscant'
        battleOverCoruscant.play(-1)
    elif musicUILabel.song == 7:
        musicUILabel.value = 'The Arena'
        theArena.play(-1)

def changeInfo(text):
    labels = [infoLabel1, infoLabel2, infoLabel3, infoLabel4, infoLabel5]
    
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if (i < len(labels)):
            labels[i].value = line

def P1Trooper187th():
    labelDecal.value = '              187th Trooper'
    invalid("", "")
    reset()
    showDecal('grunt187thP1')
    phaseIMowhawk.fill = rgb(135, 75, 150)
    phaseIVisor.toFront()
    phaseIMouthPiece.toFront()
    changeLogo(logo187th)
    opacity('grunt187thP1')

def P2Trooper187th():
    labelDecal.value = '              187th Trooper'
    invalid("", "")
    reset()
    showDecal('stripedP2')
    stripedP2.fill = rgb(135, 75, 150)
    phaseIILowerCover.fill = rgb(135, 75, 150)
    changeLogo(logo187th)
    opacity('stripedP2')
    
def P1Trooper212th():                   
    labelDecal.value = '              212th Trooper'
    invalid("", "")
    reset()
    showDecal('grunt212thP1')
    phaseIMowhawk.fill = 'orange'
    phaseIMouthPiece.toFront()
    phaseIVisor.toFront()
    changeLogo(logo212th)
    opacity('grunt212thP1')
    
def P2Trooper212th():
    labelDecal.value = '              212th Trooper'
    invalid("", "")    
    reset()
    showDecal('gruntTriangle')
    gruntTriangle.fill = 'orange'
    phaseIMowhawk.toFront()
    phaseIMowhawkLines.toFront()
    changeLogo(logo212th)
    opacity('gruntTriangle')
    
def P2Trooper332nd():
    labelDecal.value = '              332nd Trooper'
    invalid("", "")    
    reset()
    showDecal('grunt332ndP2')
    phaseIICover.fill = 'orangeRed'
    phaseIMowhawk.fill = 'orangeRed'
    phaseIMowhawk.toFront()
    phaseIMowhawkLines.toFront()
    phaseIILowerCover.fill = 'orangeRed'
    phaseIIBase.fill = 'orangeRed'
    phaseIIBase2.fill = 'orangeRed'
    changeLogo(logo332nd)
    opacity('grunt332ndP2')
    
def P1Trooper41st():
    labelDecal.value = '              41st Trooper'
    invalid("", "")    
    reset()
    showDecal('grunt41stP1')
    phaseIMowhawk.fill = 'forestGreen'
    phaseIVisor.toFront()
    phaseIMouthPiece.toFront()
    phaseIMowhawkLines.toFront()
    changeLogo(logo41st)
    opacity('grunt41stP1')
    
def P2Trooper41st():
    labelDecal.value = '              41st Trooper'
    invalid("", "")    
    reset()
    showDecal('grunt41stP2')
    phaseIMowhawk.toFront()
    phaseIMowhawkLines.toFront()
    changeLogo(logo41st)
    opacity('grunt41stP2')
    
def P1Trooper501st():
    labelDecal.value = '              501st Trooper'
    invalid("", "")    
    reset()
    showDecal('grunt501stP1')
    phaseIMowhawk.toFront()
    phaseIVisor.toFront()
    phaseIMouthPiece.toFront()
    phaseILine.toFront()
    phaseIMowhawkLines.toFront()
    changeLogo(logo501st)
    opacity('grunt501stP1')
    
def P2Trooper501st():
    labelDecal.value = '              501st Trooper'
    invalid("", "")    
    reset()
    showDecal('grunt501stP2')    
    phaseIILowerCover.fill = rgb(240, 240, 240)
    phaseIMowhawk.toFront()
    phaseIIVisor.toFront()
    phaseIILine.toFront()
    phaseIMowhawkLines.toFront()
    changeLogo(logo501st)
    opacity('grunt501stP2')
    
def P1Trooper442nd():
    labelDecal.value = '              442nd Trooper'
    invalid("", "")    
    reset()
    showDecal('grunt442ndP1')
    phaseIMowhawk.toFront()
    phaseIMowhawkLines.toFront()
    changeLogo(logo442nd)
    opacity('grunt442ndP1')
    
def P2Trooper442nd(): 
    labelDecal.value = '              442nd Trooper'
    invalid("", "")    
    reset()
    showDecal('gruntTriangle')
    gruntTriangle.fill = 'yellowGreen'
    phaseIMowhawk.toFront()
    phaseIMowhawkLines.toFront()
    changeLogo(logo442nd)
    opacity('gruntTriangle')
    
def P1Trooper327th(): 
    labelDecal.value = '              327th Trooper'
    invalid("", "")    
    reset()
    showDecal('grunt327thP1')
    phaseIMowhawk.toFront()
    phaseIVisor.toFront()
    phaseIMouthPiece.toFront()
    phaseILine.toFront()
    phaseIMowhawkLines.toFront()
    changeLogo(logo327th)
    opacity('grunt327thP1')
    
def P2Trooper327th():    
    labelDecal.value = '              327th Trooper'
    invalid("", "")    
    reset()
    showDecal('grunt327thP2')
    phaseIMowhawk.toFront()
    phaseIIVisor.toFront()
    phaseIILine.toFront()
    phaseIMowhawkLines.toFront()
    changeLogo(logo327th)
    opacity('grunt327thP2')
    
def P1TrooperCoruscantGuard():    
    labelDecal.value = '              Coruscant Guard'
    invalid("", "")    
    reset()
    showDecal('gruntCoruscantGuardP1')    
    changeLogo(logoCoruscantGuard)
    opacity('gruntCoruscantGuardP1')
    
def P2TrooperCoruscantGuard():    
    labelDecal.value = '              Coruscant Guard'
    invalid("", "")    
    reset()
    showDecal('stripedP2')
    stripedP2.fill = 'crimson'
    phaseIILowerCover.fill = 'crimson'
    changeLogo(logoCoruscantGuard)
    opacity('stripedP2')
    
def Trooper91st():    
    labelDecal.value = '              91st Trooper'
    invalid("", "")    
    reset()
    showDecal('grunt91st')
    changeLogo(logo91st)
    opacity('grunt91st')
    
def P1Trooper104th():    
    labelDecal.value = '              104th Trooper'
    invalid("", "")    
    reset()
    showDecal('grunt104thP1') 
    changeLogo(logo104th)
    opacity('grunt104thP1')
    
def P2Trooper104th():    
    labelDecal.value = '              104th Trooper'
    invalid("", "")    
    reset()
    showDecal('grunt104thP2')  
    changeLogo(logo104th)
    opacity('grunt104thP2')
    
def P1Appo():    
    labelDecal.value = '              Commander Appo'
    invalid("", "")    
    reset()
    showDecal('appoP1')
    phaseIMouthPiece.toFront()
    phaseIVisor.toFront()
    phaseILine.toFront()
    phaseIMowhawk.toFront()
    phaseIMowhawkLines.toFront()
    changeLogo(logo501st)
    opacity('appoP1')
    
def P2Appo():    
    labelDecal.value = '              Commander Appo'
    invalid("", "")    
    reset()
    showDecal('appoP2')    
    phaseIIVisor.toFront()
    phaseIILine.toFront()
    phaseIMowhawk.toFront()
    phaseIMowhawkLines.toFront()
    changeLogo(logo501st)
    opacity('appoP2')
    
def P1Bly():    
    labelDecal.value = '              Commander Bly'
    invalid("", "")    
    reset()
    showDecal('blyP1')
    phaseIMouthPiece.toFront()
    phaseIMowhawk.toFront()
    phaseIMowhawkLines.toFront()
    phaseIMowhawk.fill = 'gold'
    showShadow('p1', 'binocs')
    changeLogo(logo327th)
    opacity('blyP1')
    
def P2Bly():    
    labelDecal.value = '              Commander Bly'
    invalid("", "")    
    reset()
    showDecal('blyP2')
    phaseIMowhawk.toFront()
    phaseIMowhawkLines.toFront()
    phaseIMowhawk.fill = 'gold'
    phaseIILeftLowerHalf.fill = gradient('grey', 'gold', 'gold', 'gold', start='left-bottom')
    phaseIIRightLowerHalf.fill = gradient('grey', 'gold', 'gold', 'gold', start='right-bottom')
    phaseIILeftBottom.fill = gradient('grey', 'gold', 'gold', 'gold', start='left-bottom')
    phaseIIRightBottom.fill = gradient('grey', 'gold', 'gold', 'gold', start='right-bottom')
    phaseIILowerCover.fill = 'gold'
    phaseIIInner.fill = 'gold'
    phaseIIAeroators.toFront()
    showShadow('p2', 'binocs')
    changeLogo(logo327th)
    opacity('blyP2')
    
def P1Cody():    
    labelDecal.value = '              Commander Cody'
    invalid("", "")    
    reset()
    showDecal('codyP1')
    phaseIMowhawk.fill = 'orange'
    showShadow('p1', 'visor')
    changeLogo(logo212th)
    opacity('codyP1')
    
def P2Cody():    
    labelDecal.value = '              Commander Cody'
    invalid("", "")    
    reset()
    showDecal('codyP2')
    phaseIIAeroators.toFront()
    showShadow('p2', 'visor')
    changeLogo(logo212th)
    opacity('codyP2')
    
def P2Doom():    
    labelDecal.value = '              Commander Doom'
    invalid("", "")    
    reset()
    showDecal('doomP2')
    phaseIICover.fill = 'darkGrey'
    phaseIILowerCover.fill = 'darkGrey'
    phaseIIInner.fill = 'oliveDrab'
    phaseIIBase.fill = 'oliveDrab'
    phaseIIBase2.fill = 'oliveDrab'
    phaseIILeftLowerHalf.fill = gradient('grey', 'oliveDrab', 'oliveDrab', 'oliveDrab', start='left-bottom')
    phaseIIRightLowerHalf.fill = gradient('grey', 'oliveDrab', 'oliveDrab', 'oliveDrab', start='right-bottom')
    phaseIILeftBottom.fill = gradient('grey', 'oliveDrab', 'oliveDrab',  start='left-bottom')
    phaseIIRightBottom.fill = gradient('grey', 'oliveDrab', 'oliveDrab', start='right-bottom')
    phaseIMowhawk.toFront()
    phaseIMowhawkLines.toFront()
    phaseIMowhawk.fill = 'oliveDrab'
    showShadow('p2', 'doom')
    opacity('doomP2')
    
def P1Echo():    
    labelDecal.value = '                    Arc Trooper Echo'
    invalid("", "")    
    reset()
    showDecal('echoP1')
    phaseIMowhawk.fill = 'steelBlue'
    changeLogo(logo501st)
    opacity('echoP1')
    
def P2Echo():    
    labelDecal.value = '                    Arc Trooper Echo'
    invalid("", "")    
    reset()
    showDecal('echoP2')
    phaseIMowhawk.toFront()
    phaseIMowhawkLines.toFront()
    phaseIMowhawk.fill = 'steelBlue'
    changeLogo(logo501st)
    opacity('echoP2')
    
def P1Fives():    
    labelDecal.value = '                    Arc Trooper Fives'
    invalid("", "")    
    reset()
    showDecal('fivesP1')
    phaseIMowhawk.toFront()
    phaseIMowhawkLines.toFront()
    phaseIMowhawk.fill = 'steelBlue'
    phaseILine.toFront()
    changeLogo(logo501st)
    opacity('fivesP1')
    
def P2Fives():    
    labelDecal.value = '                    Arc Trooper Fives'
    invalid("", "")    
    reset()
    showDecal('fivesP2')
    phaseIMowhawk.fill = 'steelBlue'
    phaseIMowhawk.toFront()
    phaseIMowhawkLines.toFront()
    changeLogo(logo501st)
    opacity('fivesP2')
    
def P1Gree():    
    labelDecal.value = '              Commander Gree'
    invalid("", "")    
    reset()
    showDecal('greeP1')
    phaseIVisor.toFront()
    phaseILine.toFront()
    phaseIMowhawk.toFront()
    phaseIMowhawkLines.toFront()
    phaseIMouthPiece.toFront()
    changeLogo(logo41st)
    opacity('greeP1')
    
def P2Gree():    
    labelDecal.value = '              Commander Gree'
    invalid("", "")    
    reset()
    showDecal('greeP2')
    phaseIIVisor.fill = 'lime'
    phaseIIVisor.toFront()
    phaseIILine.toFront()
    phaseIICover.fill = gradient('white', 'silver', start = 'center')
    phaseIILowerCover.fill = gradient('white', 'silver', start = 'top')
    phaseIIInner.fill = 'silver'
    phaseIIBase.fill = gradient('white', 'silver', start = 'center')
    phaseIIBase2.fill = 'silver'
    phaseIILeftLowerHalf.fill = gradient('white',  'silver', 'silver', start='right-top')
    phaseIIRightLowerHalf.fill = gradient('white',  'silver', 'silver', start='left-top')
    phaseIILeftBottom.fill = gradient('white', 'silver', 'silver',  start='right-top')
    phaseIIRightBottom.fill = gradient('white', 'silver', 'silver', start='left-top')
    phaseIMowhawk.toFront()
    phaseIMowhawkLines.toFront()
    phaseIMowhawk.fill = 'silver'
    changeLogo(logo41st)
    opacity('greeP2')
    
def P1Hammer():    
    labelDecal.value = '                    Arc Trooper Hammer'    
    invalid("", "")    
    reset()
    showDecal('hammerP1')
    phaseICover.fill = 'darkGray'
    phaseIMouthPiece.toFront()
    changeLogo(logoRancor)
    opacity('hammerP1')
    
def P2Hammer():    
    labelDecal.value = '                    Arc Trooper Hammer'
    invalid("", "")    
    reset()
    showDecal('hammerP2')
    phaseIICover.fill = 'darkGray'
    phaseIILowerCover.fill = 'darkGray'
    changeLogo(logoRancor)
    opacity('hammerP2')
    
def P1Jesse():    
    labelDecal.value = '              Commander Jesse'
    invalid("", "")    
    reset()
    showDecal('jesseP1')
    phaseIVisor.toFront()
    phaseIMouthPiece.toFront()
    phaseIMowhawk.toFront()
    phaseIMowhawkLines.toFront()
    changeLogo(logo501st)
    opacity('jesseP1')
    
def P2Jesse():    
    labelDecal.value = '              Commander Jesse'
    invalid("", "")    
    reset()
    showDecal('jesseP2')
    phaseIMowhawk.toFront()
    phaseIMowhawkLines.toFront()
    phaseIIVisor.toFront()
    phaseIIInner.fill = 'steelBlue'
    phaseIIBase.fill = 'steelBlue'
    phaseIIBase2.fill = 'steelBlue'
    changeLogo(logo501st)
    opacity('jesseP2')
    
def P1Keeli():    
    labelDecal.value = '              Captain Keeli'
    invalid("", "")    
    reset()
    showDecal('keeliP1')
    phaseICover.fill = 'brown'
    phaseIMouthPiece.toFront()
    changeLogo(logoKeeli)
    opacity('keeliP1')
    
def P1Lock():    
    labelDecal.value = '              Captain Lock'
    invalid("", "")    
    reset()
    showDecal('lockP1')
    phaseIMowhawk.fill = 'oliveDrab'
    phaseIMowhawk.toFront()
    phaseIMowhawkLines.toFront()
    showShadow('p1', 'visor')
    opacity('lockP1')
    
def P2Lock():    
    labelDecal.value = '              Captain Lock'
    invalid("", "")    
    reset()
    showDecal('lockP2')
    phaseIMowhawk.fill = 'oliveDrab'
    phaseIMowhawk.toFront()
    phaseIMowhawkLines.toFront()
    showShadow('p2', 'visor')
    opacity('lockP2')
    
def P1Neyo():
    labelDecal.value = '              Commander Neyo'
    invalid("", "")    
    reset()
    showDecal('grunt91st')
    changeLogo(logo91st)
    opacity('grunt91st')
    
def P2Neyo():    
    labelDecal.value = '              Commander Neyo'
    invalid("", "")    
    reset()
    showDecal('neyoP2')
    phaseIIVisor.visible = False
    phaseIIMouthPiece.visible = False
    phaseIIAeroators.visible = False
    changeLogo(logo91st)
    opacity('neyoP2')
    
def P1Ponds():    
    labelDecal.value = '              Commander Ponds'
    invalid("", "")    
    reset()
    showDecal('pondsP1')
    phaseIMowhawk.fill = 'brown'
    phaseIVisor.toFront()
    phaseIBase.fill = 'brown'
    phaseIBase2.fill = 'brown'
    changeLogo(logo91st)
    opacity('pondsP1')
    
def P1Rex():    
    labelDecal.value = '              Captain Rex'
    invalid("", "")    
    reset()
    showDecal('rexP1')
    phaseIVisor.toFront()
    phaseIMouthPiece.toFront()
    labelP.toFront()
    labelDecal.toFront()
    ##changeInfo('')
    changeLogo(logo501st)
    opacity('rexP1')
    
def P2Rex():    
    labelDecal.value = '              Captain Rex'
    invalid("", "")    
    reset()
    showDecal('rexP2')
    phaseIIVisor.visible = False
    phaseIIAeroators.toFront()
    changeInfo("Captain Rex was the leader of the 501st Legion \n as well as it's subsidiary Torrent Company. Rex \n was present during many battles during the Clone \n Wars, such as Christophsis, Teth, Rishi Moon,\n Umbara, and Mandalore.")
    changeLogo(logo501st)
    opacity('rexP2')
    
def P1Stone():
    labelDecal.value = '              Commander Stone'
    invalid("", "")
    reset()
    showDecal('stoneP1')
    phaseIMowhawk.fill = 'brown'
    changeLogo(logoCoruscantGuard)
    opacity('stoneP1')
    
def P2Stone():
    labelDecal.value = '              Commander Stone'
    invalid("", "")
    reset()
    showDecal('stoneP2')
    phaseIMowhawk.fill = 'crimson'
    changeLogo(logoCoruscantGuard)
    opacity('stoneP2')
    
def P1Thorn():
    labelDecal.value = '              Commander Thorn'
    invalid("", "")    
    reset()
    showDecal('thornP1')    
    phaseIVisor.toFront()
    phaseIMouthPiece.toFront()
    showShadow('p1', 'thorn')
    changeLogo(logoCoruscantGuard)
    opacity('thornP1')
    
def P2Thorn():    
    labelDecal.value = '              Commander Thorn'
    invalid("", "")    
    reset()
    showDecal('thornP2')
    phaseIICover.fill = 'crimson'
    phaseIILowerCover.fill = 'crimson'
    phaseIIVisor.toFront()
    phaseIIAeroators.toFront()
    showShadow('p2', 'visor')
    changeLogo(logoCoruscantGuard)
    opacity('thornP2')    
    
def P2Vaughn():    
    labelDecal.value = '              Captain Vaughn'
    invalid("", "")    
    reset()
    showDecal('vaughnP2')  
    phaseIICover.fill = 'orangeRed'
    phaseIMowhawk.fill = 'orangeRed'
    phaseIMowhawk.toFront()
    phaseIMowhawkLines.toFront()
    phaseIILowerCover.fill = 'orangeRed'
    phaseIIBase.fill = 'orangeRed'
    phaseIIBase2.fill = 'orangeRed'
    showShadow('p2', 'visor')
    changeLogo(logo332nd)
    opacity('vaughnP2')
    
def P1Wolffe():    
    labelDecal.value = '              Commander Wolffe'
    invalid("", "")    
    reset()
    showDecal('wolffeP1')
    phaseILine.toFront()
    phaseIMowhawk.fill = 'lightSlateGray'
    phaseIMowhawk.toFront()
    phaseIMowhawkLines.toFront()
    phaseILower.fill = 'lightSlateGray'
    phaseIMouthPiece.toFront()
    changeLogo(logo104th)
    opacity('wolffeP1')
    
def P2Wolffe():    
    labelDecal.value = '              Commander Wolffe'
    invalid("", "")    
    reset()
    showDecal('wolffeP2')    
    phaseIILine.toFront()
    phaseIMowhawk.toFront()
    phaseIMowhawkLines.toFront()
    phaseIMowhawk.fill = 'lightSlateGray'
    phaseIIVisor.visible = False
    phaseIIAeroators.visible = False
    phaseIILeftLowerHalf.fill = gradient('grey', 'lightSlateGray', 'lightSlateGray', 'lightSlateGray', start='left-bottom')
    phaseIIRightLowerHalf.fill = gradient('grey', 'lightSlateGray', 'lightSlateGray', 'lightSlateGray', start='right-bottom')
    changeLogo(logo104th)
    opacity('wolffeP2')


def onKeyPress(key):
    if (startInfo.visible == True):
        startInfo.shown = False
        
    if (key == 'space'):
        if (labelDecal.value == 'Grunt'):
            invalid("", "")
        if (labelP.value == 'Phase I'):
            phaseIHelmet.visible = False
            phaseIVisor.visible = False
            phaseIMouthPiece.visible = False
            phaseILine.visible = False
            phaseICover.visible = False
            phaseILower.visible = False
            phaseISides.visible = False
            phaseIBase.visible = False
            phaseIBase2.visible = False
            phaseIIHelmet.visible = True
            phaseIIBase.visible = True
            phaseIIBase2.visible = True
            phaseIIVisor.visible = True
            phaseIIMouthPiece.visible = True
            phaseIICover.visible = True
            phaseIILine.visible = True
            phaseIILowerCover.visible = True
            phaseIIAeroators.visible = True
            phaseIILeftBottom.visible = True
            phaseIIRightBottom.visible = True
            phaseIIBase.visible = True
            phaseIILeftLowerHalf.visible = True
            phaseIIRightLowerHalf.visible = True
            phaseIILowerDetails.visible = True
            phaseIIInner.visible = True
            labelP.value = 'Phase II'
            
            if (labelDecal.value == '              187th Trooper'):
                P2Trooper187th()
            if (labelDecal.value == '              212th Trooper'):
                P2Trooper212th()
            if (labelDecal.value == '              332nd Trooper'):
                P2Trooper332nd()
            if (labelDecal.value == '              41st Trooper'):
                P2Trooper41st()
            if (labelDecal.value == '              501st Trooper'):
                P2Trooper501st()
            if (labelDecal.value == '              442nd Trooper'):
                P2Trooper442nd()
            if (labelDecal.value == '              327th Trooper'):
                P2Trooper327th()
            if (labelDecal.value == '              Coruscant Guard'):
                P2TrooperCoruscantGuard()
            if (labelDecal.value == '              104th Trooper'):
                P2Trooper104th()
            if (labelDecal.value == '              91st Trooper'):
                Trooper91st()
            if (labelDecal.value == '              Commander Appo'):
                P2Appo()
            if (labelDecal.value == '              Commander Bly'):
                P2Bly()
            if (labelDecal.value == '              Commander Cody'):
                P2Cody()
            if (labelDecal.value == '              Commander Doom'):
                P2Doom()
            if (labelDecal.value == '                    Arc Trooper Echo'):
                P2Echo()
            if (labelDecal.value == '                    Arc Trooper Fives'):
                P2Fives()
            if (labelDecal.value == '              Commander Gree'):
                P2Gree()
            if (labelDecal.value == '                    Arc Trooper Hammer'):
                P2Hammer()
            if (labelDecal.value == '              Commander Jesse'):
                P2Jesse()
            if (labelDecal.value == '              Captain Keeli'):
                invalid("", "Invalid: Non-canon. Keeli died before Phase II.")
                reset()
                labelDecal.value = '              Captain Keeli'
                showDecal('shiny')
            if (labelDecal.value == '              Captain Lock'):
                P2Lock()
            if (labelDecal.value == '              Commander Neyo'):
                P2Neyo()
            if (labelDecal.value == '              Commander Ponds'):
                invalid("", "Invalid: Non-canon. Ponds died before Phase II.")
                reset()
                labelDecal.value = '              Commander Ponds'
                showDecal('shiny')
            if (labelDecal.value == '              Captain Rex'):
                P2Rex()
            if (labelDecal.value == '              Commander Stone'):
                P2Stone()
            if (labelDecal.value == '              Commander Thorn'):
                P2Thorn()
            if (labelDecal.value == '              Captain Vaughn'):
                P2Vaughn()
            if (labelDecal.value == '              Commander Wolffe'):
                P2Wolffe()
        
        else:
            phaseIHelmet.visible = True
            phaseIVisor.visible = True
            phaseIMouthPiece.visible = True
            phaseILine.visible = True
            phaseICover.visible = True
            phaseILower.visible = True
            phaseISides.visible = True
            phaseIBase.visible = True
            phaseIBase2.visible = True
            phaseIIHelmet.visible = False
            phaseIIBase.visible = False
            phaseIIBase2.visible = False
            phaseIIVisor.visible = False
            phaseIIMouthPiece.visible = False
            phaseIICover.visible = False
            phaseIILine.visible = False
            phaseIILowerCover.visible = False
            phaseIIAeroators.visible = False
            phaseIILeftBottom.visible = False
            phaseIIRightBottom.visible = False
            phaseIIBase.visible = False
            phaseIILeftLowerHalf.visible = False
            phaseIIRightLowerHalf.visible = False
            phaseIILowerDetails.visible = False
            phaseIIInner.visible = False
            labelP.value = 'Phase I'
            
            if (labelDecal.value == '              187th Trooper'):
                P1Trooper187th()
            if (labelDecal.value == '              212th Trooper'):
                P1Trooper212th()
            if (labelDecal.value == '              332nd Trooper'):
                showDecal('shiny')
                reset()
                invalid(11, "Invalid: Non-canon. 332nd Troopers were made after Phase II.")
                labelDecal.value = '              332nd Trooper'
            if (labelDecal.value == '              41st Trooper'):
                P1Trooper41st()
            if (labelDecal.value == '              501st Trooper'):
                P1Trooper501st()
            if (labelDecal.value == '              442nd Trooper'):
                P1Trooper442nd()
            if (labelDecal.value == '              327th Trooper'):
                P1Trooper327th()
            if (labelDecal.value == '              Coruscant Guard'):
                P1TrooperCoruscantGuard()
            if (labelDecal.value == '              91st Trooper'):
                Trooper91st()
            if (labelDecal.value == '              104th Trooper'):
                P1Trooper104th()
            if (labelDecal.value == '              Commander Appo'):
                P1Appo()
            if (labelDecal.value == '              Commander Bly'):
                P1Bly()
            if (labelDecal.value == '              Commander Cody'):
                P1Cody()
            if (labelDecal.value == '              Commander Doom'):
                showDecal('shiny')
                reset()
                invalid("", "Invalid: Non-canon.")
                labelDecal.value = '              Commander Doom'
            if (labelDecal.value == '                    Arc Trooper Echo'):
                P1Echo()
            if (labelDecal.value == '                    Arc Trooper Fives'):
                P1Fives()
            if (labelDecal.value == '              Commander Gree'):
                P1Gree()
            if (labelDecal.value == '                    Arc Trooper Hammer'):
                P1Hammer()
            if (labelDecal.value == '              Commander Jesse'):
                P1Jesse()
            if (labelDecal.value == '              Captain Keeli'):
                P1Keeli()
            if (labelDecal.value == '              Captain Lock'):
                P1Lock()
            if (labelDecal.value == '              Commander Neyo'):
                P1Neyo()
            if (labelDecal.value == '              Commander Ponds'):
                P1Ponds()
            if (labelDecal.value == '              Captain Rex'):
                P1Rex()
            if (labelDecal.value == '              Commander Stone'):
                P1Stone()
            if (labelDecal.value == '              Commander Thorn'):
                P1Thorn()
            if (labelDecal.value == '              Captain Vaughn'):
                invalid("", "Invalid: Non-canon.")
                reset()
                labelDecal.value = '              Captain Vaughn'
                showDecal('shiny')
            if (labelDecal.value == '              Commander Wolffe'):
                P1Wolffe()

    elif (key == '1'):                          
        if (labelP.value == 'Phase I'):
            P1Trooper187th()
        else:
            P2Trooper187th()
    elif (key == '2'):      
        if (labelP.value == 'Phase I'):
            P1Trooper212th()
        else:
            P2Trooper212th()
    elif (key == '3'):
        if (labelP.value == 'Phase I'):
            showDecal('shiny')
            reset()
            invalid(11, "Invalid: Non-canon. 332nd Troopers were made after Phase II.")
            labelDecal.value = '              332nd Trooper'
        else:
            P2Trooper332nd()
    elif (key == '4'):
        if (labelP.value == 'Phase I'):
            P1Trooper41st()
        else:
            P2Trooper41st()
    elif (key == '5'):
        if (labelP.value == 'Phase I'):
            P1Trooper501st()
        else:
            P2Trooper501st()
    elif (key == '6'):
        if (labelP.value == 'Phase I'):
            P1Trooper442nd()
        else:
            P2Trooper442nd()
    elif (key == '7'):
        if (labelP.value == 'Phase I'):
            P1Trooper327th()
        else:
            P2Trooper327th()
    elif (key == '8'):
        if (labelP.value == 'Phase I'):
            P1TrooperCoruscantGuard()
        else:
            P2TrooperCoruscantGuard()
    elif (key == '9'):
        Trooper91st()
    elif (key == '0'):
        if (labelP.value == 'Phase I'):
            P1Trooper104th()
        else:
            P2Trooper104th()
    
    elif (key == 'a'):
        if (labelP.value == 'Phase I'):  
            P1Appo()
        else:
            P2Appo()
    elif (key == 'b'):
        if (labelP.value == 'Phase I'):
            P1Bly()
        else:
            P2Bly()
    elif (key == 'c'):
        if (labelP.value == 'Phase I'):
            P1Cody()
        else:
            P2Cody()
    elif (key == 'd'):
        if (labelP.value == 'Phase I'):
            reset()
            invalid("", "Invalid: Non-canon")
            showDecal('shiny')
            labelDecal.value = '              Commander Doom'
        else:
            P2Doom()
    elif (key == 'e'):
        if (labelP.value == 'Phase I'):
            P1Echo()
        else:
            P2Echo()
    elif (key == 'f'):
        if (labelP.value == 'Phase I'):
            P1Fives()
        else:
            P2Fives()
    elif (key == 'g'):
        if (labelP.value == 'Phase I'):
            P1Gree()
        else:
            P2Gree()
    elif (key == 'h'):
        if (labelP.value == 'Phase I'):
            P1Hammer()
        else:
            P2Hammer()
    elif (key == 'i'):
        errorSound.stop()
        errorSound.play()
    elif (key == 'j'):
        if (labelP.value == 'Phase I'):
            P1Jesse()
        else:
            P2Jesse()
    elif (key == 'k'):
        if (labelP.value == 'Phase I'):
            P1Keeli()
        else:
            invalid("", "Invalid: Non-canon. Keeli died before Phase II.")
            reset()
            labelDecal.value = '              Captain Keeli'
            showDecal('shiny')
    elif (key == 'l'):
        if (labelP.value == 'Phase I'):
            P1Lock()
        else:
            P2Lock()
    elif (key == 'm'):
        errorSound.stop()
        errorSound.play()
    elif (key == 'n'):
        if (labelP.value =='Phase I'):
            P1Neyo()
        else:
            P2Neyo()
    elif (key == 'o'):
        errorSound.stop()
        errorSound.play()
    elif (key == 'p'):
        if (labelP.value =='Phase I'):
            P1Ponds()
        else:
            invalid("", "Invalid: Non-canon. Ponds died before Phase II.")
            reset()
            labelDecal.value = '              Commander Ponds'
            showDecal('shiny')
    elif (key == 'q'):
        errorSound.stop()
        errorSound.play()
    elif (key == 'r'):
        if (labelP.value =='Phase I'):
            P1Rex()
        else:
            P2Rex()
    elif (key == 's'):
        if (labelP.value == 'Phase I'):
            P1Stone()
        else:
            P2Stone()
    elif (key == 't'):
        if (labelP.value =='Phase I'):
            P1Thorn()
        else:
            P2Thorn()
    elif (key == 'u'):
        errorSound.stop()
        errorSound.play()
    elif (key == 'v'):
        if (labelP.value =='Phase I'):
            invalid("", "Invalid: Non-canon.")
            reset()
            labelDecal.value = '              Captain Vaughn'
            showDecal('shiny')
        else:
            P2Vaughn()
    elif (key == 'w'):
        if (labelP.value =='Phase I'):
            P1Wolffe()
        else:
            P2Wolffe()
    elif (key == 'x'):
        errorSound.stop()
        errorSound.play()
    elif (key == 'y'):
        errorSound.stop()
        errorSound.play()
    elif (key == 'z'):
        errorSound.stop()
        errorSound.play()
    elif (key == 'backspace'):
        showDecal('shiny')
        reset()
        invalid("", "")
        labelDecal.value = "Grunt"
        changeLogo(logoRepublic)
        
    elif (key == 'enter'):  
        list.visible = True
        list.opacity = 0
        vignette.toFront()
        list.toFront()
        listSound.stop()
        listSound.play()
        list.shown = True
        vignette.shown = True
        
    labelP.toFront()
    labelDecal.toFront()
        
def onKeyRelease(key):
    if (key == 'enter'):
        list.shown = False
        vignette.shown = False

cursor = Rect(1,1,1,1, visible=False)
def onMouseMove(x, y):
    cursor.centerX=x
    cursor.centerY=y

    cursorLabel.centerX = x - 20
    cursorLabel.centerY = y + 20
    
    if (cursor.hitsShape(musicIcon)==True):
        cursorLabel.shown = True
        cursorLabelLabel.value = "Music"
    elif (cursor.hitsShape(backgroundIcon)==True):
        cursorLabel.shown = True
        cursorLabelLabel.value = "Background"
    elif (cursor.hitsShape(infoIcon)==True):
        cursorLabel.shown = True
        cursorLabelLabel.value = "Info"
    else:
        cursorLabel.shown = False

def onMousePress(mouseX, mouseY):
    if (startInfo.visible == True):
        startInfo.shown = False
        
    if (cursor.hitsShape(musicIcon)==True):
        musicUI.shown=True
        vignette.shown = True
        musicUILabel.shown=True
        vignette.toFront()
        musicUI.toFront()
        musicUILabel.toFront()
        listSound.stop()
        listSound.play()
    if (musicUI.shown==True):
    
        if (cursor.hitsShape(musicUIX)==True):    
            musicUI.shown=False
            musicUILabel.shown=False
            vignette.shown=False
        elif (cursor.hitsShape(musicUILeft)==True):
            musicUILabel.size=14
            musicUILabel.opacity=0
            musicUILabel.song -= 1
            changeMusic()
        
        elif (cursor.hitsShape(musicUIRight)==True):
            musicUILabel.size=14
            musicUILabel.opacity=0
            musicUILabel.song += 1
            changeMusic()


    if (cursor.hitsShape(backgroundIcon)==True):
        backgroundUI.shown=True
        vignette.shown = True
        backgroundUILabel.shown=True
        vignette.toFront()
        backgroundUI.toFront()
        backgroundUILabel.toFront()
        listSound.stop()
        listSound.play()
    if (backgroundUI.shown==True):
    
        if (cursor.hitsShape(backgroundUIX)==True):    
            backgroundUI.shown=False
            backgroundUILabel.shown=False
            vignette.shown=False
        elif (cursor.hitsShape(backgroundUILeft)==True):
            backgroundUILabel.opacity=0
            backgroundUILabel.image -= 1
            changeBackground()
        
        elif (cursor.hitsShape(backgroundUIRight)==True):
            backgroundUILabel.opacity=0
            backgroundUILabel.image += 1
            changeBackground()

    if (cursor.hitsShape(infoIcon)==True):
        vignette.shown=True
        vignette.toFront()
        infoUI.shown=True
        infoUI.toFront()
        infoLabel1.toFront()
        infoLabel2.toFront()
        infoLabel3.toFront()
        infoLabel4.toFront()
        infoLabel5.toFront()
        listSound.stop()
        listSound.play()

    if (infoUI.shown==True):
    
        if (cursor.hitsShape(infoUIX)==True):    
            infoUI.shown=False
            infoLabel1.shown=False
            infoLabel2.shown=False
            infoLabel3.shown=False
            infoLabel4.shown=False
            infoLabel5.shown=False
            vignette.shown=False

cmu_graphics.run()
