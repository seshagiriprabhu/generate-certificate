Introduction
============
This repository contains a python script to generate certificates of contests. All you need to give an input with the details of the team and team members in the below given format: 

<pre>
no of teams
position of team: 1, 2, 3, 4, 5,
Name of team
Name of college
Name of mentor
no of members
member list
-
<pre>

A sample file is included in this repo i.e inctf13.txt

Run the script:
<pre> $ python gen_cert.py < inctf13.txt </pre>

Based on the position of the teams you will have to add certificate image file. You can add certificate images of any format which python image library supports. As the file size of the certificates which I used are huge. I did not add them to this repository.

Enjoy!
