from pathlib import Path

from helpers import get_settings, get_ditamap_articles, package_translation
import api


hc = get_settings('hc')
ditamap_articles = get_ditamap_articles()
transformed_files = Path('transformed_dita_files')
files = list(transformed_files.glob(f'**/*.html'))
skips = []
for file in files:
    isMapped = False
    for article in ditamap_articles:
        if article['dita'] == file.stem:
            isMapped = True
            if article['id'] is None:
                skips.append('  - \"{}\" (article id not defined in the ditamap)'.format(file.name))
                continue
            # if article['dita'] not in ['out_email_template']:       # test articles
            #     continue
            print('Publishing \"{}\" as {}'.format(file.name, article['id']))
            url = '{}/articles/{}/translations/{}.json'.format(hc['root'], article['id'], hc['locale'])
            payload = package_translation(file)
            response = api.put_resource(url, payload)
            if response is False:
                skips.append('  - \"{}\" (failed to update article)'.format(file.name))
            break
    if not isMapped:
        skips.append('  - \"{}\" (filename not in the ditamap)'.format(file.name))

if skips:
    print('\nThe following HTML file or files were skipped. Upload them manually.')
    for skip in skips:
        print(skip)
