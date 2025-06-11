# Channel-Schedule-Scraper

*Python based web scraper to retrieve schedule from StaseraInTv website*

![Last Commit](https://img.shields.io/github/last-commit/pingmyheart/Channel-Schedule-Scraper)
![Repo Size](https://img.shields.io/github/repo-size/pingmyheart/Channel-Schedule-Scraper)
![Issues](https://img.shields.io/github/issues/pingmyheart/Channel-Schedule-Scraper)
![Pull Requests](https://img.shields.io/github/issues-pr/pingmyheart/Channel-Schedule-Scraper)
![License](https://img.shields.io/github/license/pingmyheart/Channel-Schedule-Scraper)
![Top Language](https://img.shields.io/github/languages/top/pingmyheart/Channel-Schedule-Scraper)
![Language Count](https://img.shields.io/github/languages/count/pingmyheart/Channel-Schedule-Scraper)

## Why Channel-Schedule-Scraper?

This project provides a simple and efficient way to scrape TV schedules from the StaseraInTv website. The core features
include:

- 🌐 **Multi-channel Support**: Scrapes schedules for multiple TV channels.
- 📦 **Lightweight**: Built with Python, ensuring a minimal footprint.
- 🤝 **Open Source Collaboration**: Built under the MIT License, promoting innovation and community contributions.

# Getting started

## Native Installation

1. **Clone the repository**:

```bash
git clone https://github.com/pingmyheart/Channel-Schedule-Scraper.git
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3**Run the service**:

```bash
python main.py
```

## Docker Installation

1. **Pull the Docker image**:

```bash
docker pull ghcr.io/pingmyheart/channel-schedule-scraper:${VERSION}
```

2. **Run the Docker container**:

```yaml
services:
  scraper:
    image: ghcr.io/pingmyheart/channel-schedule-scraper:${VERSION}
    ports:
      - "8080:8080"
```

# Usage

```bash
# Retrieve all channels
curl --location 'localhost:8080/channel-schedule-scraper/schedule/channels'

# Retrieve the schedule for a specific channel
curl --location 'localhost:8080/channel-schedule-scraper/schedule?channel_href=/programmi_stasera_iris.html#pal'
```