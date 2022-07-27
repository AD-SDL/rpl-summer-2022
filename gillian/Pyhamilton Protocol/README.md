# Pyhamilton Protocol
Gillian Camacho, Halona Dantes, Arleen Hidalgo

## Objective
This code runs an automated assay on replicated plates so that *E. coli* cells will be grown in 80 different nutrient environments. The environments differ based on their relative nutrient compositions, and they each contain different concentrations of Carbon, Nitrogen, and Phosphorus. Optical density measurements taken at the initial plate creation and after a 12 hour growth period, which are used to compare how the cells react to each condition.

## Outline 
The outline of the code for this consists of 3 sections:
- making the dilution plate
- transferring cells into the assay plate
- transferring nutrients from the dilution plate to the assay plate 

### Deck Layout
Position 1 = stock treatments 
Position 2 = empty
Position 3 = tips 
Position 4 = assay plate 
Position 5 = stock M9 
Position 6 = dilution plate 
Position 7 = stock cells plate 
Position 8 = empty

### Nutrient Information
**Carbon**: 10X stock is used, and is contained in columns 1-4 of the "stock treatments" plate
**Nitrogen**: 20X stock is used and is contained in columns 5-8 of the "stock treatments" plate
**Phosphorus**: 10X stock is used and is contained in columns 9-12 of the "stock treatments" plate

### Plate Information
All stock materials are contained in