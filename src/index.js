const TimelineStream = require('./lib/timeline-stream')
const ConnectionStream = require('./lib/connection-stream')
const getUserProfile = require('./lib/twitter-query').getUserProfile

module.exports = {
  TimelineStream,
  ConnectionStream,
  getUserProfile
}
