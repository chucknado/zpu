import yaml
import configparser
from pathlib import Path

from bs4 import BeautifulSoup


def get_settings(target):
    config = configparser.ConfigParser()
    config.read('settings.ini')

    if target == 'hc':
        hc = config['HC']
        return {'root': 'https://{}.zendesk.com/api/v2/help_center'.format(hc['subdomain']), 'locale': hc['locale']}

    elif target == 'ditamap':
        ditamap = config['DITAMAP']
        ditamap_path = Path(ditamap['path'])
        if ditamap_path.exists():
            return ditamap_path
        else:
            print('The file path you specified in settings.ini does not exist. Exiting.')
            exit()

    else:
        print('Missing argument for get_settings(). Exiting.')
        exit()


def get_ditamap_articles():
    ditamap = get_settings('ditamap')
    with ditamap.open(mode='r') as f:
        return yaml.load(f)


def package_translation(file):
    """
    Creates a payload from an HTML file for a PUT translation request.
    :param file: A path object to an HTML file
    :return: Dictionary with a title and body property
    """
    with file.open(mode='r') as f:
        html_source = f.read()
    tree = BeautifulSoup(html_source, 'lxml')
    title = tree.h1.string.strip()
    tree.h1.decompose()
    body = str(tree.body)
    if title is None or body is None:
        print('ERROR: title or body problem in \"{}\" (extra inner tags, etc)'.format(file.name))
        exit()
    package = {
        'title': title,
        'body': body
    }
    return {'translation': package}
