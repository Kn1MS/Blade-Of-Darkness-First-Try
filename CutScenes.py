import AbreCam
import Bladex

# Starting cut-scene
def CutScene1():
    AbreCam.ResetNode()
    AbreCam.AddNode((2154, -3317, -11282), (10559, -797, -6485), 3)
    AbreCam.AddNode((10479, -3175, -6278), (9512, -593, 2935), 3)
    AbreCam.AddNode((11515, -3039, 847), (2069, -175, -758), 3)
    AbreCam.AddNode((427, -2627, 1614), (-8993, -752, -1172), 4)
    AbreCam.AddNode((427, -2627, 1614), (-8993, -752, -1172), 2)
    AbreCam.LastTime = 0
    AbreCam.AbreCam()

# Beginning of the boss fight
def CutScene2():
	AbreCam.ResetNode()
	AbreCam.AddNode((2467, -3366, 85), (-7355, -1492, -34), 1)
	AbreCam.AddNode((805, -3714, -2879), (-6952, -291, 1997), 3)
	AbreCam.AddNode((-5186, -4321, -2044), (2082, 907, 2410), 2)
	AbreCam.AddNode((-5186, -4321, -2044), (2082, 907, 2410), 2)
	AbreCam.LastTime = 0
	AbreCam.AbreCam()


# After killing the boss
def CutScene3():
    AbreCam.ResetNode()
    AbreCam.AddNode((-486, -3001, -100), (-10105,-463, -1759), 2)
    AbreCam.AddNode((-4970, -1257, 3327), (-11017, 504, -4602), 3)
    AbreCam.AddNode((-4970, -1257, 3327), (-11017, 504, -4602), 2)
    AbreCam.AddNode((-5837, -2762, -1552), (3702, -1281, 1059), 3)
    AbreCam.AddNode((17829, -2667, -952), (27524, -1371, 1130), 5)
    AbreCam.LastTime=0
    AbreCam.AbreCam()

# Getting into trap room
def CutScene4():
    AbreCam.ResetNode()
    AbreCam.AddNode ((36701, -3084, -1164), (27788, 979, 848), 2)
    AbreCam.AddNode ((36701, -3084, -1164), (27788, 979, 848), 3)
    AbreCam.AddNode ((23720, -3254, 307), (33239, -195, 94), 2)
    AbreCam.LastTime=0
    AbreCam.AbreCam()

# Ending
def CutScene5():
    AbreCam.ResetNode() 
    AbreCam.AddNode ((64788, -607, -1393), (74308, -2569, -954), 0)
    AbreCam.AddNode ((64788, -607, -1393), (74308, -2569, -954), 8)
    AbreCam.LastTime=0
    AbreCam.AbreCam()

