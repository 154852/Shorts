# TypeRacer Hacker
This is a program to win at the [TypeRacer](https://play.typeracer.com/) game, with it a score of around 350WPM is obtainable.

## To use
1. On your computer, ensure you have node and npm installed
2. Run `npm install robotjs`
3. Download the server.js file
4. Run `node server.js`
5. Go to [play.typeracer.com](https://play.typeracer.com/)
6. Open the devloper tools
7. Copy and paste the contents of client.js
8. Click 'Enter a typing race'
9. Click on the pasted code to bring focus to the dev panel
10. Hover your mouse over the input
11. Press enter
12. Win.

## How it works
Server.js sets up a server running locally (port 8080) that will take any request and just take the keyboard and type it out. 
This means that JavaScript, who cannot do this, only has to send a request to your server with the desired text in it (hence the XMLHttpRequest).
This desired text can be found in the innerText of the parent of the element at the selector `.inputPanel span`. The interval is there to
ensure that typing starts as early as is possible without starting before the timer allows, it simply checks if the countdown has reached 0.
