import Doors
import Levers
import Locks
import Objects
import Sounds
import Sparks
import darfuncs
import Stars

# DOORS
# First sound - door opening
# Second sound - door closing
snd_doorslidewood = Sounds.CreateEntitySound("..\\..\\Sounds\\puerta-madera-deslizando.wav","WoodDoorSlide")
snd_doorhitwood = Sounds.CreateEntitySound("..\\..\\Sounds\\puerta-madera-golpe.wav","WoodDoorHit")

# Minotaur door
door1 = Doors.CreateDoor("Door1", (-6750, 0, 0), (0, 1, 0), 500, 4000, Doors.CLOSED)
door1.opentype = Doors.UNIF
door1.o_med_vel = -750
door1.o_med_displ = 3500
door1.closetype = Doors.AC
door1.c_init_displ = 3500
door1.c_med_vel = 1500
# assign the sounds you defined above
door1.SetWhileOpenSound(snd_doorslidewood)
door1.SetWhileCloseSound(snd_doorslidewood)
door1.SetEndOpenSound(snd_doorhitwood)
door1.SetEndCloseSound(snd_doorhitwood)

# Escape door
door2 = Doors.CreateDoor("Door2",(22750, 0, 0),(0,1,0),500,4000, Doors.CLOSED)
door2.opentype = Doors.UNIF
door2.o_med_vel = -750
door2.o_med_displ = 3500
door2.closetype = Doors.AC
door2.c_init_displ = 3500
door2.c_med_vel = 3000
# assign the sounds you defined above
door2.SetWhileOpenSound(snd_doorslidewood)
door2.SetWhileCloseSound(snd_doorslidewood)
door2.SetEndOpenSound(snd_doorhitwood)
door2.SetEndCloseSound(snd_doorhitwood)

# Ending door
endDoor = Doors.CreateDoor("EndDoor",(70750, -2900, 0), (0, 1, 0), 500, 4000, Doors.CLOSED)
endDoor.opentype = Doors.UNIF
endDoor.o_med_vel = -750
endDoor.o_med_displ = 3500
endDoor.closetype = Doors.AC
endDoor.c_init_displ = 3500
endDoor.c_med_vel = 3000
# assign the sounds you defined above
endDoor.SetWhileOpenSound(snd_doorslidewood)
endDoor.SetWhileCloseSound(snd_doorslidewood)
endDoor.SetEndOpenSound(snd_doorhitwood)
endDoor.SetEndCloseSound(snd_doorhitwood)


# GATES
snd_slidegate = Sounds.CreateEntitySound("..\\..\\Sounds\\rastrillo.wav", "GateSlideSound")
snd_slidegate.MaxDistance = 20000
snd_slidegate.MinDistance = 2000

snd_hitgate = Sounds.CreateEntitySound("..\\..\\Sounds\\golpe-metal-mediano.wav", "GateHitSound")
snd_hitgate.MaxDistance = 20000
snd_hitgate.MinDistance = 2000

# Boss gate
bossGate = Bladex.CreateEntity("BossGate", "Rastrillo10", 6750, -2900, 0, "Physic")
bossGate.Scale = 1.0
bossGate.Orientation = 0.5, 0.5, -0.5, 0.5
bossGate.Frozen = 1
bossGate = Sparks.SetMetalSparkling(bossGate.Name) # This makes sparks if you hit the gate.
bossGateObj = Objects.CreateDinamicObject(bossGate.Name) # Assigns data to handle moving.

# Trap line gate
trapsGate = Bladex.CreateEntity("TrapsGate", "Rastrillo10", 45000, -2900, 0, "Physic")
trapsGate.Scale = 1.0
trapsGate.Orientation = 0.5, 0.5, -0.5, 0.5
trapsGate.Frozen = 1
trapsGate = Sparks.SetMetalSparkling(trapsGate.Name) # This makes sparks if you hit the gate.
trapsGateObj = Objects.CreateDinamicObject(trapsGate.Name) # Assigns data to handle moving.


"""
(0.5, 0.5, 0.5, -0.5) # to face west
(0.5, 0.5, -0.5, 0.5) # east
(0.0, 0.0, 0.5, -0.5) # north
(0.707, 0.707, 0.0, 0.0) # south
"""

# Minotaur Lock
minoLock = Locks.PlaceLock("MinoLock", "Cerraduracutre", (-5980, -1000, 2500), (0.707, 0.707, 0.0, 0.0), 1.6)
minoLock.key = "Minokey"
darfuncs.SetHint(minoLock.obj, "Great Lock")
minoLock.OnUnLockFunc = MinoGate
minoLock.OnUnLockArgs = ()

# Boss Gate Lever
bossGateLever = Levers.PlaceLever("BossGateLever", Levers.LeverType3, (7350, -1000, 2250) ,(0.5, 0.5, -0.5, 0.5), 0.8)
bossGateLever.mode = 1
bossGateLever.OnTurnOnFunc=OpenBossGate
bossGateLever.OnTurnOnArgs=(bossGateObj,)

# Dull lever in spike room
dullLever = Levers.PlaceLever("DullLever", Levers.LeverType3, (24500, -1000, -2150),( 0.0, 0.0, 0.5, -0.5), 0.8)
dullLever.mode = 1
# Purtcullis lever in spike room
portLever = Levers.PlaceLever("TrapsGateLever", Levers.LeverType3, (43750, -1000, 2150) ,(0.707, 0.707, 0.0, 0.0), 0.8)
portLever.mode = 1
portLever.OnTurnOnFunc = StopTrapLine
portLever.OnTurnOnArgs = ()

# Ending door lever
endDoorLever = Levers.PlaceLever("EndDoorLever", Levers.LeverType3, (69900, -1000, -3000) ,(0.5, 0.5, 0.5, -0.5), 0.8)
endDoorLever.mode = 1
endDoorLever.OnTurnOnFunc = StartEndScene
endDoorLever.OnTurnOnArgs = ()