# Logs Analysis
This project is part of Udacity's [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

**by Rafael Rios**

## About
A python script that extracts information from a large SQL database.

## Dependencies

   * Python 2.7+
   * VirtualBox
   * Vagrant

## Instructions

   1. Download the project as a zip file or clone it to your desktop
   2. Download the [database files](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)  and move them to vagrant installation directory
   3. `cd` to vagrant installation directory
   4. Run the commands `vagrant up` and `vagrant ssh` to start the virtual machine
   5. Inside the vm, `cd` to `/vagrant` directory
   6. Type `psql -d news -f newsdata.sql` to load the database
   7. Run the script by typing `python analise_de_logs.py` into the terminal.