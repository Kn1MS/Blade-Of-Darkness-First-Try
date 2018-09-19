import Bladex
import GameText
import darfuncs
import Sounds
import Objects
import AuxFuncs
import Actions
import Scorer

GameText.MapList['FIRSTMAP'] = 'FirstMap'
CurrentMusic = "" # declare a variable and assign and empty string ""
Bladex.SetSun(1,-10,21,4)

def UnhideBoss(sector,entity):
    # Checking whether it's the player
    if entity == "Player1":
        darfuncs.UnhideBadGuy("KnightBoss")
        sect_knight.OnEnter = None
    else:
        pass

def StartMusic():
	Bladex.ExeMusicEvent(Bladex.GetMusicEvent("Atmos24"))

def ChangeMusic(music):
    Bladex.KillMusic()
    Bladex.ExeMusicEvent(Bladex.GetMusicEvent(music))
    global CurrentMusic
    CurrentMusic = music

def ResumeMusic():
    global CurrentMusic
    Bladex.KillMusic()
    if CurrentMusic != "": 
         Bladex.ExeMusicEvent(Bladex.GetMusicEvent(CurrentMusic))

def StopMusic():
    global CurrentMusic
    Bladex.KillMusic()
    CurrentMusic=""

# Crow sound on the map
snd_crow1 = Sounds.CreatePeriodicSound("..\\..\\sounds\\raven-call.wav","SoundCrow1",20,8,(14000,-4000,0))
snd_crow1.sound.Volume=1.0
snd_crow1.MinDistance=5000
snd_crow1.MaxDistance=14000
snd_crow1.sound.BaseVolume=1.0
snd_crow1.sound.SendNotify=0
snd_crow1.PlayPeriodic()

##################################################################################################################
#### SPIKE TRAP ####
####################
PinchosActivated = 0

def ActivatePinchos():
    global PinchosActivated
    PinchosActivated = 1
    PinchoGetUp(pincho1obj, pincho1)
    Bladex.AddScheduledFunc(Bladex.GetTime()+0.2, PinchoGetUp, (pincho2obj, pincho2))
    Bladex.AddScheduledFunc(Bladex.GetTime()+0.4, PinchoGetUp, (pincho3obj, pincho3))
    Bladex.AddScheduledFunc(Bladex.GetTime()+0.6, PinchoGetUp, (pincho4obj, pincho4))
    Bladex.AddScheduledFunc(Bladex.GetTime()+0.8, PinchoGetUp, (pincho5obj, pincho5))
    Bladex.AddScheduledFunc(Bladex.GetTime()+1, PinchoGetUp, (pincho6obj, pincho6))

def DeactivatePinchos():
    global PinchosActivated
    PinchosActivated = 0

def PinchoGetDown(pinchoobj, pinchovar):
    displacement = (1150, 1150)
    vectors = (0.0, 1.0, 0.0), (0.0, 1.0, 0.0)
    vel_init = (15000, 15000)
    vel_fin = (15000, 15000)
    whilesnd = ("", "")
    endsnd = ("", "")
    Objects.NDisplaceObject(pinchoobj, displacement, vectors, vel_init, vel_fin, (), whilesnd, endsnd)
    Bladex.AddScheduledFunc(Bladex.GetTime()+1, PinchoGetUp, (pinchoobj, pinchovar))

def PinchoGetUp(pinchoobj, pinchovar):
    global PinchosActivated
    if PinchosActivated == 1:
        displacement = (1150, 1150) # Displacement of the Pincho (2300 total)
        vectors = (0.0, -1.0, 0.0), (0.0, -1.0, 0.0)
        vel_init = (15000, 15000) # Initial speed of movement
        vel_fin = (15000, 15000) # Final speed of movement
        whilesnd = (sonidopinchosaliendo, "") # While sound
        endsnd = ("", pinchosgolpeando1) # End sound
        pinchovar.MessageEvent(MESSAGE_START_WEAPON,0,0)
        Objects.NDisplaceObject(pinchoobj, displacement, vectors, vel_init, vel_fin, (), whilesnd, endsnd)
        Bladex.AddScheduledFunc(Bladex.GetTime()+0.2, PinchoGetDown, (pinchoobj, pinchovar))
    else:
        pass

##################################################################################################################
#### DOORS AND GATES ####
#########################
def OpenDoor1():
    door1.OpenDoor()

def OpenDoor2():
    door2.OpenDoor()

def OpenEndDoor():
    endDoor.OpenDoor()

def CloseDoor2():
    door2.CloseDoor()

def OpenBossGate(gate, d1=2500, d2=600):
    displacement=(d1,d2)
    vectors = (0.0,-1.0,0.0),(0.0,-1.0,0.0)
    vel_init = (500, 2000)
    vel_fin = (2000, 500)
    whilesnd = (snd_slidegate, snd_slidegate)
    endsnd = ("", snd_hitgate)
    Objects.NDisplaceObject(gate, displacement, vectors, vel_init, vel_fin, (), whilesnd, endsnd)
    bossGateLever.OnTurnOnFunc = None
    bossGateLever.OnTurnOnArgs = None

def OpenGate(gate, d1=2500, d2=600):
    displacement=(d1,d2)
    vectors = (0.0,-1.0,0.0),(0.0,-1.0,0.0)
    vel_init = (500, 2000)
    vel_fin = (2000, 500)
    whilesnd = (snd_slidegate, snd_slidegate)
    endsnd = ("", snd_hitgate)
    Objects.NDisplaceObject(gate, displacement, vectors, vel_init, vel_fin, (), whilesnd, endsnd)

def CloseGate(gate,d1=2500,d2=600):
    displacement = (d1,d2)
    vectors = (0.0, 1.0, 0.0), (0.0, 1.0, 0.0)
    vel_init = (1000, 3000)
    vel_fin = (3000, 1000)
    whilesnd = (snd_slidegate, snd_slidegate)
    endsnd = ("", snd_hitgate)
    Objects.NDisplaceObject(gate, displacement, vectors, vel_init, vel_fin, (), whilesnd, endsnd)

# BOSS FIGHT
def SetPlayerCorrPos():
    player = Bladex.GetEntity("Player1")
    player.Position = 5000, -1100, 0

def MoveBoss1():
    darfuncs.UnhideBadGuy("KnightBoss")
    knightBoss.Deaf = 1
    knightBoss.Blind = 1
    knightBoss.GoTo(-4000,-1100, 0)

def MoveBoss2():
    knightBoss.GoTo(-3000,-1100, 0)

def MovePlayer1():
    player = Bladex.GetEntity("Player1")
    player.GoTo(4000, -1100, 0)

def MakeBossFight():
    knightBoss.Deaf = 0
    knightBoss.Blind = 0

def InitiateBossFight(sector,entity):
    if entity == "Player1":
        CloseGate(bossGateObj,)
        CutScene2()
        ChangeMusic("BossAppears")
        Bladex.AddScheduledFunc(Bladex.GetTime()+1, SetPlayerCorrPos, ())
        Bladex.AddScheduledFunc(Bladex.GetTime()+1, MoveBoss1, ())
        Bladex.AddScheduledFunc(Bladex.GetTime()+5, MoveBoss2, ())
        Bladex.AddScheduledFunc(Bladex.GetTime()+5, MovePlayer1, ())
        Bladex.AddScheduledFunc(Bladex.GetTime()+7, MakeBossFight, ())
        sect_boss.OnEnter = None
    else:
        pass

# MINO FIGHT
def MinoGate():
    OpenDoor1()
    OpenDoor2()
    OpenGate(bossGateObj,)
    EnemyTypes.EnemyDefaultFuncs(mino)
    mino.Deaf = 0
    mino.Blind = 0
    minoLock.OnUnLockFunc = None
    minoLock.OnUnLockArgs = None

# Trap Line
def InitiateTrapLine(sector,entity):
    if entity == "Player1":
        ChangeMusic("TrapsOn")
        CloseDoor2()
        Bladex.AddScheduledFunc(Bladex.GetTime()+2, ActivatePinchos, ())
        CutScene4()
        player = Bladex.GetEntity("Player1")
        player.GoTo(25500, -1100, 0)
        sect_traps.OnEnter = None
    else:
        pass

def StopTrapLine():
    ChangeMusic("Atmos24")
    OpenGate(trapsGateObj,)
    DeactivatePinchos()
    portLever.OnTurnOnFunc = None
    portLever.OnTurnOnArgs = None

# Cutscene after killing the boss
def StartCutScene3(entity):
    ChangeMusic("Atmos24")
    Bladex.GetEntity(entity).Data.DefImDeadFunc(entity)
    Bladex.AddScheduledFunc(Bladex.GetTime()+1, CutScene3, ())

# Ending
def SetPlayerEndPos():
    player = Bladex.GetEntity("Player1")
    player.Position = 69250, -1150, 0

def MoveToEndingPoint():
    player = Bladex.GetEntity("Player1")
    player.GoTo(85500, -1100, 0)

def StartEndScene():
    Bladex.DeactivateInput()
    Scorer.SetVisible(0)
    OpenEndDoor()
    AuxFuncs.FadeTo(3.0, 180.0,)
    Actions.FreeBothHands("Player1")
    Bladex.AddScheduledFunc(Bladex.GetTime()+3, AuxFuncs.FadeFrom, (0.6,1,))
    Bladex.AddScheduledFunc(Bladex.GetTime()+3, SetPlayerEndPos, ())
    Bladex.AddScheduledFunc(Bladex.GetTime()+3, CutScene5, ())
    Bladex.AddScheduledFunc(Bladex.GetTime()+5, MoveToEndingPoint, ())
    Bladex.AddScheduledFunc(Bladex.GetTime()+8, AuxFuncs.FadeTo, (3.0, 180.0,))
    Bladex.AddScheduledFunc(Bladex.GetTime()+11, Bladex.ActivateInput,())
    Bladex.AddScheduledFunc(Bladex.GetTime()+11, Bladex.LoadLevel, ("Casa"))

def TeleportToEnd(sector, entity):
    if entity == "Player1":
        player = Bladex.GetEntity("Player1")
        player.Position = 68250, -1150, 0
    else:
        pass      