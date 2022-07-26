from re import S
from liquidhandling import SoloSoft, SoftLinx

#can we get rid of this one below I don't know what purpose it's serving#
from liquidhandling import Plate_96_Corning_3635_ClearUVAssay

softLinx = SoftLinx("Fourth_attempt", "C:\\Users\\svcaibio\\Dev\\Summer_stduents\\rpl-summer-2022\\gillian\\TipBoxTest.slvp")
for i in range(7):
    softLinx.plateCraneMovePlate(["SoftLinx.PlateCrane.Stack4"],["SoftLinx.Solo.Position3"],poolID = 4)
    softLinx.plateCraneMovePlate(["SoftLinx.Solo.Position3"],["SoftLinx.PlateCrane.Stack2"],poolID = 2)
softLinx.saveProtocol()