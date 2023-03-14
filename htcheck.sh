#!/bin/bash

# prompt the user for the file name
read -p "Enter the path to the Rainbow Hash Table: " filename

# prompt the user for the hash
read -p "Enter the Hash: " searchterm

# loop through the lines in the file
while read line
do
    # split the line into its three fields
    field1=$(echo $line | cut -d':' -f1)
    field2=$(echo $line | cut -d':' -f2)
    field3=$(echo $line | cut -d':' -f3)

    # check if the hash matches the third field
    if [ "$field1" == "$searchterm" ]
    then
        # if there's a match, print the second field and exit the loop
        echo "Password found: $field2"
        exit
    fi
done < "$filename"

# if we get here, there was no match
echo "No match found."
