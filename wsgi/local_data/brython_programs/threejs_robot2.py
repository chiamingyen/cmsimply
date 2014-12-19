from browser import document as doc
from browser import window
from javascript import JSConstructor
import math

canvasWidth = window.innerWidth
canvasHeight = window.innerHeight
canvasRatio = canvasWidth/canvasHeight
#print(canvasWidth, canvasHeight, canvasRatio)

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

# materialC
materialC = JSConstructor(window.THREE.MeshPhongMaterial )
robotBaseMaterial  = materialC({"color": 0x6E23BB, "specular": 0x6E23BB, "shininess": 20})
robotForearmMaterial = materialC({"color": 0xF4C154, "specular": 0xF4C154, "shininess": 100})
robotUpperArmMaterial = materialC({"color": 0x95E4FB, "specular": 0x95E4FB, "shininess": 100})

torusgeometryC = JSConstructor(window.THREE.TorusGeometry)
torusgeometry = torusgeometryC(22, 15, 32, 32)

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
print(arm.position.x)
print(arm.position.y)
arm.position.y = -100
scene.add(arm)

rendererC = JSConstructor(window.THREE.CanvasRenderer)
renderer = rendererC({ "antialias": True } )
renderer.gammaInput = True
renderer.gammaOutput = True
renderer.setSize(canvasWidth, canvasHeight)

doc <= renderer.domElement
renderer.render( scene, camera )

def animate(i):
    window.requestAnimationFrame( animate )
    forearm.rotation.y += 0.1
    forearm.rotation.z += 0.1
    renderer.render( scene, camera )  
animate(0)
