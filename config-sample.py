DELICIOUS, TWITTER, BLOG = range(3)
LIMIT = 10
TEASER_LEN = 280

FEEDS = [
    # type (BLOG|TWITTER|DELICIOUS), site, feed url and flavor (atom|rss)
#    (BLOG, 'http://someblog.com/', 'http://someblog.com/feed/', 'atom'),
#    (DELICIOUS, 'http://delicious.com/username', 'http://feeds.delicious.com/v2/rss/username?count=15', 'rss'),
    (TWITTER, 'http://twitter.com/passiomatic', 'https://api.twitter.com/1/statuses/user_timeline.rss?screen_name=passiomatic', 'rss'),
]

