#!/bin/bash 
# shellcheck disable=SC1017
VARIABLE="Shell Scripting is Fun!"
echo -e "$VARIABLE \n"

# When assigning a variable to the output of a command, the command/
# should be enclosed in parethesis and preceded by a dollar sign
VARIABLETWO=$(hostname)

VARIABLETHREE="This script is running on $VARIABLETWO."
echo -e "$VARIABLETHREE \n"

# if [-e /etc/shadow]
# then echo "Shadow passwords are enabled."
# else
# echo "Shadow passwords not found"
# fi

# Check if file exists and notify user of determination
if [ -e text.txt ]
then echo -e "text.txt exists!\n"
fi

# Check if file is writeable and notify user of determination
if [ -w text.txt ]
then echo "You have permissions to edit text.txt"
else
echo "You do not have permissions to edit text.txt"
fi

# "read -p" user input, like in input("prompt") in python
# convention with USERNAME being the variable the input will be assigned to:
# read -p "Please enter your username" USERNAME

# Read list and print all items
for ANIMAL in "man" "bear" "pig" "dog" "cat" "sheep"
do echo $ANIMAL
done

# New line and prompt for file input to user
echo -e "\n"
read -p "Please enter the name of a file" FILE

# Determine if file is a directory or not and use conditions
# to reflect determination to user 
if [ -d "$FILE" ]
then echo "Input is a directory"
elif [ -f "$FILE" ]
then echo "Input is a regular file"
else 
echo "$FILE is an unknown file type"
fi
