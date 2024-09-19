
---

## ETHICS.md

# Ethical Considerations for Web Scraping

Web scraping can be a powerful tool for data collection and analysis, but it also raises several ethical and legal concerns. Below are some considerations and measures taken in this project to ensure responsible scraping practices.

## Legal Considerations

1. **Terms of Service Compliance**
   - We reviewed Craigslist’s ToS to ensure that our activities do not violate their guidelines.

2. **Respect for User Privacy**
   - The scraper does not collect personal user data, such as names or contact information, from Craigslist. It only gathers publicly available information related to apartment listings.

3. **Frequency and Volume of Requests**
   - To minimize the impact on Craigslist’s servers, the scraper is designed to send requests at a reasonable frequency. This prevents overloading the server and respects the website’s resources.

4. **Transparency and Attribution**
   - This project is transparent about its purpose and the data it collects. Additionally, the project does not redistribute the data for commercial purposes or present it as proprietary content.

## Ethical Considerations

1. **Impact on Website Functionality**
   - Scraping activities are designed to be lightweight and infrequent to avoid disrupting the normal functionality of the Craigslist website. We use polite scraping techniques, such as adhering to `robots.txt` instructions and implementing delays between requests.

2. **Data Accuracy and Use**
   - While scraping can collect data quickly, it's important to acknowledge that the information may not always be up-to-date or accurate. Users of the data are advised to use it as a supplementary tool and verify the information through official channels.

3. **Respecting the Community**
   - Craigslist listings are user-generated content. The project aims to respect the community by not collecting or publishing any sensitive information or misrepresenting the data collected.

4. **Purpose of Data Collection**
   - The primary goal of this project is educational and analytical. It is intended for learning purposes and for users to gain insights into the rental market in NYC. The data is not used for commercial gain or to manipulate the rental market in any way.

## Mitigation Strategies

- **Rate Limiting**: The scraper is designed to include delays between requests to avoid overwhelming the website.
- **Data Scope**: The scraper collects only a limited set of non-sensitive information, focusing on publicly available apartment listings.
- **Respecting `robots.txt`**: Before scraping, we ensure the website allows scraping of the data we are targeting by checking the `robots.txt` file.

## Conclusion

This project strives to balance the benefits of data collection with the ethical responsibility to respect the website, its users, and their data. We welcome feedback on how we can improve our practices and ensure responsible data scraping.


