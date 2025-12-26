import os
import json
import feedparser
import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time
from collections import defaultdict

class LatamNewsBot:
      def __init__(self):
                self.sources = {
                              'bbc_latam': 'https://feeds.bbc.co.uk/mundo/index.xml',
                              'reuters': 'https://feeds.reuters.com/reuters/businessNews',
                              'apnews': 'https://apnews.com/hub/latin-america/feed',
                              'economist': 'https://www.economist.com/feed.rss',
                              'ft': 'https://feeds.ft.com/ft/news',
                              'bloomberg': 'https://feeds.bloomberg.com/markets/news.rss',
                }

        self.keywords = {
                      'trade': ['trade', 'tariff', 'commerce', 'export', 'import', 'nafta', 'mercosur', 'customs', 'bilateral'],
                      'ai': ['artificial intelligence', 'ai', 'machine learning', 'neural', 'automation', 'tech', 'software', 'chatgpt', 'algorithm'],
                      'investment': ['investment', 'fund', 'venture capital', 'startup', 'ipo', 'fintech', 'banking', 'capital', 'acquisition', 'merger'],
                      'creative': ['creative', 'film', 'music', 'art', 'media', 'entertainment', 'streaming', 'production', 'gaming', 'design', 'cultural', 'content']
        }

        self.articles = defaultdict(list)

    def fetch_articles(self):
              """Fetch articles from all news sources"""
              print(f"[{datetime.now()}] Fetching articles from {len(self.sources)} sources...")

        for source_name, feed_url in self.sources.items():
                      try:
                                        feed = feedparser.parse(feed_url)
                                        for entry in feed.entries[:20]:
                                                              article = {
                                                                                        'source': source_name,
                                                                                        'title': entry.get('title', ''),
                                                                                        'link': entry.get('link', ''),
                                                                                        'published': entry.get('published', ''),
                                                                                        'summary': entry.get('summary', ''),
                                                              }

                    if self.is_latam_related(article):
                                              self.articles['all'].append(article)

except Exception as e:
                print(f"Error fetching from {source_name}: {e}")

    def is_latam_related(self, article):
              """Check if article is related to Latin America"""
              latam_countries = [
                  'argentina', 'brazil', 'chile', 'colombia', 'mexico', 'peru', 'venezuela',
                  'ecuador', 'bolivia', 'paraguay', 'uruguay', 'costa rica', 'panama',
                  'guatemala', 'honduras', 'el salvador', 'nicaragua', 'dominican republic',
                  'cuba', 'haiti', 'jamaica', 'latam', 'latin america'
              ]

        content = (article['title'] + ' ' + article['summary']).lower()
        return any(country in content for country in latam_countries)

    def categorize_articles(self):
              """Categorize articles by topic"""
              categorized = defaultdict(list)

        for article in self.articles['all']:
                      content = (article['title'] + ' ' + article['summary']).lower()

            for category, keywords in self.keywords.items():
                              if any(keyword in content for keyword in keywords):
                                                    categorized[category].append(article)

                      return categorized

    def generate_summary(self, categorized_articles):
              """Generate a weekly summary report"""
              summary = f"""
      ╔══════════════════════════════════════════════════════════════╗
      ║   LATIN AMERICA WEEKLY NEWS RECAP - {datetime.now().strftime('%B %d, %Y')}   ║
      ╚══════════════════════════════════════════════════════════════╝
      """

        for category in ['trade', 'ai', 'investment', 'creative']:
                      articles = categorized_articles.get(category, [])

            summary += f"\n{'='*70}\n"
            summary += f"📌 {category.upper()}\n"
            summary += f"{'='*70}\n"
            summary += f"Total articles: {len(articles)}\n\n"

            for i, article in enumerate(articles[:3], 1):
                              summary += f"{i}. {article['title']}\n"
                              summary += f"   Source: {article['source']} | {article['published']}\n"
                              summary += f"   Read more: {article['link']}\n"
                              summary += f"   Summary: {article['summary'][:150]}...\n\n"

        summary += f"\n{'='*70}\n"
        summary += "📊 KEY STATISTICS\n"
        summary += f"{'='*70}\n"
        summary += f"Total articles analyzed: {len(categorized_articles.get('all', []))}\n"
        summary += f"Data collection period: Last 7 days\n"
        summary += f"Report generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"

        return summary

    def save_summary(self, summary):
              """Save summary to file"""
              filename = f"latam_recap_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
              with open(filename, 'w', encoding='utf-8') as f:
                            f.write(summary)
                        print(f"Summary saved to {filename}")
        return filename

    def run_weekly(self, recipient_email=None):
              """Run the bot and generate weekly recap"""
        print(f"\n{'='*70}")
        print(f"STARTING WEEKLY NEWS RECAP - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*70}\n")

        self.fetch_articles()
        categorized = self.categorize_articles()
        summary = self.generate_summary(categorized)

        print(summary)
        filename = self.save_summary(summary)

        return filename

if __name__ == "__main__":
      bot = LatamNewsBot()
    bot.run_weekly()
