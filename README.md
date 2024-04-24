# Message-Processor

**Instructions:** Run the main function. 
This should bring up the GUI with the necessary fields to either type or select.
1. When selecting a guest, the first_name, last_name and room_number fields will populate with the guest data.
2. You may create your own message or use one of the pre-loaded message templates.
3. The greeting is based on your local time, so depending on when the message is sent, the greetings will be different.

**Design Process:**
From the beginning I knew I wanted to use a GUI. I wanted the user to be able to see and select their option
and how that was going to be implemented into the textfields. I ended up using Customtkinter for the GUI
portion, since it was a modernized version of Tkinter, a commonly used python framework, to build GUIs.
After having selected the tools to build out the GUI, I wanted to be able to store that values in some sort of database,
but for a project this size, this might have been unreasonable. So instead, I went ahead with storing the values in Class objects
of each other file that we were expected to use. From there it was just logic and connecting the GUI to the
different class objects.

**Language decision:**
My decision was mainly based on the fact that, I've mostly worked with Python. I built most of the automation in
python, so coming off of Python and attempting another language might have taken a longer time.

**Process for verifying:**
My process for verifying my program, was to have my program meet the requirements listed out on the assessment page. So
being able open up a json file, parse through the data, load that data into a textfield, and ultimately
printing that message, as if it would be sent to a guest.

**What else could I have done?:**
Firstly, I would work out how I open up the file and parse through the file differently. 
There might have been an easier way there with the usage of dictionaries, and I would have liked
to explore that option more thoroughly.
Secondly, I'd want to set up some sort of database system, where I could store that data and call
it, rather than having to pass a class object around.
Thirdly, I think if I was more comfortable working with a frontend language, I'd build 
the application out in another language.
