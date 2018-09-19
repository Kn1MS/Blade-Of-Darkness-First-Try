import darfuncs
import Bladex

Bladex.AddScheduledFunc(Bladex.GetTime(), StartMusic, ())

Bladex.AddScheduledFunc(Bladex.GetTime()+2, CutScene1, ())

sect_boss = Bladex.GetSector(5000, 0, 0)
sect_boss.OnEnter = InitiateBossFight

sect_traps = Bladex.GetSector(23250, 0, 0)
sect_traps.OnEnter = InitiateTrapLine

sect_tp = Bladex.GetSector(10750, 0, -10750)
sect_tp.OnEnter = None