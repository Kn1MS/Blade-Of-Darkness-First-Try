import Bladex
import Sounds
import DMusic

# Music
Bladex.AddMusicEventADPCM("Atmos24","..\\..\\sounds\\ATMOSFERA24.wav", 1.0, 1.0, 1.0, 1.0, 0, -1)
Bladex.AddMusicEventADPCM("BossAppears","..\\..\\sounds\\SORPRESA4.wav", 1.0, 1.0, 1.0, 1.0, 0, 0)
Bladex.AddMusicEventADPCM("TrapsOn","..\\..\\sounds\\SORPRESA3.wav", 1.0, 1.0, 1.0, 1.0, 0, 0)
#Bladex.AddMusicEventMP3("Atmos22","..\\..\\sounds\\ATMOSFERA22.mp3",1.0,1.0,1.0,1.0,0,-1)

# Battle music for minotaur and knight boss
DMusic.AddCombatMusic("Mino", "..\\..\\sounds\\COMBATE4.wav", 400, 1.0, 1.0, 1.0, 1.0)
DMusic.AddCombatMusic("KnightBoss", "..\\..\\sounds\\combate-ligth.wav", 400, 1.0, 1.0, 1.0, 1.0)