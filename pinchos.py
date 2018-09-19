import Bladex
import Ontake

MESSAGE_START_WEAPON=7

#SOUNDS
sonidoroturahueco = Bladex.CreateSound("..\\..\\Sounds\\single-boulder-impact.wav", "SonidoRoturaHueco")
sonidopinchosaliendo = Sounds.CreateEntitySound("..\\..\\Sounds\\blunt-impact3.wav", "SonidoPinchoSaliendo")
pinchosgolpeando1 = Sounds.CreateEntitySound("..\\..\\Sounds\\golpe-metal-mediano.wav", "PinchosGolpeando1")

#PINCHOS
pincho1 = Bladex.CreateEntity("Pincho1", "PinchoManuel", 28500, 1600, 1500, "Weapon")
pincho1.Scale = 1.6
pincho1.Orientation= 0.632, 0.316, 0.316, 0.632
pincho1.Frozen = 1
pincho1.Solid = 1
pincho1obj = Objects.CreateDinamicObject ("Pincho1")

pincho2 = Bladex.CreateEntity("Pincho2", "PinchoManuel", 28500, 1600, 0, "Weapon")
pincho2.Scale = 1.6
pincho2.Orientation= 0.632, 0.316, 0.316, 0.632
pincho2.Frozen = 1
pincho2.Solid = 1
pincho2obj = Objects.CreateDinamicObject ("Pincho2")

pincho3 = Bladex.CreateEntity("Pincho3", "PinchoManuel", 28500, 1600, -1500, "Weapon")
pincho3.Scale = 1.6
pincho3.Orientation= 0.632, 0.316, 0.316, 0.632
pincho3.Frozen = 1
pincho3.Solid = 1
pincho3obj = Objects.CreateDinamicObject ("Pincho3")

pincho4 = Bladex.CreateEntity("Pincho4", "PinchoManuel", 32000, 1600, 1500, "Weapon")
pincho4.Scale = 1.6
pincho4.Orientation= 0.632, 0.316, 0.316, 0.632
pincho4.Frozen = 1
pincho4.Solid = 1
pincho4obj = Objects.CreateDinamicObject ("Pincho4")

pincho5 = Bladex.CreateEntity("Pincho5", "PinchoManuel", 32000, 1600, 0, "Weapon")
pincho5.Scale = 1.6
pincho5.Orientation= 0.632, 0.316, 0.316, 0.632
pincho5.Frozen = 1
pincho5.Solid = 1
pincho5obj = Objects.CreateDinamicObject ("Pincho5")

pincho6 = Bladex.CreateEntity("Pincho6", "PinchoManuel", 32000, 1600, -1500, "Weapon")
pincho6.Scale = 1.6
pincho6.Orientation= 0.632, 0.316, 0.316, 0.632
pincho6.Frozen = 1
pincho6.Solid = 1
pincho6obj = Objects.CreateDinamicObject ("Pincho6")