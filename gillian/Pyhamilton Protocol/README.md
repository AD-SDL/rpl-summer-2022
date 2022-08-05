# Pyhamilton Protocol
Gillian Camacho, Halona Dantes, Arleen Hidalgo

## Objective
This code runs an automated assay on replicated plates so that *E. coli* cells will be grown in 80 different nutrient environments. The environments differ based on their relative nutrient compositions, and they each contain different concentrations of Carbon, Nitrogen, and Phosphorus. Optical density measurements taken at the initial plate creation and after a 14 hour growth period, which are used to compare how the cells react to each condition.

### Deck Layout
Position 1 = stock treatments 

Position 2 = empty

Position 3 = tips 

Position 4 = assay plate 

Position 5 = stock M9 

Position 6 = dilution plate 

Position 7 = stock cells plate 

Position 8 = empty

### Stack Layout
Position 1 = used assay plates

Position 2 = used tip boxes

Position 3 = empty

Position 4 = full tip boxes

Position 5 = unused sterile assay plates with lids

### Nutrient Information
**Carbon**: 10X stock glucose is used, and is contained in columns 1-4 of the "stock treatments" plate

**Nitrogen**: 20X stock ammonium chloride is used and is contained in columns 5-8 of the "stock treatments" plate

**Phosphorus**: 10X stock dibasic sodium phosphate is used and is contained in columns 9-12 of the "stock treatments" plate

### Disposables Used
* Axygen 180 uL filtered pipette tips
* Corning 96-Well CLear Flat Bottom UV-Transparent Microplates
* VWR 96-Well Deep Well Plates

### Automated Equipment
* Hudson Plate Crane
* Hudson SOLO Liquid Handler
* Liconic Automated Incubator
* Hidex Microplate Reader

## Outline 
The outline of the code for this consists of the following sections:
* making the dilution plate
* transferring cells into the assay plate
* transferring nutrients from the dilution plate to the assay plate
* incubating the assay plates


•	Transferring M9 media (volumes depend on the concentration of nutrient assigned) from Position 5 to empty deep well at Position 6
•	Transferring nutrients from Position 1 to Position 6. This concludes the process of making the dilution plate
•	Transferring cells from Position 7 to Position 4
•	Transferring solutions from dilution plate at Position 6 to the final assay plate at Position 4; Column 6 and Column 12 were used as control columns and contained 1X of each nutrient.
•	Moving the final assay plate to the Hidex plate reader and measuring absorbance of wells
•	Moving the final assay plate from the Hidex plate reader to Liconic Incubator
•	Incubating for 13.5 hours
•	Moving the final assay plate to the Hidex plate reader and measuring absorbance of wells
