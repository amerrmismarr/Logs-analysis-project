**Logs Analysis Project**

This project is part of Udacity's Full Stack Web Developer Nanodegree program.It asked me to use a large SQL database about several authors and the articles they wrote to extract statistics and write a report to demonstrate the most famous articles according to the number of views and the most popular authors. I was also asked to extract the days where more than 1% of the errors during viewing the articles occured. The projects suggested only one query to complete the requirements for eachtask. It also suggested that I don't change the database but create useful helpful views to get the information needed.

**Requirements**

Python - The code uses Python ver Python 3

Vagrant - A virtual environment builder and manager

VirtualBox - An open source virtualiztion product.

Git - An open source version control system

**How to access the project?**


Download Gitbash from https://git-scm.com/downloads

Download Virtual box from https://www.virtualbox.org/wiki/Downloads

Download Vagrant from https://www.vagrantup.com/downloads.html

Download the data provided by Udacity from https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

Unzip the file in order to extract newsdata.sql. This file should be inside the Vagrant folder.

Load the database using psql -d news -f newsdata.sql.

Connect to the database using psql -d news.

Create the Views given below. Then exit psql.

Now execute the Python file - python reportdb.py.


**Views used in this project:**

_For question 2:_

'''sql
CREATE VIEW
author_with_slug AS
SELECT authors.name, articles.slug
FROM articles, authors
WHERE articles.author = authors.id;
'''

_For Question 3:_

'''sql
CREATE VIEW errors AS
SELECT cast(time as date) as day, count(*) AS sum 
FROM log 
WHERE status = '404 NOT FOUND' group by day;
'''

'''sql
CREATE VIEW total AS
SELECT cast(time as date) AS day, count(*) AS totalnum
FROM log 
GROUP BY day;
'''

