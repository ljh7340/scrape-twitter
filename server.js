const express = require('express')
const bodyParser = require('body-parser')
const app = express()
const execa = require('execa')
app.set('view engine', 'ejs')
app.use(bodyParser.urlencoded({ extended: true }));

app.get('/', function (req, res) {
  res.render('index')
})

app.post('/', function (req, res) {
    let handle = req.body.handle;
    console.log('Scraping: ' + handle);
    const command = execa('scrape-twitter-timeline', [handle, '-c', 10])
    command.stdout.pipe(process.stdout)
    command.stderr.pipe(process.stderr)
})
port = process.env.PORT || 80;
app.listen(port, function () {
  console.log('Example app listening on port ${port}!')
})