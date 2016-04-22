#! /usr/bin/python
import json
import os

import git
import requests

def main():
    repo_html_urls = {}
    repo_page_count = 1
    next_url = 'https://api.github.com/orgs/openstack/repos'
    while next_url:
        print 'request repo page %s' % repo_page_count
        resp = requests.get(next_url)
        if resp.status_code == 403:
            print 'API rate limit exceeded, exit'
            exit(1)
        repo_page = json.loads(resp.content)
        for repo in repo_page:
            repo_html_urls[repo['name']] = repo['html_url']
        next_url = resp.links.get('next', {}).get('url')
        repo_page_count += 1

    print 'total repo count: %s' % len(repo_html_urls)

    repo_count = 1
    for name, url in repo_html_urls.items():
        dest_dir = os.path.join('./', name)
        if not os.path.exists(dest_dir):
            print '%s: %s: git clone %s' % (repo_count, name, url)
            repo = git.Repo.clone_from(url, dest_dir)
        else:
            print '%s: %s: git pull --ff-only' % (repo_count, name)
            git.cmd.Git(dest_dir).pull(ff_only=True)
        repo_count += 1

    print 'all %s repositories succeed!' % repo_count - 1

if __name__ == '__main__':
    main()
