#########################Fourth Assembly with pipette volume edits and hso file splitting edits########################################

from liquidhandling import SoloSoft, SoftLinx
from liquidhandling import Plate_96_Corning_3635_ClearUVAssay

'''
This code makes the required hso files that will be called in 
next section
The code for this is divided into 3 sections:
- making the dilution plate
- transferring cells into the final assay
- transferring nutrients from dilution plate to final assay plate
'''

#declaring variables used throughout protocol
assay = "Position4"
cells = "Position7"
tips = "Position3"
dilution = "Position6"
stock_M9 = "Position5"
stock_treatments = "Position1"
dispenseHeight = 2
aspirateHeight = 2
syringeSpeed = 50
mixCycles = 3
mixVolume = 60
cells_volume = 80

plate_list= [
        "DeepBlock.96.VWR-75870-792.sterile",
        "Empty",
        "TipBox.180uL.Axygen-EVF-180-R-S.bluebox",
        "Plate.96.Corning-3635.ClearUVAssay", 
        "DeepBlock.96.VWR-75870-792.sterile",
        "DeepBlock.96.VWR-75870-792.sterile",
        "DeepBlock.96.VWR-75870-792.sterile", 
        "Empty",
   ]


#making dilution plate
############################M9 media into dilution plate#############################
rows = ["A", "B", "C", "D", "E", "F", "G", "H"]

'''Phosphorus columns (stock is 10X)
Rows 1-2 should have no media
Rows 3-4 should have 600 uL media
Rows 5-6 should have 900 uL media
Rows 7-8 should have 1050 uL media

'''

#run this hso twice#
soloSoft = SoloSoft(
    filename = "dilution_P_M9_1.hso",
    plateList = plate_list,
    ) 

soloSoft.getTip(position=tips, num_tips=2)

for j in range(1,4):
    for row in rows[2::2]:
        for i in range(1,3):
            x = [1, 1.5, 1.75]
            transfer_volume = 100 * x[rows[2::2].index(row)] 
            soloSoft.aspirate(
                position = stock_M9,
                aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell(row, i, transfer_volume),
                aspirate_shift = [0, 0, 2],
                ##aspirate_height = aspirateHeight,
                syringe_speed = syringeSpeed,        
                )    
            soloSoft.dispense(
                position = dilution,
                dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell(row, i, transfer_volume),
                dispense_shift = [0, 0, 2],
                ##dispense_height = dispenseHeight,
                syringe_speed = syringeSpeed,
                )

soloSoft.shuckTip()

soloSoft.savePipeline()

#TIPS: after running twice, uses 4 tips#

'''Carbon columns
C1 cells should have no media
C2 cells should have 600 ul media
C3 cells should have 900 uL media
C4 cells should have 1050 uL media
'''

#C2#
soloSoft = SoloSoft(
    filename = "dilution_C_M9_1.hso",
    plateList = plate_list,
    ) 

soloSoft.getTip(position=tips, num_tips=1)

for j in range(1,5):
    for row in rows[1::2]:
        for i in range(3,5):
            transfer_volume = 150
            soloSoft.aspirate(
                position = stock_M9,    
                aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell(row, i, transfer_volume),
                aspirate_shift = [0, 0, 2],
               # #aspirate_height = aspirateHeight,
                syringe_speed = syringeSpeed,        
                )    
            soloSoft.dispense(
                position = dilution,
                dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell(row, i, transfer_volume),
                dispense_shift = [0, 0, 2],
               # #dispense_height = dispenseHeight,
                syringe_speed = syringeSpeed,
                )

soloSoft.shuckTip()

soloSoft.savePipeline()

#TIPS: uses 1 tips (5 total at this point)

#C3#
soloSoft = SoloSoft(
    filename = "dilution_C_M9_2.hso",
    plateList = plate_list,
    ) 

soloSoft.getTip(position=tips, num_tips=1)

for j in range(1,4):
    for row in rows[::2]:
        for i in range(5,7):
            transfer_volume = 180
            soloSoft.aspirate(
                position = stock_M9,    
                aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell(row, i, transfer_volume),
                aspirate_shift = [0, 0, 2],
                #aspirate_height = aspirateHeight,
                syringe_speed = syringeSpeed,        
                )    
            soloSoft.dispense(
                position = dilution,
                dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell(row, i, transfer_volume),
                dispense_shift = [0, 0, 2],
                ##dispense_height = dispenseHeight,
                syringe_speed = syringeSpeed,
                )

soloSoft.shuckTip()

soloSoft.savePipeline()

soloSoft = SoloSoft(
    filename = "dilution_C_M9_3.hso",
    plateList = plate_list,
    ) 

soloSoft.getTip(position=tips, num_tips=1)

for j in range(1,3):
    for row in rows[::2]:
        for i in range(5,7):
            transfer_volume = 180
            soloSoft.aspirate(
                position = stock_M9,    
                aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell(row, i, transfer_volume),
                aspirate_shift = [0, 0, 2],
                #aspirate_height = aspirateHeight,
                syringe_speed = syringeSpeed,        
                )    
            soloSoft.dispense(
                position = dilution,
                dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell(row, i, transfer_volume),
                dispense_shift = [0, 0, 2],
                ##dispense_height = dispenseHeight,
                syringe_speed = syringeSpeed,
                )

soloSoft.shuckTip()

soloSoft.savePipeline()

#TIPS: uses 1 tips (7 total at this point)

#C4#
#CALL TWICE
soloSoft = SoloSoft(
    filename = "dilution_C_M9_4.hso",
    plateList = plate_list,
    ) 

soloSoft.getTip(position=tips, num_tips=1)

for j in range(1,4):
    for row in rows[1::2]:
        for i in range(5,7):
            transfer_volume = 175
            soloSoft.aspirate(
                position = stock_M9,    
                aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell(row, i, transfer_volume),
                aspirate_shift = [0, 0, 2],
                #aspirate_height = aspirateHeight,
                syringe_speed = syringeSpeed,        
                )    
            soloSoft.dispense(
                position = dilution,
                dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell(row, i, transfer_volume),
                dispense_shift = [0, 0, 2],
                #dispense_height = dispenseHeight,
                syringe_speed = syringeSpeed,
                )

soloSoft.shuckTip()

soloSoft.savePipeline()

#TIPS: uses 1 tips (i column and 1 tip in next column used at this point because called twice)


'''Nitrogen columns
column 7 should have no media
column 8 should have 600 uL media
column 9 should have 900 uL media
column 10 should have 1050 uL media
column 11 should have 1125 uL media
'''

soloSoft = SoloSoft(
    filename = "dilution_N_M9_1.hso",
    plateList = plate_list,
    ) 

soloSoft.getTip(tips)

#N2#
for j in range(1,5):
    transfer_volume = 150
    soloSoft.aspirate(
        position = stock_M9,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(8, transfer_volume),
        aspirate_shift = [0, 0, 2],
        #  #aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,        
        )
    soloSoft.dispense(
        position = dilution,
        dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(8, transfer_volume),
        dispense_shift = [0, 0, 2],
        #  #dispense_height = dispenseHeight,
        syringe_speed = syringeSpeed,
        )

#N3#
for j in range(1,6):
    transfer_volume = 180
    soloSoft.aspirate(
        position = stock_M9,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(9, transfer_volume),
        aspirate_shift = [0, 0, 2],
        #  #aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,        
        )
    soloSoft.dispense(
        position = dilution,
        dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(9, transfer_volume),
        dispense_shift = [0, 0, 2],
        #  #dispense_height = dispenseHeight,
        syringe_speed = syringeSpeed,
        )

soloSoft.shuckTip()

soloSoft.savePipeline()

#TIPS: uses a column of tips (2 columns used at this point)

soloSoft = SoloSoft(
    filename = "dilution_N_M9_2.hso",
    plateList = plate_list,
    ) 

soloSoft.getTip(tips)

#N4#
for j in range(1,7):
    transfer_volume = 175
    soloSoft.aspirate(
        position = stock_M9,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(10, transfer_volume),
        aspirate_shift = [0, 0, 2],
        #  #aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,        
        )
    soloSoft.dispense(
        position = dilution,
        dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(10, transfer_volume),
        dispense_shift = [0, 0, 2],
        #  #dispense_height = dispenseHeight,
        syringe_speed = syringeSpeed,
        )

#N5#
for j in range(1,10):
    transfer_volume = 125
    soloSoft.aspirate(
        position = stock_M9,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(11, transfer_volume),
        aspirate_shift = [0, 0, 2],
        #  #aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,        
        )
    soloSoft.dispense(
        position = dilution,
        dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(11, transfer_volume),
        dispense_shift = [0, 0, 2],
        #  #dispense_height = dispenseHeight,
        syringe_speed = syringeSpeed,
        )

soloSoft.shuckTip()

soloSoft.savePipeline()

#TIPS: uses a column of tips (3 columns used at this point)

############################Treatments into dilution plate#############################
rows = ["A", "B", "C", "D", "E", "F", "G", "H"]

#Phosphorus
#P1 at 10X, P2 at 5X, P3 at 2.5X, P4 at 1.25X
soloSoft = SoloSoft(
    filename = "dilution_P_treatment_1.hso",
    plateList = plate_list,
    ) 

soloSoft.getTip(position=tips, num_tips=2)

transfer_volume = 150

#for P4#
for i in range(1,3):
    soloSoft.aspirate(
        position = stock_treatments,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell('G', 9, transfer_volume),
        aspirate_shift = [0, 0, 2],
        mix_at_start = True,
        mix_cycles = mixCycles,
        mix_volume = mixVolume,
        #aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,        
        )    
    soloSoft.dispense(
        position = dilution,
        dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell('G', i, transfer_volume),
        dispense_shift = [0, 0, 2],
        #dispense_height = dispenseHeight,
        syringe_speed = syringeSpeed,
        )

#for P3#
#there are two for loops because we need to transfer into two columns then repeat that a second time#
for j in range(1,3):
    for i in range(1,3):
        soloSoft.aspirate(
            position = stock_treatments,
            aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell('E', 9, transfer_volume),
            aspirate_shift = [0, 0, 2],
            mix_at_start = True,
            mix_cycles = mixCycles,
            mix_volume = mixVolume,
            #aspirate_height = aspirateHeight,
            syringe_speed = syringeSpeed,        
            )    
        soloSoft.dispense(
            position = dilution,
            dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell('E', i, transfer_volume),
            dispense_shift = [0, 0, 2],
            #dispense_height = dispenseHeight,
            syringe_speed = syringeSpeed,
            )

#for P2#
#the two for loops are because we need to transfer to two columns and repeat the same transfer 4 times#
for j in range(1,5):
    for i in range(1,3):
        soloSoft.aspirate(
            position = stock_treatments,
            aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell('C', i+8, transfer_volume),
            aspirate_shift = [0, 0, 2],
            mix_at_start = True,
            mix_cycles = mixCycles,
            mix_volume = mixVolume,
            #aspirate_height = aspirateHeight,
            syringe_speed = syringeSpeed,        
            )    
        soloSoft.dispense(
            position = dilution,
            dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell('C', i, transfer_volume),
            dispense_shift = [0, 0, 2],
            #dispense_height = dispenseHeight,
            syringe_speed = syringeSpeed,
            )

soloSoft.shuckTip()

soloSoft.savePipeline()

#TIPS: uses 2 tips (3 columns and 2 of fourth column used at this point)

soloSoft = SoloSoft(
    filename = "dilution_P_treatment_2.hso",
    plateList = plate_list,
    ) 

soloSoft.getTip(position=tips, num_tips=2)

transfer_volume = 150

#for P1#
for j in range(1,9):
    for i in range(1,3):
        soloSoft.aspirate(
            position = stock_treatments,
            aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell('A', ((j-1)//2) + 9, transfer_volume),
            aspirate_shift = [0, 0, 2],
            mix_at_start = True,
            mix_cycles = mixCycles,
            mix_volume = mixVolume,
            #aspirate_height = aspirateHeight,
            syringe_speed = syringeSpeed,        
            )    
        soloSoft.dispense(
            position = dilution,
            dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell('A', i, transfer_volume),
            dispense_shift = [0, 0, 2],
            #dispense_height = dispenseHeight,
            syringe_speed = syringeSpeed,
            )

soloSoft.shuckTip()

soloSoft.savePipeline()

#TIPS: uses 2 tips (3 columns and 4 of fourth column used at this point)

#Carbon
soloSoft = SoloSoft(
    filename = "dilution_C_treatment_1.hso",
    plateList = plate_list,
    )

soloSoft.getTip(position=tips, num_tips=1)

#prepping C4 cells (1.25X)#
for row in rows[1::2]:
    for i in range(5,7):
        transfer_volume = 150
        soloSoft.aspirate(
            position = stock_treatments,    
            aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell(row, 1, transfer_volume),
            aspirate_shift = [0, 0, 2],
            mix_at_start = True,
            mix_cycles = mixCycles,
            mix_volume = mixVolume,
            #aspirate_height = aspirateHeight,
            syringe_speed = syringeSpeed,        
            )    
        soloSoft.dispense(
            position = dilution,
            dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell(row, i, transfer_volume),
            dispense_shift = [0, 0, 2],
            #dispense_height = dispenseHeight,
            syringe_speed = syringeSpeed,
            )

#prepping C3 cells (2.5X)
for j in range(1,3):
    for row in rows[::2]:
        for i in range(5,7):
            transfer_volume = 150
            soloSoft.aspirate(
                position = stock_treatments,    
                aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell(row, 1, transfer_volume),
                aspirate_shift = [0, 0, 2],
                mix_at_start = True,
                mix_cycles = mixCycles,
                mix_volume = mixVolume,
                #aspirate_height = aspirateHeight,
                syringe_speed = syringeSpeed,        
                )    
            soloSoft.dispense(
                position = dilution,
                dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell(row, i, transfer_volume),
                dispense_shift = [0, 0, 2],
                #dispense_height = dispenseHeight,
                syringe_speed = syringeSpeed,
                )

soloSoft.shuckTip()

soloSoft.savePipeline()

#TIPS: uses 1 tip (3 columns and 5 of fourth column used at this point)

#prepping C2 cells (5X)
soloSoft = SoloSoft(
    filename = "dilution_C_treatment_2.hso",
    plateList = plate_list,
    )

soloSoft.getTip(position=tips, num_tips=1)

for j in range(1,5):
    for row in rows[1::2]:
        for i in range(3,5):
            transfer_volume = 150
            soloSoft.aspirate(
                position = stock_treatments,    
                aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell(row, i-1, transfer_volume),
                aspirate_shift = [0, 0, 2],
                mix_at_start = True,
                mix_cycles = mixCycles,
                mix_volume = mixVolume,
                #aspirate_height = aspirateHeight,
                syringe_speed = syringeSpeed,        
                )    
            soloSoft.dispense(
                position = dilution,
                dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell(row, i, transfer_volume),
                dispense_shift = [0, 0, 2],
                #dispense_height = dispenseHeight,
                syringe_speed = syringeSpeed,
                )

soloSoft.shuckTip()

soloSoft.savePipeline()

#TIPS: uses 1 tip (3 columns and 6 of fourth column used at this point)


soloSoft = SoloSoft(
    filename = "dilution_C_treatment_3.hso",
    plateList = plate_list,
    )

soloSoft.getTip(position=tips, num_tips=1)

#prepping C1 cells (10X)
for j in range(1,5):
    for row in rows[::2]:
        for i in range(3,5):
            transfer_volume = 150
            soloSoft.aspirate(
                position = stock_treatments,    
                aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell(row, i, transfer_volume),
                aspirate_shift = [0, 0, 2],
                mix_at_start = True,
                mix_cycles = mixCycles,
                mix_volume = mixVolume,
             #   #aspirate_height = aspirateHeight,
                syringe_speed = syringeSpeed,        
                )    
            soloSoft.dispense(
                position = dilution,
                dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell(row, i, transfer_volume),
                dispense_shift = [0, 0, 2],
            #    #dispense_height = dispenseHeight,
                syringe_speed = syringeSpeed,
                )

soloSoft.shuckTip()

soloSoft.savePipeline()

#TIPS: uses 1 tip (3 columns and 8 of fourth column used at this point because run twice)


#Nitrogen
#N1 should be 20X (1200 uL),N2 should be 10X (600 uL), N3 should be 5X (300 uL), N4 should be 2.5X (150 uL), N5 should be 1.25X (75 uL)

soloSoft = SoloSoft(
    filename = "dilution_N_treatment_1.hso",
    plateList = plate_list,
    ) 

transfer_volume = 150

soloSoft.getTip(tips) 
#### N5#####
# #75 uL#
soloSoft.aspirate(
    position = stock_treatments,
    aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(5, transfer_volume*0.5),
    aspirate_shift = [0, 0, 2],
    mix_at_start = True,
    mix_cycles = mixCycles,
    mix_volume = mixVolume,
    #aspirate_height = aspirateHeight,
    syringe_speed = syringeSpeed,
    ) 

soloSoft.dispense(
    position = dilution,
    dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(11, transfer_volume*0.5),
    dispense_shift = [0, 0, 2],
   # dispense_height = dispenseHeight,
    syringe_speed = syringeSpeed,
    )

### N4###
#150 uL#
soloSoft.aspirate(
    position = stock_treatments,
    aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(5, transfer_volume),
    aspirate_shift = [0, 0, 2],
    mix_at_start = True,
    mix_cycles = mixCycles,
    mix_volume = mixVolume,
   # aspirate_height = aspirateHeight,
    syringe_speed = syringeSpeed,        
    )

soloSoft.dispense(
    position = dilution,
    dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(10, transfer_volume),
    dispense_shift = [0, 0, 2],
   # dispense_height = dispenseHeight,
    syringe_speed = syringeSpeed,
    )

###N3####
for j in range(1,3):
    soloSoft.aspirate(
        position = stock_treatments,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(5, transfer_volume),
        aspirate_shift = [0, 0, 2],
        mix_at_start = True,
        mix_cycles = mixCycles,
        mix_volume = mixVolume,
        #aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,        
        )
    soloSoft.dispense(
        position = dilution,
        dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(9, transfer_volume),
        dispense_shift = [0, 0, 2],
       # dispense_height = dispenseHeight,
        syringe_speed = syringeSpeed,
        )

soloSoft.shuckTip()

soloSoft.savePipeline() 

#TIPS: uses 1 column (5 colums used at this point)

###N2####
soloSoft = SoloSoft(
    filename = "dilution_N_treatment_2.hso",
    plateList = plate_list,
    ) 

soloSoft.getTip(tips) 

for j in range(1,5):
    transfer_volume = 150
    soloSoft.aspirate(
        position = stock_treatments,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(6, transfer_volume),
        aspirate_shift = [0, 0, 2],
        mix_at_start = True,
        mix_cycles = mixCycles,
        mix_volume = mixVolume,
       # aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,        
        )
    soloSoft.dispense(
        position = dilution,
        dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(8, transfer_volume),
        dispense_shift = [0, 0, 2],
        #dispense_height = dispenseHeight,
        syringe_speed = syringeSpeed,
        )

soloSoft.shuckTip()

soloSoft.savePipeline()

#TIPS: uses 1 column (6 colums used at this point)

######N1#######
soloSoft = SoloSoft(
    filename = "dilution_N_treatment_3.hso",
    plateList = plate_list,
    ) 

soloSoft.getTip(tips)

for j in range(1,9):
    transfer_volume = 150
    soloSoft.aspirate(
        position = stock_treatments,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(((j-1)//4)+7, transfer_volume),
        aspirate_shift = [0, 0, 2],
        mix_at_start = True,
        mix_cycles = mixCycles,
        mix_volume = mixVolume,
      #  aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,        
        )
    soloSoft.dispense(
        position = dilution,
        dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(7, transfer_volume),
        dispense_shift = [0, 0, 2],
     #   dispense_height = dispenseHeight,
        syringe_speed = syringeSpeed,
        )

soloSoft.shuckTip()

soloSoft.savePipeline()

#TIPS: uses 1 column (7 colums used at this point)

##############################making control#####################################

#need to change tip box before prepping control column#




'''
The following code makes the control column on the dilution plate (control means 1x of every nutrient and no cells)
'''

soloSoft = SoloSoft(
    filename = "dilution_control.hso",
    plateList = plate_list,
    ) 

#M9#
soloSoft.getTip(tips)

for i in range(1,6):
    soloSoft.aspirate(
        position = stock_M9,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(12, 180),
        aspirate_shift = [0, 0, 2],
        ##aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,
        )
    soloSoft.dispense(
        position = dilution,
        dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(12, 180),
        dispense_shift = [0, 0, 2],
        #dispense_height = dispenseHeight,
        syringe_speed = syringeSpeed,
        )

soloSoft.shuckTip()

#C#
c_control_volume = 120

soloSoft.getTip(tips)

soloSoft.aspirate(
    position = stock_treatments,
    aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(4, c_control_volume),
    aspirate_shift = [0, 0, 2],
    mix_at_start = True,
    mix_cycles = mixCycles,
    mix_volume = mixVolume,
    ##aspirate_height = aspirateHeight,
    syringe_speed = syringeSpeed,
    )
soloSoft.dispense(
    position = dilution,
    dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(12, c_control_volume),
    dispense_shift = [0, 0, 2],
    ##dispense_height = dispenseHeight,
    syringe_speed = syringeSpeed,
    )

soloSoft.shuckTip()

#P#
p_control_volume = 120

soloSoft.getTip(tips)

soloSoft.aspirate(
    position = stock_treatments,
    aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(12, p_control_volume),
    aspirate_shift = [0, 0, 2],
    mix_at_start = True,
    mix_cycles = mixCycles,
    mix_volume = mixVolume,
    #aspirate_height = aspirateHeight,
    syringe_speed = syringeSpeed,
    )
soloSoft.dispense(
    position = dilution,
    dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(12, p_control_volume),
    dispense_shift = [0, 0, 2],
    #dispense_height = dispenseHeight,
    syringe_speed = syringeSpeed,
    )

soloSoft.shuckTip()

#N#
n_control_volume = 60

soloSoft.getTip(tips)

soloSoft.aspirate(
    position = stock_treatments,
    aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(4, n_control_volume),
    aspirate_shift = [0, 0, 2],
    mix_at_start = True,
    mix_cycles = mixCycles,
    mix_volume = mixVolume,
    #aspirate_height = aspirateHeight,
    syringe_speed = syringeSpeed,
    )
soloSoft.dispense(
    position = dilution,
    dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(12, n_control_volume),
    dispense_shift = [0, 0, 2],
    #dispense_height = dispenseHeight,
    syringe_speed = syringeSpeed,
    )

soloSoft.shuckTip()

soloSoft.savePipeline()

#TIPS: uses 4 columns of tips

#############################cells to assay##########################
'''
The following code transfers cells to the final assay plate
'''

soloSoft = SoloSoft(
    filename = "cells_assay_1.hso",
    plateList = plate_list,
    ) 

soloSoft.getTip(tips)

for i in range(1,6):   
    soloSoft.aspirate(
        position = cells,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(i, cells_volume),
        aspirate_shift = [0, 0, 2],
        mix_at_start = True,
        mix_cycles = mixCycles,
        mix_volume = mixVolume,
        ##aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,
        )
    soloSoft.dispense(
        position = assay,
        dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(i, cells_volume),
        dispense_shift = [0, 0, 2],
        #dispense_height = dispenseHeight,
        syringe_speed = syringeSpeed,
        )

soloSoft.shuckTip()

soloSoft.savePipeline() 

#TIPS: uses 1 column of tips (5 columns used at this point)

soloSoft = SoloSoft(
    filename = "cells_assay_2.hso",
    plateList = plate_list,
    ) 

soloSoft.getTip(tips)

for i in range(7,12):   
    soloSoft.aspirate(
        position = cells,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(i, cells_volume),
        aspirate_shift = [0, 0, 2],
        mix_at_start = True,
        mix_cycles = mixCycles,
        mix_volume = mixVolume,
        ##aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,
        )
    soloSoft.dispense(
        position = assay,
        dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(i, cells_volume),
        dispense_shift = [0, 0, 2],
        #dispense_height = dispenseHeight,
        syringe_speed = syringeSpeed,
        )

soloSoft.shuckTip()

soloSoft.savePipeline() 

#TIPS: uses 1 column of tips (6 columns used at this point)

soloSoft = SoloSoft(
    filename = "control_assay.hso",
    plateList = plate_list,
    ) 

soloSoft.getTip(tips)

#dilution to assay
for j in range(1,3):
    soloSoft.aspirate(
        position = dilution,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(12, 180),
        aspirate_shift = [0, 0, 2],
        mix_at_start = True,
        mix_cycles = mixCycles,
        mix_volume = mixVolume,
        #aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,
        )
    for i in [6,12]:
        soloSoft.dispense(
            position = assay,
            dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(i, 90),
            dispense_shift = [0, 0, 2],
            #dispense_height = dispenseHeight,
            syringe_speed = syringeSpeed,
            )

soloSoft.savePipeline()

#TIPS: uses 1 column of tips (7 columns used at this point)

################################################################

'''
The following code transfers nutrients to the final assay plate
'''

##############Dilution assay######## 
########Phosphorus########
#######Starting new SoloSoft for phosphorus on the assay plate#####

soloSoft = SoloSoft(
    filename = "dilution_assay_P_1.hso",
    plateList = plate_list,
    ) 

soloSoft.getTip(tips)

transfer_volume = 20

#for i in range(1,6):
for i in range(1,3):
    soloSoft.aspirate(
        position = dilution,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(1, transfer_volume*5),
        aspirate_shift = [0, 0, 2],
        mix_at_start = True,
        mix_cycles = mixCycles,
        mix_volume = mixVolume,
        #aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,
        ) 
    for i in range(1,6):
        soloSoft.dispense(
            position = assay,
            dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(i, transfer_volume),
            dispense_shift = [0, 0, 2],
            mix_at_finish = True,
            mix_cycles = mixCycles,
            mix_volume = mixVolume,
            #dispense_height = dispenseHeight,
            syringe_speed = syringeSpeed,
            )

for i in range(1,3):
    soloSoft.aspirate(
        position = dilution,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(2, transfer_volume*5),
        aspirate_shift = [0, 0, 2],
        mix_at_start = True,
        mix_cycles = mixCycles,
        mix_volume = mixVolume,
        #aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,
        ) 
    for i in range(7,12):
        soloSoft.dispense(
            position = assay,
            dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(i, transfer_volume),
            dispense_shift = [0, 0, 2],
            mix_at_finish = True,
            mix_cycles = mixCycles,
            mix_volume = mixVolume,
            #dispense_height = dispenseHeight,
            syringe_speed = syringeSpeed,
            )

soloSoft.savePipeline() 

#TIPS: uses 1 column of tips (8 columns used at this point) EMPTY
#NEED TO GET NEW TIP BOX

##########Carbon####### 
#######Starting a new SoloSoft for carbon on the first half of the assay plate######
soloSoft = SoloSoft(
    filename = "dilution_assay_C_1.hso",
    plateList = plate_list,
    ) 

soloSoft.getTip(tips)

transfer_volume = 20 

for i in range(1,3):
    soloSoft.aspirate(
        position = dilution,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(3, transfer_volume*5),
        aspirate_shift = [0, 0, 2],
        mix_at_start = True,
        mix_cycles = mixCycles,
        mix_volume = mixVolume,
        #aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,
        ) 
    for i in reversed(range(1,6)):
        soloSoft.dispense(
            position = assay,
            dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(i, transfer_volume),
            dispense_shift = [0, 0, 2],
            mix_at_finish = True,
            mix_cycles = mixCycles,
            mix_volume = mixVolume,
            #dispense_height = dispenseHeight,
            syringe_speed = syringeSpeed,
            )

soloSoft.shuckTip()

soloSoft.savePipeline() 

#TIPS: uses 1 column of tips

#######Starting a new SoloSoft for carbon on the second half of the assay plate######
soloSoft = SoloSoft(
    filename = "dilution_assay_C_2.hso",
    plateList = plate_list,
    ) 

soloSoft.getTip(tips)

transfer_volume = 20 

for i in range(1,3):
    soloSoft.aspirate(
        position = dilution,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(5, transfer_volume*5),
        aspirate_shift = [0, 0, 2],
        mix_at_start = True,
        mix_cycles = mixCycles,
        mix_volume = mixVolume,
        #aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,
        ) 
    for i in reversed(range(7,12)):
        soloSoft.dispense(
            position = assay,
            dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(i, transfer_volume),
            dispense_shift = [0, 0, 2],
            mix_at_finish = True,
            mix_cycles = mixCycles,
            mix_volume = mixVolume,
            #dispense_height = dispenseHeight,
            syringe_speed = syringeSpeed,
            )

soloSoft.shuckTip()

soloSoft.savePipeline() 

#TIPS: uses 1 column of tips (2 columns used at this point)

#######Nitrogen############ 
#######Starting a new SoloSoft for nitrogen on the first half of the assay plate######

soloSoft = SoloSoft(
    filename = "dilution_assay_N_1.hso",
    plateList = plate_list,
    ) 

for i in reversed(range(1,6)):
    soloSoft.getTip(tips)
    transfer_volume = 40 
    soloSoft.aspirate(
        position = dilution,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(i+6, transfer_volume),
        aspirate_shift = [0, 0, 2],
        mix_at_start = True,
        mix_cycles = mixCycles,
        mix_volume = mixVolume,
        #aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,
        ) 
    soloSoft.dispense(
        position = assay,
        dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(i, transfer_volume),
        dispense_shift = [0, 0, 2],
        mix_at_finish = True,
        mix_cycles = mixCycles,
        mix_volume = mixVolume,
        #dispense_height = dispenseHeight,
        syringe_speed = syringeSpeed,
        )
    soloSoft.shuckTip()

soloSoft.savePipeline() 

#TIPS: uses 5 column of tips (7 columns used at this point)
#GET NEW TIP BOX HERE#

#######Starting a new SoloSoft for nitrogen on the second half of the assay plate######
soloSoft = SoloSoft(
    filename = "dilution_assay_N_2.hso",
    plateList = plate_list,
    ) 

for i in reversed(range(7,12)):
    soloSoft.getTip(tips)
    transfer_volume = 40 
    soloSoft.aspirate(
        position = dilution,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(i, transfer_volume),
        aspirate_shift = [0, 0, 2],
        mix_at_start = True,
        mix_cycles = mixCycles,
        mix_volume = mixVolume,
        #aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,
        ) 
    soloSoft.dispense(
        position = assay,
        dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(i, transfer_volume),
        dispense_shift = [0, 0, 2],
        mix_at_finish = True,
        mix_cycles = mixCycles,
        mix_volume = mixVolume,
        #dispense_height = dispenseHeight,
        syringe_speed = syringeSpeed,
        )
    soloSoft.shuckTip()

soloSoft.savePipeline() 

##############################################################
'''
This is the Softlinx part of the code that entails the crane 
movements as well as the execution of the hso files
'''

softLinx = SoftLinx("Fourth_attempt", "Fourth_attempt.slvp") # display name, path to saves
softLinx.setPlates({"SoftLinx.PlateCrane.Stack5": "Plate_96_Corning_3635_ClearUVAssay", "SoftLinx.PlateCrane.Stack4":"TipBox.50uL.Axygen-EV-50-R-S.tealbox"})
#this is hwere you would softlinx run solo stuff, preparing diltuion stock (fill stuff in)###############
softLinx.plateCraneMovePlate(["SoftLinx.PlateCrane.Stack5"],["SoftLinx.Solo.Position4"],poolID = 5)
softLinx.plateCraneRemoveLid(["SoftLinx.Solo.Position4"],["SoftLinx.PlateCrane.LidNest2"])
softLinx.plateCraneMovePlate(["SoftLinx.PlateCrane.Stack4"],["SoftLinx.Solo.Position3"],poolID = 4)

list_of_dilution = ["dilution_P_M9_1.hso", "dilution_P_M9_1.hso", "dilution_C_M9_1.hso", 
                    "dilution_C_M9_2.hso", "dilution_C_M9_3.hso", "dilution_C_M9_4.hso", "dilution_C_M9_4.hso", "dilution_N_M9_1.hso", 
                    "dilution_N_M9_2.hso", "dilution_P_treatment_1.hso", "dilution_P_treatment_2.hso", 
                    "dilution_C_treatment_1.hso", "dilution_C_treatment_2.hso", 
                    "dilution_C_treatment_3.hso", "dilution_C_treatment_3.hso", 
                    "dilution_N_treatment_1.hso", "dilution_N_treatment_2.hso", 
                    "dilution_N_treatment_3.hso"]

for c in list_of_dilution:
    softLinx.soloSoftRun(c)
softLinx.plateCraneMovePlate(["SoftLinx.Solo.Position3"],["SoftLinx.PlateCrane.Stack2"],poolID = 2)
softLinx.plateCraneMovePlate(["SoftLinx.PlateCrane.Stack4"],["SoftLinx.Solo.Position3"],poolID = 4)
softLinx.soloSoftRun("dilution_control.hso")

#prep the first assay plate###### 
list_of_final_1 = ["cells_assay_1.hso", "cells_assay_2.hso", "control_assay.hso", 
                "dilution_assay_P_1.hso"]               
list_of_final_2= ["dilution_assay_C_1.hso", "dilution_assay_C_2.hso", 
                "dilution_assay_N_1.hso"]
# still run at end "dilution_assay_N_2.hso"

for c in list_of_final_1:
    softLinx.soloSoftRun(c)
softLinx.plateCraneMovePlate(["SoftLinx.Solo.Position3"],["SoftLinx.PlateCrane.Stack2"],poolID = 2)
softLinx.plateCraneMovePlate(["SoftLinx.PlateCrane.Stack4"],["SoftLinx.Solo.Position3"],poolID = 4)
for c in list_of_final_2:
    softLinx.soloSoftRun(c)
softLinx.plateCraneMovePlate(["SoftLinx.Solo.Position3"],["SoftLinx.PlateCrane.Stack2"],poolID = 2)
softLinx.plateCraneMovePlate(["SoftLinx.PlateCrane.Stack4"],["SoftLinx.Solo.Position3"],poolID = 4)
softLinx.soloSoftRun("dilution_assay_N_2.hso")

softLinx.plateCraneMovePlate(["SoftLinx.Solo.Position4"],["SoftLinx.Hidex.Nest"])
softLinx.plateCraneMoveCrane("SoftLinx.PlateCrane.Safe")
softLinx.hidexRun("pyhamilton")
softLinx.plateCraneMovePlate(["SoftLinx.Hidex.Nest"],["SoftLinx.Liconic.Nest"])
softLinx.plateCraneReplaceLid(["SoftLinx.PlateCrane.LidNest2"],["SoftLinx.Liconic.Nest"])
softLinx.liconicLoadIncubator(loadID=1)

softLinx.plateCraneMovePlate(["SoftLinx.Solo.Position3"],["SoftLinx.PlateCrane.Stack2"],poolID = 2)

#at this point the layout has been reset so a new plate can be made be repeating the same thing#