# Web-Database-Application-For-Baseball
Web-database application for the most recent Lahman baseball database


Group Name: KHz

Group Member:

    Zhengyan Hu
    Jingke Shi
    

Before start:
        1. cd dataFile/
        2. cp *.csv .. 
    Set Up Environment:
        3. python -m venv venv
        4  Linux/Mac: source venv/bin/activate 
           Windows: venv\Scripts\activate
        5. pip install -r requirements.txt
    Create database:
        6. mysql -u root -p
        7. source KHz.sql
        8. exit;
    Load data: 
        9. python data.py
        (Before: Change csi3335fall2021.py to your database username and password)
    Run flask server:
        10. python baseball.py
    

PS: 

1. At the top left of the page, left of the MLB picture, you can select your favorite team or switch to display the standings.
 
2. CSV Files in dataFile and data.py should be in same directory
   Suggestion for moving the files:


DataFiles From http://www.seanlahman.com/baseball-archive/statistics/
