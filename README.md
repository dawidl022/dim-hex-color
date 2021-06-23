# Simple Hex Color code dimmer
The python script decreases the value of each digit in hex code by 1, unless already set to 0, and prints out the new hex code. The resulting color is slightly dimmer than the one input, useful for i.e. making HTML buttons darker when hovered over. Accepts both 3 digit values, as well as full 6 digit values. The `#` character is optional, but if used in command line must be escaped: `\#`

`dim-color` can be placed in folder with PATH scripts to be executed quickly from command line with command:  
 `dim-color <hex-value>`

`dim-color` can be also used normally as an argument for the python3 interpreter:  
`python3 <path-to>/dim-color <hex-value>`

If you have any suggestions please let me know 😁

Example usages:   
```
$ dim-color \#34efa1
#23de90
``` 
```
$ dim-color 12ff01
01ee00
```
```
$ dim-color abc
9ab
```
```
$ python3 dim-color \#49f
#38e
```
