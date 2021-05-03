## Description

I made a website to collect reaction images, feel free to upload some!
(provide them the ip, if you're following the setup to test the challgenge it would be the ip of the machine running the docker container)

### Setup

1. docker build . -t revshl
2. docker run -p 80:80 revshl

this is an instanced challenge -- we'll try using Pico's instanced docker challenge type

## Solution

`gigem{R3vER5e_R3ver5e!}`

I downloaded a php reverse shell off the internet, named it revshell.png.php, and navigated to that location in the uploads directory.  File extension is calculated by splitting the filename by a period and then comparing filename[1] to an array of allowed file extensions.  png.php passes that but is still a PHP file so Apache will execute code for us.  
