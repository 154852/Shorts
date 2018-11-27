let robot = require('robotjs');
let http = require('http');

http.createServer(function (req, res) {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.end();

    robot.mouseClick();
    robot.typeStringDelayed(decodeURIComponent(req.url.slice(1)), 0);
}).listen(8080);
