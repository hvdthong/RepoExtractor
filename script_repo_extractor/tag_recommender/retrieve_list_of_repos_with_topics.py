'''
Obtain list of recently-updated repos that have at least one topic, ordered by popularity
'''
import configparser
import pandas
import logging
import sqlite3
from sqlite3 import Error
import requests
import time
import urllib.parse

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('../../config/config.cfg')
    db_filename = config['DEFAULT']['db_filename']
    oauth_token = config['DEFAULT']['github_oauth_token']

    log_filename = '../../log/obtain_list_of_repos_with_topics.log'
    logging.basicConfig(handlers=[logging.FileHandler(log_filename, 'w+', 'utf-8')], level=20)
    logging.getLogger().addHandler(logging.StreamHandler())

    conn = sqlite3.connect(db_filename)
    try:
        headers = {'Authorization': 'token ' + oauth_token, 'Accept': 'application/vnd.github.mercy-preview+json'}
        # headers = {'Accept' : 'application/vnd.github.mercy-preview+json'}
        languages = ['c', 'c++', 'c#', 'go', 'java', 'javascript', 'python', 'php', 'ruby', 'shell']
        # languages = ['c']
        '''
        Search criteria: 
        - Public repository
        - Has at least 1 topic
        - Written in one of the programming languages in the list (meant as a method to eliminate repositories that contain non-software projects)
        - Updated in 2017 June or later
        - Not a fork
        - Not archived
        - Not a mirror
        Sorting is done by number of stars, in descending order (meant to increase the chance that the partial repository list retrieved is actually 
        the most widely used "real-world" project instead of, for example, a personal practice repo)
        - Pick 100 repositories per language for further filtering
        '''
        for l in languages:
            for i in range(1, 11):
                target_url = ('https://api.github.com/search/repositories?' +
                              'q=topics%3A>0+language%3A{0}+pushed%3A>2017-06-01+'.format(urllib.parse.quote_plus(l)) +
                              'is%3Apublic+fork%3Afalse+archived%3Afalse+mirror%3Afalse&' +
                              'sort=stars&order=desc&page={0}&per_page=100'.format(i))
                logging.info(target_url)
                response = requests.get(target_url, headers=headers)
                with open('../../output/repos_with_topics/{0}_{1}.txt'.format(l, i), 'wb') as output_file:
                    # Save the JSON for later parsing
                    output_file.write(response.content)

                # Avoid making too many requests within short period of time
                time.sleep(3)

    except Exception as e:
        logging.exception(e)
    finally:
        conn.close()
    logging.info('Extraction completed')
    logging.info("Loading of repository topics has been completed")
