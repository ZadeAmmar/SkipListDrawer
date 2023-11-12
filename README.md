# SkipListPrinter
A python script to visualize a skiplist based off of the value of the node and its height.

### Instructions for use:
___
Open a terminal. In the terminal, navigate into the folder containing the **skiplist.py** file. You can do this using the following command:
```bash
cd <path to skiplist.py file>
```
Once you are in that directory, you may create the skiplist in 1 of 2 ways:

1. The manual way:
   In your terminal, enter the command:
   ```bash
   python skiplist.py
   ```
   The program will continuously prompt you for a node value and then a corresponding height. To exit, enter the word "quit" instead of the node value.
   The script will output a neat visualization of the skiplist to the terminal.
   
2. The automatic way:
   Create a new txt file. Open the txt file and, in order, write the node value, then on the next line, the node height.
   Repeat this until you have all your desired nodes and their attributes written down. Once you are done, create a last line and write the word "quit" in it.
   In your terminal, enter the command:
   ```bash
   python skiplist.py < [txtFileName.txt]
   ```
   The script will automatically read the values from the text file and output a neat visualization of the skiplist to the terminal.
___

### Remember, a skiplist node's height starts at 0, not 1. You may find the height of the output is 1 higher than you expected. This is because a node of height 0 only has a node on level 0 (the lowest level). It does not mean that the node does not exist. 
   
