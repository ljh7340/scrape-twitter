const express = require('express')
const bodyParser = require('body-parser')
const app = express()
const execa = require('execa')
const fs = require('fs')
app.set('view engine', 'ejs')
app.use(bodyParser.urlencoded({ extended: true }));

const scrapeTwitter = require('./src')

const {
  TimelineStream,
  LikeStream,
  ConnectionStream,
  ConversationStream,
  TweetStream,
  ListStream,
  getUserProfile
} = scrapeTwitter

app.get('/', function (req, res) {
  res.render('index')
})

app.post('/', function (req, res) {
    let handle = req.body.handle;
    console.log('Scraping: ' + handle);
    const timelineStream = new TimelineStream(handle, false, true, 10, process.env)
    console.log(timelineStream._read())
    var wstream = fs.createWriteStream('test.txt')
    timelineStream.on('end', function (wstream) {
      timelineStream.pipe(wstream)
      console.log("done!")
    })
    wstream.write("Hey!")
})
port = process.env.PORT || 3000;
app.listen(port, function () {
  console.log('Example app listening on port ' + port)
})