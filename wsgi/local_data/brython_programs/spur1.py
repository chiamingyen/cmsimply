from javascript import JSConstructor
import math
 
cango = JSConstructor(window.Cango2D)
shapes2d = window.shapes2D
#tweener = JSConstructor(Tweener)
#drag2d = JSConstructor(Drag2D)
#svgtocgo2d = JSConstructor(svgToCgo2D)
#involutebezcoeffs = JSConstructor(involuteBezCoeffs)
creategeartooth = JSConstructor(window.createGearTooth)
#createintgeartooth= JSConstructor(createIntGearTooth)

cgo = cango("plotarea")

module = 3
teeth = 17
pressureAngle = 25

######################################
# 畫正齒輪輪廓
#####################################
'''
Rpitch = module*teeth/2
# base circle radius
Rb = Rpitch * math.cos(pressureAngle*math.pi/180)
print("基圓半徑:", Rb)
#generate Higuchi involute approximation
fs = 0.01  # start 1% off the base circle
fm = 0.25  # break 25% along involute
fe = 1     #end at 100%
dedBz = involutebezcoeffs(module, teeth, pressureAngle, 3, fs, fm)
addBz = involutebezcoeffs(module, teeth, pressureAngle, 3, fm, fe)
print(dedBz[0].x, addBz[3].x)
data = ["M", dedBz[0].x, dedBz[0].y, "C", \
    dedBz[1].x, dedBz[1].y, dedBz[2].x, dedBz[2].y, \
    dedBz[3].x, dedBz[3].y, "C", addBz[1].x, addBz[1].y, \
    addBz[2].x, addBz[2].y, addBz[3].x, addBz[3].y]
# draw the involute using Cango library
gear = cgo.drawPath(data, -Rpitch, 100, 'blue', 21)
'''

m = module # Module = mm of pitch diameter per tooth
Zg = teeth
phi = pressureAngle
Rg = Zg*m/2 # gear Pitch radius
scale = 10
# generate gear
data = creategeartooth(m, Zg, phi)
gearTooth = cgo.compileShape(data, '#ddd0dd', '#606060', scale)
gearTooth.rotate(180/Zg) # rotate gear 1/2 tooth to mesh
gear = gearTooth.dup()
#cgo.render(gearTooth)

for i in range(1, Zg):
    newTooth = gearTooth.dup()
    newTooth.rotate(360*i/Zg)
    gear.appendPath(newTooth, True) # trim move command = true

# add axle hole
Dsg = 0.6*Rg # diameter of gear shaft
shaft = cgo.compilePath(shapes2d.circle)
shaft.scale(Dsg*scale)
shaft.revWinding()
gear.appendPath(shaft) # retain the 'moveTo' command for shaft sub path
gear.translate(300, 300)
cgo.render(gear)