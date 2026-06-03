# FlightDealsPro — JustFly Affiliate Site

> 20-page static affiliate site promoting JustFly.
> Live at: **https://brightlane.github.io/justfly/**
> Affiliate URL: `https://track.rqqft.com/aff_c?offer_id=25631&aff_id=21885`

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
6. Live at `https://brightlane.github.io/justfly/`

## Customise

```python
AFF  = "https://track.rqqft.com/aff_c?offer_id=25631&aff_id=21885"  # Your affiliate URL
BASE = "https://brightlane.github.io/justfly"  # Your GitHub Pages URL
SUB  = "/justfly"  # Repo name
```

## Affiliate Disclosure

FlightDealsPro is an independent affiliate partner of JustFly. Not operated by JustFly.

## License
MIT
