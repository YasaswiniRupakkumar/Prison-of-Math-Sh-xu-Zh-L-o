-------------
-------------
Introduction
-------------
-------------
Prison of Math: Shùxué Zhī Láo invites you to embark on a thrilling text-based adventure set in the Song Dynasty. Step into the shoes of Shu Yin, a revered warrior whose courage and intellect are put to the ultimate test. The emperor, Zhao Kuangyin, has been imprisoned in the mythical "Prison of Math," a labyrinth of challenging puzzles and intellectual traps. Only you can guide Shu Yin to victory and save the emperor!

This game blends storytelling and problem-solving into a simple yet captivating experience. As you progress, you'll encounter a series of math puzzles designed to challenge your mind and test your problem-solving skills. Each success brings you closer to the emperor’s freedom, while failures remind you of the stakes and inspire you to try again.

Key features include:

Engaging Storyline: Immerse yourself in the legend of Shu Yin and the rich culture of the Song Dynasty.
Interactive Gameplay: Solve puzzles directly in the command line to advance the narrative.
Dynamic Feedback: Get personalized motivational messages based on your performance.
Accessible and Lightweight: Perfect for both beginners and experienced Python enthusiasts.
Playing Prison of Math is simple. Clone the repository, install the necessary dependencies, and run the game in your terminal. No fancy setups or complicated installations—just a pure, fun gaming experience built with Python.

Whether you’re a math enthusiast, a history lover, or someone looking for a quick and enjoyable game, Prison of Math delivers an exciting challenge with a touch of cultural flair. Sharpen your wits, immerse yourself in the story, and see if you have what it takes to conquer the Prison of Math and save the kingdom.

Are you ready to take on the challenge? Shu Yin and the emperor are counting on you!


-------------
-------------
Prerequisites
-------------
-------------


1. Python 3.7+
   Ensure Python is installed on your system. You can check the version by running:  

   `````````````````
   python --version
   `````````````````

2. Install Required Modules:

   Check whether rich and MariaDB have been installed.

   ````````````````
   pip show rich
   ````````````````

	AND

   ````````````````
   pip show MariaDB
   ````````````````

   If not, open command prompt in admin mode and execute the following commands

   ````````````````````
   pip install rich
   pip install MariaDB
   ````````````````````

	OR

   ```````````````````````````````
   pip install -r requirements.txt
   ```````````````````````````````

3. Database Setup: 
   - Download and install XAMPP. Start Apache and MySQL.  
   - Open phpMyAdmin by visiting `http://localhost/phpMyAdmin` in your browser.  
   - Go to the SQL tab and execute:  

     ````````````````````````
     CREATE DATABASE prisonofmath;
     ````````````````````````  

   - Select the `prisonofmath` database (that you just created), navigate to the Import tab, and upload the provided `prisonofmath.sql` file.  


-----------------------------------
-----------------------------------
Running python file (in the terminal)
-----------------------------------
-----------------------------------

change (redirect) the console path to where the main python file prisonofmath.py is present currently, and type prisonofmath in the console.

Further arguments like prisonofmath -e, prisonofmath -h, prisonofmath -m can be given to activate different modes at the beginning itself.