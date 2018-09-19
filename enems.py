import Bladex
import Reference
import EnemyTypes
import Actions
import darfuncs
import pocimac
from math import pow

knightBoss=Bladex.CreateEntity("KnightBoss", "Knight_Traitor", -5000, -1100, 3750, "Person")
knightBoss.Freeze()
knightBoss.Angle = 180
knightBoss.Level = 1
knightBoss.Life = 30.0
# Creating sword, shield and potion
BossSword=Bladex.CreateEntity("BossSword", "Gladius", 0, 0, 0, "Weapon")
BossSword.Scale = 1.000000
BossShield=Bladex.CreateEntity("BossShield", "Escudo2", 0, 0, 0, "Weapon")
BossShield.Scale = 1.000000
ItemTypes.ItemDefaultFuncs(BossShield)
potion=Bladex.CreateEntity("BossPotion", "Pocima25", 0, 0, 0)
potion.Static = 0
potion.Solid = 0
potion.Scale = 1.25
pocimac.CreatePotion("BossPotion")
# Make him take it
Actions.TakeObject("KnightBoss", "BossShield")
Actions.TakeObject("KnightBoss", "BossSword")
Actions.TakeObject("KnightBoss", "BossPotion")
# Assigning the zones
knightBoss.ActionAreaMin = pow(2,0) # Prim
knightBoss.ActionAreaMax = pow(2,1)  # Sec
# Enabling the char
EnemyTypes.EnemyDefaultFuncs(knightBoss)
# Putting the char on floor
knightBoss.SetOnFloor()
# Assigning a cutscene function for death
knightBoss.Data.DefImDeadFunc = knightBoss.ImDeadFunc
knightBoss.ImDeadFunc = StartCutScene3
# Hiding
darfuncs.HideBadGuy("KnightBoss")

# Creating mino key
minokey = Bladex.CreateEntity("Minokey", "Llavecutre", 0, 0, 0, "Physic")
minokey.Data = darfuncs.EmptyClass()
minokey.Data.Used = 10
minokey.Scale = 1.2 
darfuncs.SetHint(minokey,"Knight Key")
Actions.TakeObject("KnightBoss", "Minokey")

knightEnem1 = Bladex.CreateEntity("KnightEnem1", "Knight_Traitor", 7750, -1000, 3000, "Person")
knightEnem1.Angle = -1.8
knightEnem1.Level = 0
knightEnem1.Life = 10.0
# Sword and shield
KnightSword1 = Bladex.CreateEntity("KnightSword1", "Gladius", 0, 0, 0, "Weapon")
KnightSword1.Scale = 1.000000
KnightShield1 = Bladex.CreateEntity("KnightShield1", "Escudo5", 0, 0, 0, "Weapon")
KnightShield1.Scale = 1.000000
ItemTypes.ItemDefaultFuncs(KnightShield1)
# Make him to take them
Actions.TakeObject("KnightEnem1", "KnightShield1")
Actions.TakeObject("KnightEnem1", "KnightSword1")
# Define the zones
knightEnem1.ActionAreaMin = pow(2,2) # Prim
knightEnem1.ActionAreaMax = pow(2,3)  # Sec
EnemyTypes.EnemyDefaultFuncs(knightEnem1)
knightEnem1.SetOnFloor()

knightEnem2 = Bladex.CreateEntity("KnightEnem2", "Knight_Traitor", 11500, -1000, -2000, "Person")
knightEnem2.Angle = 1.35
knightEnem2.Level = 0
knightEnem2.Life = 10.0
# Sword and shield
KnightSword2 = Bladex.CreateEntity("KnightSword2", "Gladius", 0, 0, 0, "Weapon")
KnightSword2.Scale = 1.000000
KnightShield2 = Bladex.CreateEntity("KnightShield2", "Escudo5", 0, 0, 0, "Weapon")
KnightShield2.Scale = 1.000000
ItemTypes.ItemDefaultFuncs(KnightShield2)
# Make him to take them
Actions.TakeObject("KnightEnem2", "KnightShield2")
Actions.TakeObject("KnightEnem2", "KnightSword2")
# Define the zones
knightEnem2.ActionAreaMin = pow(2,2) # Prim
knightEnem2.ActionAreaMax = pow(2,3)  # Sec
EnemyTypes.EnemyDefaultFuncs(knightEnem2)
knightEnem2.SetOnFloor()

mino = Bladex.CreateEntity("Mino", "Minotaur",-10750, -1000, 0, "Person")
mino.Level = 0
mino.Angle = -90
mino.Deaf = 1
mino.Blind = 1
minoBlade = Bladex.CreateEntity("MinoBlade", "Hachacarnicero", 0, 0, 0, "Weapon")
Actions.TakeObject("Mino", "MinoBlade")
mino.ActionAreaMin = pow(2,4) # Prim
mino.ActionAreaMax = pow(2,5)  # Sec
mino.SetOnFloor()