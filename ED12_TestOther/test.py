import snscrape.modules.twitter as sntwitter
import pandas as pd

query = 'python'
profile = 'BuganDonneraxt'

# TwitterProfileScraper(profile)


for twitt in sntwitter.TwitterUserScraper(profile).get_items():
    print(twitt)


# for tweet in sntwitter.TwitterSearchScraper(query).get_items():
#     print(vars(tweet))
#     break



