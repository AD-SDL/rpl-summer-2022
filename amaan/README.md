# Amaan Khan

**Project name:** Robotics Dashboard Web App for Laboratory Monitoring   
**Advisor:** Arvind Ramanathan   
**Email:** amaan.khan@anl.gov   

## Project description
In the secure biosystems lab, there are many robots that are in play. It is very difficult to control and debug all the robots separately using command-line-interfaces. Therefore, I am developing a Web Dashboard App that will allow users to view various data visualizations, log outputs, messages from ROS topics, camera outputs, and being able to control the various robots from the app.

## Daily Log

### Friday, 6.24.22
* Installed ROS on a Ubuntu Virtual Machine
* Weekly Meeting in rpl
* Met with Rory and planned out how to create the publisher/subscriber model with the dasboard
* Journal Club - took notes as the scribe

### Monday, 6.27.22
* Finished writing publisher.py and began writing subscriber.py for having the camera publish frames to a ROS topic and have the subscriber subscribe to the topic and send those camera frames to the dashboard when possible.
* Read on how ROS Workspace Packages work
* Had weekly meeting with Carla, Frank, Dana, and Mariam where we discussed our progress on our projects
* Met with Mariam to decide on a Journal Club article since we are presenting this week.
* Began reading journal club article
* Met with Rory and showed my progress so far, and helped clear any confusion I had. Told me to upload my code under `rpl-camera-vision/rpl_cv/dashbaord`
* **TODO:**    
  - [x] Finish reading journal club article in depth and split up work for presentation with Mariam tomorrow
  - [x] Create directory 'dashboard' under `AD-SDL/rpl-camera-vision/rpl_cv/` and put your dashboard code there
  - [x] Finish writing subscriber.py
  - [x] Create a ROS workspace and package by following this [tutorial](https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace.html#new-directory)

### Tuesday, 6.28.22
* Read journal club article in depth and took notes
* Met with Mariam to split up the work for the journal club presentation
* Rory was able to get `opencv` and `rclpy` python packages working on the NUC so I was able to test out my code and debug issues
* Worked on writing subscriber.py and moved code to rpl-camera-vision repo (have not made a pull request yet - only pushed to my fork for now)

### Wednesday, 6.29.22
* Worked on subscriber.py
* Worked on taking notes for journal club article

### Thursday, 6.30.22
* Finished writing subscriber.py
* Created ROS package and workspace -- ran into an error and spent time debugging it
* Made journal club article presentation

### Friday, 7.1.22
* Made finishing touches on journal club presentation & met with Mariam to go over it
* Weekly RPL Meeting
* Gave journal club presentation

### Tuesday, 7.5.22
* Spent time debugging the ROS package/workspace error
* Had weekly meeting with Carla and team

### Wednesday 7.6.22
* Fixed ROS package/workspace error
* ran into few bugs w/ publisher and subscriber code so spent time on trying to fix them
* Worked on personal website and resume on overleaf since Raf suggested we create a personal website and create resume on overleaf

### Thursday, 7.7.22
* Got publisher & subscriber successfully sending images b/w each other. 
* Met with Rory and we discussed methods to send the data/images from subscriber to the dashboard. Decided to use a socket connection. Rory explained to me how that will work
* Began writing code for the socket server

### Friday, 7.8.22
* Finished writing the socket server code and ran into a few bugs so spent time fixing them. There was one bug that I could not fix by the end of the day
* Meeting at 11am w/ RPL group
* Journal Club at 2pm

### Monday, 7.11.22
* Had weekly meeting with Carla and team - updated on progress
* Socket server portion successfully works now. Fixed a bug where it kept saying that the connection/port is already in use. I had tried changing ports but it never fixed it. Finally realized that if I turned the 'debug' status to False in the Flask App it will fix the error. 
* Dashboard app with the publisher and subscriber nodes now work successfully. Publisher sends frames to a ros topic, where the subscriber listens in on that topic, and when new frames arrive, it sends it through a socket server to the dashboard, which then displays the live video feed successfully.
* Gave a live demo of my dashboard app working with the publisher + subscriber + socket-server to Rory and Dr. Ramanathan.
* Rory and I discussed next steps to do.
* **TODO**    
  - [x] Clean up code, comment/document code, rename files/packages to be better, remove unncessary files, and commit + push everything to your forked repo.    
  - [x] Create pull request w/ your forked repo   
  - [ ] NEW Feature: Create a way for the dashboard to have a button that when you click, it sends a message to a ROS topic (e.g., "log_topic"), and then create a subscriber on the NUC that subscribes to that ros topic and prints out the messages whenever it receives it.   

### Tuesday, 7.12.22
* Worked on personal website
* Worked on cleaning up code and documenting it

### Wednesday 7.13.22
* Had the student internship meeting in morning at 9
* Renamed ros workspace, packages, and files to be more relevant. Cleaned up github repo to only have relevant files. And then made pull request to merge my code with the `AD-SDL/rpl-camera-vision` repo. Rory then merged the pull request
* Created a button with textbox in the dashboard app for users to write text and when they click the submit button, it sends the message over a socket to the ROS topic. Currently working on the socket and subscriber code for that.

### Thursday, 7.14.22
* Had meeting in morning with Dr. Boomsma where he talked about the poster that's due next Thursday. Began work on the poster
* Worked on the code for the dashboard to send data to a ROS topic on the NUC. Spent some time architecting how it should work.
  * Ran into a design issue. I didn't know if I should 
    1. have the dashboard establish a new socket connection for the button message sending since there is already a socket connection for the camera frames. 
    2. OR if I should have the dashboard just connect to one socket, and then instead of having a cam_subscriber.py and msg_subscriber.py, I would have just one file called client.py that when it receives messages on the socket it forwards it to the correct thread (one thread handles the CamSubscriber node and another thread handles the MessageSubscriber node). 
  * Talked with Rory about this and for now we decided to keep it simple and simply create a new socket connection (option a), even though it's scalable. This is because in the future we want to get rid of the socket connection and have the dashboard tightly integrated with ROS, so we won't have this problem. And dealing with threads makes it unnecessarily more complicated.
* Began coding out what Rory and I decided above

### Friday, 7.15.22
* 11am Weekly RPL Meeting 
* 2pm Journal Club
* Worked on the code from yesterday
* **TODO:**
  - [x] Fork repo, and move all contents in `rpl-camera-vision/rpl_cv/dashbord/` folder to `rpl-camera-vision/rpl_dashboard`
  - [x] Add a README inside `rpl_dashboard` folder explaining how to run project, dependencies, how to install everything, how to run the app, etc.
  - [x] Create a pull request with the changes in the forked repo to merge changes to main repo
  - [x] Finish socket server code for the 2-way communication w/ the button

### Monday, 7.18.22
* In Carla's weekly meeting, I presented on my progress so far by giving a PowerPoint presentation and explaining my research.
* Worked on the two-way communication code

### Tuesday, 7.19.22
* Began working on poster
* Worked on two-way communication code, ran into some bugs

### Wednesday, 7.20.22
* Finished 1st draft of poster. Sent it to Rory to check over. He sent back feedback and I made those changes
* Met with Rory to discuss an issue I had with my socket server connection for the two-way communication. Realized I might need multiple threads, so we discussed and realized and found a new solution without using multiple threads, which is good because we wanted to avoid using multiple threads/processes since that will make things more complicated
* Finished draft 2 of my poster and gave it to Carla for her to edit and then I made the changes she mentioned

### Thursday, 7.21.22
* Made some new changes to my poster, made it look better with more color, changed the design.
* Sent new draft to Carla
* Submitted poster
* Ice-cream social with RPL lab :)

### Friday, 7.22.22
* Had 11am weekly meeting with RPL
* During journal club, Carla and Rory gave a presentation on how the poster presentation will go. They gave tips as well.

### Monday, 7.25.22
* Worked on solving the SIGPIPE bug that I had with the two-way communication
* Met with Rory and he helped explain what pipes are and what a SIGPIPE error means. We then went through my code together and he gave me pointers to what the issue may be

### Tuesday, 7.26.22
* Fixed the SIGPIPE error, two-way communication is now working. The solution was that I had to swap the client & server. The dashboard was initially the server and the client was initially the NUC, but I had to switch them so that the dashboard was the client and the NUC was the server.
* Wrote the subscriber for the dash messages as well. Tested it out and now the user can send messages to the NUC, in which the ROS publisher receives it from a socket server and then publishes it to a ROS topic, and then a subscriber reads it and prints it to the console.

### Wednesday, 7.27.22
* Cleaned up the code, added documentation, moved the code from `rpl-camera-vision/rpl_cv/dashboard/*` to `rpl-camera-vision/rpl_dashboard/*`, and then I made a pull request. Changes are now merged with the main branch
* Attended a workshop on how to write my paper with Dr. Boomsma. Began creating an outline for my paper

### Thursday, 7.28.22
* Worked on creating my outline for my paper

### Friday, 7.29.22
* Worked on my paper
* Had 11am weekly meeting

### Monday, 8.1.22 - Friday, 8.5.22
* On Monday I practiced my poster presentation during Carla's presentation where she gave us feedback.
* Worked on deliverables such as final paper, peer review, and abstracts. 
* Practiced for Learning on the Lawn presentation and gave learning on the lawn poster presentation on Thursday
* On Friday I submitted all my deliverables, had last 11am weekly Friday meeting at RPL, did photoshoot for the photographer for RPL, journal club, and then had an ice cream social at 3pm with the Ramanathan Lab and RPL lab. 
