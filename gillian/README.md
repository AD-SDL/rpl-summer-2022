# Gillian Camacho
**Project name:** Pyhamilton Protocol Implementation on Hudson

**Advisor:** Arvind Ramanathan

**Email:** gcamacho@anl.gov

## Project Description
In a recent paper entitled "Flexible open-source automation for robotic engineering" (Chory et al. 2021), a new software package named Pyhamilton was presented which allows the user to program the actions of Hamilton STAR and STARlet liquid handling robots using standard Python. The capabilities of Pyhamilton were demonstrated by preforming several biological experiments including the use of a feedback loop to maintain culture turbidostats and a high-throughput perturbation analysis of metabolites.For this project, we will reproduce one of the biological experiments presented in this paper using the Python interface that has been developed for the Hudson SOLO liquid handler and Hudson SoftLinx integration system. We aim to prove that our completely open-source Python API is capable of executing the same biological experiments as Pyhamilton with similar results. Students on this project will also contribute to the growing library of biological protocols written for our Hudson robotic experimentation platform.

Link to paper: https://pubmed.ncbi.nlm.nih.gov/33764680/

## Diary

### 6/24
* I attended a group recap meeting 
* I presented for journal club and finished the slides for that
* I learned how to add to github and make a pull request
* I downloaded git

### 6/27
* I met with Halona and Arleen to work on the PyHamilton Protocol
* I read and annotated the Chemputer/XDL paper
* I read more of *Machine Learning: A Concise Introduction*

### 6/28
* I met with Halona and Arleen to continue our work from 6/27 and assemble the code we wrote in the right chronological order
* I met with Casey to rework our approach for the coding of preparing the dilution plate
* I read more of *Machine Learning: A Concise Introduction*
* I started the new code for the preparation of the dilution plate and made calculations for the volumes we would use of each treatment and M9 media 

### 6/29
* I wrote code for preparing the dilution plate from stock cells
* I rethought the dilution amounts we would need because our initial idea may be wrong
* I attended a student connects meeting and panel discussion about possible career paths for my internship program

### 6/30
* I updated my dilution plate code to match the new concentration ideas using 20X stock nitrogen, 10X stock carbon, and 10X stock phosphorus with the different corresponding transfer volumes
* I attended a meeting outlining DNA assembly and how it was implemented in the past on the OT-2
* I ran my dilution ideas by Jeff in Bio and he approved it in theory
* I met with Halona and Arleen to edit the rest of our code for the changes we made to the dilution plate setup and cell stock transfer volumes

### 7/01
* I met with Halona and Arleen to create our slides for the recap meeting and touch base on how we felt about the code we made so that we could make any necessary corrections before we tested it (we still need to change the transfer volumes from the dilution plate to assay plate from 33 uL to 40uL)
* I attended this week's group recap meeting and presented about the progress myproject has made
* I attended journal club and took notes on this week's presentation about machine learning and MRIs 

### 7/05
* I found my first 8 papers on DNA assembly and DNA transformation for Priyanka
* I started to write out the procedures of interest from each of the papers I found

### 7/06
* I attended a seminar on delivering effective oral and poster presentations
* I met with Casey, Halona, and Arleen to talk about the progress we have made in our protocol for the Hudson and we scheduled a time to check our hso files and debug the code
* I attended a talk about bacterial protein nanowires
* I met for an update with HR to talk about starting my deliverables and to ask any questions I had
* We all went to 446 to check our code with Abe's help and we decided what we would need to address for correction

### 7/07
* I read the paper that will be presented on in journal club this week
* I attended a github tutorial from Alex Brace
* I calculated how to change the volumes in our protocol to work with the size of pipettes we have available and started rewriting the code in those sections
* I met with Arleen to finish the changes we had to make, and we will keep thinking of ways to make what we wrote shorthand because we were not able to think of any solutions

### 7/08
* I checked the code I wrote on 7/08 for errors and documentation problems
* I met with Halona and Arleen to make our presentation for the recap meeting at 11:00
* I attended the group recap meeting and journal club presentatinos

### 7/11
* I wrote protocol for a paper I found for Priyanka
* I met with Arleen and Halona to decide when we would need to refill tip boxes in our pyhamilton protocol and also recheck the math for the dilutions I made
* We all went to the bio building 446 to test our code in the lab, which involved making sure the code had no errors, making sure the hso files had less than 72 steps each, and seeing how the robot carried out what we called for. It was successful overall, we just have to make a change to use one full plate of M9 and one full plate of stock treatments instead of letting them split a plate. While we were there we also defined the deep well plates correctly and defined the position of the stock plate and the size of tips we were using

### 7/12
* I met with Halona and Arleen to mke the changes we discussed: adding a stock M9 plate, rearranging where the plates are on the stage, etc.
* We all went back to bio to test the new code using water
* While at bio, we changed the aspirate and dispense heights to make mixing more fluid and we noted some problem areas we may have to look closer at in the code
* I wrote protocols for a second paper for Priyanka and started working on a third

### 7/13
* I finished the protocols I was writing for Priyanka's third and fourth papers
* I attended a seminar about the deliverables required by my internship
* I attended a talk about using cardiac muscle cells to form an oscillator and to use it in computing
* I attended a student connects meeting where we talked about the progress of our respective projects
* I fixed the pyhamilton protocol to make sure that none of the wells would be aspirated too many times so that they would be empty

### 7/14
* I wrote a protocol for a fifth paper for Priyanka and will complete it on 7/15
* I attended a talk from the materials science division about lithiation in newly developed cathodes
* I started working on my poster for Learning on the Lawn. I just about completed the motivations and future directions sections but I am waiting for a full test of our protocol on 7/15 to write much more in the progress section. I intend to have a draft completed by 7/18 so that I can meet with Arvind and others for feedback
* I attended a Learn Something New meeting where Rory talked about computer vision, graphics, and some python skills

### 7/15
* I met with Halona and Arleen to make our presentation for the weekly update meeting
* I finished the protocol I was writing for Priyanka and uploaded all of my finished papers and procedures to the XDL Box folder we are using
* I started working on the 150 word abstract for the poster presentation which I would also like to have a complete draft for by the start of next week so that I can meet with Bob to get feedback
* I met with Priyanka to talk about the progress I've made for the XDL project and to discuss how I should continue going about writing protocols
* We all tested out protocol using water and food dye to see how well it would run from top to bottom. It gave us an idea of where improvements can be made like moving the plate crane to safe after changing tip boxes, so we will meet next week to make edits. Overall it was a successful first run

### 7/18
* I worked more on my poster
* I attended a talk about nitrogen vacancies in diamonds
* I attended a talk about using deep learning to model fluid dynamics
* I made the changes to the pyhamilton protocol and recounted how many tips would be used so that I could restructure where it would be ideal to replace the tip box. I also had to add more tip replacements because I did not want to contaminate the dilution plate with cells
* I met with Arleen and Halona to go through the full code in depth to see where there may be any small errors and we decided it was ready for another test
* I completed a first draft of my poster and sent it out for feedback to Arvind. I am still adding to my motivations section and I want to make a better graphic for the procedure

### 7/19
* I sent my poster draft to Carla for feedback
* I finished a draft of my 150-word abstract and kept thinking of title ideas
* I set up the next test of our code with Casey at 12:30
* We all tested the protocol including three replicate assay plates. There were minor issues with plate definitions and the software slowing down, but it was relatively successful and almost ready to test with the real materials

### 7/20
* I attended a resume workshop and updated my resume to include this internship. I still have changes to make to the format and things to add to make it more representative of my experience level but it is improving
* I finished a second draft of my poster and resent it to Arvind for feedback
* I went through the code and made more detailed comments that describe the procedure as it is supposed to happen
* I sent my poster to Casey for feedback

### 7/21
* I edited my poster with Casey and Arvind's recommendations in mind and finished a new draft of it
* I wrote a protocol for another paper for Priyanka and the XDL project
* I submitted my final poster draft
* I updated my resume

### 7/22
* I met with Arleen and Halona to prepare our presentations for the weekly update meeting
* I attended the RPL weekly update meeting and presented my progress with Arleen
* I went to journal club to discuss poster presentations

### 7/25
* I wrote out protocols for 2 more papers for Priyanka's project
* I met with Arleen to compile a list of reagents needed in our experiment
* We continued documenting our code

### 7/26
* I finished additional updates to my resume and linkedin
* I met with Arleen, Halona, and Casey to test the plate crane movements and time the shaking step so that a second OD reading can be taken after 12 hours
* I met with Arleen to create a README for the protocol

### 7/27
* I added to the README for the protocol
* We ran the protocol in bio on live cells starting at 12:30 and ending at 5:00

### 7/28
* We looked at the data we got from the OD readings and made graphs of our results
* We interpreted the results and found that they do align with what we expected based on the paper, mostly that a deficiency of phosphorus could be rescued by a surplus of carbon but not nitrogen
* I started writing my paper and made an outline of what I want to include in each section
* I started writing a script for the audio recording of my poster presentation I have to do