import AniSound
import Reference
import Basic_Funcs
import Sparks
import Breakings
import ItemTypes

char=Bladex.CreateEntity("Player1","Knight_N",-10000,-1100,-9500,"Person")
char.Angle=-90.0	
char=Bladex.GetEntity("Player1")
char.Data=Basic_Funcs.PlayerPerson(char)
AniSound.AsignarSonidosCaballero('Player1')

char.SendTriggerSectorMsgs=1

inv=char.GetInventory()

PlayerShield=Bladex.CreateEntity("PlayerShield","Escudo2",0,0,0,"Weapon")
Sparks.MakeShield("PlayerShield")
PlayerShield.Scale=1.000000
ItemTypes.ItemDefaultFuncs(PlayerShield)
inv.AddShield("PlayerShield")
inv.LinkLeftHand("PlayerShield")

PlayerSword=Bladex.CreateEntity("PlayerSword","Gladius",0,0,0,"Weapon")
PlayerSword.Scale=1.000000
inv.AddWeapon("PlayerSword")
inv.LinkRightHand("PlayerSword")

