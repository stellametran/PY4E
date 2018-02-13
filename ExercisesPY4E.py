#--------------------------------------- Why Program? ---------------------------------------
#Write a program that uses a print statement to say 'hello world' as shown in 'Desired Output'.
# the code below almost works
    print("hello world")

    
#--------------------------------------- Variables, expressions, and statements ---------------------------------------
#2.3 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking or bad user data.
# This first line is provided for you

    hrs = input("Enter Hours:")
    rate = input("Enter Rate:")
    pay = float(hrs)*float(rate)
    print(pay)  
    

#--------------------------------------- Conditional Execution ---------------------------------------
#3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.

    hrs = input("Enter Hours:")
    h = float(hrs)
    rate = input("Enter Rate:")
    r = float(rate)
    if(h) > 40 :
        pay = (40*r) + (h-40)*(r*1.5)
    else : 
        pay = (h*r) 
    print(pay)

#3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

    score = input("Enter a score between 0.0 and 1.0:")
    try : 
      score = float(score)
      if(score < 0.0) :
        print("Invalid value")
      if (score > 1.0) :
        print("Invalid value")
    except : 
      print("Invalid value")
      
    if score >= 0.9 :
      print("A")
    elif score >= 0.8 :
      print("B")
    elif score >= 0.7  :
      print("C")
    elif score >= 0.6 :
      print("D")
    elif score < 0.6 :
      print("F")
    else :
      print("Invalid value")
    

#--------------------------------------- Functions ---------------------------------------
#4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Award time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of time-and-a-half in a function called computepay() and use the function to do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. Do not name your variable sum or use the sum() function.

    hrs = input("Enter Hours:")
    h = float(hrs)
    rate = input("Enter Rate:")
    r = float(rate)

    def computepay(h,r) :
      if(h) > 40 :
        pay = (40*r) + (h-40)*(r*1.5)
      else : 
        pay = (h*r) 
      return pay
            
    print(computepay(h,r))

 
#--------------------------------------- Loops and Iterations ---------------------------------------
#5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

    largest = None
    smallest = None
    number = None
    count = 0

    #Loops until "done"
    while True :
      
      number = input("Enter an integer number:")
      if number == "done" : break
      
      #Test for valid number and initiate variables with the first value
      try : 
        number = int(number) 
        if count == 0 :
            largest = number
            smallest = number
      except :
        print("Invalid input")
        continue
     
     #Test variables for min and maximum numbers
      if(number > int(largest)) :
        largest = number
      if(number < int(smallest)) :
        smallest = number
        
      count = count +1
      
    print("Maximum is",largest)
    print("Minimum is",smallest)
    

#--------------------------------------- Strings ---------------------------------------
#6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.
#text = "X-DSPAM-Confidence:    0.8475";

    text = "X-DSPAM-Confidence:    0.8475";
    print(float((text[(text.find(":"))+1:3000]).strip()))

#--------------------------------------- Files ---------------------------------------
#7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

    #Read the filename or if null use the standard name
    fname = input("Enter file name: ")
    fh = open(fname)
    
    count = 0
    total = 0
    
    #Check each line for a specific sentence, collect a number after the ":" and count how many times it happened
    for line in fh:
        if not line.startswith("X-DSPAM-Confidence:") : continue
        count = count + 1
        total = total + float((line[(line.find(":"))+1:3000]).strip())

    print("Average spam confidence:",(total/count))


#--------------------------------------- Lists ---------------------------------------
#8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
#You can download the sample data at http://www.py4e.com/code3/romeo.txt

    #Read the filename or if null use the standard name
    fname = input("Enter file name: ")
    fh = open(fname)
    
    lst = list()
    templst = list()

    #Transforms each line in lists of words and add new words into a list
    for line in fh:
       templst = line.split()
       for word in templst :
         if word in lst : continue
         else : lst.append(word)
         
    lst.sort()
    print(lst)

#8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

    #Read the filename or if null use the standard name
    fname = input("Enter file name: ")
    if len(fname) < 1 : fname = "mbox-short.txt"
    fh = open(fname)
    
    count = 0
    templist = list()
    
    #Transforms each line in lists of words and count the words into a list
    for line in fh:
      templist = line.split()
      if "From" in templist :
        count = count + 1   
        print(templist[1])
      else : continue

    print("There were", count, "lines in the file with From as the first word")

    
#--------------------------------------- Dictionaries ---------------------------------------
#9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

    #Read the filename or if null use the standard name
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    handle = open(name)
    
    count = 0
    templist = list()
    tempdict = dict()
    bigsender = 0
    bigsenderqtt = 0

    #Transforms each line in lists of words and count the words into a dictionary
    for line in handle:
        templist = line.split()
        if "From" in templist :
          tempdict[templist[1]] = tempdict.get(templist[1],0) + 1
        else : continue

   
    #Reads the dictionary to find the biggest value and the sender's name
    for key in tempdict:
        if tempdict[key] > bigsenderqtt :
           bigsender = key
           bigsenderqtt = tempdict[key]
        
    print(bigsender,bigsenderqtt)


#--------------------------------------- Tuples ---------------------------------------
#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

    #Read the filename or if null use the standard name
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    handle = open(name)

    words = list()
    count = 0
    tempdict = dict()


    #Transforms each line in a list of words
    for line in handle:
      words = line.split()
      
      #Collect the time (00:00:00) from the lines starting with "From"
      if "From" in words:
           hour = words[5].split(":")
           
           #Count how many times each hour appears in the file
           tempdict[hour[0]] = tempdict.get(hour[0],0) + 1

    #Sort the dictionary, transform in a tuple and print the tuples
    temptuples = sorted(tempdict.items())
    for x,y in temptuples: print(x,y)



#--------------------------------------- Regular Expressions ---------------------------------------
# Finding Numbers in a Haystack
# In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.
#
# Data Files
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
        # Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
        # Actual data: http://py4e-data.dr-chuck.net/regex_sum_71935.txt (There are 92 values and the sum ends with 907)
# These links open in a new window. Make sure to save the file into the same folder as you will be writing your Python program. Note: Each student will have a distinct data file for the assignment - so only use your own data file for analysis.
#
# Data Format
# The file contains much of the text from the introduction of the textbook except that random numbers are inserted throughout the text. Here is a sample of the output you might see:
        # Why should you learn to write programs? 7746
        # 12 1929 8827
        # Writing programs (or programming) is a very creative 
        # 7 and rewarding activity.  You can write programs for 
        # many reasons, ranging from making your living to solving
        # 8837 a difficult data analysis problem to having fun to helping 128
        # someone else solve a problem.  This book assumes that 
        # everyone needs to know how to program ...
        # The sum for the sample text above is 27486. The numbers can appear anywhere in the line. There can be any number of numbers in each line (including none).
# Handling The Data
# The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.

    #Read the filename or if null use the standard name
    name = input("Enter file:")
    if len(name) < 1 : name = "regex_sum_71935.txt"
    handle = open(name)

    words = list()
    total = 0

    import re

    #Transforms each line in a list of words
    for line in handle:
      words = line.split()
      
      #Check each word for one or more numbers
      for word in words: 
        if re.search('[0-9]+',word) : 
          #If number, sum to the total
          for i in re.findall('[0-9]+',word) : 
             total = total + int(i)
        else : continue
       
    print(total)
   
    
# Optional: Just for Fun
# There are a number of different ways to approach this problem. While we don't recommend trying to write the most compact code possible, it can sometimes be a fun exercise. Here is a a redacted version of two-line version of this program using list comprehension:

# Python 2
# import re
# print sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] )

# Python 3:
# import re
# print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )
# Please don't waste a lot of time trying to figure out the shortest solution until you have completed the homework. List comprehension is mentioned in Chapter 10 and the read() method is covered in Chapter 7.

    import re
    print(sum([int(i) for i in re.findall('[0-9]+',open("regex_sum_42.txt").read())]))

       
    
#--------------------------------------- Network Programming ---------------------------------------
# Exploring the HyperText Transport Protocol
# You are to retrieve the following document using the HTTP protocol in a way that you can examine the HTTP Response headers.
# http://data.pr4e.org/intro-short.txt
# There are three ways that you might retrieve this web page and look at the response headers:
# Preferred: Modify the socket1.py (https://www.py4e.com/code3/socket1.py) program to retrieve the above URL and print out the headers and data. Make sure to change the code to retrieve the above URL - the values are different for each URL.
# Open the URL in a web browser with a developer console or FireBug and manually examine the headers that are returned.
# Use the telnet program as shown in lecture to retrieve the headers and content.
# Enter the header values in each of the fields below and press "Submit".

    import socket

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))
    cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if (len(data) < 1):
            break
        print(data.decode(),end='')
    mysock.close()

    
# Scraping Numbers from HTML using BeautifulSoup 
# In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
# Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_71937.html (Sum ends with 45)
# You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
# Data Format
# The file is a table of names and comment counts. You can ignore most of the data in the file except for lines like the following:
# <tr><td>Modu</td><td><span class="comments">90</span></td></tr>
# <tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
# <tr><td>Hubert</td><td><span class="comments">87</span></td></tr>
# You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.
# Look at the sample code provided. It shows how to find all of a certain kind of tag, loop through the tags and extract the various aspects of the tags.
# ...
# Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
   # Look at the parts of a tag
   # print 'TAG:',tag
   # print 'URL:',tag.get('href', None)
   # print 'Contents:',tag.contents[0]
   # print 'Attrs:',tag.attrs
# You need to adjust this code to look for span tags and pull out the text content of the span tag, convert them to integers and add them up to complete the assignment.
# Sample Execution
# $ python3 solution.py
# Enter - http://py4e-data.dr-chuck.net/comments_42.html
# Count 50
# Sum 2...


    # To run this, you can install BeautifulSoup
    # https://pypi.python.org/pypi/beautifulsoup4

    # Or download the file
    # http://www.py4e.com/code3/bs4.zip
    # and unzip it in the same directory as this file

    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    import ssl

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = input('Enter - ')
    html = urlopen(url, context=ctx).read()

    # html.parser is the HTML parser included in the standard Python 3 library.
    # information on other HTML parsers is here:
    # http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve all of the span tags
    tags = soup('span')
    total = 0
    count = 0

    for tag in tags:
        # Look at the parts of span tag
        count = count + 1
        total = total + int(tag.contents[0])

    print("Count", count)
    print("Sum", total)

    
# Following Links in Python

# In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

# We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment

# Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html 
# Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah 
# Last name in sequence: Anayah
# Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Matilda.html 
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: P
# Strategy
# The web pages tweak the height between the links and hide the page after a few seconds to make it difficult for you to do the assignment without writing a Python program. But frankly with a little effort and patience you can overcome these attempts to make it a little harder to complete the assignment without writing a Python program. But that is not the point. The point is to write a clever Python program to solve the program.

# Sample execution

# Here is a sample execution of a solution:

# $ python3 solution.py
# Enter URL: http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Enter count: 4
# Enter position: 3
# Retrieving: http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Retrieving: http://py4e-data.dr-chuck.net/known_by_Montgomery.html
# Retrieving: http://py4e-data.dr-chuck.net/known_by_Mhairade.html
# Retrieving: http://py4e-data.dr-chuck.net/known_by_Butchi.html
# Retrieving: http://py4e-data.dr-chuck.net/known_by_Anayah.html

    # To run this, you can install BeautifulSoup
    # https://pypi.python.org/pypi/beautifulsoup4

    # Or download the file
    # http://www.py4e.com/code3/bs4.zip
    # and unzip it in the same directory as this file

    import urllib.request, urllib.parse, urllib.error
    from bs4 import BeautifulSoup
    import ssl

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = input('Enter - ')
    position = int(input('Position - '))
    repeats = int(input('Repeats - '))
    count = 0

    # Retrieve all of the anchor tags
    while (count + 1) <= repeats :
        #Open current URL
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        #Collects all links - tag a
        tags = soup('a')
        #Find the link in a certain position
        url = str(tags[position - 1].get('href', None))
        count = count + 1
        print("Retrieving:",url)    

        
        
#--------------------------------------- Using Web Services --------------------------------------- 
# Extracting Data from XML

# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_71939.xml (Sum ends with 43)
# You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
# Data Format and Approach
# The data consists of a number of names and comment counts in XML as follows:

# <comment>
  # <name>Matthias</name>
  # <count>97</count>
# </comment>
# You are to look through all the <comment> tags and find the <count> values sum the numbers. The closest sample code that shows how to parse XML is geoxml.py. But since the nesting of the elements in our data is different than the data we are parsing in that sample code you will have to make real changes to the code.
# To make the code a little simpler, you can use an XPath selector string to look through the entire tree of XML for any tag named 'count' with the following line of code:

# counts = tree.findall('.//count')
# Take a look at the Python ElementTree documentation and look for the supported XPath syntax for details. You could also work from the top of the XML down to the comments node and then loop through the child nodes of the comments node.
# Sample Execution

# $ python3 solution.py
# Enter location: http://py4e-data.dr-chuck.net/comments_42.xml
# Retrieving http://py4e-data.dr-chuck.net/comments_42.xml
# Retrieved 4189 characters
# Count: 50
# Sum: 2...
# Turning in the Assig

    import urllib.request, urllib.parse, urllib.error
    import xml.etree.ElementTree as ET

    url = 'http://py4e-data.dr-chuck.net/comments_71939.xml'

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved', len(data), 'characters')

    #Converts the xml to a string
    tree = ET.fromstring(data)

    #filters by .//count same as comments/comment/count
    results = tree.findall('.//count')
    iterations = 0
    total = 0

    #Loop all items in the list
    for item in results:

        iterations = iterations + 1
        
        #Gets the text value from the tag count
        total = total + int(item.text)    
        
    print("Count:",iterations)
    print("Sum:",total)

    
# Extracting Data from JSON

# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_71940.json (Sum ends with 69)
# You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
# Data Format
# The data consists of a number of names and comment counts in JSON as follows:

# {
  # comments: [
    # {
      # name: "Matthias"
      # count: 97
    # },
    # {
      # name: "Geomer"
      # count: 97
    # }
    # ...
  # ]
# }
# The closest sample code that shows how to parse JSON and extract a list is json2.py. You might also want to look at geoxml.py to see how to prompt for a URL and retrieve data from a URL.

# Sample Execution

# $ python3 solution.py
# Enter location: http://py4e-data.dr-chuck.net/comments_42.json
# Retrieving http://py4e-data.dr-chuck.net/comments_42.json
# Retrieved 2733 characters
# Count: 50
# Sum: 2...

    import urllib.request, urllib.parse, urllib.error
    import json

    url = 'http://py4e-data.dr-chuck.net/comments_71940.json'

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved', len(data), 'characters')

    # Converts the json to a dictionary
    tree = json.loads(data)

    iterations = 0
    total = 0

    #This tree has 2 nodes in the first level: "note" and "comments"
    #This loop is only for the 'comments'
    for item in tree['comments']:

       iterations = iterations + 1
       total = total + int(item['count'])  
        
    print("Count:",iterations)
    print("Sum:",total)

# Calling a JSON API

# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py. The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
# API End Points

# To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:

# http://py4e-data.dr-chuck.net/geojson?
# This API uses the same parameter (address) as the Google API. This API also has no rate limit so you can test as often as you like. If you visit the URL with no parameters, you get a list of all of the address values which can be used with this API.
# To call the API, you need to provide address that you are requesting as the address= parameter that is properly URL encoded using the urllib.urlencode() fuction as shown in http://www.py4e.com/code3/geojson.py

# Test Data / Sample Execution

# You can test to see if your program is working with a location of "South Federal University" which will have a place_id of "ChIJJ8oO7_B_bIcR2AlhC8nKlok".

# $ python3 solution.py
# Enter location: South Federal UniversityRetrieving http://...
# Retrieved 2101 characters
# Place id ChIJJ8oO7_B_bIcR2AlhC8nKlok
# Turn In

# Please run your program to find the place_id for this location:

# University of Chicago

    import urllib.request, urllib.parse, urllib.error
    import json

    serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

    address = input('Enter location: ')
    #address = "South Federal University"
    #address = "University of Chicago"

    url = serviceurl + urllib.parse.urlencode({'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
        print("Place id",js["results"][0]["place_id"])

    except:
        js = None  
        print('==== Failure To Retrieve ====')


#--------------------------------------- Databases --------------------------------------- 

# Instructions
# If you don't already have it, install the SQLite Browser from http://sqlitebrowser.org/.

# Then, create a SQLITE database or use an existing database and create a table in the database called "Ages":

# CREATE TABLE Ages ( 
  # name VARCHAR(128), 
  # age INTEGER
# )
# Then make sure the table is empty by deleting any rows that you previously inserted, and insert these rows and only these rows with the following commands:

# DELETE FROM Ages;
# INSERT INTO Ages (name, age) VALUES ('Elijah', 37);
# INSERT INTO Ages (name, age) VALUES ('Livie', 19);
# INSERT INTO Ages (name, age) VALUES ('Brannan', 29);
# INSERT INTO Ages (name, age) VALUES ('Girls', 38);
# INSERT INTO Ages (name, age) VALUES ('Rebekkah', 18);
# INSERT INTO Ages (name, age) VALUES ('Samara', 18);
# Once the inserts are done, run the following SQL command:
# SELECT hex(name || age) AS X FROM Ages ORDER BY X
# Find the first row in the resulting record set and enter the long string that looks like 53656C696E613333.
# Note: This assignment must be done using SQLite - in particular, the SELECT query above will not work in any other database. So you cannot use MySQL or Oracle for this assignment.

    import sqlite3

    conn = sqlite3.connect('ExerciseAges.db')
    cur = conn.cursor()

    myDictionary = {'Elijah': 37, 'Livie': 19, 'Brannan': 29, 'Girls': 38, 'Rebekkah': 18 , 'Samara': 18} 

    cur.execute('''
        CREATE TABLE IF NOT EXISTS Ages (name VARCHAR(128), 
                       age INTEGER)''')
                       
    cur.execute('''DELETE FROM Ages''')                   
                       
    for x in myDictionary : 
        cur.execute('''INSERT INTO Ages (name, age) VALUES 
                            (?, ?)''',
                            (x,myDictionary[x]))

                            
    conn.commit()
    
    # This exercise was meant to be executed in SQLite so the "select" clause at the end doesn't work in Python and need to be executed manually in SQLite.
    # resultHex = cur.execute('''SELECT hex(name || age) AS X FROM Ages ORDER BY X LIMIT 1''')
    # print(resultHex)
    conn.close()


# Counting Organizations
# This application will read the mailbox data (mbox.txt) and count the number of email messages per organization (i.e. domain name of the email address) using a database with the following schema to maintain the counts.

# CREATE TABLE Counts (org TEXT, count INTEGER)
# When you have run the program on mbox.txt upload the resulting database file above for grading.
# If you run the program multiple times in testing or with dfferent files, make sure to empty out the data before each run.

# You can use this code as a starting point for your application: http://www.py4e.com/code3/emaildb.py.

# The data file for this application is the same as in previous assignments: http://www.py4e.com/code3/mbox.txt.

# Because the sample code is using an UPDATE statement and committing the results to the database as each record is read in the loop, it might take as long as a few minutes to process all the data. The commit insists on completely writing all the data to disk every time it is called.

# The program can be speeded up greatly by moving the commit operation outside of the loop. In any database program, there is a balance between the number of operations you execute between commits and the importance of not losing the results of operations that have not yet been committed.

    import sqlite3

    #Read the filename or if null use the standard name
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox.txt"
    handle = open(name)

    templist = list()
    count = 0

    #Open database connection
    conn = sqlite3.connect('CountingOrganizations.sqlite')
    cur = conn.cursor()

    #Create table or delete its content
    cur.execute('''CREATE TABLE IF NOT EXISTS Counts (org TEXT, count INTEGER)''')           
    cur.execute('''DELETE FROM Counts''') 

    #Find all emails in the From lines
    for line in handle:
         line = line.rstrip()
         if not line.startswith('From ') : continue
         #Get the domains
         words = line.split()
         domain = words[1].split("@")
         #Check if domain exist in the database         
         cur.execute('''SELECT count FROM Counts where org = ?''',(domain[1],))
         count = cur.fetchone()
         #If not create an entry
         if count is None: 
              cur.execute('''INSERT INTO Counts (org, count) VALUES (?,1)''',(domain[1],))
         else :
              #If it does update the record
              cur.execute('''UPDATE Counts SET count = count + 1  WHERE org = ?''',(domain[1],))
         
    conn.commit()

    table = 'SELECT org, count FROM Counts ORDER BY count DESC'
    for line in cur.execute(table): 
        print(str(line[0]), ":", str(line[1]))

    conn.close()

# Musical Track Database
# This application will read an iTunes export file in XML and produce a properly normalized database with this structure:

# CREATE TABLE Artist (
    # id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    # name    TEXT UNIQUE
# );

# CREATE TABLE Genre (
    # id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    # name    TEXT UNIQUE
# );

# CREATE TABLE Album (
    # id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    # artist_id  INTEGER,
    # title   TEXT UNIQUE
# );

# CREATE TABLE Track (
    # id  INTEGER NOT NULL PRIMARY KEY 
        # AUTOINCREMENT UNIQUE,
    # title TEXT  UNIQUE,
    # album_id  INTEGER,
    # genre_id  INTEGER,
    # len INTEGER, rating INTEGER, count INTEGER
# );
# If you run the program multiple times in testing or with different files, make sure to empty out the data before each run.

# You can use this code as a starting point for your application: http://www.py4e.com/code3/tracks.zip. The ZIP file contains the Library.xml file to be used for this assignment. You can export your own tracks from iTunes and create a database, but for the database that you turn in for this assignment, only use the Library.xml data that is provided.

# To grade this assignment, the program will run a query like this on your uploaded database and look for the data it expects to see:

# SELECT Track.title, Artist.name, Album.title, Genre.name 
    # FROM Track JOIN Genre JOIN Album JOIN Artist 
    # ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        # AND Album.artist_id = Artist.id
    # ORDER BY Artist.name LIMIT 3
# The expected result of the modified query on your database is:
# Select Language​▼
# Track	Artist	Album	Genre
# Chase the Ace	AC/DC	Who Made Who	Rock
# D.T.	AC/DC	Who Made Who	Rock
# For Those About To Rock (We Salute You)	AC/DC	Who Made Who	Rock

    import sqlite3
    import urllib.request, urllib.parse, urllib.error
    import xml.etree.ElementTree as ET
        
    #Get file
    fname = input('Enter file name: ')
    if ( len(fname) < 1 ) : fname = 'Library.xml'
    uh = open(fname)

    #Open database connection
    conn = sqlite3.connect('iTunesLibrary.sqlite')
    cur = conn.cursor()

    #Create tables or delete their content
    cur.executescript('''
                    CREATE TABLE IF NOT EXISTS Artist (
                                id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                                name    TEXT UNIQUE);
                                
                    CREATE TABLE IF NOT EXISTS Genre (
                                id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                                name    TEXT UNIQUE);
                                
                    CREATE TABLE IF NOT EXISTS Album (
                                id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                                artist_id  INTEGER,
                                title   TEXT UNIQUE);
                                
                    CREATE TABLE IF NOT EXISTS Track (
                                id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                                title TEXT  UNIQUE,
                                album_id  INTEGER,
                                genre_id  INTEGER,
                                len INTEGER, 
                                rating INTEGER, 
                                count INTEGER);
                                
                    DELETE FROM Artist;
                    DELETE FROM Genre;
                    DELETE FROM Album;
                    DELETE FROM Track
    ''') 


    #Function that reconstruct the dictionaries in a standard format, from:
    # <key>Track ID</key><integer>369</integer>
    # <key>Name</key><string>Another One Bites The Dust</string>
    # <key>Artist</key><string>Queen</string>
    # to ("Track ID" : 369) , ("Name" : "Another One Bites The Dust") , ("Artist" : "Queen")
    def lookup(d, key):
        found = False
        for child in d:
            if found : return child.text
            if child.tag == 'key' and child.text == key :
                found = True
        return None

        
    #Parsing xml
    stuff = ET.parse(fname)
    #Finding all dict (3rd levels)
    all = stuff.findall('dict/dict/dict')
    print('Dict count:', len(all))

    #For each dict (track) insert values in the database
    for entry in all:

        #Cleaning up some incomplete records
        if ( lookup(entry, 'Track ID') is None ) : continue
        if ( lookup(entry, 'Genre') is None ) : continue
        
        #Collecting all fields from the track
        name = lookup(entry, 'Name')
        artist = lookup(entry, 'Artist')
        album = lookup(entry, 'Album')
        count = lookup(entry, 'Play Count')
        rating = lookup(entry, 'Rating')
        length = lookup(entry, 'Total Time')
        genre = lookup(entry, 'Genre')

        if name is None or artist is None or album is None : continue

        # print(name, artist, album, count, rating, length, genre)

        #Insert or ignore if already exist this record in Artist
        cur.execute('''INSERT OR IGNORE INTO Artist (name) 
            VALUES ( ? )''', ( artist, ) )
        cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
        artist_id = cur.fetchone()[0]

        #Insert or ignore if already exist this record in Album
        cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
            VALUES ( ?, ? )''', ( album, artist_id ) )
        cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
        album_id = cur.fetchone()[0]

        #Insert or ignore if already exist this record in Genre
        cur.execute('''INSERT OR IGNORE INTO Genre (name) 
            VALUES ( ? )''', (genre, ) )
        cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
        genre_id = cur.fetchone()[0]
        
        #Insert or update values in Track
        cur.execute('''INSERT OR REPLACE INTO Track
            (title, album_id, len, rating, count, genre_id) 
            VALUES ( ?, ?, ?, ?, ?, ? )''', 
            ( name, album_id, length, rating, count, genre_id ) )

            
    conn.commit()

    #Result query
    table = '''SELECT Track.title, Artist.name, Album.title, Genre.name 
                FROM Track JOIN Genre JOIN Album JOIN Artist 
                ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
                AND Album.artist_id = Artist.id
                ORDER BY Artist.name LIMIT 3'''
    for line in cur.execute(table): 
        print(str(line[0]), "|", str(line[1]),"|", str(line[2]),"|", str(line[3]))

    conn.close()

    
# Many Students in Many Courses

# Instructions
# This application will read roster data in JSON format, parse the file, and then produce an SQLite database that contains a User, Course, and Member table and populate the tables from the data file.

# You can base your solution on this code: http://www.py4e.com/code3/roster/roster.py - this code is incomplete as you need to modify the program to store the role column in the Member table to complete the assignment.

# Each student gets their own file for the assignment. Download this file and save it as roster_data.json. Move the downloaded file into the same folder as your roster.py program.

# Once you have made the necessary changes to the program and it has been run successfully reading the above JSON data, run the following SQL command:

# SELECT hex(User.name || Course.title || Member.role ) AS X FROM 
    # User JOIN Member JOIN Course 
    # ON User.id = Member.user_id AND Member.course_id = Course.id
    # ORDER BY X
# Find the first row in the resulting record set and enter the long string that looks like 53656C696E613333.


    import json
    import sqlite3

    conn = sqlite3.connect('rosterdb.sqlite')
    cur = conn.cursor()

    # Do some setup
    cur.executescript('''
                        DROP TABLE IF EXISTS User;
                        DROP TABLE IF EXISTS Member;
                        DROP TABLE IF EXISTS Course;

                        CREATE TABLE User (
                            id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                            name   TEXT UNIQUE
                        );

                        CREATE TABLE Course (
                            id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                            title  TEXT UNIQUE
                        );

                        CREATE TABLE Member (
                            user_id     INTEGER,
                            course_id   INTEGER,
                            role        INTEGER,
                            PRIMARY KEY (user_id, course_id)
                        )
    ''')

    fname = input('Enter file name: ')
    if len(fname) < 1:
        fname = 'roster_data.json'

    # [
    #   [ "Charley", "si110", 1 ],
    #   [ "Mea", "si110", 0 ],

    str_data = open(fname).read()
    json_data = json.loads(str_data)

    for entry in json_data:

        user = entry[0];
        course = entry[1];
        role = entry[2];

        print((user, course, role))

        cur.execute('''INSERT OR IGNORE INTO User (name)
            VALUES ( ? )''', ( user, ) )
        cur.execute('SELECT id FROM User WHERE name = ? ', (user, ))
        user_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Course (title)
            VALUES ( ? )''', ( course, ) )
        cur.execute('SELECT id FROM Course WHERE title = ? ', (course, ))
        course_id = cur.fetchone()[0]

        cur.execute('''INSERT OR REPLACE INTO Member
            (user_id, course_id, role) VALUES ( ?, ?, ? )''',
            ( user_id, course_id, role, ) )

    conn.commit()
    conn.close()

    #The following query must be run in SQLite directly:
    #SELECT hex(User.name || Course.title || Member.role ) AS X FROM 
    # User JOIN Member JOIN Course 
    # ON User.id = Member.user_id AND Member.course_id = Course.id
    # ORDER BY X





