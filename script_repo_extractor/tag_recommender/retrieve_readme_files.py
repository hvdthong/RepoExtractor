import configparser
import requests
import base64
import pandas
import logging
import sqlite3
from sqlite3 import Error
import json
import time

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('../../config/config.cfg')
    db_filename = config['DEFAULT']['db_filename']
    oauth_token = config['DEFAULT']['github_oauth_token']
    output_readme_dir = '../../output/downloaded_README/'
    
    log_filename = '../../log/retrieve_readme_files.log'
    logging.basicConfig(handlers=[logging.FileHandler(log_filename, 'w+', 'utf-8')], level=20)
    logging.getLogger().addHandler(logging.StreamHandler())
    
    conn = sqlite3.connect(db_filename)
    try:
        df = pandas.read_sql(sql='SELECT repo_full_name FROM tag_recommender_ground_truth_repo_topics ORDER BY repo_full_name',con=conn) 
        for i,r in df.iterrows():
            repo_full_name = r[0]
            target_url = ('https://api.github.com/repos/{0}/readme'.format(repo_full_name))
            logging.info(target_url)
            
            # Check README file. For consistency with dataset of the paper, ignore if name is not README.md
            headers = {'Authorization': 'token ' + oauth_token, 'Accept' : 'application/vnd.github.mercy-preview+json'}
            response = requests.get(target_url, headers=headers)
            readme_json_object = json.loads(response.content)
            try:
                if(readme_json_object['name'] == 'README.md'):
                    readme_content = base64.b64decode(readme_json_object['content'])
                    filename = output_readme_dir + repo_full_name.replace('/','.') + '.md' 
                    with open(filename, 'wb') as f:
                        f.write(readme_content)
                        logging.info('Downloaded README of {0} into {1}'.format(repo_full_name, filename))
                else:
                    logging.info('Repository {0} uses README other than README.md ({1}). Skipping'.format(repo_full_name, 
                                                                                                          readme_json_object['name'])) 
            except KeyError:    
                logging.info('Repository {0} does not have defined README. Skipping'.format(repo_full_name)) 
            # Avoid making too many requests within short period of time
            time.sleep(2)       
    except Error as e:
        logging.exception(e)        
    except Exception as e:
        logging.exception(e)
    finally:
        conn.close()    
    
    logging.info('README retrieval completed')

