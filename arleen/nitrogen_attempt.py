#Nitrogen

#N1 should be 20X (1200 uL),N2 should be 10X (600 uL), N3 should be 5X (300 uL), N4 should be 2.5X (150 uL), N5 should be 1.25X (75 uL)

soloSoft = SoloSoft(
    filename = "dilution_N_main.hso",
    plateList = plate_list,
    ) 
soloSoft.getTip(tips) 
#### N5#####
    trasnfer_volume = 75
    soloSoft.aspirate(
        position = stock,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(5, transfer_volume)
        aspirate_shift = [0, 0, 2],
        aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,
        ) 
    soloSoft.dispense(
        position = assay,
        dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(11, transfer_volume),
        dispense_shift = [0, 0, 2],
        dispense_height = dispenseHeight,
        syringe_speed = syringeSpeed,
        )

### N4###
    transfer_volume = 150
    soloSoft.aspirate(
        position = stock,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(5, transfer_volume),
        aspirate_shift = [0, 0, 2],
        aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,        
        )
    soloSoft.dispense(
        position = dilution,
        dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(10, transfer_volume),
        dispense_shift = [0, 0, 2],
        dispense_height = dispenseHeight,
        syringe_speed = syringeSpeed,
        )

###N3####
for j in range(1,3):
    transfer_volume = 150
    soloSoft.aspirate(
        position = stock,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(5, transfer_volume),
        aspirate_shift = [0, 0, 2],
        aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,        
        )
    soloSoft.dispense(
        position = dilution,
        dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(9, transfer_volume),
        dispense_shift = [0, 0, 2],
        dispense_height = dispenseHeight,
        syringe_speed = syringeSpeed,
        )
soloSoft.savePipeline() 

###N2####
soloSoft = SoloSoft(
    filename = "dilution_N2_main.hso",
    plateList = plate_list,
    ) 
soloSoft.getTip(tips) 
for j in range(1,5):
    transfer_volume = 150
    soloSoft.aspirate(
        position = stock,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(5, transfer_volume),
        aspirate_shift = [0, 0, 2],
        aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,        
        )
    soloSoft.dispense(
        position = dilution,
        dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(8, transfer_volume),
        dispense_shift = [0, 0, 2],
        dispense_height = dispenseHeight,
        syringe_speed = syringeSpeed,
        )
soloSoft.savePipeline()

######N1#######
soloSoft = SoloSoft(
    filename = "dilution_N3_main.hso",
    plateList = plate_list,
    ) 
soloSoft.getTip(tips)
for j in range(1,9):
    transfer_volume = 150
    soloSoft.aspirate(
        position = stock,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(5, transfer_volume),
        aspirate_shift = [0, 0, 2],
        aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,        
        )
    soloSoft.dispense(
        position = dilution,
        dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(7, transfer_volume),
        dispense_shift = [0, 0, 2],
        dispense_height = dispenseHeight,
        syringe_speed = syringeSpeed,
        )
soloSoft.savePipeline()