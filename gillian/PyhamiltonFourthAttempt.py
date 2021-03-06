#########################Fourth Assembly with pipette volume edits and hso file splitting edits########################################

from re import S
from liquidhandling import SoloSoft, SoftLinx

#can we get rid of this one below I don't know what purpose it's serving#
from liquidhandling import Plate_96_Corning_3635_ClearUVAssay

'''
This code makes the required hso files that will be called in 
the end section chronologically to run the desired experiment

The code for this is divided into 3 sections:
- making the dilution plate
- transferring cells into the final assay
- transferring nutrients from dilution plate to final assay plate
'''

Path = "C:\\Users\\svcaibio\\Dev\\Summer_stduents\\rpl-summer-2022\\gillian\\"

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
rows = ["A", "B", "C", "D", "E", "F", "G", "H"]

#defines what plate type is at each location on the stage with position 1 being the first item in the list and position 8 being the last
#this includes plates that the plate crane will move into place once the protocol begins as well as what is placed manually
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
############################ M9 media into dilution plate #############################

'''Phosphorus columns (stock is 10X)
Rows 1-2 should have no media
Rows 3-4 should have 600 uL media
Rows 5-6 should have 900 uL media
Rows 7-8 should have 1050 uL media

the rest of the working volume (1200 uL) is taken up by the treatments themselves to make the desired concentrations

For columnns 1 and 2 in the third through eighth row, different volumes of media are added so that the final M9
volumes will equal what is desired (above). 

Because 2 tips are use and the placement of the first tip determines where the rest aspirate and dispense, the cell that
is set as the destination for the liquid handler skips one row each time. The second tip performs the commands for the 
"skipped" row. This code aspirates and dispenses 100 uL, then 150 uL, then 175 uL across columns 1 and 2 for 3 repetitions 
(given by the j for loop), and this incremental increase goes down the column to create four regions of increasing media volume

The same volumes are put into a row of wells in each column (i) first, then the liquid handler does the same in the next 2 rows,
then this process is repeated 3 times
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
    columns 3-4 every other row starting with the first
C2 cells should have 600 ul media
    columns 3-4 every other row starting with the second
C3 cells should have 900 uL media
    columns 5-6 every other row starting with the first
C4 cells should have 1050 uL media
    columns 5-6 every other row starting with the second
'''

#C2#
'''
For columnns 3 and 4 in every other row starting with the second row, different volumes of media are added so that the final M9
volumes will equal what is desired (above) after 4 repetitions

This code aspirates and dispenses 150 into a row of wells in each column (i) first, then the liquid handler does the same for every other
row going down the columns. The j for loop repeats the process 4 times for a total volume of 600 uL
'''

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
'''
For columnns 5 and 6 in every other row starting with the first row, different volumes of media are added so that the final M9
volumes will equal what is desired (above) after 5 repetitions

This code aspirates and dispenses 180 into a row of wells in each column (i) first, then the liquid handler does the same for every other
row going down the columns. The first j for loop repeats the process 3 times for a total volume of 540 uL. The next sectino of code does the same for 2
repetitions for a total volume of 360 uL, so a total 900 uL is added as desired.

These are split into two different hso files because if they were combined, the total number of steps
would exceed what can be handled by the software
'''

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

#TIPS: at this point 6 tips used#

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
#call this hso twice#

'''
For columnns 5 and 6 in every other row starting with the second row, different volumes of media are added so that the final M9
volumes will equal what is desired (above) after 6 repetitions

This code aspirates and dispenses 175 into a row of wells in each column (i) first, then the liquid handler does the same for every other
row going down the columns. The j for loop repeats the process 3 times for a total volume of 525 uL. The hso is called twice, giving a
total volume of 1050 uL as desired

These are split into two different hso files because if they were combined, the total number of steps
would exceed what can be handled by the software
'''

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
'''
This code makes 4 transfers (j for loop) of 150 uL to column 8 in the dilution plate from the same column of the
stock media plate. This adds to a volume of 600 uL as desired
'''

for j in range(1,5):
    transfer_volume = 150
    soloSoft.aspirate(
        position = stock_M9,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(8, transfer_volume),
        aspirate_shift = [0, 0, 2],
        dispense_height = dispenseHeight,
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
'''
This code makes 5 transfers (j for loop) of 180 uL to column 9 in the dilution plate from the same column of the
stock media plate. This adds to a volume of 900 uL as desired
'''

for j in range(1,6):
    transfer_volume = 180
    soloSoft.aspirate(
        position = stock_M9,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(9, transfer_volume),
        aspirate_shift = [0, 0, 2],
        dispense_height = dispenseHeight,
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

#TIPS: uses a column of tips (2 columns used at this point and one of another)

soloSoft = SoloSoft(
    filename = "dilution_N_M9_2.hso",
    plateList = plate_list,
    ) 

soloSoft.getTip(tips)

#N4#
'''
This code makes 6 transfers (j for loop) of 175 uL to column 10 in the dilution plate from the same column of the
stock media plate. This adds to a volume of 1050 uL as desired
'''

for j in range(1,7):
    transfer_volume = 175
    soloSoft.aspirate(
        position = stock_M9,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(10, transfer_volume),
        aspirate_shift = [0, 0, 2],
        dispense_height = dispenseHeight,
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
'''
This code makes 9 transfers (j for loop) of 125 uL to column 11 in the dilution plate from columns 11 and 12 of the
stock media plate. This adds to a volume of 1125 uL as desired

This takes 500 uL (4 x 125) from column 11 of the stock media plate and 625 (5 x 125) from column 12 because
taking all 1125 uL from the same column would result in too little media remaining by the final transfer. This
could result in an inaccurate volume being trasferred, so it was split into two sections
'''

for j in range(1,5):
    transfer_volume = 125
    soloSoft.aspirate(
        position = stock_M9,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(11, transfer_volume),
        aspirate_shift = [0, 0, 2],
        dispense_height = dispenseHeight,
        syringe_speed = syringeSpeed,        
        )
    soloSoft.dispense(
        position = dilution,
        dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(11, transfer_volume),
        dispense_shift = [0, 0, 2],
        #  #dispense_height = dispenseHeight,
        syringe_speed = syringeSpeed,
        )

for j in range(1,6):
    transfer_volume = 125
    soloSoft.aspirate(
        position = stock_M9,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(12, transfer_volume),
        aspirate_shift = [0, 0, 2],
        dispense_height = dispenseHeight,
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

#TIPS: uses a column of tips (3 columns used at this point and one of another)

############################Treatments into dilution plate#############################

#Phosphorus
'''
P1 at 10X, P2 at 5X, P3 at 2.5X, P4 at 1.25X

Rows 1-2 should have 1200 uL P
Rows 3-4 should have 600 uL P
Rows 5-6 should have 300 uL P
Rows 7-8 should have 150 uL P
'''

soloSoft = SoloSoft(
    filename = "dilution_P_treatment_1.hso",
    plateList = plate_list,
    ) 

soloSoft.getTip(position=tips, num_tips=2)

transfer_volume = 150

#for P4#
'''
This code makes a transfer of 150 uL (transfer_volume) to columns 1 and 2 (i) with the first tip being set in row G.
This uses two tips, so the second tip makes the transfer to the following row, row H
'''

for i in range(1,3):
    soloSoft.aspirate(
        position = stock_treatments,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell('G', 9, transfer_volume),
        aspirate_shift = [0, 0, 2],
        mix_at_start = True,
        mix_cycles = mixCycles,
        mix_volume = mixVolume,
        dispense_height = dispenseHeight,
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
'''
This code makes a transfer of 150 uL (transfer_volume) to columns 1 and 2 (i) with the first tip being set in row E.
This uses two tips, so the second tip makes the transfer to the following row, row F

This is repeated twice via the j for loop to transfer a total volume of 300 uL to each of these wells
'''

for j in range(1,3):
    for i in range(1,3):
        soloSoft.aspirate(
            position = stock_treatments,
            aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell('E', 9, transfer_volume),
            aspirate_shift = [0, 0, 2],
            mix_at_start = True,
            mix_cycles = mixCycles,
            mix_volume = mixVolume,
            dispense_height = dispenseHeight,
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
'''
This code makes a transfer of 150 uL (transfer_volume) to columns 1 and 2 (i) with the first tip being set in row C.
This uses two tips, so the second tip makes the transfer to the following row, row D

This is repeated 4 times via the j for loop to transfer a total volume of 600 uL to each of these wells
'''

for j in range(1,5):
    for i in range(1,3):
        soloSoft.aspirate(
            position = stock_treatments,
            aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell('C', i+8, transfer_volume),
            aspirate_shift = [0, 0, 2],
            mix_at_start = True,
            mix_cycles = mixCycles,
            mix_volume = mixVolume,
            dispense_height = dispenseHeight,
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

#TIPS: uses 2 tips (3 columns and 3 of a fourth column used at this point)

soloSoft = SoloSoft(
    filename = "dilution_P_treatment_2.hso",
    plateList = plate_list,
    ) 

soloSoft.getTip(position=tips, num_tips=2)

transfer_volume = 150

#for P1#
'''
This code makes a transfer of 150 uL (transfer_volume) to columns 1 and 2 (i) with the first tip being set in row A.
This uses two tips, so the second tip makes the transfer to the following row, row B

This is repeated 8 times via the j for loop to transfer a total volume of 1200 uL to each of these wells

The expression:
    ((j-1)//2) + 9
is used to aspirate P from columns 9, 10, 11, then 12. The first repetition (j = 1) makes the expression equal to 9, so 150 uL is aspirated from
column 9. The second repetition is the same. The third repetition (j = 3) makes the expression equal to 10, so 150 uL is aspirated from column 10 instead.
This pattern repeats and takes 300 ul from each of the 4 columns instead of taking 1200 from a single one

This prevents too much volume from being taken from the same columns, which could result in running out of treatment or leaving too little treatment
in the column for the liquid handler to take up the necessary amount.
'''

for j in range(1,9):
    for i in range(1,3):
        soloSoft.aspirate(
            position = stock_treatments,
            aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell('A', ((j-1)//2) + 9, transfer_volume),
            aspirate_shift = [0, 0, 2],
            mix_at_start = True,
            mix_cycles = mixCycles,
            mix_volume = mixVolume,
            dispense_height = dispenseHeight,
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

#TIPS: uses 2 tips (3 columns and 5 of fourth column used at this point)

#Carbon

soloSoft = SoloSoft(
    filename = "dilution_C_treatment_1.hso",
    plateList = plate_list,
    )

soloSoft.getTip(position=tips, num_tips=1)
'''
This code makes a transfer of 150 uL (transfer_volume) to columns 5 and 6 (i) from column 1. The tip aspirates from
and dispenses into rows B, D, F, H. 
'''
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
            dispense_height = dispenseHeight,
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
'''
This code makes a transfer of 150 uL (transfer_volume) to columns 5 and 6 (i) from column 1. The tip aspirates from
and dispenses into rows A, C, E, G. 

This is repeated 2 times via the j for loop to transfer a total volume of 300 uL to each of these wells
'''
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
                dispense_height = dispenseHeight,
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

#prepping C2 cells (5X)
soloSoft = SoloSoft(
    filename = "dilution_C_treatment_2.hso",
    plateList = plate_list,
    )

soloSoft.getTip(position=tips, num_tips=1)
'''
This code makes a transfer of 150 uL (transfer_volume) to columns 3 and 4 (i) from column 1 and 2 respectively. The tip aspirates from
and dispenses into rows B, D, F, H. 

This is repeated 4 times via the j for loop to transfer a total volume of 600 uL to each of these wells
'''
for j in range(1,5):
    for row in rows[1::2]:
        for i in range(3,5):
            transfer_volume = 150
            soloSoft.aspirate(
                position = stock_treatments,    
                aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell(row, i-2, transfer_volume),
                aspirate_shift = [0, 0, 2],
                mix_at_start = True,
                mix_cycles = mixCycles,
                mix_volume = mixVolume,
                dispense_height = dispenseHeight,
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

#TIPS: uses 1 tip (3 columns and 7 of fourth column used at this point)


soloSoft = SoloSoft(
    filename = "dilution_C_treatment_3.hso",
    plateList = plate_list,
    )

soloSoft.getTip(position=tips, num_tips=1)
'''
This code makes a transfer of 150 uL (transfer_volume) to columns 3 and 4 (i) from column 1 and 2 respectively. The tip aspirates from
and dispenses into rows A, C, E, G. 

This is repeated 4 times via the j for loop to transfer a total volume of 600 uL to each of these wells
'''
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
                dispense_height = dispenseHeight,
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

#TIPS: 4 whole columns used at this point#
'''
This code makes a transfer of 150 uL (transfer_volume) to columns 3 and 4 (i) from column 1 and 2 respectively. The tip aspirates from
B, D, F, and H and dispenses into rows A, C, E, G respectively. 

This is repeated 4 times via the j for loop to transfer a total volume of 600 uL to each of these wells
'''
soloSoft = SoloSoft(
    filename = "dilution_C_treatment_4.hso",
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
                aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell(rows[rows.index(row)+1], i, transfer_volume),
                aspirate_shift = [0, 0, 2],
                mix_at_start = True,
                mix_cycles = mixCycles,
                mix_volume = mixVolume,
                dispense_height = dispenseHeight,
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

#TIPS: uses 1 tip (4 columns and 1 of another column used at this point)


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
'''
This code makes a transfer of 75 uL (transfer_volume) to column 11 from column 5.  
'''
soloSoft.aspirate(
    position = stock_treatments,
    aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(5, transfer_volume*0.5),
    aspirate_shift = [0, 0, 2],
    mix_at_start = True,
    mix_cycles = mixCycles,
    mix_volume = mixVolume,
    dispense_height = dispenseHeight,
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
'''
This code makes a transfer of 150 uL (transfer_volume) to column 10 from column 5.  
'''
#150 uL#
soloSoft.aspirate(
    position = stock_treatments,
    aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(5, transfer_volume),
    aspirate_shift = [0, 0, 2],
    mix_at_start = True,
    mix_cycles = mixCycles,
    mix_volume = mixVolume,
   dispense_height = dispenseHeight,
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
'''
This code makes a transfer of 150 uL (transfer_volume) to column 9 from column 5.

This is repeated 2 times via the j for loop to transfer a total volume of 300 uL to each of these wells
'''
for j in range(1,3):
    soloSoft.aspirate(
        position = stock_treatments,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(5, transfer_volume),
        aspirate_shift = [0, 0, 2],
        mix_at_start = True,
        mix_cycles = mixCycles,
        mix_volume = mixVolume,
        dispense_height = dispenseHeight,
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

#TIPS: uses 1 column (5 colums used at this point and one of another)

###N2####
'''
This code makes a transfer of 150 uL (transfer_volume) to column 8 from column 6.

This is repeated 4 times via the j for loop to transfer a total volume of 600 uL to each of these wells
'''
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
        dispense_height = dispenseHeight,
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

#TIPS: uses 1 column (6 colums used at this point and one of another)

######N1#######

soloSoft = SoloSoft(
    filename = "dilution_N_treatment_3.hso",
    plateList = plate_list,
    ) 

soloSoft.getTip(tips)
'''
This code makes a transfer of 150 uL (transfer_volume) to column 7 from column 7 four times and column 8 the other four times.

This is repeated 8 times via the j for loop to transfer a total volume of 1200 uL to each of these wells
'''
for j in range(1,9):
    transfer_volume = 150
    soloSoft.aspirate(
        position = stock_treatments,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(((j-1)//4)+7, transfer_volume),
        aspirate_shift = [0, 0, 2],
        mix_at_start = True,
        mix_cycles = mixCycles,
        mix_volume = mixVolume,
        dispense_height = dispenseHeight,
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

#TIPS: uses 1 column (7 colums used at this point and one of another)

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
'''
This code makes a transfer of 180 uL (transfer_volume) to column 12 from column 7.

This is repeated 5 times via the j for loop to transfer a total volume of 900 uL to each of these wells
'''
for i in range(1,6):
    soloSoft.aspirate(
        position = stock_M9,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(7, 180),
        aspirate_shift = [0, 0, 2],
        dispense_height = dispenseHeight,
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

#TIPS: uses 1 column of tips#

#C#
c_control_volume = 120
'''
This code makes a transfer of 120 uL (transfer_volume) to column 12 from column 4.
'''
soloSoft.getTip(tips)

soloSoft.aspirate(
    position = stock_treatments,
    aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(4, c_control_volume),
    aspirate_shift = [0, 0, 2],
    mix_at_start = True,
    mix_cycles = mixCycles,
    mix_volume = mixVolume,
    dispense_height = dispenseHeight,
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

#TIPS: uses 1 column (2 columns used at this point)

#P#
p_control_volume = 120
'''
This code makes a transfer of 120 uL (transfer_volume) to column 12 from column 12.
'''
soloSoft.getTip(tips)

soloSoft.aspirate(
    position = stock_treatments,
    aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(12, p_control_volume),
    aspirate_shift = [0, 0, 2],
    mix_at_start = True,
    mix_cycles = mixCycles,
    mix_volume = mixVolume,
    dispense_height = dispenseHeight,
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

#TIPS: uses 1 column (3 columns used at this point)

#N#
n_control_volume = 60
'''
This code makes a transfer of 60 uL (transfer_volume) to column 12 from column 5.
'''
soloSoft.getTip(tips)

soloSoft.aspirate(
    position = stock_treatments,
    aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(5, n_control_volume),
    aspirate_shift = [0, 0, 2],
    mix_at_start = True,
    mix_cycles = mixCycles,
    mix_volume = mixVolume,
    dispense_height = dispenseHeight,
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

#TIPS: uses 4 columns of tips total in this hso

#############################cells to assay##########################
'''
The following code transfers cells to the final assay plate, 80 uL per well (cells_volume). 
Uses 8 tips (1 column) for colums 1 through 5 of the assay plate and another column of tips for columns 7 through 11 of the assay plate. 
'''
#start with its own new tip box so that adding adding additional plates can be done easily without extra math to see how many tips are used#

'''
This code makes a transfer of 80 uL (transfer_volume) of cells from and to columns 1-5 respectively .
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
        dispense_height = dispenseHeight,
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

#TIPS: uses 1 column of tips

soloSoft = SoloSoft(
    filename = "cells_assay_2.hso",
    plateList = plate_list,
    ) 

soloSoft.getTip(tips)
'''
This code makes a transfer of 80 uL (transfer_volume) of cells from and to columns 7-12 respectively
'''
for i in range(7,12):   
    soloSoft.aspirate(
        position = cells,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(i, cells_volume),
        aspirate_shift = [0, 0, 2],
        mix_at_start = True,
        mix_cycles = mixCycles,
        mix_volume = mixVolume,
        dispense_height = dispenseHeight,
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

#TIPS: uses 1 column of tips (2 columns used at this point)
'''
The following code transfers the control column from the dilution plate (column 12) to the assay plate (colum 6 and 12). 
This is repeated 2 times via the j for loop to transfer a total volume of 180 uL to each well. Uses 8 tips per loop for a total of two columns. 
'''

soloSoft = SoloSoft(
    filename = "control_assay.hso",
    plateList = plate_list,
    ) 

#dilution to assay
for j in range(1,3):
    soloSoft.getTip(tips)
    soloSoft.aspirate(
        position = dilution,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(12, 180),
        aspirate_shift = [0, 0, 2],
        mix_at_start = True,
        mix_cycles = mixCycles,
        mix_volume = mixVolume,
        dispense_height = dispenseHeight,
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
    soloSoft.shuckTip()

#TIPS: uses 2 columns (4 columns used at this point)

soloSoft.savePipeline()

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

transfer_volume = 20
'''
This code makes a transfer of 20 uL (transfer_volume) to columns 1-5 from column 1.

This is repeated 2 times via the j for loop to transfer a total volume of 40 uL to each of these wells
'''
#for i in range(1,6):
for j in range(1,3):
    soloSoft.getTip(tips)
    soloSoft.aspirate(
        position = dilution,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(1, transfer_volume*5),
        aspirate_shift = [0, 0, 2],
        mix_at_start = True,
        mix_cycles = mixCycles,
        mix_volume = mixVolume,
        dispense_height = dispenseHeight,
        syringe_speed = syringeSpeed,
        ) 
    for i in range(1,6):
        soloSoft.dispense(
            position = assay,
            dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(i, transfer_volume),
            dispense_shift = [0, 0, 2],
            #mix_at_finish = True,
            #mix_cycles = mixCycles,
            #mix_volume = mixVolume,
            aspirate_height = aspirateHeight,
            syringe_speed = syringeSpeed,
            )
    soloSoft.shuckTip()
'''
This code makes a transfer of 20 uL (transfer_volume) to columns 7-12 from column 2.

This is repeated 2 times via the j for loop to transfer a total volume of 40 uL to each of these wells
'''
for j in range(1,3):
    soloSoft.getTip(tips)
    soloSoft.aspirate(
        position = dilution,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(2, transfer_volume*5),
        aspirate_shift = [0, 0, 2],
        mix_at_start = True,
        mix_cycles = mixCycles,
        mix_volume = mixVolume,
        dispense_height = dispenseHeight,
        syringe_speed = syringeSpeed,
        ) 
    for i in range(7,12):
        soloSoft.dispense(
            position = assay,
            dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(i, transfer_volume),
            dispense_shift = [0, 0, 2],
            #mix_at_finish = True,
            #mix_cycles = mixCycles,
            #mix_volume = mixVolume,
            aspirate_height = aspirateHeight,
            syringe_speed = syringeSpeed,
            )
    soloSoft.shuckTip()

soloSoft.savePipeline() 

#TIPS: uses 4 column of tips (8 columns used at this point)

##########Carbon####### 
#######Starting a new SoloSoft for carbon on the first half of the assay plate######
soloSoft = SoloSoft(
    filename = "dilution_assay_C_1.hso",
    plateList = plate_list,
    ) 

transfer_volume = 20 
'''
This code makes a transfer of 20 uL (transfer_volume) to columns 5,4,3,2,1 (in this order) from column 3.

This is repeated 2 times via the j for loop to transfer a total volume of 40 uL to each of these wells
'''
for j in range(1,3):
    soloSoft.getTip(tips)
    soloSoft.aspirate(
        position = dilution,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(3, transfer_volume*5),
        aspirate_shift = [0, 0, 2],
        mix_at_start = True,
        mix_cycles = mixCycles,
        mix_volume = mixVolume,
        dispense_height = dispenseHeight,
        syringe_speed = syringeSpeed,
        ) 
    for i in reversed(range(1,6)):
        soloSoft.dispense(
            position = assay,
            dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(i, transfer_volume),
            dispense_shift = [0, 0, 2],
            #mix_at_finish = True,
            #mix_cycles = mixCycles,
            #mix_volume = mixVolume,
            #aspirate_height = aspirateHeight,
            syringe_speed = syringeSpeed,
            )
    soloSoft.shuckTip()

soloSoft.savePipeline() 

#TIPS: uses 2 columns of tips (10 used at this point)

#######Starting a new SoloSoft for carbon on the second half of the assay plate######
soloSoft = SoloSoft(
    filename = "dilution_assay_C_2.hso",
    plateList = plate_list,
    ) 

transfer_volume = 20 
'''
This code makes a transfer of 20 uL (transfer_volume) to columns 12,11,10,9,8,7 from column 5.

This is repeated 2 times via the j for loop to transfer a total volume of 40 uL to each of these wells
'''

for i in range(1,3):
    soloSoft.getTip(tips)
    soloSoft.aspirate(
        position = dilution,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(5, transfer_volume*5),
        aspirate_shift = [0, 0, 2],
        mix_at_start = True,
        mix_cycles = mixCycles,
        mix_volume = mixVolume,
        dispense_height = dispenseHeight,
        syringe_speed = syringeSpeed,
        ) 
    for i in reversed(range(7,12)):
        soloSoft.dispense(
            position = assay,
            dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(i, transfer_volume),
            dispense_shift = [0, 0, 2],
            #mix_at_finish = True,
            #mix_cycles = mixCycles,
            #mix_volume = mixVolume,
            aspirate_height = aspirateHeight,
            syringe_speed = syringeSpeed,
            )
    soloSoft.shuckTip()

soloSoft.savePipeline() 

#TIPS: uses 2 column of tips (12 columns used at this point) EMPTY
#GET NEW TIP BOX HERE#

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
        dispense_height = dispenseHeight,
        syringe_speed = syringeSpeed,
        ) 
    soloSoft.dispense(
        position = assay,
        dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(i, transfer_volume),
        dispense_shift = [0, 0, 2],
        mix_at_finish = True,
        mix_cycles = mixCycles,
        mix_volume = mixVolume,
        aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,
        )
    soloSoft.shuckTip()

soloSoft.savePipeline() 

#TIPS: uses 5 column of tips
'''
This code makes a transfer of 20 uL (transfer_volume) to and from columns 12,11,10,9,8,7 respectively.
'''
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
        dispense_height = dispenseHeight,
        syringe_speed = syringeSpeed,
        ) 
    soloSoft.dispense(
        position = assay,
        dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(i, transfer_volume),
        dispense_shift = [0, 0, 2],
        mix_at_finish = True,
        mix_cycles = mixCycles,
        mix_volume = mixVolume,
        aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,
        )
    soloSoft.shuckTip()

soloSoft.savePipeline() 

#TIPS: uses 5 columns of tips (10 columns used at this point)

##############################################################
'''
This is the Softlinx part of the code that entails the crane 
movements as well as the execution of the hso files
'''

softLinx = SoftLinx("Fourth_attempt", "C:\\Users\\svcaibio\\Dev\\Summer_stduents\\rpl-summer-2022\\gillian\\Fourth_attempt.slvp") # display name, path to saves

softLinx.setPlates({"SoftLinx.PlateCrane.Stack5": "Plate.96.Corning-3635.ClearUVAssay", "SoftLinx.PlateCrane.Stack4":"TipBox.50uL.Axygen-EV-50-R-S.tealbox"})
#this is where you would softlinx run solo stuff, preparing diltuion stock (fill stuff in)###############

softLinx.plateCraneMovePlate(["SoftLinx.PlateCrane.Stack4"],["SoftLinx.Solo.Position3"],poolID = 4)

softLinx.plateCraneMoveCrane("SoftLinx.PlateCrane.Safe")


list_of_dilution = ["dilution_P_M9_1.hso", "dilution_P_M9_1.hso", "dilution_C_M9_1.hso", 
                    "dilution_C_M9_2.hso", "dilution_C_M9_3.hso", "dilution_C_M9_4.hso", 
                    "dilution_C_M9_4.hso", "dilution_N_M9_1.hso", "dilution_N_M9_2.hso", 
                    "dilution_P_treatment_1.hso", "dilution_P_treatment_2.hso", 
                    "dilution_C_treatment_1.hso", "dilution_C_treatment_2.hso", 
                    "dilution_C_treatment_3.hso", "dilution_C_treatment_4.hso", 
                    "dilution_N_treatment_1.hso", "dilution_N_treatment_2.hso", 
                    "dilution_N_treatment_3.hso", "dilution_control.hso"]

for c in list_of_dilution:
     softLinx.soloSoftRun(Path+c)

''' In order to prepare plates in triplicate, we use a for loop to run the code 3 times
Note: Only the code that prepares the assay plate and the plate crane movements that are responsible 
for moving the plate to Hidex and the incubator are in this loop'''

for i in range(1,4):
    softLinx.plateCraneMovePlate(["SoftLinx.Solo.Position3"],["SoftLinx.PlateCrane.Stack2"],poolID = 2)
    softLinx.plateCraneMovePlate(["SoftLinx.PlateCrane.Stack5"],["SoftLinx.Solo.Position4"],poolID = 5)
    softLinx.plateCraneRemoveLid(["SoftLinx.Solo.Position4"],["SoftLinx.PlateCrane.LidNest2"])

    softLinx.plateCraneMovePlate(["SoftLinx.PlateCrane.Stack4"],["SoftLinx.Solo.Position3"],poolID = 4)
    softLinx.plateCraneMoveCrane("SoftLinx.PlateCrane.Safe")

    '''
    prepare assay plate

    hso files listed to be run in chronological order and divided into a new list once the 
    tip box is empty and needs to be replaced
    '''

    list_of_final_1 = ["cells_assay_1.hso", "cells_assay_2.hso", "control_assay.hso", 
                    "dilution_assay_P_1.hso", "dilution_assay_C_1.hso", "dilution_assay_C_2.hso"]               
    list_of_final_2= ["dilution_assay_N_1.hso", "dilution_assay_N_2.hso"]

    for c in list_of_final_1:
        softLinx.soloSoftRun(Path+c)

    '''
    Plate crane movements:
        remove empty tip box from stage
        place new full tip box on stage
        move plate crane away from possible collision with liquid handler
    '''

    softLinx.plateCraneMovePlate(["SoftLinx.Solo.Position3"],["SoftLinx.PlateCrane.Stack2"],poolID = 2)
    softLinx.plateCraneMovePlate(["SoftLinx.PlateCrane.Stack4"],["SoftLinx.Solo.Position3"],poolID = 4)
    softLinx.plateCraneMoveCrane("SoftLinx.PlateCrane.Safe")

    for c in list_of_final_2:
       softLinx.soloSoftRun(Path+c)

    softLinx.plateCraneMovePlate(["SoftLinx.Solo.Position4"],["SoftLinx.Hidex.Nest"])
    softLinx.plateCraneMoveCrane("SoftLinx.PlateCrane.Safe")
    softLinx.hidexRun("pyhamilton")
    softLinx.plateCraneMovePlate(["SoftLinx.Hidex.Nest"],["SoftLinx.Liconic.Nest"])
    softLinx.hidexClose()
    softLinx.plateCraneReplaceLid(["SoftLinx.PlateCrane.LidNest2"],["SoftLinx.Liconic.Nest"])
    softLinx.plateCraneMoveCrane("SoftLinx.PlateCrane.Safe")
    softLinx.liconicLoadIncubator(loadID=i)
    softLinx.liconicBeginShake(shaker1Speed=30)
    
# Creation loop ends

softLinx.liconicShake(shaker1Speed=30, shakeTime=[0,11,30,0])
#softLinx.liconicShake(shaker1Speed=30, shakeTime=[0,0,0,10])#shaking in the incubator
softLinx.hidexRun("SetTempWait37")
 #reading loop
for plateId in range(1,4):
    softLinx.liconicUnloadIncubator(loadID=plateId)
    softLinx.plateCraneRemoveLid(["SoftLinx.Liconic.Nest"],["SoftLinx.PlateCrane.LidNest2"])
    softLinx.plateCraneMovePlate(["SoftLinx.Liconic.Nest"],["SoftLinx.Hidex.Nest"])
    softLinx.hidexClose()
    softLinx.plateCraneMoveCrane("SoftLinx.PlateCrane.Safe")
    softLinx.hidexRun("pyhamilton")
    softLinx.plateCraneMovePlate(["SoftLinx.Hidex.Nest"],["SoftLinx.PlateCrane.Stack1"])
    softLinx.hidexClose()
    softLinx.plateCraneReplaceLid(["SoftLinx.PlateCrane.LidNest2"],["SoftLinx.PlateCrane.Stack1"])
    softLinx.plateCraneMoveCrane("SoftLinx.PlateCrane.Safe")
    if not plateId == 3:
        softLinx.liconicShake(shaker1Speed = 30, shakeTime=[0,0,20,0])
        #softLinx.liconicShake(shaker1Speed = 30, shakeTime=[0,0,0,5])

softLinx.hidexRun("SetTemp20")
softLinx.liconicEndShake()

softLinx.saveProtocol()

#at this point the layout has been reset so a new plate can be made be repeating the same thing#
