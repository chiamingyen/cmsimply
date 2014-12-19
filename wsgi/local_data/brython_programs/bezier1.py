from javascript import JSConstructor
 
cango = JSConstructor(window.Cango2D)
shapes2d = window.shapes2D
tweener = JSConstructor(window.Tweener)
drag2d = JSConstructor(window.Drag2D)
svgtocgo2d = JSConstructor(window.svgToCgo2D)
cgo = cango("plotarea")

Triangle = "M 100 100 L 300 100 L 200 300 z"
CubicBezier = "M100,200 C100,100 250,100 250,200 S400,300 400,200"
QuadBezier2 = "M200,300 Q400,50 600,300 T1000,300"
Arc1 = "M300,200 h-150 a150,150 0 1,0 150,-150 z"
Arc2 = "M275,175 v-150 a150,150 0 0,0 -150,150 z"
Arc3 = "M600,350 l 50,-25a25,25 -30 0,1 50,-25 l 50,-25 \
  a25,50 -30 0,1 50,-25 l 50,-25a25,75 -30 0,1 50,-25 l 50,-25 \
  a25,100 -30 0,1 50,-25 l 50,-25"

cgo.clearCanvas("cornsilk")
cgo.setWorldCoords(0, 0, 1000)

triData = svgtocgo2d(Triangle)
tri = cgo.compileShape(triData, 'red')
tri.translate(100, 950)
cgo.render(tri)
cBezData = svgtocgo2d(CubicBezier)
cBez = cgo.compilePath(cBezData, 'red')
cBez.translate(400, 1000)
cgo.render(cBez)
qBezData = svgtocgo2d(QuadBezier2)
qBez = cgo.compilePath(qBezData, 'red')
qBez.translate(-100, 750)
cgo.render(qBez)
a1Data = svgtocgo2d(Arc1)
a1 = cgo.compileShape(a1Data, 'red', 'blue')
a1.translate(50, 400)
cgo.render(a1)
a2Data = svgtocgo2d(Arc2)
a2 = cgo.compileShape(a2Data, "yellow", "blue")
a2.translate(50, 400)
cgo.render(a2)
a3Data = svgtocgo2d(Arc3)
a3 = cgo.compilePath(a3Data, 'red')
a3.translate(-100, 400)
cgo.render(a3)