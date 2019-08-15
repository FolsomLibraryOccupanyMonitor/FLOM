## What is HTML?
HTML is short for "HyperText Markup Language." It simply means it is a language for describing web-pages using ordinary text.
## HTML Files
Every web page is an HTML file. Each HTML file is just like a plain-text file but with a ```.html``` extension instead of ```.txt```
## HTML Tags
HTML tags are hidden *keywords* within a web page that define how your web browser must format and display the content.       
Most tags have two parts, an opening and a closing part. For example, ```<html>``` is the opening tag and ```</html>``` is the closing tag. Note that the closing tag has the same text as the opening tag, but has an additional forward-slash(/) character.       
There are some tags that are an exception to this rule, where a closing tag is not required. The ```<img>``` tag for showing images is one example of this.        
Each HTML file must have the essential tags for it to be valid, so that web browsers can understand it and display it correctly. The essential tags are:
- ```<html></html>```
- ```<head></head>```
- ```<title></title>```
- ```<body></body>```
#### Definition - ```<html> </html>```
This basically defines the document as web page. It also identifies the beginning and end of the HTML document. All other tags must fall between the html tags.
#### Header - ```<head> </head>```
The header file contains information about the document that will not appear on the actual page, such as the title of the document, the author, which stylesheet to use and also meta tags.
#### Title - ```<title> </title>```
The title tag defines the title that will appear in the title bar of your web browser. The title must appear between the head tags.
#### Body - ```<body> </body>```
The body tags contain all the information and other visible content on the page. All your images, links, and plain text must go between the ```<body>``` and ```</body>``` tags.
#### Example: Basic HTML Structure
``` 
<html>
  <head>
    <title>My Page Title</title>
  </head>
  <body>
    This is where all my web page content goes!
  </body>
</html>
```
## Tag Attributes
Attributes allow you to customize a tag, and are defined within the opening tag, for example:      
```<img src="image1.jpg>``` or ```<p align="center">```...```</p>```
## Common Tags
| HTML Code                                 | Description                                                |
| ----------------------------------------- |:----------------------------------------------------------:|
| ```<h?> heading </h?>```                  | heading (h1 for largest to h6 for smallest)                |
| ```<p> paragraph </p?>```                 | Paragraph of Text                                          |
| ```<b> bold </b>```                       | Make text between tags bold                                |  
| ```<i> italic </i>```                     | Make text between tags italic                              |
|```<a href="url"> link name </a>```        | Create a link to another page or website                   |
|```<div>...</div>```                       | Divide up page content into sections, and applyting styles |
|```<img src="filename.jpg">```             | Show an image                                              |
|```<ul> <li> list </li> </ul>```           | Unordered, bullet-point list                               |
|```<br>```                                 | Line Break (force a new line)                              |
|```<span style="color:red"> red </span>``` | Use CSS style to change text color                         |

## Text Formatting
| HTML Code                         | Description                                         |
| --------------------------------- | :-------------------------------------------------- |
| ```<h?>...</h?>```                | Heading (?=1 for largest to 6 for smallest, e.g. h1 |
|```<b>...</b>```                   | Bold Text                                           |
|```<i>...</i>```                   | Italic Text                                         |
|```<u>...</u>```                   | Underline text                                      |
|```<strike>...</strike>```         | Strikeout Text                                      |
|```<sup>...</sup>```               | Superscript - Smaller text placed above normal text |
|```<small>...</small>```           | Subscript - Smaller text placed below normal text   |
|```<tt>...</tt>```                 | Typewriter text                                     |
|```<pre>...</pre>```               | Pre-formatted Text                                  |
|```<blockquote>...</blockquote>``` | Text Block Quote                                    |
|```<strong>...</strong>```         | Strong- Shown as Bold in most browsers              |
|```<em>...</em>```                 | Emphasis - Shown as Italics in most browsers        |
|```<font>...</font>```             | Font tag obsolete, use CSS (see below)              |

## Section Divisions
| HTML Code                    | Description                               |
| ---------------------------  | :---------------------------------------- |
| ```<div>...</div>```         | Division or Section of Page Content       |
|```<span>...</span>```        | Section of text within other content      |
|```<p>...</p>```              | Paragraph of text                         |
|```<br>```                    | Line Break                                |
|```<nobr>...</nobr>```        | Line Break                                |
|```<hr>```                    | Basic horizontal Line                     |
|```<hr>``` Tag Attributes:    |                                           |
| ```   size="?"```            | Line Thickness in pixels                  |
| ```   width="?"```           | Line Width in pixels                      |
| ```   width="??%"```         | Line Width as a percentage                |
| ```   color="#??????"```     | Line Color (see below)                    |
| ```   align="?"```           | Horizontal Alignment: left, center, right |
| ```   noshade```             | No 3D cut-out                             |

## Images
| HTML Code                      | Description                               |
| ------------------------------ | :---------------------------------------- |
| ```<img sr"url" alt="text">``` | Basic Image                               |
| ```<img>``` Tag Attributes:    |                                           |
| ```   src="url"```             | URL or filename of image (required!)      |
| ```   alt="text"```            | Alternate Text (required!)                |
| ```   align="?"```             | Image alignment within surrounding text   |
| ```   width="??"```            | Image width (in pixels or %)              |
| ```   height="??"```           | Image height (in pixels or %)             |
| ```   border="??"```           | Border thickness (in pixels)              |
| ```   vpace="??"```            | Space above and below image (in pixels)   |
| ```   hspace="??"```           | Space on either side of image (in pixels) |

## Linking Tags




###### Resources: 
###### http://www.simplehtmlguide.com/whatishtml.php
###### http://www.simplehtmlguide.com/basics.php
###### http://www.simplehtmlguide.com/essential.php
###### http://www.simplehtmlguide.com/cheatsheet.php
