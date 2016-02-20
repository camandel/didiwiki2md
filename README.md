# didiwiki2md
simple text converter form didiwiki to markdown format

Features:

* converts headers H1, H2 and H3 from "=" to "#"
* converts code block from initial space to "```" block

Syntax:
```
didwiki2md.py -i <inputfile> -o <outputfile>
```
Example:
```
didwiki2md.py -i example.didiwiki -o example.md
```

example.didiwiki:
```
=header H1
==header H2
===header H3
Code example:
 s = "foo bar"
 print s
``` 
example.md:
```
# header H1
## header H2
### header H3
Code example:
```
    ```
    s = "foo bar"
    print s
    ```
