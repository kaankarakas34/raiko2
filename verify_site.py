"""Check generated SEO signals and internal navigation before publishing."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote
import xml.etree.ElementTree as ET

ROOT = Path(__file__).parent / "dist"
DOMAIN = "https://www.raiko.tech"


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.h1 = 0
        self.links = []
        self.anchors = set()
        self.canonical = []
        self.og_url = []
        self.title = False
        self.description = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "h1":
            self.h1 += 1
        if tag == "title":
            self.title = True
        if "id" in attrs:
            self.anchors.add(attrs["id"])
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical.append(attrs.get("href"))
        if tag == "meta" and attrs.get("property") == "og:url":
            self.og_url.append(attrs.get("content"))
        if tag == "meta" and attrs.get("name") == "description":
            self.description = bool(attrs.get("content"))


pages = {}
for path in ROOT.rglob("index.html"):
    route = "/" + path.parent.relative_to(ROOT).as_posix().strip("./")
    route = "/" if route == "/" else route + "/"
    page = Page()
    page.feed(path.read_text(encoding="utf-8"))
    assert page.h1 == 1 and page.title and page.description, f"Missing page metadata: {route}"
    assert page.canonical == [DOMAIN + route], f"Canonical mismatch: {route}"
    assert page.og_url == [DOMAIN + route], f"Open Graph URL mismatch: {route}"
    pages[route] = page

for route, page in pages.items():
    for href in page.links:
        parsed = urlparse(href)
        if parsed.scheme or parsed.netloc:
            continue
        target = unquote(parsed.path or route)
        if not target.startswith("/"):
            continue
        assert target in pages or (ROOT / target.lstrip("/")).is_file(), f"Broken link: {route} → {href}"
        if parsed.fragment and target in pages:
            assert parsed.fragment in pages[target].anchors, f"Missing anchor: {route} → {href}"

tree = ET.parse(ROOT / "sitemap.xml")
locs = {node.text for node in tree.findall(".//{*}loc")}
assert locs == {DOMAIN + route for route in pages}, "Sitemap and generated pages differ"
assert f"Sitemap: {DOMAIN}/sitemap.xml" in (ROOT / "robots.txt").read_text(encoding="utf-8")
assert (ROOT / "social-card.png").is_file()
print(f"Verified {len(pages)} pages, internal links, anchors, sitemap and robots.txt")
