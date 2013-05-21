Introduction
============
This repository contains a python script to generate certificates of contests. All you need to give an input with the details of the team and team members in the below given format:
File to generate the InCTF certificates for
first three places and for mentors.

<pre>
<no of teams>
<position of team>: 1, 2, 3
<Name of team>
<Name of college>
<Name of mentor>
<no of members>
<member list>
-
<pre>

A sample file is included in this repo i.e inctf13.txt

Run the script:
<pre> $ python gen_cert.py < inctf13.txt </pre>
