# Halona Dantes
**Project name:** Computer Vision/ PyHamilton Protocol Implementation
**Advisor:** Arvind Ramanathan
**Email:** hdantes@anl.gov
## Project Description
**Vision**
Our main goal is finding the presence and location of key objects in the image, to measure if the robot has picked up or moved the correct hardware in the scene. The network should be able to identify different key items depending on the training data, yet be robust to visual interference caused by other objects in the scene and backgrounds and lighting conditions. Our secondary goal is training a network to analyze a material such as liquid in a beaker, the contents of a pipette, or textured objects like a used petri dish. This network should be able to classify the object into predefined categories to inform the robot of the current experimental progress. This network will also need to be robust to visual interference from the scene.
**PyHamilton**
The goal is to reproduce one of the biological experiments presented in the PyHamilton paper using the Python interface that has been developed for the Hudson SOLO liquid handler and Hudson SoftLinx integration system. We aim to prove that our completely open-source Python API is capable of executing the same biological experiments as Pyhamilton with similar results. Students on this project will also contribute to the growing library of biological protocols written for our Hudson robotic experimentation platform. <u>*Any task that mentions PyHamilton is done in collaboration with Arleen Hidalgo and Gillian Camacho.*<u>
## 6/24
* I made a folder on the repo
* I went through a tutorial on Pytorch
* This is a change for pull request

https://user-images.githubusercontent.com/72309881/175628210-b9f65c51-b90b-44b9-a1fe-e694d0bfb19b.mp4

## 6/27
### To Do:
* Go through more tutorials on Neural Network
* Meet up with Gillian and Arleen to work on PyHamilton protocol
* Read YOLO paper
* Start working on Sci-kit dataset
* Update Github daily log
### Tasks Accomplished
* Read YOLO paper
* Completed coding for transfer from cells and dilution assay to final assay plate
* Read XDL paper
## 6/28
### To Do:
* Work with Gillian and Arleen on the PyHamilton code
### Tasks Accomplished
* Coded steps for preparing final assay plate
* Had a meeting with Casey to discuss progress
## 6/29
### To Do:
* Finish up with code for PyHamilton
* Play around with the NUC and neural networks
### Tasks Accomplished:
* Mapped out the movements of the liquid handler and wrote code for dilution assay 
## 6/30
### To Do:
* Play around with the NUC
* Finish the code for PyHamilton
### Tasks Accomplished:
* Finished code for transfer from dilution to final assay
* Read through transfer learning tutorials
* Looked at neural networks dealing with iris dataset
## 7/1
### To Do:
* Finish assembling the code
* Meet Rory to understand more about implementing neural networks on the NUC
### Tasks Accomplished:
* Attended journal club
* Completed third attempt at writing the PyHamilton code
* Had a meeting with Rory
## 7/5
### To Do: 
* Research models: understand what kind of models we are looking for
*  Work on one paper for Priyanka's project
*  Work on Journal Club presentation
### Tasks Accomplished:
* Researched models and found YOLO was common and easy to use
## 7/6
### To Do:
* Read more about YOLOx and research other models
* Read journal paper again
### Tasks Accomplished:
* Read more about YOLOx and StreamYOLO
* Checked hso files on the SoloSoft and fixed some mistakes
* Read journal article
## 7/7
### To Do:
* Prepare journal club slides
* Finalize on which model you will use and tell Rory
### Tasks Accomplished:
* Finished and practiced Journal Club presentation with Arleen
## 7/11
### To Do:
* Select two papers for Priyanka and work on them
* Select a pre-trained model
* Start pre-processing images
### Tasks AccomplishedL
* Worked on two papers for Priyanka
* Chose YOLO for the pre-trained model
* We tested the hso files on the Hudson robot in Bld 446
## 7/12
### To Do:
* Meet Rory today to talk about pre-processing
* Work on code
### Tasks Accomplished:
* We worked on the volumes of the deep well
## 7/13
### To Do:
* Work on pre-processing
* Work on Priyanka's papers
### Tasks Accomplished:
* Worked on understanding yolov5 and played around with its github
* Worked on Priyanka's papers
## 7/14
### To Do:
* Work out how to pre-process the images (make a python script for the labels)
* Work on Priyanka's papers
### Tasks Accomplished:
* Was able to find code that converts the Unity json files to YOLO-readable files
* Worked on creating a yaml file for the Unity images
* Worked on Priyanka's paper
## 7/15
### To Do:
* Work on yolov5
* Meet Priyanka
* Work on complete trial run of PyHamilton
### Tasks Accomplished:
* Met Priyanka to discuss papers
* Worked on complete trial run of PyHamilton
* Worked on yolov5 and was able to train on boxes and balls dataset and OT_1 dataset
<img width="347" alt="image" src="https://user-images.githubusercontent.com/72309881/179525217-097b4d7a-fdb8-49cd-bbb5-4b146a61e76c.png">

## 7/18
### To Do:
* Work on poster
### Tasks Accomplished:
* Worked on poster
* Met Rory and Saaya to talk about Vision
## 7/19
### To Do:
* Work on poster
* Run code for PyHamilton on Hudson
### Tasks Accomplished:
* Worked on first draft of poster
* We successfully ran the code on Hudson
* Trained network for 100 epochs to get data for poster

<img width="347" alt="image" src="https://user-images.githubusercontent.com/72309881/180072938-d7341050-b66a-4143-98ac-c78a8e5aa3ee.jpg">
<img width="347" alt="image" src="https://user-images.githubusercontent.com/72309881/180074104-11857804-8a0a-42ef-9bd3-2081d5640851.jpg">




## 7/20
### To Do:
* Finish poster
* Work on getting more data (training on new dataset) for data
### Tasks Accomplished:
* Finished poster
* Trained on OT_2

## 7/21
### To Do:
* Finish and submit poster
* Meet Saaya to talk about automating making yaml file and training using YOLO
### Tasks Accomplished:
* Submitted poster
* Met Saaya and went over automating yaml file (approach)
* Met Arvind with Rory and Saaya to talk about YOLO

## 7/22
### To Do:
* Work on student meeting presentation
### Tasks Accomplished:
* Worked and presented student meeting presentation

## 7/25
### To Do:
* Work on documentation of PyHamilton code
* Work on Priyanka's papers
* Work on automating yaml file
### Tasks Accomplished:
* Worked on two papers for Priyanka
* Worked on detecting pipettes in a video
## 7/26
### To Do:
* Read papers for Fellowship
* Work on automating files with Saaya
* Work on researching ways to improve precision of data
* Meet Casey with Gillian and Arleen at Bio
* Start working on paper
### Tasks Accomplished:
* Read papers for Fellowship
* Completed creating a script that automates making yaml files
* Met Casey with Gillian and Arleen in Bio and checked plane crane movements for PyHamilton
## 7/27
### To Do:
* Work on poster presentation script
* Work on finding ways to improve the hyperparameters 
* Meet Casey with Gillian and Arleen and run a complete trial of our code
* Start working on paper
### Tasks Accomplished:
* Worked on poster presentation script
* Worked on research report
* Ran a complete trial on Hudson with Camacho and Hidalgo
* Worked on detecting pipettes in a video of the OT-2
## 7/28
### To Do:
* Work on paper
* Work on poster presentation script
* Work on visualizations of Pyhamilton data with Camacho and Hidalgo
### Tasks Accomplished:
* Worked on research report
* Worked on poster presentation script
* Created plots to visualize data with Camacho and Hidalgo


![Results_pyhamilton1](https://user-images.githubusercontent.com/72309881/181627808-028df3a3-4856-4876-9473-0cb9eb9241ec.png)

![Results_pyhamilton2](https://user-images.githubusercontent.com/72309881/181627824-f9628bb8-b99e-4820-879f-10296c0e8287.png)
  
![Results_pyhamilton3](https://user-images.githubusercontent.com/72309881/181627839-6f94cde9-be62-4179-857d-145a0e171801.png)
  
## 7/29
### To Do:
* Work on paper
* Work on poster presentation script
* Work on combining datasets to train 
### Tasks Accomplished:
* Worked on paper
* Worked on poster presentation
## 8/1
### To Do:
* Worked on completing deliverables
* Combininig datasets and training again
### Tasks Accomplished:
* Half-way done with paper
* Combined datasets
## 8/2 
### To Do:
* Work on completing deliverables
### Tasks Accomplished:
* 3/4th way done with the paper
## 8/3
### To Do:
* Attend learning off the lawn
### Tasks Accomplished:
* Attended Learning off the lawn
* Completed Peer Review
## 8/4
### To Do:
* Present at Learning on the Lawn
* Completed all deliverables, yeah!
  


