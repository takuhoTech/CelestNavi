import pcbnew
import math

def create_via(brd, pos, diameter, drill, netname = "GND", isFree = True, viaType = pcbnew.VIATYPE_THROUGH, startLayerID = pcbnew.F_Cu, endLayerID = pcbnew.B_Cu, removeUnconnectedAnnularRing = False):
    via = pcbnew.PCB_VIA(brd)
    via.SetPosition(pcbnew.VECTOR2I(pos[0], pos[1]))
    via.SetWidth(diameter) #外径
    via.SetDrill(drill)    #ドリル径
    via.SetNet(brd.FindNet(netname)) #ネット
    via.SetIsFree(isFree)            #True=手動でビアを置く場合と同じく自動更新されない False=ビアのネットは置かれた場所によって自動更新される
    via.SetViaType(viaType)          #pcbnew.VIATYPE_THROUGH,pcbnew.VIATYPE_BLIND_BURIED,pcbnew.VIATYPE_MICROVIA,pcbnew.VIATYPE_NOT_DEFINEDのどれか
    via.SetLayerPair(startLayerID, endLayerID) #レイヤーのID 導体レイヤーは0から31
    via.SetRemoveUnconnected(removeUnconnectedAnnularRing) #True=始点,終点,および接続されたレイヤー False=すべての導体レイヤー
    brd.Add(via)

#LB1
'''
center_x     = pcbnew.FromMM(-8.662058)
center_y     = pcbnew.FromMM(8.662058)
angle_start  = math.atan(1.0/1.8)
'''

#LB2
'''
center_x     = pcbnew.FromMM(8.662058)
center_y     = pcbnew.FromMM(8.662058)
angle_start  = math.atan(1.0/1.8) + math.pi
'''

#HB2
'''
center_x     = pcbnew.FromMM(-3.889087)
center_y     = pcbnew.FromMM(-3.889087)
angle_start  = math.atan(1.0/1.8) + math.pi/2.0
'''

#HB1
center_x     = pcbnew.FromMM(3.889087)
center_y     = pcbnew.FromMM(-3.889087)
angle_start  = math.atan(1.0/1.8) + math.pi/2.0

#スイープ角度と半径
angle_d      = 2.0*math.pi - 2.0*math.atan(1.0/1.8)
radius       = pcbnew.FromMM(math.sqrt(1.8**2 + 1.0**2))

#ビア設定
via_diameter = pcbnew.FromMM(0.6)
via_drill    = pcbnew.FromMM(0.3)

#配置数計算
via_num = 1 + int(abs(angle_d)/math.acos(1 - via_diameter**2/(2*radius**2)))

board = pcbnew.GetBoard()

for step in range(via_num):
    angle_temp = angle_start + step * angle_d / (via_num - 1)
    create_via(board, [center_x + int(radius*math.cos(angle_temp)), center_y + int(radius*math.sin(angle_temp))], via_diameter, via_drill)

pcbnew.Refresh()

#exec(open("D:/GitHub/RTU-GNSS_CLAS_2/Hardware/Antenna_Module/Scripts/feed.py").read())