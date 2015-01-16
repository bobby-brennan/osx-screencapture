var Exec = require('child_process').exec;

Exec('./parser.py', function(err, stdout, stderr) {
  stdout = stdout.replace(/\(/g, '[').replace(/\)/g, ']').replace(/'/g, '')
  var winIds = JSON.parse(stdout);
  winIds = winIds.map(function(d) { return d[1] })
  console.log('stdout:' + JSON.stringify(winIds));
  winIds.forEach(function(d) {
    Exec('screencapture -l' + d + ' ' + d + '.jpg')
  })
})
