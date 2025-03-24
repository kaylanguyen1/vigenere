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
