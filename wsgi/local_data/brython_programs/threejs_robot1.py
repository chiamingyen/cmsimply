print('start ...')
from browser import document as doc
from browser import window
from javascript import JSConstructor
import math

gridX = True
gridY = False
gridZ = False
axes = True
ground = True
effectController = {}
canvasWidth = window.innerWidth
canvasHeight = window.innerHeight
canvasRatio = canvasWidth/canvasHeight
print("canvasWidth:", canvasWidth, "canvasHeight:", \
        canvasHeight, "canvasRatio:", canvasRatio)

# good
def createRobotExtender(part, length, material):
    cylindergeometryC = JSConstructor(window.THREE.CylinderGeometry)
    #CylinderGeometry(radiusTop, radiusBottom, height, radiusSegments, heightSegments, openEnded)
    cylindergeometry = cylindergeometryC(22, 22, 6, 32)
    meshC = JSConstructor(window.THREE.Mesh)
    cylinder = meshC(cylindergeometry, material)
    part.add(cylinder)
    for i in range(4):
        cubegeometryC = JSConstructor(window.THREE.CubeGeometry)
        #CubeGeometry(width, height, depth, widthSegments, heightSegments, depthSegments)
        cubegeometry = cubegeometryC(4, length, 4)
        meshC = JSConstructor(window.THREE.Mesh)
        box = meshC(cubegeometry, material)
        if i <2:
            box.position.x = -8
        else:
            box.position.x = 8
        box.position.y = length/2
        if i%2:
            box.position.z = -8
        else:
            box.position.z = 8
        part.add( box )

    cylindergeometry = cylindergeometryC(15, 15, 40, 32)
    meshC = JSConstructor(window.THREE.Mesh)
    cylinder = meshC(cylindergeometry, material)
    cylinder.rotation.x = 90 * math.pi/180
    cylinder.position.y = length
    part.add(cylinder)

# good
def createRobotCrane(part, length, material):
    cubegeometryC = JSConstructor(window.THREE.CubeGeometry)
    cubegeometry = cubegeometryC(18, length, 18)
    meshC = JSConstructor(window.THREE.Mesh)
    box = meshC(cubegeometry, material)
    box.position.y = length/2
    part.add(box)
    spheregeometryC = JSConstructor(window.THREE.SphereGeometry)
    #SphereGeometry(radius, widthSegments, heightSegments, phiStart, phiLength, thetaStart, thetaLength)
    spheregeometry = spheregeometryC(20, 32, 16)
    meshC = JSConstructor(window.THREE.Mesh)
    sphere = meshC(spheregeometry, material)
    # place sphere at end of arm
    sphere.position.y = length
    part.add(sphere)

def setupGui():
    global effectController
    effectController = {
        "newGridX": gridX,
        "newGridY": gridY,
		"newGridZ": gridZ,
		"newGround": ground,
		"newAxes": axes,
		
		"uy": 70.0,
		"uz": -15.0,

		"fy": 10.0,
		"fz": 60.0
	}
    guiC = JSConstructor(dat.GUI)
    gui = guiC()
    h = gui.addFolder("Grid display")
    h.add(effectController, "newGridX").name("Show XZ grid")
    h.add(effectController, "newGridY" ).name("Show YZ grid")
    h.add(effectController, "newGridZ" ).name("Show XY grid")
    h.add(effectController, "newGround" ).name("Show ground")
    h.add(effectController, "newAxes" ).name("Show axes")
    '''
    h = gui.addFolder("Arm angles")
    h.add(effectController, "uy", list(range(-180, 180, 1))).name("Upper arm y")
    h.add(effectController, "uz", -45.0, 45.0, 0.025).name("Upper arm z")
    h.add(effectController, "fy", -180.0, 180.0, 0.025).name("Forearm y")
    h.add(effectController, "fz", -120.0, 120.0, 0.025).name("Forearm z")
    '''
# camera
cameraC = JSConstructor( window.THREE.PerspectiveCamera )
camera = cameraC( 30, canvasRatio, 1, 10000 )
camera.position.z = 500
#camera.position.set( -510, 240, 1000 )

sceneC = JSConstructor( window.THREE.Scene );
scene = sceneC();

# LIGHTS
ambientlightC = JSConstructor(window.THREE.AmbientLight)
ambientLight = ambientlightC(0x222222)
lightC = JSConstructor(window.THREE.DirectionalLight)
light = lightC(0xffffff, 1.0)
light.position.set( 200, 400, 500 );

light2C = JSConstructor(window.THREE.DirectionalLight)
light2 = light2C(0xffffff, 1.0)
light2.position.set( -500, 250, -200 )

scene.add(ambientLight)
scene.add(light)
scene.add(light2)

'''
geometryC = JSConstructor(window.THREE.CubeGeometry)
geometry = geometryC(20, 20, 20)
materialC = JSConstructor( window.THREE.MeshBasicMaterial )

material = materialC( { "color": "#ff0000", "wireframe": True } )

meshC = JSConstructor(window.THREE.Mesh)
mesh = meshC(geometry, material)
scene.add(mesh);
'''

# materialC
materialC = JSConstructor(window.THREE.MeshPhongMaterial )
robotBaseMaterial  = materialC({"color": 0x6E23BB, "specular": 0x6E23BB, "shininess": 20})
robotForearmMaterial = materialC({"color": 0xF4C154, "specular": 0xF4C154, "shininess": 100})
robotUpperArmMaterial = materialC({"color": 0x95E4FB, "specular": 0x95E4FB, "shininess": 100})

torusgeometryC = JSConstructor(window.THREE.TorusGeometry)
torusgeometry = torusgeometryC(22, 15, 32, 32)

# torus
'''
meshC = JSConstructor(window.THREE.Mesh)
torus = meshC(torusgeometry, robotBaseMaterial)
scene.add(torus)
'''

# forearm
object3DC = JSConstructor(window.THREE.Object3D)
forearm = object3DC()
faLength = 80
createRobotExtender(forearm, faLength, robotForearmMaterial)

arm = object3DC()
uaLength = 120
createRobotCrane(arm, uaLength, robotUpperArmMaterial)

# Move the forearm itself to the end of the upper arm.
forearm.position.y = uaLength
arm.add(forearm)
print("arm.position.x:", arm.position.x)
print("arm.position.y:", arm.position.y)
#arm.position.x = -50
arm.position.y = -100
scene.add(arm)

rendererC = JSConstructor(window.THREE.CanvasRenderer)
renderer = rendererC({ "antialias": True } )
renderer.gammaInput = True
renderer.gammaOutput = True
renderer.setSize(canvasWidth, canvasHeight)
#renderer.setClearColorHex( 0xAAAAAA, 1.0 )


doc <= renderer.domElement
renderer.render( scene, camera )

def animate(i):
    # note: window.THREE.js includes requestAnimationFrame shim
    window.requestAnimationFrame( animate )

    #mesh.rotation.x += 0.05
    #mesh.rotation.y += 0.1
    doc["console"].value = ""
    print("forearm.rotation.z:", forearm.rotation.z)
    print("forearm.rotation.y:", forearm.rotation.y)
    forearm.rotation.y += 0.1
    forearm.rotation.z += 0.1

    renderer.render( scene, camera )  

#setupGui()
animate(0)
