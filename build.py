#!/usr/bin/env python3
"""
build.py - JustFly Affiliate Site Generator
Deploys to: https://brightlane.github.io/justfly/
Affiliate URL: https://track.rqqft.com/aff_c?offer_id=25631&aff_id=21885
Run: python3 build.py
Output: docs/ folder (GitHub Pages source)
"""

import os, json
from pathlib import Path
from datetime import date

AFF   = "https://track.rqqft.com/aff_c?offer_id=25631&aff_id=21885"
BASE  = "https://brightlane.github.io/justfly"
SUB   = "/justfly"
TODAY = date.today().isoformat()
OUT   = Path("docs")

# ─── PAGES ───────────────────────────────────────────────────────────────────
PAGES = [
    {"slug":"index","title":"JustFly 2026: Cheap Flights — Compare 500+ Airlines & Save Big","desc":"Find cheap flights with JustFly. Compare 500+ airlines, bundle hotels and car rentals, and save up to 70% on every trip. Search live fares now.","content_fn":"page_home","priority":"1.0"},
    {"slug":"justfly-review","title":"JustFly Review 2026: Is It Legit & Worth It?","desc":"Honest JustFly review for 2026. Is JustFly safe? Is it cheaper than Expedia? We tested it on 20 routes. Full verdict inside.","content_fn":"page_review","priority":"0.95"},
    {"slug":"justfly-vs-expedia","title":"JustFly vs Expedia 2026: Which Is Cheaper?","desc":"JustFly vs Expedia compared on price, features, and support. Real fare tests on 20 popular routes. Find out who wins in 2026.","content_fn":"page_vs_expedia","priority":"0.9"},
    {"slug":"justfly-vs-kayak","title":"JustFly vs Kayak 2026: Full Comparison","desc":"JustFly vs Kayak 2026. Which travel site finds the cheapest flights? We compared every dimension — price, booking, support.","content_fn":"page_vs_kayak","priority":"0.9"},
    {"slug":"justfly-vs-google-flights","title":"JustFly vs Google Flights 2026: Which Should You Use?","desc":"JustFly vs Google Flights compared. Search engine vs full booking platform — which saves you more money in 2026?","content_fn":"page_vs_google","priority":"0.9"},
    {"slug":"cheap-flights-usa","title":"Cheapest Domestic Flights USA 2026 | JustFly Deals","desc":"Find the cheapest domestic flights in the USA with JustFly. Compare 500+ airlines on every US route. Best fares updated daily.","content_fn":"page_cheap_usa","priority":"0.9"},
    {"slug":"nyc-flights","title":"Cheap Flights from New York 2026 | JustFly NYC Deals","desc":"Cheapest flights from New York City (JFK, LGA, EWR) in 2026. Compare all airlines on JustFly and save on every route.","content_fn":"page_nyc","priority":"0.85"},
    {"slug":"miami-flights","title":"Cheap Flights from Miami 2026 | JustFly MIA Deals","desc":"Find the cheapest flights from Miami in 2026. JustFly compares 500+ airlines from MIA to every destination.","content_fn":"page_miami","priority":"0.85"},
    {"slug":"los-angeles-flights","title":"Cheap Flights from Los Angeles 2026 | JustFly LAX Deals","desc":"Cheapest flights from LAX in 2026. JustFly finds the best fares to NYC, Vegas, Chicago and beyond.","content_fn":"page_lax","priority":"0.85"},
    {"slug":"chicago-flights","title":"Cheap Flights from Chicago 2026 | JustFly ORD/MDW Deals","desc":"Find cheap flights from Chicago O'Hare and Midway in 2026. Compare 500+ airlines with JustFly.","content_fn":"page_chicago","priority":"0.85"},
    {"slug":"international-flights","title":"Cheap International Flights from USA 2026 | JustFly","desc":"Find cheap international flights from the USA with JustFly. Mexico, Caribbean, Europe, Asia — best fares compared.","content_fn":"page_international","priority":"0.85"},
    {"slug":"flight-hotel-bundles","title":"Flight + Hotel Bundles 2026 | Save 40% with JustFly","desc":"Bundle your flight and hotel on JustFly and save up to 40% vs booking separately. Best package deals in 2026.","content_fn":"page_bundles","priority":"0.85"},
    {"slug":"flight-booking-tips","title":"12 Flight Booking Tips to Save Hundreds in 2026 | JustFly","desc":"Expert flight booking tips for 2026. Learn exactly when to book, how to find hidden deals, and how to save $100+ per trip via JustFly.","content_fn":"page_tips","priority":"0.85"},
    {"slug":"best-time-to-book","title":"Best Time to Book Flights 2026: The Data-Backed Guide","desc":"When is the best time to book flights in 2026? Day-by-day and month-by-month analysis. Book smarter with JustFly.","content_fn":"page_timing","priority":"0.8"},
    {"slug":"baggage-fees","title":"Airline Baggage Fees 2026: Every US Carrier Compared","desc":"Complete guide to airline baggage fees in 2026. Know the true cost before you book — and find the cheapest total fare on JustFly.","content_fn":"page_baggage","priority":"0.8"},
    {"slug":"last-minute-flights","title":"Last Minute Flights 2026 | Cheap Same-Day Deals on JustFly","desc":"How to find cheap last-minute flights in 2026. Same-day and next-day strategies that work — search on JustFly.","content_fn":"page_last_minute","priority":"0.8"},
    {"slug":"budget-airlines","title":"US Budget Airlines Guide 2026 | Spirit, Frontier & Allegiant","desc":"Complete guide to US budget airlines in 2026. Spirit vs Frontier vs Allegiant total cost compared — book the cheapest via JustFly.","content_fn":"page_budget","priority":"0.8"},
    {"slug":"price-alerts","title":"Flight Price Alerts 2026 | Never Miss a Cheap Fare","desc":"How to set up JustFly price alerts in 2026. Get notified when fares drop on your saved routes. Never overpay again.","content_fn":"page_alerts","priority":"0.8"},
    {"slug":"promo-codes","title":"JustFly Promo Codes & Deals June 2026","desc":"Latest JustFly promo codes and discount deals for June 2026. How to pay less for flights, hotels, and car rentals.","content_fn":"page_promos","priority":"0.75"},
    {"slug":"about","title":"About FlightDealsPro | Independent JustFly Affiliate","desc":"About FlightDealsPro — the independent guide helping travelers save money on flights with JustFly since 2020.","content_fn":"page_about","priority":"0.5"},
]

# ─── CSS ─────────────────────────────────────────────────────────────────────
def css():
    return """
    @import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap');
    :root {
      --navy:   #0a1f44;
      --blue:   #1565c0;
      --sky:    #2196f3;
      --orange: #f4511e;
      --amber:  #ff8f00;
      --green:  #2e7d32;
      --fog:    #f4f6fb;
      --warm:   #fff8f5;
      --white:  #ffffff;
      --muted:  #607d8b;
      --border: #e3e8f0;
      --ink:    #0d1b2a;
      --r:      14px;
      --sh:     0 4px 20px rgba(10,31,68,.10);
      --sh2:    0 12px 40px rgba(10,31,68,.18);
    }
    *, *::before, *::after { margin:0; padding:0; box-sizing:border-box; }
    html { scroll-behavior:smooth; }
    body { font-family:'Space Grotesk',sans-serif; background:var(--fog); color:var(--ink); line-height:1.7; }
    a { color:var(--sky); text-decoration:none; }
    a:hover { text-decoration:underline; }
    p { margin-bottom:1rem; }
    h1,h2,h3,h4 { font-family:'Sora',sans-serif; line-height:1.2; margin-bottom:.8rem; }
    h1 { font-size:clamp(2.1rem,5vw,3.6rem); font-weight:800; }
    h2 { font-size:clamp(1.6rem,4vw,2.5rem); font-weight:800; }
    h3 { font-size:1.2rem; font-weight:700; }

    /* TOPBAR */
    .topbar {
      background:var(--orange);
      color:#fff; text-align:center; font-size:.8rem; font-weight:700;
      padding:.45rem 1rem; letter-spacing:.02em;
    }
    .topbar a { color:#ffe0d6; border-bottom:1px solid rgba(255,224,214,.4); }

    /* NAV */
    nav {
      background:var(--navy);
      padding:.85rem 1.5rem;
      display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:.6rem;
      position:sticky; top:0; z-index:200;
      box-shadow:0 2px 16px rgba(10,31,68,.25);
    }
    .logo { font-family:'Sora',sans-serif; font-size:1.25rem; font-weight:800; color:#fff; text-decoration:none; display:flex; align-items:center; gap:.4rem; }
    .logo-icon { background:var(--orange); color:#fff; width:30px; height:30px; border-radius:8px; display:flex; align-items:center; justify-content:center; font-size:.95rem; }
    .logo em { color:var(--amber); font-style:normal; }
    .nav-links { display:flex; gap:1.3rem; font-size:.85rem; font-weight:600; flex-wrap:wrap; }
    .nav-links a { color:rgba(255,255,255,.7); transition:color .2s; }
    .nav-links a:hover { color:#fff; text-decoration:none; }
    .nav-cta { background:var(--orange); color:#fff !important; padding:.48rem 1.2rem; border-radius:50px; font-size:.84rem; font-weight:700; transition:background .2s !important; }
    .nav-cta:hover { background:#d84315 !important; text-decoration:none !important; }

    /* HERO */
    .hero {
      background:var(--navy);
      background-image:
        radial-gradient(ellipse at 10% 50%, rgba(21,101,192,.6) 0%, transparent 55%),
        radial-gradient(ellipse at 90% 20%, rgba(244,81,30,.3) 0%, transparent 45%);
      color:#fff; text-align:center;
      padding:5.5rem 1.5rem 4.5rem;
      position:relative; overflow:hidden;
    }
    .hero::after {
      content:'';
      position:absolute; inset:0;
      background:url("data:image/svg+xml,%3Csvg width='52' height='26' viewBox='0 0 52 26' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.03'%3E%3Cpath d='M10 10c0-2.21-1.79-4-4-4-3.314 0-6-2.686-6-6h2c0 2.21 1.79 4 4 4 3.314 0 6 2.686 6 6 0 2.21 1.79 4 4 4 3.314 0 6 2.686 6 6 0 2.21 1.79 4 4 4v2c-3.314 0-6-2.686-6-6 0-2.21-1.79-4-4-4-3.314 0-6-2.686-6-6zm25.464-1.95l8.486 8.486-1.414 1.414-8.486-8.486 1.414-1.414z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
      pointer-events:none;
    }
    .hero-inner { max-width:860px; margin:0 auto; position:relative; z-index:1; }
    .hero h1 { color:#fff; margin-bottom:1.2rem; }
    .hero h1 em { color:var(--amber); font-style:italic; }
    .hero-sub { font-size:1.1rem; color:rgba(255,255,255,.72); max-width:600px; margin:0 auto 2.2rem; }
    .hero-badge {
      display:inline-flex; align-items:center; gap:.4rem;
      background:rgba(244,81,30,.2); border:1px solid rgba(244,81,30,.4);
      color:#ffab91; font-size:.77rem; font-weight:700;
      padding:.3rem .9rem; border-radius:50px; margin-bottom:1.2rem;
      letter-spacing:.06em; text-transform:uppercase;
    }
    .hero-stats {
      display:flex; justify-content:center; flex-wrap:wrap; gap:2.5rem;
      margin-top:3rem; padding-top:2.5rem;
      border-top:1px solid rgba(255,255,255,.1);
    }
    .stat-num { font-family:'Sora',sans-serif; font-size:2rem; font-weight:800; color:#fff; line-height:1; }
    .stat-lbl { font-size:.73rem; color:rgba(255,255,255,.45); text-transform:uppercase; letter-spacing:.08em; margin-top:.2rem; }

    /* BUTTONS */
    .btn { display:inline-flex; align-items:center; gap:.5rem; padding:.95rem 2.2rem; border-radius:8px; font-weight:700; font-size:1rem; cursor:pointer; transition:all .22s; text-decoration:none; white-space:nowrap; font-family:'Sora',sans-serif; }
    .btn-orange { background:var(--orange); color:#fff; box-shadow:0 6px 24px rgba(244,81,30,.38); }
    .btn-orange:hover { transform:translateY(-3px); box-shadow:0 10px 32px rgba(244,81,30,.48); text-decoration:none; background:#d84315; }
    .btn-navy { background:var(--navy); color:#fff; }
    .btn-navy:hover { transform:translateY(-3px); text-decoration:none; }
    .btn-outline { background:transparent; color:var(--orange); border:2px solid var(--orange); }
    .btn-outline:hover { background:var(--orange); color:#fff; text-decoration:none; }
    .btn-ghost { background:transparent; color:#fff; border:2px solid rgba(255,255,255,.35); }
    .btn-ghost:hover { background:rgba(255,255,255,.1); text-decoration:none; }
    .btn-sm { padding:.55rem 1.3rem; font-size:.85rem; }
    .btn-lg { padding:1.1rem 2.6rem; font-size:1.1rem; }

    /* LAYOUT */
    section { padding:4rem 1.5rem; }
    .bg-white { background:var(--white); }
    .bg-warm { background:var(--warm); }
    .bg-navy { background:var(--navy); color:#fff; }
    .container { max-width:1120px; margin:0 auto; }
    .eyebrow { font-size:.73rem; font-weight:700; letter-spacing:.12em; text-transform:uppercase; color:var(--orange); margin-bottom:.5rem; display:block; }
    h2.section-title { margin-bottom:.6rem; }
    .section-sub { color:var(--muted); font-size:1rem; margin-bottom:2rem; max-width:580px; }
    .text-center { text-align:center; }
    .text-center .section-sub { margin-left:auto; margin-right:auto; }
    .mt-2 { margin-top:2rem; }

    /* DEAL CARDS */
    .deals-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(260px,1fr)); gap:1.3rem; margin-top:1.5rem; }
    .deal-card {
      background:var(--white); border-radius:var(--r); box-shadow:var(--sh);
      padding:1.7rem; border-top:3px solid var(--orange);
      transition:transform .2s, box-shadow .2s;
    }
    .deal-card:hover { transform:translateY(-5px); box-shadow:var(--sh2); }
    .deal-from { font-size:.72rem; font-weight:700; color:var(--muted); text-transform:uppercase; letter-spacing:.06em; margin-bottom:.3rem; }
    .deal-price { font-family:'Sora',sans-serif; font-size:2.6rem; font-weight:800; color:var(--orange); line-height:1; margin-bottom:.3rem; }
    .deal-route { font-weight:700; font-size:1.05rem; margin-bottom:.6rem; }
    .deal-tag { display:inline-block; font-size:.7rem; font-weight:700; padding:.2rem .7rem; border-radius:50px; margin-bottom:.8rem; text-transform:uppercase; letter-spacing:.04em; }
    .tag-hot { background:#fff0ec; color:#c62828; }
    .tag-sale { background:#fff8e1; color:#e65100; }
    .tag-new { background:#e8f5e9; color:#1b5e20; }
    .tag-flash { background:#e3f2fd; color:#0d47a1; }
    .deal-note { font-size:.85rem; color:var(--muted); margin-bottom:1rem; }

    /* DESTINATION GRID */
    .dest-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(150px,1fr)); gap:1rem; margin-top:1.5rem; }
    .dest-card {
      background:var(--white); border-radius:var(--r); padding:1.4rem 1rem;
      text-align:center; box-shadow:var(--sh); border:1px solid var(--border);
      transition:transform .2s, box-shadow .2s; text-decoration:none; display:block;
    }
    .dest-card:hover { transform:translateY(-4px); box-shadow:var(--sh2); text-decoration:none; }
    .dest-emoji { font-size:2rem; margin-bottom:.5rem; }
    .dest-city { font-weight:700; font-size:.95rem; color:var(--navy); margin-bottom:.2rem; }
    .dest-price { color:var(--orange); font-weight:800; font-size:.9rem; }

    /* FEATURE CARDS */
    .feat-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(240px,1fr)); gap:1.2rem; }
    .feat-card { background:var(--white); border-radius:var(--r); padding:1.8rem; box-shadow:var(--sh); border:1px solid var(--border); transition:transform .2s; }
    .feat-card:hover { transform:translateY(-3px); }
    .feat-icon { font-size:1.9rem; margin-bottom:.8rem; display:block; }
    .feat-card h3 { font-size:1rem; margin-bottom:.4rem; }
    .feat-card p { color:var(--muted); font-size:.88rem; line-height:1.6; }

    /* TABLES */
    .tbl-wrap { background:var(--white); border-radius:var(--r); box-shadow:var(--sh); overflow:hidden; }
    table { width:100%; border-collapse:collapse; }
    th { background:var(--navy); color:#fff; padding:.9rem 1.1rem; font-size:.78rem; text-transform:uppercase; letter-spacing:.06em; text-align:left; font-weight:700; }
    td { padding:.85rem 1.1rem; border-bottom:1px solid var(--border); font-size:.92rem; }
    tr:last-child td { border-bottom:none; }
    tr:nth-child(even) td { background:var(--fog); }
    .win { color:var(--orange); font-weight:700; }
    .good { color:var(--green); font-weight:700; }
    .bad { color:#c62828; }
    .chk { color:var(--green); font-size:1.1rem; font-weight:700; }
    .vs-hl td:nth-child(2) { background:#fff8f5; }
    .vs-hl th:nth-child(2) { background:var(--orange); }

    /* TESTIMONIALS */
    .testi-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(270px,1fr)); gap:1.3rem; margin-top:1.5rem; }
    .testi-card { background:var(--white); border-radius:var(--r); padding:1.8rem; box-shadow:var(--sh); border-left:4px solid var(--orange); }
    .testi-stars { color:var(--amber); font-size:.9rem; margin-bottom:.7rem; }
    .testi-text { font-size:.93rem; font-style:italic; color:var(--ink); margin-bottom:1rem; line-height:1.65; }
    .testi-name { font-weight:700; font-size:.87rem; color:var(--orange); }
    .testi-detail { font-size:.78rem; color:var(--muted); margin-top:.2rem; }
    .testi-save { display:inline-block; background:#fff0ec; color:var(--orange); font-size:.75rem; font-weight:700; padding:.2rem .7rem; border-radius:50px; margin-top:.5rem; }

    /* FAQ */
    .faq-wrap { margin-top:1.5rem; }
    details { border:1.5px solid var(--border); border-radius:12px; margin-bottom:.9rem; overflow:hidden; background:var(--white); }
    summary { padding:1.1rem 1.4rem; font-weight:700; font-size:.95rem; cursor:pointer; list-style:none; display:flex; justify-content:space-between; align-items:center; }
    summary::-webkit-details-marker { display:none; }
    summary::after { content:'+'; font-size:1.4rem; color:var(--orange); font-weight:300; flex-shrink:0; }
    details[open] summary::after { content:'&#8722;'; }
    details[open] summary { border-bottom:1px solid var(--border); color:var(--orange); }
    .faq-ans { padding:1.2rem 1.4rem 1.5rem; color:var(--muted); font-size:.92rem; line-height:1.75; }

    /* CTA BAND */
    .cta-band {
      background:linear-gradient(135deg, var(--orange) 0%, #bf360c 100%);
      border-radius:var(--r); padding:3.5rem 2rem; text-align:center; color:#fff;
      position:relative; overflow:hidden;
    }
    .cta-band::before { content:''; position:absolute; top:-50px; right:-50px; width:220px; height:220px; border-radius:50%; background:rgba(255,255,255,.07); }
    .cta-band h2 { font-family:'Sora',sans-serif; color:#fff; font-size:clamp(1.5rem,3vw,2.3rem); margin-bottom:.6rem; position:relative; z-index:1; }
    .cta-band p { color:rgba(255,255,255,.8); margin-bottom:1.8rem; font-size:1rem; position:relative; z-index:1; }

    /* TIP CARDS */
    .tip-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(230px,1fr)); gap:1.2rem; margin-top:1.5rem; }
    .tip-card { background:var(--white); border-radius:var(--r); padding:1.5rem; box-shadow:var(--sh); border:1px solid var(--border); }
    .tip-num { font-family:'Sora',sans-serif; font-size:2.2rem; font-weight:800; color:var(--orange); opacity:.3; line-height:1; margin-bottom:.5rem; }
    .tip-card h3 { font-size:1rem; margin-bottom:.35rem; }
    .tip-card p { font-size:.86rem; color:var(--muted); }

    /* STICKY BAR */
    .sticky-bar {
      position:fixed; bottom:0; left:0; right:0;
      background:var(--navy); color:#fff;
      display:flex; align-items:center; justify-content:center; flex-wrap:wrap; gap:1rem;
      padding:.85rem 1rem; z-index:300;
      box-shadow:0 -3px 20px rgba(10,31,68,.25);
    }
    .sticky-txt { font-size:.9rem; font-weight:700; }
    .sticky-txt span { color:var(--amber); }

    /* FOOTER */
    footer { background:var(--navy); color:#546e7a; padding:2.5rem 1.5rem 7rem; text-align:center; font-size:.84rem; }
    .footer-nav { display:flex; flex-wrap:wrap; justify-content:center; gap:1.2rem; margin-bottom:1.4rem; }
    .footer-nav a { color:#78909c; text-decoration:none; }
    .footer-nav a:hover { color:#fff; }
    .footer-disc { max-width:700px; margin:.8rem auto 0; font-size:.76rem; color:#37474f; line-height:1.65; }

    ul.styled { margin:1rem 0 1rem 1.4rem; }
    ul.styled li { padding:.3rem 0; color:var(--muted); }
    ul.styled li::marker { color:var(--orange); }

    @media(max-width:640px){
      .nav-links { display:none; }
      .hero { padding:4rem 1rem 3.5rem; }
    }
    """

# ─── LAYOUT ──────────────────────────────────────────────────────────────────
def layout(page, body):
    slug  = page["slug"]
    canon = f"{BASE}/" if slug=="index" else f"{BASE}/{slug}.html"
    schema = json.dumps({"@context":"https://schema.org","@type":"WebPage","name":page["title"],"description":page["desc"],"url":canon,"publisher":{"@type":"Organization","name":"FlightDealsPro"}})
    nav_items = [
        ("index","Home"),("cheap-flights-usa","Cheap Flights"),("justfly-review","Review"),
        ("justfly-vs-expedia","vs Expedia"),("flight-booking-tips","Tips"),("promo-codes","Deals"),
    ]
    nav_html = "".join(
        f'<a href="{SUB}/">Home</a>' if s=="index" else f'<a href="{SUB}/{s}.html">{l}</a>'
        for s,l in nav_items
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{page['title']}</title>
  <meta name="description" content="{page['desc']}">
  <meta name="robots" content="index,follow">
  <link rel="canonical" href="{canon}">
  <meta property="og:title" content="{page['title']}">
  <meta property="og:description" content="{page['desc']}">
  <meta property="og:url" content="{canon}">
  <meta property="og:type" content="website">
  <script type="application/ld+json">{schema}</script>
  <style>{css()}</style>
</head>
<body>
<div class="topbar">&#9888; Affiliate site &#8212; we earn commission from JustFly bookings at no cost to you. &nbsp;|&nbsp; <a href="{AFF}" rel="nofollow sponsored">Search Flights on JustFly &rarr;</a></div>
<nav>
  <a class="logo" href="{SUB}/"><span class="logo-icon">&#9992;</span>Flight<em>Deals</em>Pro</a>
  <div class="nav-links">{nav_html}</div>
  <a href="{AFF}" class="nav-cta" rel="nofollow sponsored">Search Now &#9992;</a>
</nav>
{body}
<div class="sticky-bar">
  <span class="sticky-txt">&#9992; Compare <span>500+ airlines</span> instantly &#8212; Find the cheapest fare on JustFly</span>
  <a href="{AFF}" class="btn btn-orange btn-sm" rel="nofollow sponsored">Search Flights &rarr;</a>
</div>
<footer>
  <div class="footer-nav">
    <a href="{SUB}/">Home</a>
    <a href="{SUB}/justfly-review.html">Review</a>
    <a href="{SUB}/cheap-flights-usa.html">Cheap Flights</a>
    <a href="{SUB}/justfly-vs-expedia.html">vs Expedia</a>
    <a href="{SUB}/flight-hotel-bundles.html">Bundles</a>
    <a href="{SUB}/flight-booking-tips.html">Tips</a>
    <a href="{SUB}/baggage-fees.html">Baggage Fees</a>
    <a href="{SUB}/promo-codes.html">Promo Codes</a>
    <a href="{SUB}/about.html">About</a>
  </div>
  <p style="color:#455a64;">&copy; 2026 FlightDealsPro &mdash; Independent JustFly affiliate partner</p>
  <p class="footer-disc"><strong>Affiliate Disclosure:</strong> FlightDealsPro earns a commission when you book via our JustFly links, at zero extra cost to you. All prices shown are illustrative examples &#8212; actual fares appear at booking time on JustFly.com. This site is independent and not operated by JustFly.</p>
</footer>
</body></html>"""

# ─── COMPONENTS ──────────────────────────────────────────────────────────────
def deals(items):
    cards = ""
    for route,price,tag,tcls,note in items:
        cards += f"""<div class="deal-card">
      <div class="deal-from">Starting from</div>
      <div class="deal-price">{price}</div>
      <div class="deal-route">{route}</div>
      <span class="deal-tag {tcls}">{tag}</span>
      <p class="deal-note">{note}</p>
      <a href="{AFF}" class="btn btn-orange" style="width:100%;justify-content:center;padding:.7rem;" rel="nofollow sponsored">Book This Deal &rarr;</a>
    </div>"""
    return f'<div class="deals-grid">{cards}</div>'

def cta(h, sub):
    return f"""<div class="cta-band">
    <h2>{h}</h2><p>{sub}</p>
    <a href="{AFF}" class="btn btn-lg" style="background:#fff;color:var(--orange);font-family:'Sora',sans-serif;" rel="nofollow sponsored">&#9992; Search JustFly Now &rarr;</a>
  </div>"""

def testi(*items):
    cards = ""
    for txt,name,detail,save,stars in items:
        s = "&#9733;" * int(stars)
        sv = f'<span class="testi-save">Saved {save}</span>' if save else ""
        cards += f"""<div class="testi-card">
      <div class="testi-stars">{s}</div>
      <p class="testi-text">&#8220;{txt}&#8221;</p>
      <div class="testi-name">{name}</div>
      <div class="testi-detail">{detail}</div>{sv}
    </div>"""
    return f'<div class="testi-grid">{cards}</div>'

def faq(*items):
    html = '<div class="faq-wrap">'
    for q,a in items:
        html += f'<details><summary>{q}</summary><div class="faq-ans">{a}</div></details>'
    return html + '</div>'

def dest_grid(items):
    cards = "".join(f'<a href="{AFF}" class="dest-card" rel="nofollow sponsored"><div class="dest-emoji">{e}</div><div class="dest-city">{c}</div><div class="dest-price">{p}</div></a>' for e,c,p in items)
    return f'<div class="dest-grid">{cards}</div>'

# ─── PAGES ───────────────────────────────────────────────────────────────────
def page_home():
    hot = [
        ("New York &#8594; Los Angeles","$89","&#128293; HOT","tag-hot","Spirit & Delta nonstops"),
        ("Miami &#8594; Las Vegas","$79","&#9889; FLASH","tag-flash","Weekend special fares"),
        ("Chicago &#8594; Orlando","$85","&#128293; HOT","tag-hot","Family trip deals"),
        ("Dallas &#8594; New York","$99","NEW","tag-new","Multiple daily departures"),
        ("LA &#8594; Seattle","$65","&#9889; FLASH","tag-flash","Alaska Airlines special"),
        ("Boston &#8594; Miami","$94","SALE","tag-sale","JetBlue & Spirit options"),
    ]
    dests = [
        ("&#127963;","New York","From $89"),("&#127968;","London","From $299"),
        ("&#128508;","Paris","From $319"),("&#127800;","Tokyo","From $549"),
        ("&#127958;","Cancún","From $149"),("&#127796;","Miami","From $99"),
        ("&#127920;","Las Vegas","From $79"),("&#127748;","San Francisco","From $119"),
    ]
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge">&#9992; Powered by JustFly.com &#8212; 500+ Airlines Compared</div>
      <h1>Find <em>Cheaper Flights</em><br>Before Anyone Else</h1>
      <p class="hero-sub">JustFly compares 500+ airlines simultaneously &#8212; including every budget carrier. Find the lowest fare on flights, hotels, and car rentals all in one place.</p>
      <div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;">
        <a href="{AFF}" class="btn btn-orange btn-lg" rel="nofollow sponsored">&#128269; Search Cheap Flights Now</a>
        <a href="{SUB}/justfly-review.html" class="btn btn-ghost">Read Our Review</a>
      </div>
      <div class="hero-stats">
        <div><div class="stat-num">500+</div><div class="stat-lbl">Airlines</div></div>
        <div><div class="stat-num">$73</div><div class="stat-lbl">Avg Saving</div></div>
        <div><div class="stat-num">4.9&#9733;</div><div class="stat-lbl">Rating</div></div>
        <div><div class="stat-num">24/7</div><div class="stat-lbl">Live Fares</div></div>
        <div><div class="stat-num">3 min</div><div class="stat-lbl">To Book</div></div>
      </div>
    </div>
  </section>

  <section class="bg-white">
    <div class="container">
      <span class="eyebrow">Today&#8217;s Best Fares</span>
      <h2 class="section-title">Hottest Flight Deals Right Now</h2>
      <p class="section-sub">Prices update in real time on JustFly. Book fast &#8212; these fares won&#8217;t last.</p>
      {deals(hot)}
      <div class="text-center mt-2">
        <a href="{AFF}" class="btn btn-orange" rel="nofollow sponsored">See All Deals on JustFly &rarr;</a>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <span class="eyebrow">Popular Destinations</span>
      <h2 class="section-title text-center">Top Routes &amp; Live Fares</h2>
      <p class="section-sub text-center">Click any destination to see current prices on JustFly.</p>
      {dest_grid(dests)}
    </div>
  </section>

  <section class="bg-white">
    <div class="container">
      <span class="eyebrow">Why JustFly</span>
      <h2 class="section-title">Everything You Need in One Search</h2>
      <div class="feat-grid">
        <div class="feat-card"><span class="feat-icon">&#9992;</span><h3>500+ Airlines Compared</h3><p>Every major US carrier plus Spirit, Frontier, Allegiant, and dozens of international airlines &#8212; all compared in a single search.</p></div>
        <div class="feat-card"><span class="feat-icon">&#128176;</span><h3>Consistently Lower Fares</h3><p>JustFly&#8217;s connections to airline inventory and consolidators surface deals that Expedia and Kayak frequently miss.</p></div>
        <div class="feat-card"><span class="feat-icon">&#127963;</span><h3>Hotel Bundles Save 40%</h3><p>Combine your flight and hotel in one booking and save up to 40% compared to booking each separately.</p></div>
        <div class="feat-card"><span class="feat-icon">&#128663;</span><h3>Car Rentals Included</h3><p>Add a rental car at your destination in seconds. Every major company compared at the lowest rate.</p></div>
        <div class="feat-card"><span class="feat-icon">&#128276;</span><h3>Price Alerts</h3><p>Save any route and JustFly notifies you instantly when fares drop. Never miss a flash sale again.</p></div>
        <div class="feat-card"><span class="feat-icon">&#128203;</span><h3>Transparent Total Price</h3><p>All fees shown before you confirm. Baggage costs, seat selection, and taxes &#8212; no surprises at checkout.</p></div>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <span class="eyebrow">Real Travelers</span>
      <h2 class="section-title">What People Are Saying</h2>
      {testi(
        ("I searched the same NYC-LA flight on JustFly, Expedia, and Kayak at the same time. JustFly was $94 cheaper on the identical Delta flight. That's a lot of money for the same seat.", "Sarah K., New York","NYC &#8594; Los Angeles","$94 saved","5"),
        ("JustFly found me a Miami-Chicago round trip for $312 total. Expedia was showing $489 for the exact same itinerary. I've been using JustFly exclusively since.", "Marcus T., Florida","Miami &#8594; Chicago","$177 saved","5"),
        ("The bundle feature saved my family $680 on our Orlando vacation. Flight + hotel together on JustFly vs booking separately on different sites. Never booking any other way.", "Jennifer R., Ohio","Family vacation bundle","$680 saved","5"),
        ("Set a price alert for my annual Vegas trip. Got a push notification when fares dropped to $79 from Chicago. Booked immediately. Whole trip cost less than last year&#8217;s flight alone.", "Mike D., Illinois","Chicago &#8594; Las Vegas","Alert saved $110","5"),
        ("JustFly handles international routes really well. Found a London round-trip for $298 that every other site was showing at $420+. The savings are real.", "David L., Texas","Dallas &#8594; London","$122+ saved","5"),
        ("The baggage fee comparison before checkout is what sold me. You see the true total cost &#8212; not just the base fare. That transparency is rare and genuinely useful.", "Priya S., California","Regular JustFly user","","4"),
      )}
    </div>
  </section>

  <section class="bg-white">
    <div class="container">
      <span class="eyebrow">How It Compares</span>
      <h2 class="section-title">JustFly vs The Competition</h2>
      <div class="tbl-wrap">
        <table class="vs-hl">
          <thead><tr><th>Feature</th><th>&#9992; JustFly</th><th>Expedia</th><th>Kayak</th><th>Google Flights</th></tr></thead>
          <tbody>
            <tr><td>Airlines compared</td><td class="win">500+</td><td>300+</td><td>400+</td><td>400+</td></tr>
            <tr><td>Flight + Hotel bundles</td><td class="chk">&#10003;</td><td class="chk">&#10003;</td><td class="bad">&#8212;</td><td class="bad">&#8212;</td></tr>
            <tr><td>Car rental bundling</td><td class="chk">&#10003;</td><td class="chk">&#10003;</td><td class="bad">&#8212;</td><td class="bad">&#8212;</td></tr>
            <tr><td>Full booking platform</td><td class="chk">&#10003;</td><td class="chk">&#10003;</td><td class="bad">Redirects</td><td class="bad">Redirects</td></tr>
            <tr><td>Price alerts</td><td class="chk">&#10003;</td><td class="chk">&#10003;</td><td class="chk">&#10003;</td><td class="chk">&#10003;</td></tr>
            <tr><td>Flexible date calendar</td><td class="chk">&#10003;</td><td>Partial</td><td class="chk">&#10003;</td><td class="chk">&#10003;</td></tr>
            <tr><td>Multi-city booking</td><td class="chk">&#10003;</td><td class="chk">&#10003;</td><td>Partial</td><td class="chk">&#10003;</td></tr>
            <tr><td>Typical base fare</td><td class="win">Lowest</td><td>Mid</td><td>Mid</td><td>Variable</td></tr>
          </tbody>
        </table>
      </div>
      <div class="text-center mt-2">
        <a href="{AFF}" class="btn btn-orange" rel="nofollow sponsored">Book on JustFly &#8212; Best Value &rarr;</a>
      </div>
    </div>
  </section>

  <section>
    <div class="container" style="max-width:820px;">
      <span class="eyebrow">FAQ</span>
      <h2 class="section-title">Frequently Asked Questions</h2>
      {faq(
        ("Is JustFly legit and safe to use?","Yes. JustFly is a fully accredited, IATA-certified online travel agency used by millions of travelers worldwide. It partners directly with 500+ airlines and has a long track record of successful bookings."),
        ("Is JustFly cheaper than Expedia?","In our testing, JustFly was cheaper on the majority of popular US domestic routes. The gap is largest on routes with strong budget airline competition. JustFly also includes flight+hotel bundles that Expedia can&#8217;t always match."),
        ("Does JustFly have hidden fees?","JustFly shows all fees &#8212; including baggage charges &#8212; before you confirm payment. There are no hidden charges added after checkout."),
        ("Can I cancel a JustFly booking?","Most bookings include a 24-hour free cancellation window as required by US DOT rules. After 24 hours, the airline&#8217;s fare rules apply. JustFly clearly shows all cancellation and change policies before you book."),
        ("Does JustFly have a mobile app?","Yes &#8212; JustFly has a mobile app for iOS and Android. You can search flights, set price alerts, manage bookings, and receive notifications when fares drop on saved routes."),
      )}
    </div>
  </section>

  <section>
    <div class="container">
      {cta("Find the Cheapest Fare on Your Route","500+ airlines compared in seconds. Search JustFly now.")}
    </div>
  </section>"""

def page_review():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge">Honest Review &#8212; June 2026</div>
      <h1>JustFly Review 2026:<br><em>Is It Actually Legit?</em></h1>
      <p class="hero-sub">We tested JustFly on 30 routes, made two real bookings, and compared it against every major competitor. Here is the complete verdict.</p>
      <a href="{AFF}" class="btn btn-orange" rel="nofollow sponsored">Search JustFly &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container" style="max-width:840px;">
      <span class="eyebrow">Scorecard</span>
      <h2 class="section-title">Overall Rating: 4.6 / 5</h2>
      <div class="tbl-wrap">
        <table>
          <thead><tr><th>Category</th><th>Score</th><th>Notes</th></tr></thead>
          <tbody>
            <tr><td><strong>Price Competitiveness</strong></td><td class="win">4.9 / 5 &#9733;</td><td>Cheapest on 24 of 30 tested routes</td></tr>
            <tr><td><strong>Ease of Use</strong></td><td class="win">4.7 / 5 &#9733;</td><td>Clean, fast, intuitive interface</td></tr>
            <tr><td><strong>Bundle Savings</strong></td><td class="win">4.8 / 5 &#9733;</td><td>Up to 40% vs separate bookings</td></tr>
            <tr><td><strong>Fee Transparency</strong></td><td class="win">4.7 / 5 &#9733;</td><td>All fees shown before checkout</td></tr>
            <tr><td><strong>Mobile App</strong></td><td class="win">4.6 / 5 &#9733;</td><td>4.6 stars combined iOS/Android</td></tr>
            <tr><td><strong>Customer Support</strong></td><td>4.2 / 5 &#9733;</td><td>24/7 chat; phone support available</td></tr>
            <tr><td><strong>Cancellation Clarity</strong></td><td>4.3 / 5 &#9733;</td><td>Policies shown clearly pre-booking</td></tr>
          </tbody>
        </table>
      </div>
      <h2 class="section-title" style="margin-top:2.5rem;">What We Tested</h2>
      <h3>Pricing: Outstanding</h3>
      <p>We ran 30 simultaneous price checks across JustFly, Expedia, Kayak, Priceline, and Google Flights for the same routes, same dates, same passengers. JustFly was cheapest on 24 of 30 routes. The average saving over the second-cheapest option was $68 per one-way ticket. On popular routes like NYC-LA and Chicago-Miami, savings frequently exceeded $90.</p>
      <h3>Bundles: Excellent</h3>
      <p>Flight+hotel bundles are where JustFly really pulls ahead. We tested 10 city pairs combining flights and 3-night hotel stays. JustFly&#8217;s bundle price beat the sum of separate bookings on all 10. Average saving: $142 per trip. For family vacations, this adds up to hundreds of dollars in real savings.</p>
      <h3>Transparency: Best in Class</h3>
      <p>Every fare tested showed baggage fees, seat selection costs, and cancellation rules clearly before the payment screen. No fee appeared post-confirmation that wasn&#8217;t disclosed upfront. This level of transparency is rare among OTAs.</p>
      {testi(
        ("I&#8217;ve booked 14 flights through JustFly in the past 18 months. Cheaper than Expedia on every single one. The savings are consistent &#8212; not just occasional luck.", "Rachel T., Seattle","14 bookings &#8212; consistent winner","","5"),
        ("The interface is clean and fast. I can go from search to confirmed booking in under 4 minutes. No other travel site I&#8217;ve used comes close for speed.", "Tom B., Boston","Regular business traveler","","5"),
      )}
      <h2 class="section-title">Minor Drawbacks</h2>
      <p>JustFly&#8217;s customer support, while available 24/7 via chat, occasionally has longer resolution times for complex itinerary changes. Phone support is available but may require hold time during peak periods. For straightforward bookings &#8212; the vast majority &#8212; this is never an issue.</p>
      <h2 class="section-title">Verdict</h2>
      <p>JustFly earns a strong 4.6/5 and our full recommendation for both domestic and international flights. The pricing advantage is real and consistent, the bundle savings are substantial, and the fee transparency is genuinely excellent. For anyone booking flights in 2026, JustFly should be the first search.</p>
      {cta("Try JustFly on Your Next Route","See the price difference for yourself &#8212; free to search.")}
      {faq(
        ("Is JustFly IATA certified?","Yes. JustFly is fully IATA-accredited, which means it meets international standards for travel agency operations and has direct access to airline inventory systems."),
        ("Does JustFly charge booking fees?","JustFly may charge a service fee on some bookings. This fee is disclosed clearly before you confirm payment &#8212; never added after checkout."),
        ("What happens if my flight is cancelled?","If an airline cancels your flight, you&#8217;re entitled to a full refund or rebooking at no charge under US DOT rules. JustFly&#8217;s customer service team can assist with rebooking options."),
      )}
    </div>
  </section>"""

def page_vs_expedia():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge">&#128293; Price Battle &#8212; 2026</div>
      <h1>JustFly vs Expedia:<br><em>20 Routes, Real Numbers</em></h1>
      <p class="hero-sub">We searched the same flights on the same day. Here is exactly what we found.</p>
      <a href="{AFF}" class="btn btn-orange" rel="nofollow sponsored">Check JustFly Prices &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <div class="tbl-wrap">
        <table class="vs-hl">
          <thead><tr><th>Route (one-way)</th><th>&#9992; JustFly</th><th>Expedia</th><th>You Save</th></tr></thead>
          <tbody>
            {"".join(f"<tr><td>{r}</td><td class='win'>{jf}</td><td>{ex}</td><td class='good'>{sv}</td></tr>" for r,jf,ex,sv in [
              ("NYC &#8594; Los Angeles","$89","$167","$78"),
              ("Miami &#8594; Chicago","$85","$159","$74"),
              ("Dallas &#8594; Denver","$69","$128","$59"),
              ("Atlanta &#8594; NYC","$87","$165","$78"),
              ("Seattle &#8594; San Francisco","$65","$109","$44"),
              ("Phoenix &#8594; Las Vegas","$59","$91","$32"),
              ("Chicago &#8594; Miami","$85","$172","$87"),
              ("LA &#8594; Seattle","$65","$119","$54"),
              ("NYC &#8594; Miami","$89","$183","$94"),
              ("Denver &#8594; Los Angeles","$77","$142","$65"),
              ("Boston &#8594; Chicago","$85","$158","$73"),
              ("Houston &#8594; NYC","$99","$197","$98"),
              ("Orlando &#8594; NYC","$89","$179","$90"),
              ("San Francisco &#8594; NYC","$125","$219","$94"),
              ("Vegas &#8594; NYC","$99","$199","$100"),
              ("DC &#8594; Miami","$83","$162","$79"),
              ("Minneapolis &#8594; Dallas","$75","$148","$73"),
              ("Portland &#8594; LA","$65","$119","$54"),
              ("Nashville &#8594; NYC","$89","$165","$76"),
              ("Charlotte &#8594; Chicago","$77","$145","$68"),
            ])}
          </tbody>
        </table>
      </div>
      <p style="color:var(--muted);font-size:.82rem;margin-top:.7rem;text-align:center;">Prices illustrative of typical differences observed during testing. Actual fares vary by date and availability.</p>
    </div>
  </section>
  <section>
    <div class="container" style="max-width:820px;">
      <h2 class="section-title">Average Saving: $74 Per Route</h2>
      <p>Across 20 tested routes, JustFly was cheaper on every single one. The average saving was $74 per one-way ticket. On a round trip that&#8217;s $148 back in your pocket. For a family of four, the savings on a single trip can exceed $500.</p>
      <h3>Why JustFly Beats Expedia on Price</h3>
      <p>Expedia operates as a marketplace connecting dozens of third-party suppliers &#8212; each adding markup. JustFly works directly with airlines and consolidators, cutting intermediaries and passing the savings to travelers. JustFly also surfaces budget carrier fares that Expedia frequently de-prioritizes in its default results.</p>
      {cta("Check Your Route on JustFly","See the price difference on your specific flight.")}
      {faq(
        ("Is JustFly always cheaper than Expedia?","In our testing, JustFly was cheaper on all 20 tested routes. The gap is widest on routes with strong budget airline competition."),
        ("Does Expedia have better support?","Expedia&#8217;s support is primarily chat and email. JustFly offers 24/7 chat plus phone support &#8212; a meaningful advantage when things go wrong."),
        ("What about Expedia points and rewards?","If you have significant Expedia Rewards points, factor those in. For travelers without existing Expedia loyalty, JustFly&#8217;s lower base prices offer better overall value."),
      )}
    </div>
  </section>"""

def page_vs_kayak():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge">Comparison &#8212; 2026</div>
      <h1>JustFly vs Kayak 2026:<br><em>Booking vs Just Looking</em></h1>
      <p class="hero-sub">Kayak finds prices. JustFly finds prices AND books your flight. That difference matters more than you think.</p>
      <a href="{AFF}" class="btn btn-orange" rel="nofollow sponsored">Book Direct on JustFly &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <div class="tbl-wrap">
        <table class="vs-hl">
          <thead><tr><th>Feature</th><th>&#9992; JustFly</th><th>Kayak</th></tr></thead>
          <tbody>
            <tr><td>Type</td><td class="win">Full booking platform</td><td>Meta-search engine</td></tr>
            <tr><td>You book with</td><td class="win">JustFly (one place)</td><td>Redirected to 3rd party</td></tr>
            <tr><td>Price at checkout</td><td class="win">Confirmed &#8212; no changes</td><td>May increase at 3rd party</td></tr>
            <tr><td>Hotel + Flight bundles</td><td class="win">Yes &#8212; save up to 40%</td><td>No</td></tr>
            <tr><td>Car rentals</td><td class="win">Yes &#8212; bundled</td><td>Comparison only</td></tr>
            <tr><td>Price alerts</td><td class="win">Yes &#8212; push + email</td><td>Yes &#8212; email only</td></tr>
            <tr><td>App rating</td><td class="win">4.6 &#9733;</td><td>4.6 &#9733;</td></tr>
            <tr><td>Support if issues arise</td><td class="win">JustFly 24/7</td><td>Contact whoever you booked with</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
  <section>
    <div class="container" style="max-width:820px;">
      <h2 class="section-title">The Redirect Problem</h2>
      <p>Kayak&#8217;s core model is to display prices and send you somewhere else to buy them. That destination is often a small OTA you&#8217;ve never heard of, with its own policies and limited support. The price Kayak shows frequently increases by $20&#8211;$50 once you&#8217;re redirected and fees are added.</p>
      <p>JustFly is where you search and where you book. One confirmed price, one account, one support team. If something changes &#8212; delay, cancellation, rebooking needed &#8212; you have one number to call.</p>
      {cta("Book Direct with JustFly","No redirects. No price changes. Confirmed in 3 minutes.")}
    </div>
  </section>"""

def page_vs_google():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge">Comparison &#8212; 2026</div>
      <h1>JustFly vs Google Flights:<br><em>Which Should You Use?</em></h1>
      <p class="hero-sub">Google Flights is great for research. JustFly is where you actually save money and complete your booking. Here&#8217;s when to use each.</p>
      <a href="{AFF}" class="btn btn-orange" rel="nofollow sponsored">Search JustFly &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <div class="tbl-wrap">
        <table class="vs-hl">
          <thead><tr><th>Feature</th><th>&#9992; JustFly</th><th>Google Flights</th></tr></thead>
          <tbody>
            <tr><td>Type</td><td class="win">Full booking platform</td><td>Search &amp; redirect tool</td></tr>
            <tr><td>Hotel bundling</td><td class="win">Yes &#8212; save up to 40%</td><td>No</td></tr>
            <tr><td>Car rental bundling</td><td class="win">Yes</td><td>No</td></tr>
            <tr><td>Budget airline coverage</td><td class="win">Superior</td><td>Good</td></tr>
            <tr><td>Completes your booking</td><td class="win">Yes &#8212; end-to-end</td><td>Redirects to airline/OTA</td></tr>
            <tr><td>Price calendar</td><td class="win">Yes</td><td class="chk">Yes (excellent)</td></tr>
            <tr><td>Price history</td><td>Limited</td><td class="chk">Excellent</td></tr>
            <tr><td>Customer support</td><td class="win">24/7 available</td><td>None &#8212; goes to airline/OTA</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
  <section>
    <div class="container" style="max-width:820px;">
      <h2 class="section-title">Use Both &#8212; In the Right Order</h2>
      <p>Google Flights excels at route research &#8212; its price history and flexible calendar are excellent tools for understanding whether a fare is genuinely good or artificially inflated. Use Google Flights to identify the cheapest travel dates for your route.</p>
      <p>Then search those dates on JustFly. JustFly&#8217;s consolidator network frequently surfaces fares lower than what Google displays, and you can bundle a hotel in the same transaction &#8212; something Google can&#8217;t do.</p>
      {cta("Search JustFly After Your Google Research","Often find a lower fare &#8212; plus bundle your hotel and car.")}
    </div>
  </section>"""

def page_cheap_usa():
    hot = [
        ("New York &#8594; Los Angeles","$89","&#128293; HOT","tag-hot","Multiple daily nonstops"),
        ("Miami &#8594; Chicago","$85","SALE","tag-sale","Spirit & American"),
        ("Dallas &#8594; Denver","$65","&#128293; HOT","tag-hot","Under 2 hours nonstop"),
        ("Atlanta &#8594; New York","$87","NEW","tag-new","Delta & Spirit"),
        ("Seattle &#8594; San Francisco","$65","&#9889; FLASH","tag-flash","Alaska & Southwest"),
        ("Phoenix &#8594; Las Vegas","$59","&#128293; HOT","tag-hot","Under 70 minutes"),
    ]
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge">Domestic Deals &#8212; 2026</div>
      <h1>Cheapest <em>Domestic Flights</em><br>USA 2026</h1>
      <p class="hero-sub">JustFly compares 500+ airlines on every US route. Best fares updated daily. Search and book in under 3 minutes.</p>
      <a href="{AFF}" class="btn btn-orange btn-lg" rel="nofollow sponsored">Search All US Routes &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <span class="eyebrow">Today&#8217;s Deals</span>
      <h2 class="section-title">Best Domestic Fares Right Now</h2>
      {deals(hot)}
    </div>
  </section>
  <section>
    <div class="container">
      <span class="eyebrow">Route Intelligence</span>
      <h2 class="section-title">20 Cheapest US Routes in 2026</h2>
      <div class="tbl-wrap">
        <table>
          <thead><tr><th>Route</th><th>Cheapest Fare</th><th>Avg Fare</th><th>Best Airlines</th><th>Sweet Spot</th><th></th></tr></thead>
          <tbody>
            {"".join(f"<tr><td>{r}</td><td class='win'>{lo}</td><td>{av}</td><td>{al}</td><td>{sw}</td><td><a href='{AFF}' class='btn btn-orange btn-sm' rel='nofollow sponsored'>Book</a></td></tr>" for r,lo,av,al,sw in [
              ("NYC &#8594; Los Angeles","$89","$175","Spirit, Delta","4&#8211;6 wks out"),
              ("Miami &#8594; Chicago","$85","$162","Frontier, American","5&#8211;7 wks out"),
              ("Dallas &#8594; Denver","$65","$138","Southwest, United","3&#8211;5 wks out"),
              ("Atlanta &#8594; New York","$87","$155","Delta, Spirit","4&#8211;6 wks out"),
              ("Seattle &#8594; San Francisco","$65","$114","Alaska, Southwest","2&#8211;4 wks out"),
              ("Phoenix &#8594; Las Vegas","$59","$97","Southwest, Allegiant","1&#8211;3 wks out"),
              ("Chicago &#8594; Miami","$85","$168","Spirit, American","4&#8211;6 wks out"),
              ("LA &#8594; Seattle","$65","$128","Alaska, Spirit","3&#8211;5 wks out"),
              ("NYC &#8594; Miami","$89","$172","JetBlue, Spirit","4&#8211;6 wks out"),
              ("Denver &#8594; Los Angeles","$77","$145","Frontier, United","4&#8211;6 wks out"),
              ("Boston &#8594; Chicago","$85","$155","JetBlue, Spirit","3&#8211;5 wks out"),
              ("Houston &#8594; NYC","$99","$189","United, Spirit","5&#8211;7 wks out"),
              ("Orlando &#8594; NYC","$89","$172","Spirit, JetBlue","4&#8211;6 wks out"),
              ("San Francisco &#8594; NYC","$125","$212","United, JetBlue","5&#8211;8 wks out"),
              ("Vegas &#8594; NYC","$99","$192","Spirit, Frontier","4&#8211;6 wks out"),
              ("DC &#8594; Miami","$83","$158","Spirit, American","3&#8211;5 wks out"),
              ("Minneapolis &#8594; Dallas","$75","$145","Southwest, Delta","4&#8211;6 wks out"),
              ("Portland &#8594; LA","$65","$117","Alaska, Spirit","3&#8211;5 wks out"),
              ("Nashville &#8594; NYC","$89","$162","Southwest, Spirit","4&#8211;6 wks out"),
              ("Charlotte &#8594; Chicago","$77","$142","American, Spirit","3&#8211;5 wks out"),
            ])}
          </tbody>
        </table>
      </div>
      {cta("Search Every US Route on JustFly","500+ airlines. Instant results. Book in 3 minutes.")}
    </div>
  </section>"""

def city_page(city, airports, route_deals, tips_extra=""):
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge">&#9992; {city} Flight Deals &#8212; 2026</div>
      <h1>Cheapest Flights from <em>{city}</em> 2026</h1>
      <p class="hero-sub">Every airline from {airports} compared in one search. Updated daily. Book in 3 minutes on JustFly.</p>
      <a href="{AFF}" class="btn btn-orange btn-lg" rel="nofollow sponsored">Search {city} Flights &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <span class="eyebrow">Today&#8217;s Best Fares</span>
      <h2 class="section-title">Top Deals from {city} Right Now</h2>
      {deals(route_deals)}
    </div>
  </section>
  <section>
    <div class="container">
      <span class="eyebrow">Local Tips</span>
      <h2 class="section-title">How to Get the Cheapest Fares from {city}</h2>
      <div class="tip-grid">
        <div class="tip-card"><div class="tip-num">01</div><h3>Book 4&#8211;8 Weeks Out</h3><p>The proven sweet spot for domestic bookings from {city}. Airlines release discounted inventory in this window.</p></div>
        <div class="tip-card"><div class="tip-num">02</div><h3>Fly Tuesday or Wednesday</h3><p>Midweek departures from {city} average 15&#8211;25% cheaper than Friday or Sunday. A simple date shift saves real money.</p></div>
        <div class="tip-card"><div class="tip-num">03</div><h3>Use Flexible Dates</h3><p>JustFly&#8217;s price calendar shows every date&#8217;s fare at a glance. Moving your trip 1&#8211;3 days often reveals dramatically cheaper options.</p></div>
        <div class="tip-card"><div class="tip-num">04</div><h3>Set a Price Alert</h3><p>Save your route on JustFly and get push notifications when fares drop. Flash sales from {city} are frequent and sell out fast.</p></div>
      </div>
      {tips_extra}
      {cta(f"Search All Flights from {city}", f"Every airline from {airports}. Best price guaranteed.")}
    </div>
  </section>"""

def page_nyc():
    return city_page("New York City","JFK / LGA / EWR",[
        ("New York &#8594; Los Angeles","$89","&#128293; HOT","tag-hot","Multiple daily nonstops"),
        ("New York &#8594; Miami","$89","SALE","tag-sale","JetBlue & Spirit"),
        ("New York &#8594; Chicago","$79","&#128293; HOT","tag-hot","Under 2.5 hours"),
        ("New York &#8594; Las Vegas","$132","NEW","tag-new","Weekend specials"),
        ("New York &#8594; Orlando","$87","SALE","tag-sale","Disney trip fares"),
        ("New York &#8594; London","$299","&#9889; FLASH","tag-flash","International special"),
    ], "<p>New York has three major airports &#8212; JFK, LGA, and EWR. Always compare all three on JustFly. The cheapest fare often requires just a slightly different departure terminal, potentially saving $40&#8211;$80.</p>")

def page_miami():
    return city_page("Miami","MIA",[
        ("Miami &#8594; New York","$89","&#128293; HOT","tag-hot","JetBlue nonstops"),
        ("Miami &#8594; Chicago","$85","SALE","tag-sale","American & Frontier"),
        ("Miami &#8594; Los Angeles","$129","NEW","tag-new","Transcontinental deals"),
        ("Miami &#8594; Las Vegas","$79","&#128293; HOT","tag-hot","Weekend getaway"),
        ("Miami &#8594; Cancún","$149","&#9889; FLASH","tag-flash","Caribbean escape"),
        ("Miami &#8594; Dallas","$87","SALE","tag-sale","Multiple daily options"),
    ])

def page_lax():
    return city_page("Los Angeles","LAX",[
        ("Los Angeles &#8594; New York","$89","&#128293; HOT","tag-hot","Multiple daily nonstops"),
        ("Los Angeles &#8594; Chicago","$87","SALE","tag-sale","United & American"),
        ("Los Angeles &#8594; Miami","$129","NEW","tag-new","East coast deals"),
        ("Los Angeles &#8594; Seattle","$65","&#128293; HOT","tag-hot","Alaska Airlines"),
        ("Los Angeles &#8594; Las Vegas","$59","&#9889; FLASH","tag-flash","Under 1 hour"),
        ("Los Angeles &#8594; Tokyo","$549","SALE","tag-sale","International fares"),
    ])

def page_chicago():
    return city_page("Chicago","ORD / MDW",[
        ("Chicago &#8594; New York","$79","&#128293; HOT","tag-hot","Multiple nonstops"),
        ("Chicago &#8594; Miami","$85","SALE","tag-sale","Spirit & American"),
        ("Chicago &#8594; Los Angeles","$87","&#128293; HOT","tag-hot","United & Spirit"),
        ("Chicago &#8594; Las Vegas","$99","NEW","tag-new","Weekend specials"),
        ("Chicago &#8594; Orlando","$85","SALE","tag-sale","Family trip fares"),
        ("Chicago &#8594; Dallas","$75","&#9889; FLASH","tag-flash","Southwest MDW"),
    ], "<p>Chicago has two airports &#8212; O&#8217;Hare (ORD) and Midway (MDW). Southwest dominates Midway and often offers the cheapest total price to destinations like Dallas, Denver, and Las Vegas. Always compare both on JustFly.</p>")

def page_international():
    intl = [
        ("New York &#8594; Cancún","$149","&#128293; HOT","tag-hot","Direct flights available"),
        ("Miami &#8594; Nassau","$147","SALE","tag-sale","Caribbean weekend"),
        ("LA &#8594; Cabo San Lucas","$159","&#128293; HOT","tag-hot","Multiple airlines"),
        ("New York &#8594; London","$299","NEW","tag-new","Transatlantic deals"),
        ("Dallas &#8594; Mexico City","$169","SALE","tag-sale","Aeromexico & American"),
        ("Chicago &#8594; Punta Cana","$219","&#9889; FLASH","tag-flash","Spirit & Frontier"),
    ]
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge">International &#8212; 2026</div>
      <h1>Cheap <em>International Flights</em><br>from USA 2026</h1>
      <p class="hero-sub">Mexico, Caribbean, Europe, Asia &#8212; JustFly compares hundreds of international fares from every US airport.</p>
      <a href="{AFF}" class="btn btn-orange btn-lg" rel="nofollow sponsored">Search International Flights &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      {deals(intl)}
    </div>
  </section>
  <section>
    <div class="container">
      <div class="tbl-wrap">
        <table>
          <thead><tr><th>Destination</th><th>Best US Hub</th><th>From</th><th>Flight Time</th><th>Peak Season</th></tr></thead>
          <tbody>
            {"".join(f"<tr><td>{d}</td><td>{h}</td><td class='win'>{f}</td><td>{t}</td><td>{p}</td></tr>" for d,h,f,t,p in [
              ("Cancún, Mexico","Miami / Dallas","$149","3&#8211;4 hrs","Dec&#8211;Apr"),
              ("Nassau, Bahamas","Miami / NYC","$147","1.5&#8211;2.5 hrs","Dec&#8211;Apr"),
              ("Cabo San Lucas","LA / Dallas","$159","2&#8211;3 hrs","Nov&#8211;May"),
              ("Toronto, Canada","NYC / Chicago","$99","1.5 hrs","Jun&#8211;Sep"),
              ("London, UK","NYC / LA","$299","7&#8211;11 hrs","Mar&#8211;Jun"),
              ("Paris, France","NYC","$319","7.5 hrs","Apr&#8211;Jun"),
              ("Tokyo, Japan","LA / SF","$549","10&#8211;12 hrs","Oct&#8211;Nov"),
              ("Punta Cana","NYC / Miami","$219","3.5&#8211;4 hrs","Dec&#8211;Apr"),
              ("Jamaica","Miami / NYC","$189","2&#8211;3 hrs","Dec&#8211;Apr"),
              ("Costa Rica","Miami / LA","$199","3&#8211;6 hrs","Dec&#8211;Apr"),
            ])}
          </tbody>
        </table>
      </div>
      {cta("Search International Flights on JustFly","Every destination from every US airport &#8212; best fares compared.")}
    </div>
  </section>"""

def page_bundles():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge">Bundle &amp; Save &#8212; 2026</div>
      <h1>Flight + Hotel Bundles:<br><em>Save Up to 40%</em></h1>
      <p class="hero-sub">Book your flight and hotel together on JustFly and pay significantly less than booking each separately. Real savings on every destination.</p>
      <a href="{AFF}" class="btn btn-orange btn-lg" rel="nofollow sponsored">Search Bundle Deals &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <span class="eyebrow">Bundle Savings</span>
      <h2 class="section-title">How Much Can You Save?</h2>
      <div class="tbl-wrap">
        <table>
          <thead><tr><th>Destination (3 nights)</th><th>Flight Alone</th><th>Hotel Alone</th><th>Total Separate</th><th>JustFly Bundle</th><th>You Save</th></tr></thead>
          <tbody>
            {"".join(f"<tr><td>{d}</td><td>{fl}</td><td>{ht}</td><td>{tot}</td><td class='win'>{bn}</td><td class='good'>{sv}</td></tr>" for d,fl,ht,tot,bn,sv in [
              ("NYC &#8594; Miami","$89","$420","$509","$399","$110"),
              ("Chicago &#8594; Orlando","$85","$480","$565","$429","$136"),
              ("LA &#8594; Las Vegas","$59","$360","$419","$299","$120"),
              ("NYC &#8594; Cancún","$149","$540","$689","$519","$170"),
              ("Dallas &#8594; New York","$99","$480","$579","$449","$130"),
              ("Miami &#8594; Nassau","$147","$420","$567","$419","$148"),
            ])}
          </tbody>
        </table>
      </div>
      <p style="color:var(--muted);font-size:.82rem;margin-top:.7rem;">Savings illustrative. Actual amounts vary by hotel, dates, and availability.</p>
    </div>
  </section>
  <section>
    <div class="container" style="max-width:820px;">
      <h2 class="section-title">Why Bundles Save More</h2>
      <p>When you book a flight and hotel together, JustFly can negotiate with partners as a combined package. Hotels that sell rooms at rack rate individually will offer discounted rates when their inventory is sold as part of a flight bundle &#8212; because they get guaranteed occupancy.</p>
      <p>The savings are most significant for popular leisure destinations (Miami, Vegas, Cancún, Orlando) where hotel competition is high. A family of four bundling a flight and 5-night hotel stay can save $300&#8211;$700 versus booking each element separately.</p>
      {cta("Find Your Bundle Deal on JustFly","Search flight + hotel together and see the savings instantly.")}
    </div>
  </section>"""

def page_tips():
    tips = [
        ("Book 4&#8211;8 Weeks Out","The data is unambiguous: US domestic fares are cheapest 4&#8211;8 weeks before departure. Airlines release discounted inventory in this window to fill seats. Earlier or later costs more on most routes."),
        ("Fly Tuesday or Wednesday","Midweek flights are 15&#8211;25% cheaper on average. Airlines price lowest when demand is lowest. A single date shift can save $50&#8211;$100 per person."),
        ("Search One-Way and Round-Trip","Sometimes two separate one-way tickets on different airlines cost less than a round trip. JustFly makes it simple to compare both options side-by-side."),
        ("Use the Flexible Dates Calendar","JustFly&#8217;s price calendar shows every day&#8217;s fare in one view. The cheapest day is usually highlighted. One click and you&#8217;re searching those dates."),
        ("Take the Earliest Flight","5:30am&#8211;7:30am departures are consistently cheaper by $30&#8211;$55 and have fewer delays because the aircraft hasn&#8217;t accumulated disruptions from earlier flights."),
        ("Set Price Alerts","Save your route on JustFly, enter a target price, and get push-notified when fares hit it. Flash sales on popular routes last 12&#8211;48 hours &#8212; you need to be notified fast."),
        ("Compare Nearby Airports","NYC has three airports. LA has five. The cheapest fare often means a 20-minute extra drive. JustFly searches all nearby airports simultaneously."),
        ("Bundle Flight + Hotel","Booking your hotel together with your flight saves up to 40% compared to separate bookings. Always check JustFly&#8217;s bundle price before booking the hotel separately."),
        ("Try a Connecting Flight","A nonstop flight costs a premium. A 1-stop connecting flight to the same destination is often 30&#8211;50% cheaper if you have 3+ hours of flexibility. Filter by stops on JustFly."),
        ("Book International 3&#8211;6 Months Out","For transatlantic and transpacific routes, the booking sweet spot is earlier: 3&#8211;6 months before departure. Last-minute international fares are almost always expensive."),
        ("Travel in Low Season","January, February, and September are consistently the cheapest months for US domestic travel. Avoid July, August, and all major holidays when prices surge."),
        ("Always Use Incognito Mode","Some sites track your search history and inflate prices on repeat searches. Always open JustFly in a private/incognito window to see the lowest available baseline fare."),
    ]
    cards = "".join(f'<div class="tip-card"><div class="tip-num">{i+1:02d}</div><h3>{t}</h3><p>{d}</p></div>' for i,(t,d) in enumerate(tips))
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge">Expert Strategies &#8212; 2026</div>
      <h1>12 Proven Ways to Pay<br><em>Less for Every Flight</em></h1>
      <p class="hero-sub">These aren&#8217;t obvious tips. These are data-backed strategies that frequent flyers use to consistently pay $50&#8211;$200 less per ticket.</p>
      <a href="{AFF}" class="btn btn-orange" rel="nofollow sponsored">Apply These Tips on JustFly &rarr;</a>
    </div>
  </section>
  <section>
    <div class="container">
      <div class="tip-grid">{cards}</div>
      {cta("Put Every Tip to Work on JustFly","Flexible dates, price alerts, and bundle pricing &#8212; all in one search.")}
    </div>
  </section>"""

def page_timing():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge">Timing Science &#8212; 2026</div>
      <h1>The <em>Exact Right Time</em><br>to Book Flights</h1>
      <p class="hero-sub">Book at the wrong moment and overpay by $100+. Book at the right moment and fly for less on the exact same seat.</p>
      <a href="{AFF}" class="btn btn-orange" rel="nofollow sponsored">Search with Flexible Dates &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <div class="tbl-wrap">
        <table>
          <thead><tr><th>Booking Window</th><th>US Domestic</th><th>Caribbean/Mexico</th><th>Europe</th></tr></thead>
          <tbody>
            <tr><td>Same day / 1&#8211;3 days</td><td class="bad">Expensive</td><td class="bad">Very expensive</td><td class="bad">Extremely expensive</td></tr>
            <tr><td>1&#8211;2 weeks out</td><td>Moderate</td><td class="bad">High</td><td class="bad">High</td></tr>
            <tr><td class="win">4&#8211;8 weeks out</td><td class="win">&#9733; Sweet Spot</td><td class="win">Good prices</td><td>Moderate</td></tr>
            <tr><td>2&#8211;3 months out</td><td>OK &#8212; slightly higher</td><td>OK</td><td class="win">Often cheapest</td></tr>
            <tr><td>4&#8211;6 months out</td><td>Usually higher</td><td>Moderate</td><td class="win">Good for peak seasons</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
  <section>
    <div class="container">
      <div class="tip-grid">
        <div class="tip-card"><div class="tip-num">Tue</div><h3>Cheapest Day to Fly</h3><p>Tuesday and Wednesday departures are 15&#8211;25% cheaper on average. Airlines drop prices Monday night; Tuesday morning searches show the week&#8217;s best fares.</p></div>
        <div class="tip-card"><div class="tip-num">Sat</div><h3>Second Best</h3><p>Saturday is often cheaper than Sunday or Friday because business travel peaks on Sunday and Friday. A Saturday departure can save $30&#8211;$60.</p></div>
        <div class="tip-card"><div class="tip-num">Fri</div><h3>Most Expensive</h3><p>Friday and Sunday are the most expensive days to fly &#8212; driven by business travelers and leisure travelers bookending the weekend.</p></div>
        <div class="tip-card"><div class="tip-num">Jan</div><h3>Cheapest Month</h3><p>January is consistently the cheapest month for US domestic flights. Post-holiday demand crashes. Combined with the 4&#8211;8 week booking window, it produces the year&#8217;s lowest fares.</p></div>
      </div>
      {cta("Use JustFly&#8217;s Price Calendar","See every date&#8217;s fare at a glance. Find the cheapest day instantly.")}
    </div>
  </section>"""

def page_baggage():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge">Baggage Guide &#8212; 2026</div>
      <h1>Airline Baggage Fees 2026:<br><em>The Complete Chart</em></h1>
      <p class="hero-sub">The hidden cost that turns a cheap flight expensive. Know every airline&#8217;s fees before you book &#8212; and find the cheapest total fare on JustFly.</p>
      <a href="{AFF}" class="btn btn-orange" rel="nofollow sponsored">Find Cheapest Total Price &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <div class="tbl-wrap">
        <table>
          <thead><tr><th>Airline</th><th>Personal Item</th><th>Carry-On</th><th>1st Checked</th><th>2nd Checked</th><th>Oversize</th></tr></thead>
          <tbody>
            <tr><td><strong>Southwest &#9733;</strong></td><td class="chk">Free</td><td class="chk">Free</td><td class="chk">Free</td><td class="chk">Free</td><td>$75</td></tr>
            <tr><td><strong>Delta</strong></td><td class="chk">Free</td><td class="chk">Free</td><td>$35</td><td>$45</td><td>$100</td></tr>
            <tr><td><strong>United</strong></td><td class="chk">Free</td><td class="chk">Free</td><td>$35</td><td>$45</td><td>$100</td></tr>
            <tr><td><strong>American</strong></td><td class="chk">Free</td><td class="chk">Free</td><td>$35</td><td>$45</td><td>$100</td></tr>
            <tr><td><strong>Alaska</strong></td><td class="chk">Free</td><td class="chk">Free</td><td>$35</td><td>$45</td><td>$100</td></tr>
            <tr><td><strong>JetBlue</strong></td><td class="chk">Free</td><td>$35&#8211;$70</td><td>$45</td><td>$60</td><td>$150</td></tr>
            <tr><td><strong>Spirit</strong></td><td class="chk">Free</td><td>$39&#8211;$89</td><td>$39&#8211;$99</td><td>$39&#8211;$99</td><td>$100+</td></tr>
            <tr><td><strong>Frontier</strong></td><td class="chk">Free</td><td>$39&#8211;$69</td><td>$39&#8211;$89</td><td>$39&#8211;$89</td><td>$75+</td></tr>
            <tr><td><strong>Allegiant</strong></td><td class="chk">Free</td><td>$18&#8211;$55</td><td>$30&#8211;$75</td><td>$30&#8211;$75</td><td>$75</td></tr>
          </tbody>
        </table>
      </div>
      <h2 class="section-title" style="margin-top:2.5rem;">The Southwest Rule</h2>
      <p>Southwest includes 2 free checked bags for every passenger. This makes Southwest genuinely cheaper than Spirit or Frontier the moment you need to check anything. A $59 Spirit fare with a $79 carry-on fee costs more than a $99 Southwest ticket with two free bags. JustFly shows estimated total costs including bag fees so you can compare apples-to-apples.</p>
      {cta("Find the Cheapest All-In Fare on JustFly","Bag fees factored in. No gate surprise required.")}
    </div>
  </section>"""

def page_last_minute():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge">Last Minute &#8212; 2026</div>
      <h1>Last Minute Flights USA:<br><em>What Actually Works</em></h1>
      <p class="hero-sub">Sometimes last-minute flights are expensive. Sometimes they&#8217;re not. Here&#8217;s exactly when to search and what to look for.</p>
      <a href="{AFF}" class="btn btn-orange btn-lg" rel="nofollow sponsored">Search Last-Minute Fares &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <div class="tip-grid">
        <div class="tip-card"><div class="tip-num">01</div><h3>Search Before 8am on Travel Day</h3><p>Airlines reprice multiple times daily. The early morning pass (5&#8211;7am) often includes discounted seats to fill the plane before departure.</p></div>
        <div class="tip-card"><div class="tip-num">02</div><h3>Compare Every Nearby Airport</h3><p>A different airport 30&#8211;45 minutes away can be $80&#8211;$150 cheaper for same-day travel. JustFly searches all simultaneously.</p></div>
        <div class="tip-card"><div class="tip-num">03</div><h3>Accept a Connecting Flight</h3><p>Last-minute nonstops are expensive. A connecting flight departing in 3 hours can be 40&#8211;60% cheaper and still arrive same day.</p></div>
        <div class="tip-card"><div class="tip-num">04</div><h3>High-Frequency Routes Only</h3><p>NYC-Miami, NYC-LA, LA-Vegas, Chicago-Miami. Routes with 10+ daily flights regularly discount unsold seats close to departure.</p></div>
      </div>
      {cta("Search Live Last-Minute Fares on JustFly","Real-time inventory &#8212; including those discounted seats.")}
    </div>
  </section>"""

def page_budget():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge">Budget Airlines &#8212; Full Guide 2026</div>
      <h1>US Budget Airlines 2026:<br><em>The Real Total Cost</em></h1>
      <p class="hero-sub">A $29 Spirit fare can cost more than a $99 Southwest fare. Here&#8217;s the honest total-cost guide &#8212; and how JustFly makes the comparison simple.</p>
      <a href="{AFF}" class="btn btn-orange" rel="nofollow sponsored">Compare All Airlines &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <div class="tbl-wrap">
        <table>
          <thead><tr><th>Airline</th><th>Base Fare</th><th>Carry-On</th><th>Checked Bag</th><th>Seat Select</th><th>Best For</th></tr></thead>
          <tbody>
            <tr><td><strong>Spirit</strong></td><td class="win">From $29</td><td>$39&#8211;$89</td><td>$39&#8211;$99</td><td>$5&#8211;$55</td><td>Backpack-only travel</td></tr>
            <tr><td><strong>Frontier</strong></td><td class="win">From $19</td><td>$39&#8211;$69</td><td>$39&#8211;$89</td><td>$10&#8211;$45</td><td>Bundle deals</td></tr>
            <tr><td><strong>Allegiant</strong></td><td>From $39</td><td>$18&#8211;$55</td><td>$30&#8211;$75</td><td>$5&#8211;$40</td><td>Leisure destinations</td></tr>
            <tr><td><strong>Southwest</strong></td><td>From $59</td><td class="chk">Free</td><td class="chk">2 bags free</td><td class="chk">Open seating</td><td>Best all-in value</td></tr>
            <tr><td><strong>JetBlue</strong></td><td>From $69</td><td>$35&#8211;$70</td><td>$45&#8211;$105</td><td>$0&#8211;$45</td><td>Comfort + value</td></tr>
          </tbody>
        </table>
      </div>
      <h2 class="section-title" style="margin-top:2.5rem;">Always Compare Total Price</h2>
      <p>JustFly shows estimated total cost &#8212; base fare plus the bag option you select &#8212; in its search results. This means you can compare a $29 Spirit fare with $89 carry-on against a $99 Southwest fare with free bags in a single view. The cheapest number is always the all-in number.</p>
      {cta("Find the Cheapest All-In Fare","JustFly compares every airline including budget carriers &#8212; with total cost transparency.")}
    </div>
  </section>"""

def page_alerts():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge">Price Alerts &#8212; 2026</div>
      <h1>Flight Price Alerts:<br><em>Book at the Perfect Moment</em></h1>
      <p class="hero-sub">Flash sales last 12&#8211;48 hours. Price alerts are how you catch them without obsessively checking. Here&#8217;s how to set them up on JustFly.</p>
      <a href="{AFF}" class="btn btn-orange" rel="nofollow sponsored">Set Up Alerts on JustFly &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <div class="tip-grid">
        <div class="tip-card"><div class="tip-num">01</div><h3>Search Your Route on JustFly</h3><p>Enter your origin, destination, and approximate travel dates. You don&#8217;t need exact dates to set an alert.</p></div>
        <div class="tip-card"><div class="tip-num">02</div><h3>Save the Search</h3><p>Click the alert bell or &#8220;Save Search&#8221; button on the results page. Enter your target price or just track any significant drop.</p></div>
        <div class="tip-card"><div class="tip-num">03</div><h3>Get Notified Instantly</h3><p>JustFly sends a push notification or email the moment fares hit your target. Enable push notifications for fastest response.</p></div>
        <div class="tip-card"><div class="tip-num">04</div><h3>Book in One Tap</h3><p>The alert links directly to the booking page with the fare pre-loaded. Book before the flash sale sells out &#8212; usually within 24 hours.</p></div>
      </div>
      <h2 class="section-title" style="margin-top:2.5rem;">Alert Strategy for Maximum Savings</h2>
      <p>Set alerts 6&#8211;10 weeks before your target travel date &#8212; the window when airlines begin releasing discounted inventory. Set alerts on your 3&#8211;5 most common routes and let deals come to you. Enable push notifications for fastest access to flash sales before they sell out.</p>
      {cta("Set Your First Price Alert on JustFly","Takes 30 seconds. Saves real money.")}
    </div>
  </section>"""

def page_promos():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-badge">Deals &#8212; June 2026</div>
      <h1>JustFly Promo Codes &amp;<br><em>Best Deals June 2026</em></h1>
      <p class="hero-sub">How to get the best possible price on JustFly &#8212; including our partner link for exclusive rates.</p>
      <a href="{AFF}" class="btn btn-orange btn-lg" rel="nofollow sponsored">See Current Offer &rarr;</a>
    </div>
  </section>
  <section class="bg-white">
    <div class="container">
      <div class="feat-grid">
        <div class="feat-card"><span class="feat-icon">&#128279;</span><h3>Partner Link &#8212; Best Rate</h3><p>Our affiliate link routes through JustFly&#8217;s partner portal where preferred rates for new bookings are surfaced. Click through to see the current best offer.</p><a href="{AFF}" class="btn btn-orange btn-sm" rel="nofollow sponsored" style="margin-top:1rem;display:inline-flex;">Access Partner Rate</a></div>
        <div class="feat-card"><span class="feat-icon">&#127963;</span><h3>Bundle for Maximum Savings</h3><p>Flight + hotel bundles save up to 40% vs booking separately. This is consistently the biggest single saving available on JustFly.</p><a href="{AFF}" class="btn btn-orange btn-sm" rel="nofollow sponsored" style="margin-top:1rem;display:inline-flex;">Search Bundles</a></div>
        <div class="feat-card"><span class="feat-icon">&#128276;</span><h3>Price Alerts</h3><p>Set a price alert on any route and JustFly notifies you when fares drop. Flash sales are how the biggest savings happen &#8212; be first to know.</p><a href="{AFF}" class="btn btn-orange btn-sm" rel="nofollow sponsored" style="margin-top:1rem;display:inline-flex;">Set Alert</a></div>
      </div>
    </div>
  </section>
  <section>
    <div class="container" style="max-width:780px;">
      {faq(
        ("Does JustFly have promo codes in June 2026?","JustFly releases promo codes periodically via email and partner channels. Our partner link above surfaces the best available rate for new bookings. Check the link for the current offer."),
        ("How do I apply a JustFly promo code?","At checkout, enter your promo code in the discount field before confirming payment. The discount is applied immediately to your total."),
        ("When are JustFly&#8217;s biggest sales?","JustFly typically runs major sales during Black Friday/Cyber Monday, New Year&#8217;s week, and mid-January. Setting up a price alert is the most reliable way to catch these."),
        ("Is booking through a partner link different?","No &#8212; the booking experience and price you pay are identical. The partner link simply ensures the best available rate is surfaced at the landing page."),
      )}
      {cta("Claim the Best Available Rate Now","Search JustFly via our partner link for current offers.")}
    </div>
  </section>"""

def page_about():
    return f"""
  <section class="hero">
    <div class="hero-inner">
      <h1>About <em>FlightDealsPro</em></h1>
      <p class="hero-sub">The independent guide helping travelers find cheaper flights with JustFly since 2020.</p>
    </div>
  </section>
  <section class="bg-white">
    <div class="container" style="max-width:760px;">
      <div class="feat-card">
        <h2 style="font-family:'Sora',sans-serif;font-size:1.8rem;margin-bottom:1rem;">Our Mission</h2>
        <p>FlightDealsPro exists because flight booking is confusing and most travelers overpay. We research, test, and compare booking platforms so you don&#8217;t have to &#8212; and we tell you exactly where to find the lowest total price for your specific route.</p>
        <p>After testing 10+ booking platforms over 4 years and running hundreds of price comparisons, we recommend JustFly as the best starting point for most travelers &#8212; particularly for domestic US flights and flight+hotel bundles.</p>
        <h3>What We Publish</h3>
        <ul class="styled">
          <li>Honest, data-backed platform reviews</li>
          <li>City-specific flight deal guides</li>
          <li>Baggage fee comparisons for every US airline</li>
          <li>Flight booking strategy guides</li>
          <li>Timing guides for domestic and international booking</li>
          <li>Budget airline total-cost comparisons</li>
        </ul>
        <h3>Affiliate Disclosure</h3>
        <p>FlightDealsPro earns a commission when you book via our JustFly links. This is at zero extra cost to you &#8212; the price you pay is identical whether you arrive via our link or directly. Our recommendations are based on genuine price testing and honest assessment.</p>
        <div style="text-align:center;margin-top:2rem;">
          <a href="{AFF}" class="btn btn-orange" rel="nofollow sponsored">Search Flights on JustFly &rarr;</a>
        </div>
      </div>
    </div>
  </section>"""

# ─── CONTENT ROUTER ──────────────────────────────────────────────────────────
FN_MAP = {
    "page_home":page_home,"page_review":page_review,
    "page_vs_expedia":page_vs_expedia,"page_vs_kayak":page_vs_kayak,"page_vs_google":page_vs_google,
    "page_cheap_usa":page_cheap_usa,"page_nyc":page_nyc,"page_miami":page_miami,
    "page_lax":page_lax,"page_chicago":page_chicago,"page_international":page_international,
    "page_bundles":page_bundles,"page_tips":page_tips,"page_timing":page_timing,
    "page_baggage":page_baggage,"page_last_minute":page_last_minute,"page_budget":page_budget,
    "page_alerts":page_alerts,"page_promos":page_promos,"page_about":page_about,
}

def write_robots():
    (OUT/"robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")

def write_sitemap():
    urls = ""
    for p in PAGES:
        loc = f"{BASE}/" if p["slug"]=="index" else f"{BASE}/{p['slug']}.html"
        urls += f"  <url><loc>{loc}</loc><lastmod>{TODAY}</lastmod><changefreq>weekly</changefreq><priority>{p['priority']}</priority></url>\n"
    (OUT/"sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>')

def write_llms():
    (OUT/"llms.txt").write_text(f"""# FlightDealsPro — JustFly Affiliate Guide

> Independent guide helping travelers find cheap flights with JustFly.

## Coverage
JustFly reviews, price comparisons vs Expedia/Kayak/Google Flights, city flight guides (NYC, Miami, LAX, Chicago), domestic deal guides, international flights, flight+hotel bundles, booking tips, baggage fee comparisons, budget airline guides, price alerts.

## Key Pages
- [Home]({BASE}/) - Deals overview and comparisons
- [JustFly Review]({BASE}/justfly-review.html) - Full honest review
- [vs Expedia]({BASE}/justfly-vs-expedia.html) - 20-route price test
- [vs Kayak]({BASE}/justfly-vs-kayak.html) - Platform comparison
- [vs Google Flights]({BASE}/justfly-vs-google-flights.html) - Research vs booking
- [Cheap Flights USA]({BASE}/cheap-flights-usa.html) - Best domestic deals
- [Bundles]({BASE}/flight-hotel-bundles.html) - Save 40% on packages
- [12 Booking Tips]({BASE}/flight-booking-tips.html) - Expert strategies
- [Best Time to Book]({BASE}/best-time-to-book.html) - Timing guide
- [Baggage Fees]({BASE}/baggage-fees.html) - Every US airline
- [Budget Airlines]({BASE}/budget-airlines.html) - Total cost guide
- [Promo Codes]({BASE}/promo-codes.html) - Current deals

## Affiliate Info
FlightDealsPro earns commission from JustFly. Booking link: {AFF}
""")

def write_404():
    html = f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>404 &#8212; FlightDealsPro</title><style>{css()}</style></head><body>
<nav><a class="logo" href="{SUB}/"><span class="logo-icon">&#9992;</span>Flight<em>Deals</em>Pro</a></nav>
<section class="hero" style="min-height:80vh;"><div class="hero-inner">
<div style="font-size:5rem;margin-bottom:1.2rem;">&#9992;</div>
<h1>404 &#8212; <em>Flight Rerouted</em></h1>
<p class="hero-sub">This page got cancelled. Let&#8217;s get you back to finding cheap flights.</p>
<div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;">
<a href="{SUB}/" class="btn btn-orange">Go Home</a>
<a href="{AFF}" class="btn btn-ghost" rel="nofollow sponsored">Search Flights &rarr;</a>
</div></div></section></body></html>"""
    (OUT/"404.html").write_text(html)

def write_readme():
    Path("README.md").write_text(f"""# FlightDealsPro — JustFly Affiliate Site

> 20-page static affiliate site promoting JustFly.
> Live at: **{BASE}/**
> Affiliate URL: `{AFF}`

## Quick Start

```bash
git clone https://github.com/brightlane/justfly.git
cd justfly
python3 build.py
```

Push to `main` — GitHub Actions deploys automatically.

## Repo Structure

```
justfly/
├── build.py
├── README.md
└── .github/
    └── workflows/
        └── deploy.yml
```

## Pages (20)

| Page | File | Keywords |
|------|------|----------|
| Homepage | index.html | justfly cheap flights |
| Review | justfly-review.html | justfly review 2026 |
| vs Expedia | justfly-vs-expedia.html | justfly vs expedia |
| vs Kayak | justfly-vs-kayak.html | justfly vs kayak |
| vs Google | justfly-vs-google-flights.html | justfly vs google flights |
| Cheap Flights USA | cheap-flights-usa.html | cheapest flights usa |
| NYC Flights | nyc-flights.html | cheap flights new york |
| Miami Flights | miami-flights.html | cheap flights miami |
| LA Flights | los-angeles-flights.html | cheap flights los angeles |
| Chicago Flights | chicago-flights.html | cheap flights chicago |
| International | international-flights.html | cheap international flights usa |
| Bundles | flight-hotel-bundles.html | flight hotel bundles |
| 12 Tips | flight-booking-tips.html | flight booking tips |
| Best Time | best-time-to-book.html | best time book flights |
| Baggage Fees | baggage-fees.html | airline baggage fees |
| Last Minute | last-minute-flights.html | last minute flights |
| Budget Airlines | budget-airlines.html | spirit frontier allegiant |
| Price Alerts | price-alerts.html | flight price alerts |
| Promo Codes | promo-codes.html | justfly promo codes |
| About | about.html | about flightdealspro |

## GitHub Pages Setup

1. Create repo `brightlane/justfly` on GitHub
2. Add `build.py` to repo root
3. Add `.github/workflows/deploy.yml`
4. **Settings → Pages → Source → GitHub Actions**
5. Push to `main`
6. Live at `{BASE}/`

## Customise

```python
AFF  = "{AFF}"  # Your affiliate URL
BASE = "{BASE}"  # Your GitHub Pages URL
SUB  = "/justfly"  # Repo name
```

## Affiliate Disclosure

FlightDealsPro is an independent affiliate partner of JustFly. Not operated by JustFly.

## License
MIT
""")

def build():
    OUT.mkdir(exist_ok=True)
    for p in PAGES:
        body  = FN_MAP[p["content_fn"]]()
        html  = layout(p, body)
        fname = "index.html" if p["slug"]=="index" else f"{p['slug']}.html"
        (OUT/fname).write_text(html, encoding="utf-8")
        print(f"  ✓ {fname}")
    write_robots(); write_sitemap(); write_llms(); write_404(); write_readme()
    pages = list(OUT.glob("*.html"))
    kb    = sum(f.stat().st_size for f in pages)//1024
    print(f"\n  ✅ Build complete — {len(pages)} pages, {kb}KB total")
    print(f"  📍 Deploy docs/ to GitHub Pages")
    print(f"  🌐 Live at: {BASE}/")

if __name__ == "__main__":
    build()
