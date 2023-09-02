# paste.py

Script/ module to output two text files side by side to the console, based on the paste command in linux. By default, the corresponding lines of each file are separated with tabs.

### Usage: 
python3 paste.py [-d "\<seperator\>" | -s] filename1 filename2
        
positional parameters:
- filename1       : textfile
- filename2       : textfile

optional parameters:
- -d "\<separator\>": usage of specific seperator in-between, e.g. ':'
- -s              : vertical output of two files below each other
