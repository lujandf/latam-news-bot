# Latin America News Bot - Setup Guide

## Overview

The Latin America News Bot is an automated system that monitors trustworthy news sources and generates comprehensive weekly recaps of the most relevant news about Latin America, with a specific focus on:
- **Trade**: Trade agreements, tariffs, commerce developments
- - **AI Development**: Artificial intelligence, machine learning, automation
  - - **Investment**: Venture capital, startups, fintech, acquisitions
    - - **Creative Industries**: Films, music, entertainment, streaming platforms
     
      - ## Features
     
      - ✅ **Multi-source monitoring** - Tracks BBC, Reuters, AP News, The Economist, Financial Times, and Bloomberg
      - ✅ **Smart categorization** - Automatically categorizes articles by topic area
      - ✅ **Geographic filtering** - Focuses exclusively on Latin American news
      - ✅ **Automated scheduling** - Runs weekly on schedule
      - ✅ **Email delivery** - Sends formatted reports directly to your inbox
      - ✅ **Database storage** - Maintains article history and tracking
      - ✅ **JSON export** - Exports data for further analysis
     
      - ## Installation
     
      - ### 1. Prerequisites
     
      - - Python 3.8 or higher
        - - pip (Python package installer)
          - - Git
           
            - ### 2. Clone the Repository
           
            - ```bash
              git clone https://github.com/lujandf/latam-news-bot.git
              cd latam-news-bot
              ```

              ### 3. Install Dependencies

              ```bash
              pip install -r requirements.txt
              ```

              ### 4. Configure Environment Variables

              ```bash
              # Copy the example configuration
              cp .env.example .env

              # Edit the .env file with your settings
              nano .env
              ```

              **Required environment variables:**

              ```
              SENDER_EMAIL=your-gmail@gmail.com
              SENDER_PASSWORD=your-app-password
              RECIPIENT_EMAIL=recipient@example.com
              SCHEDULE_DAY=monday
              SCHEDULE_TIME=09:00
              ```

              ### 5. Gmail App Password Setup

              To use Gmail with the bot:

              1. Enable 2-Step Verification on your Gmail account
              2. 2. Go to https://myaccount.google.com/apppasswords
                 3. 3. Select "Mail" and "Windows Computer" (or your device)
                    4. 4. Generate a password
                       5. 5. Copy the 16-character password to SENDER_PASSWORD in .env
                         
                          6. ## Usage
                         
                          7. ### Run Immediately
                         
                          8. ```bash
                             python latam_news_bot.py
                             ```

                             ### Schedule Weekly Runs

                             **On Linux/Mac:**

                             ```bash
                             # Add to crontab
                             crontab -e

                             # Add this line for 9 AM Monday
                             0 9 * * 1 /usr/bin/python3 /path/to/latam_news_bot.py
                             ```

                             **On Windows:**

                             Use Task Scheduler to create a scheduled task that runs the Python script at your preferred time.

                             ## Project Structure

                             ```
                             latam-news-bot/
                             ├── latam_news_bot.py       # Main bot script
                             ├── requirements.txt         # Python dependencies
                             ├── .env.example            # Example environment configuration
                             ├── .gitignore              # Git ignore file
                             ├── README.md               # Project overview
                             ├── SETUP.md                # This setup guide
                             └── README_ES.md            # Spanish documentation
                             ```

                             ## Troubleshooting

                             ### No articles found
                             - Verify internet connectivity
                             - - Check that the news feeds are accessible
                               - - Ensure LATAM country keywords are comprehensive
                                
                                 - ### Email not sending
                                 - - Verify SENDER_EMAIL and SENDER_PASSWORD are correct
                                   - - Check that Gmail app password is properly set (16 characters)
                                     - - Verify 2-Step Verification is enabled on Gmail
                                      
                                       - ### Scheduled task not running
                                       - - Verify the Python path is correct
                                         - - Check system logs for error messages
                                           - - Ensure the script has executable permissions
                                            
                                             - ## Advanced Configuration
                                            
                                             - ### Adding Custom News Sources
                                            
                                             - Edit the `sources` dictionary in `latam_news_bot.py`:
                                            
                                             - ```python
                                               self.sources = {
                                                   'source_name': 'https://feed-url.com/rss',
                                                   # Add more sources here
                                               }
                                               ```

                                               ### Modifying Keyword Categories

                                               Update the `keywords` dictionary to add or remove search terms:

                                               ```python
                                               self.keywords = {
                                                   'trade': ['trade', 'tariff', ...],
                                                   'ai': ['artificial intelligence', ...],
                                                   # Customize categories
                                               }
                                               ```

                                               ### Adding More LATAM Countries

                                               Expand the `latam_countries` list in the `is_latam_related()` method:

                                               ```python
                                               latam_countries = [
                                                   'argentina', 'brazil', ...
                                                   # Add more countries
                                               ]
                                               ```

                                               ## Output

                                               The bot generates a comprehensive weekly report that includes:

                                               - **Trade News**: Top 3 articles on Latin American trade
                                               - - **AI Development**: Leading AI/tech developments in the region
                                                 - - **Investment**: Major investment and funding announcements
                                                   - - **Creative Industries**: Entertainment and cultural industry updates
                                                     - - **Key Statistics**: Analysis metadata and article counts
                                                      
                                                       - Reports are saved as:
                                                       - - Text files: `latam_recap_YYYYMMDD_HHMMSS.txt`
                                                         - - Sent via email with formatted summary
                                                           - - Can be exported to JSON for data analysis
                                                            
                                                             - ## Contributing
                                                            
                                                             - To improve the bot:
                                                            
                                                             - 1. Fork the repository
                                                             2. Create a feature branch (`git checkout -b feature/enhancement`)
                                                             3. 3. Make your changes
                                                                4. 4. Commit (`git commit -am 'Add enhancement'`)
                                                                   5. 5. Push (`git push origin feature/enhancement`)
                                                                      6. 6. Create a Pull Request
                                                                        
                                                                         7. ## Support & Issues
                                                                        
                                                                         8. If you encounter any issues:
                                                                        
                                                                         9. 1. Check the Troubleshooting section above
                                                                            2. 2. Review existing GitHub Issues
                                                                               3. 3. Create a new issue with:
                                                                                  4.    - Error message
                                                                                        -    - Steps to reproduce
                                                                                             -    - Your environment (OS, Python version)
                                                                                              
                                                                                                  - ## License
                                                                                              
                                                                                                  - This project is licensed under the MIT License - see LICENSE file for details.
                                                                                              
                                                                                                  - ## Future Enhancements
                                                                                              
                                                                                                  - Planned features:
                                                                                                  - - [ ] Web dashboard for viewing reports
                                                                                                    - [ ] - [ ] Database integration for long-term storage
                                                                                                    - [ ] - [ ] API endpoint for accessing reports
                                                                                                    - [ ] - [ ] Multi-language summaries
                                                                                                    - [ ] - [ ] Slack/Discord integration
                                                                                                    - [ ] - [ ] Advanced sentiment analysis
                                                                                                    - [ ] - [ ] Trend detection and analysis
                                                                                                   
                                                                                                    - [ ] ## Contact
                                                                                                   
                                                                                                    - [ ] For questions or suggestions, please open an issue on GitHub or contact the maintainer.
                                                                                                   
                                                                                                    - [ ] ---
                                                                                                   
                                                                                                    - [ ] **Last Updated:** December 2024
                                                                                                    - [ ] **Version:** 1.0.0
