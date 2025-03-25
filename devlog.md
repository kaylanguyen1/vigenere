#3/24/25 11:28 AM:
What I know about the project
        -  I need to make 3 files: 1) a logger which will log stdin; 2) an encryption program that will accept commands in the form YYYY-MM-DD HH:MM [ACTION] MESSAGE and execute them (pass, encrypt, decrypt, quit, result) or raise an error; 3) a driver program which will ask for the input, create two new processes for executing the logger and encryption program, and print a menu that the user can choose from (password, encrypt, decrypt, history, quit)
    My plan:
        I plan to first work on the driver program to ensure I'm able to create the two new processes that will be used for the logger and encryption files. From there, I plan to create the logger file then the encryption file.

#3/24/25 12:06 PM:
    a) Having problems implementing the pipes, which I plan to focus on in the next session
    b) I didn't accomplish my goal for this session; my goal was to completely finish the driver program but I didn't realize how interconnected the programs are. I set up the menu and the inputs but now I have to add the rest of the inputs/outputs that are connected to the logger and encryption file and set up the pipes.
    c) In my next session I hope to get the pipes working. I also hope to get a start on the logger and encryption programs. 

#3/24/25 12:31 PM:
    a) New thoughts: start with encryption program first, then implement logger program, then driver program last.
    b) This session I plan to accomplish the encryption program, or at least get a start on it and outline my code with comments so I can think about how to implement it. If I get through this program, I will move onto the logger program. My goal is to get some start on the encryption program or at least have a good idea of what kind of functions I need to implement to complete this program.

#3/24/25 1:04 PM:
    a) Some problems I encountered: while loop for if-else statements in the encryption program kept making infinite results and jupyter lab kept crashing; just had to to move the while loop around. Also was confused about the passkey because I'm unsure how to get it from the encryption program.
    b) I accomplished my goal for this session, I ws able to create the encryption program but I set my own passkey within this program because I didn't have it set up in the driver program yet.
    c) Next session I plan to work on the logger file. Once finished, I will try to do the driver program and integrate all three files.

#3/24/25 4:41 PM:
    a) No new developments/thoughts about project
    b) My goal for this session is to complete the logger and driver program. I believe the logger program consists of making a function that adds the date and time of each output and copies the output from other programs into the log file. It needs to accept the name of a log file and terminate once it sees the quit command from the driver. For the driver progam, I need to create the pipes that connect the stdin and stdout from the different programs. Once I get the pipes working I can correctly integrate all of the programs.

#3/24/25 7:03 PM:
    a) some problems I encountered:
        * the passkey wasn't being properly sent from the driver program to the encryption program, I was pssing it as "[PASS] key" when encryp.py accepted "PASS key"
        * encrypt.py couldn't find a passkey because I didn't have it as a locally defined variable
        * the output from encrypt.py isn't being properly printed to log file and command line, still isn't fixed
        * logger file wasn't accepting the name of the file because I wasn't reading it in
    b) I accomplished my goal for this session as I was able to complete the logger and driver program. For easier debugging, I made a copy of driver.py as a driver.ipynb so that I could see the command line if there were issues in jupyter lab. 
    c) Next session I need to work on the communication through pipes since there's an issue with the output from encrypt.py not being properly printed on the command line and log file. After that I'll be able to check if the program is working.

#3/24/25 8:03 PM:
    a) I think I should look at the class example code again to better understand how pipe communication works and see what I can add to ensure the stdin and stdout are connected properly.
    b) In this session I plan to get the stdout from encrypt.py working. To do this I will look through the cpu.py and mem.py examples and try to see what the differences are between them and my program. I will also add more checkpoints throughout my programs to see if I can find the root cause of the issue. Thus, my goal for this session is to determine why the stdout isn't working and attempt to fix it.

#3/24/25 10:22 PM:
    a) some problems I encountered:
        a) stdout not working with encrypt.py: added \n to end of every output to ensure it was accepted to the predetermined format, added print(encrypt.stdout.readline().strip()) to anywhere in the driver program where I was supposed to be printing output from the encrypt.py file. I also added more flush statements to ensure they were being sent out at the right time because they sometimes got sent out late.
        b) my checking system for if strings were alphabetic characters wasn't working because i was checking the wrong input since it was saved under two different variables
        c) the quit statements weren't showing up in the logger file, I had to move the break statement in logger.py and add the logger function to display them
    b) I accomplished my goal for this session; I figured out what was wrong with the output through the pipe by comparing my code with the example code from class and noticed that even though I was sending out output to the driver program, the driver program wasn't doing anything with the input it was receiving. By adding the print statements it actually printed what was being inputted by the encryption file. With this and some smaller problems, I was able to finish the project.
