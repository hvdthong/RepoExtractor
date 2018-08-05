import json
import logging
import pandas
import configparser
import sqlite3
from sqlite3 import Error

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('../../config/config.cfg')
    db_filename = config['DEFAULT']['db_filename']

    json_dir = '../../output/repos_with_topics/'
    languages = ['c', 'c++', 'c#', 'go', 'java', 'javascript', 'python', 'php', 'ruby', 'shell']

    log_filename = '../../log/extract_and_load_repos_with_topics_from_json_to_db.log'
    logging.basicConfig(handlers=[logging.FileHandler(log_filename, 'w+', 'utf-8')], level=20)
    logging.getLogger().addHandler(logging.StreamHandler())

    df = pandas.DataFrame(columns=['repo_full_name', 'topics'])
    for l in languages:
        for i in range(1, 11):
            filename = '{0}_{1}.txt'.format(l, i)
            logging.info('Processing {0}'.format(filename))
            with open(json_dir + filename, 'r', encoding='utf-8') as curr_file:
                json_str = curr_file.read()
                json_objects = json.loads(json_str)
                for j_obj in json_objects['items']:
                    repo_full_name = j_obj['full_name']
                    topics = ','.join(j_obj['topics'])
                    df = df.append({'repo_full_name': repo_full_name, 'topics': topics}, ignore_index=True)

    conn = sqlite3.connect(db_filename)
    try:
        # drop duplicates (possible if position of one repository shift to next page between queries
        df.drop_duplicates(subset='repo_full_name', keep='first', inplace=True)
        df.to_sql(name='tag_recommender_ground_truth_repo_topics', con=conn, if_exists='replace', index=False)
    except Error as e:
        logging.exception(e)
    except Exception as e:
        logging.exception(e)
    finally:
        conn.close()

    logging.info('Total repositories loaded: {0}'.format(len(df.index)))
