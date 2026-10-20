#!/usr/bin/env python3
"""Render the buildless catalog from videos.json using only the standard library."""
import json
from collections import OrderedDict
from html import escape
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent

ART = {
    'ddd-example': '<path d="M70 50h110M125 20v60" opacity=".4"/><rect x="30" y="30" width="50" height="40" rx="5"/><rect x="100" y="5" width="50" height="35" rx="5"/><rect x="170" y="30" width="50" height="40" rx="5"/><rect x="100" y="60" width="50" height="35" rx="5"/><circle cx="125" cy="50" r="4" fill="currentColor"/>',
    'tactical-ddd': '<rect x="36" y="10" width="178" height="80" rx="8" opacity=".5"/><rect x="52" y="25" width="65" height="50" rx="4"/><rect x="133" y="25" width="65" height="50" rx="4"/><path d="M68 42h32M68 53h21M149 42h32M149 53h21" opacity=".6"/><path d="M117 50h16"/>',
    'java-concurrency': '<path d="M125 20v24M125 44H45v28M125 44h80v28M125 44v28" opacity=".65"/><circle cx="125" cy="15" r="9"/><rect x="30" y="72" width="30" height="20" rx="4"/><rect x="110" y="72" width="30" height="20" rx="4"/><rect x="190" y="72" width="30" height="20" rx="4"/><circle cx="125" cy="44" r="3" fill="currentColor"/>',
    'latency': '<path d="M20 80h210M20 80V15" opacity=".25"/><path d="M25 67h35l12-28 18 34 16-55 18 43 15-20 16 8h65" stroke-width="2"/><path d="M30 25h32M30 32h20" opacity=".4"/>',
    'distributed-transactions': '<circle cx="40" cy="50" r="12"/><path d="M52 50h10M62 50c8 0 6-26 18-26h16M62 50h34M62 50c8 0 6 26 18 26h16" opacity=".5"/><rect x="96" y="16" width="26" height="14" rx="4"/><rect x="96" y="43" width="26" height="14" rx="4"/><rect x="96" y="70" width="26" height="14" rx="4"/><path d="M132 50h22" opacity=".4"/><circle cx="166" cy="50" r="8"/><circle cx="196" cy="50" r="8"/><circle cx="226" cy="50" r="8"/><path d="M174 50h14M204 50h14" opacity=".55"/><path d="M236 44l9 6-9 6" opacity=".9"/>',
    'computer-architecture': '<rect x="83" y="12" width="84" height="76" rx="6"/><rect x="98" y="27" width="54" height="46" rx="2" opacity=".6"/><path d="M102 41h12l-12 14h12M133 41v14m-6-14v14m-6-14v14"/><path d="M95 2v10m20-10v10m20-10v10m20-10v10M95 88v10m20-10v10m20-10v10m20-10v10M73 24h10m-10 18h10m-10 18h10m-10 18h10M167 24h10m-10 18h10m-10 18h10m-10 18h10" opacity=".5"/>',
    'ai-pr-reviewer': '<path d="M125 50L60 20M125 50l65-30M125 50L60 80M125 50l65 30" opacity=".55"/><circle cx="125" cy="50" r="16"/><circle cx="55" cy="18" r="12"/><circle cx="195" cy="18" r="12"/><circle cx="55" cy="82" r="12"/><circle cx="195" cy="82" r="12"/><circle cx="125" cy="50" r="4" fill="currentColor"/>',
    'agentic-pr-factory': '<path d="M18 84C60 84 76 24 118 20c26-2 42 6 60 6h54" stroke-width="2"/><circle cx="42" cy="72" r="5"/><circle cx="70" cy="46" r="5"/><circle cx="100" cy="28" r="5"/><circle cx="150" cy="24" r="5"/><circle cx="196" cy="26" r="5"/><path d="M18 88h214" opacity=".35"/><path d="M158 20l10 6-10 6" opacity=".8"/>',
    'system-design-course': '<path d="M40 20h50v20H40zM40 60h50v20H40zM160 20h50v20h-50zM160 60h50v20h-50z" opacity=".55"/><path d="M90 30h40M90 70h40M130 30v40" opacity=".6"/><circle cx="130" cy="50" r="7"/><path d="M20 50h13M227 50h13" opacity=".4"/><circle cx="130" cy="50" r="2.5" fill="currentColor"/>',
    'ticketmaster-design': '<rect x="28" y="24" width="194" height="52" rx="9"/><path d="M148 24v52" stroke-dasharray="6 5"/><circle cx="183" cy="50" r="9"/><path d="M48 40h66M48 60h46" opacity=".55"/>',
}


def render():
    videos = json.loads((ROOT / 'videos.json').read_text())
    groups = OrderedDict()
    for video in videos:
        groups.setdefault(video['group'], []).append(video)
    topic_links = ['<a class="active" href="#library">All topics <span>%02d</span></a>' % len(videos)]
    sections = []
    for number, (group, entries) in enumerate(groups.items(), 1):
        topic = entries[0]['topic']
        topic_links.append(f'<a href="#{escape(group)}">{escape(topic)} <span>{len(entries):02d}</span></a>')
        cards = []
        for video in entries:
            path = quote(video['folder'], safe='') + '/' + quote(video['page'], safe='')
            tags = ''.join(f'<span>{escape(tag)}</span>' for tag in video['tags'])
            searchable = escape(video['topic'] + ' ' + video['venue'])
            cards.append(f'''<article class="study-card" data-tone="{escape(video['tone'])}" data-search="{searchable}">
  <div class="card-art" aria-hidden="true"><span class="card-index">{videos.index(video)+1:02d} / {len(videos):02d}</span>
    <svg viewBox="0 0 250 100" fill="none" stroke="currentColor" stroke-width="1.4">{ART.get(video['id'], ART['ddd-example'])}</svg>
    <span class="art-label">{escape(video['tags'][0]).upper()}</span>
  </div>
  <div class="card-content">
    <div class="card-meta"><span>{escape(video['venue'])}</span><span class="small-dot"></span><span>{escape(video['duration'])} video</span></div>
    <h3><a href="{path}">{escape(video['title'])}</a></h3>
    <p>{escape(video['description'])}</p>
    <div class="card-tags">{tags}</div>
    <div class="card-bottom"><span>{escape(video['speaker'])}</span><a href="{path}" aria-label="Read the guide: {escape(video['title'])}">Read guide <span aria-hidden="true">↗</span></a></div>
  </div>
</article>''')
        sections.append(f'''<section class="topic-group" id="{escape(group)}" aria-labelledby="{escape(group)}-title">
  <div class="group-heading"><h2 id="{escape(group)}-title">{escape(topic)}</h2><span class="group-number">{number:02d} / {len(entries)} {'guide' if len(entries)==1 else 'guides'}</span></div>
  <div class="study-grid {'single' if len(entries)==1 else ''}">{''.join(cards)}</div>
</section>''')
    html = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="A developer's video study library. Explore structured guides to domain-driven design, Java concurrency, distributed systems, computer architecture, and AI agents.">
  <meta name="theme-color" content="#111513"><title>Video Notes — A developer's study library</title>
  <link rel="icon" href="assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="assets/site.css">
  <script src="assets/site.js" defer></script>
</head>
<body class="catalog-page" id="top">
<a class="skip-link" href="#library">Skip to the library</a>
<header class="site-bar"><div class="site-bar-inner">
  <a class="site-brand" href="index.html" aria-label="Video Notes home"><span class="brand-mark" aria-hidden="true">⌁</span><span>Video Notes<span class="brand-dot">.</span></span></a>
  <nav class="site-nav" aria-label="Site navigation"><a href="#library" aria-current="page">The library</a><a href="#about">About</a><span class="nav-note">MADE FOR CURIOUS DEVELOPERS</span></nav>
</div></header>
<main class="catalog">
  <section class="catalog-hero" aria-labelledby="page-title">
    <div><span class="eyebrow">A developer's study library</span><h1 id="page-title">Long talks.<br><em>Lasting ideas.</em></h1>
      <p>Good engineering talks deserve a second life. Explore their ideas through structured notes, code examples, and visual explanations.</p></div>
    <div class="hero-aside"><div class="collection-stats"><div><strong>{len(videos):02d}</strong><span>study guides</span></div><div><strong>{len(groups):02d}</strong><span>topic collections</span></div></div>
      <div><span class="section-label">From watching to understanding</span><p>Pick a topic. Follow the reasoning. Keep the details close when you need them again.</p></div></div>
  </section>
  <div class="library-toolbar" id="library"><h2>The collection <small id="result-count" role="status" aria-live="polite">{len(videos)} guides</small></h2>
    <label class="search-field"><span aria-hidden="true">⌕</span><input id="library-search" type="search" placeholder="Search topics, talks, or speakers…" aria-label="Search guides" autocomplete="off"></label></div>
  <div class="library-layout">
    <aside class="topic-sidebar"><span class="section-label">Browse by topic</span><nav aria-label="Topics">{''.join(topic_links)}</nav>
      <p class="sidebar-note">Each guide preserves the talk's reasoning, with examples and a link to the original recording.</p></aside>
    <div class="library-groups">{''.join(sections)}
      <div class="empty-state" id="empty-state" hidden><h2>No guides found</h2><p>Try a topic such as Java, DDD, or AI, or search for a speaker.</p><button id="clear-search" type="button">Clear search</button></div>
    </div>
  </div>
</main>
<footer class="site-footer" id="about"><span>Video Notes · A personal collection of developer study guides.<br>Original ideas belong to the speakers. Follow each guide for sources and context.</span><a href="#top">Back to top ↑</a></footer>
</body>
</html>
'''
    (ROOT / 'index.html').write_text(html)
    print(f'Rendered catalog: {len(videos)} guides in {len(groups)} topic groups.')


if __name__ == '__main__':
    render()
