import feedparser, hashlib
from datetime import datetime
from dateutil import tz
import dateparser

def parse_rss(url: str, tz_name: str = "Europe/London"):
    feed = feedparser.parse(url)
    zone = tz.gettz(tz_name)
    for e in feed.entries:
        title = e.get("title", "").strip()
        link = e.get("link")
        summary = (e.get("summary") or e.get("description") or "").strip()
        dt = None
        if pub := e.get("published") or e.get("updated"):
            dt = dateparser.parse(pub)
        if dt:
            dt = dt.astimezone(zone)
        # crude company/location guess; refined later
        key = f"{title}|{link}"
        yield {
            "id": hashlib.sha1(key.encode()).hexdigest(),
            "title": title,
            "url": link,
            "snippet": summary,
            "published_at": dt,
            "source": url
        }