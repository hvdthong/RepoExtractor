import configparser
import requests
import time


def load_file(path):
    lines = [line.rstrip('\n') for line in open(path)]
    return lines


def repositories(urls):
    names = list()
    for u in urls:
        names.append(u.replace("https://github.com/", ""))
    return names


if __name__ == "__main__":
    path_url = "./Project_URLs.txt"
    urls_ = load_file(path_url)
    names = repositories(urls=urls_)

    config = configparser.ConfigParser()
    config.read('../../config/config.cfg')
    oauth_token = config['DEFAULT']['github_oauth_token']
    try:
        headers = {'Authorization': 'token ' + oauth_token, 'Accept': 'application/vnd.github.mercy-preview+json'}
        # headers = {'Accept': 'application/vnd.github.mercy-preview+json'}
        for r in names:
            target_url = "https://api.github.com/repos/" + r
            response = requests.get(target_url, headers=headers)
            with open("./output_url_json/%s.txt" % (r.replace("/", "_")), "wb") as output_file:
                content = response.content
                output_file.write(content)
                print content
        # exit()
        time.sleep(3)
    except Exception as e:
        print e
