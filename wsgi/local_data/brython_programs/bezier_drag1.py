from javascript import JSConstructor
 
cango = JSConstructor(window.Cango2D)
shapes2d = window.shapes2D
tweener = JSConstructor(window.Tweener)
drag2d = JSConstructor(window.Drag2D)
svgtocgo2d = JSConstructor(window.svgToCgo2D)
cgo = cango("plotarea")
x1, y1 = 40, 20
cx1, cy1 = 90, 120
x2, y2 = 120, 100
cx2, cy2 = 130, 20
cx3, cy3 = 150, 120
x3, y3 = 180, 60

#called in scope of dragNdrop obj
def dragC1(mousePos):
    global cx1, cy1
    cx1 = mousePos.x
    cy1 = mousePos.y
    drawCurve()

def dragC2(mousePos):
    global cx2, cy2
    cx2 = mousePos.x
    cy2 = mousePos.y
    drawCurve()

def dragC3(mousePos):
    global cx3, cy3
    cx3 = mousePos.x
    cy3 = mousePos.y
    drawCurve()

def drawCurve():
    # curve change shape so it must be re-compiled each time
    # draw a quadratic bezier from x1,y2 to x2,y2
    qbezdata = ['M', x1, y1, 'Q', cx1, cy1, x2, y2]
    qbez = cgo.compilePath(qbezdata, 'blue')
    cbezdata = ['M', x2, y2, 'C', cx2, cy2, cx3, cy3, x3, y3]
    cbez = cgo.compilePath(cbezdata, 'green')
    # show lines to control point
    data = ['M', x1, y1, 'L', cx1, cy1, x2, y2]
    # semi-transparent gray
    L1 = cgo.compilePath(data, "rgba(0, 0, 0, 0.2)")
    data = ['M', x2, y2, 'L', cx2, cy2]
    L2 = cgo.compilePath(data, "rgba(0, 0, 0, 0.2)")
    data = ['M', x3, y3, 'L', cx3, cy3]
    L3 = cgo.compilePath(data, "rgba(0, 0, 0, 0.2)")
    # draw draggable control points
    c1.transform.reset()
    c1.transform.translate(cx1, cy1)
    c2.transform.reset()
    c2.transform.translate(cx2, cy2)
    c3.transform.reset()
    c3.transform.translate(cx3, cy3)
    grp = cgo.createGroup2D(qbez, cbez, L1, L2, L3, c1, c2, c3)
    cgo.renderFrame(grp)

cgo.clearCanvas("lightyellow")
cgo.setWorldCoords(0, 0, 200)

# pre-compile the draggable control point
dragObj1 = drag2d(cgo, None, dragC1, None)
c1 = cgo.compileShape(shapes2d.circle, 'red', 'red', 4)
c1.enableDrag(dragObj1)
dragObj2 = drag2d(cgo, None, dragC2, None)
c2 = cgo.compileShape(shapes2d.circle, 'red', 'red', 4)
c2.enableDrag(dragObj2)
dragObj3 = drag2d(cgo, None, dragC3, None)
c3 = cgo.compileShape(shapes2d.circle, 'red', 'red', 4)
c3.enableDrag(dragObj3)

drawCurve()