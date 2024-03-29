
## Batch publishing tool

This tool batch-publishes HTML files transformed from DITA source files to Help Center.


### Limitation

The tool updates existing articles in Help Center. In other words, the articles must have known Help Center ids. To publish a batch of new articles, the tool must be modified to specify the target section of each article, as well as use the `post_resource()` instead of the `put_resource()` helper in **api.py**. Here's a quick script that'll upload a collection of HTML files to Help Center: https://gist.github.com/chucknado/40ff923e6a2eef6ad529bf32cd12640f.


### Requirements

- Python 3.6 or later
- requests library - http://docs.python-requests.org/en/master/
- BeautifulSoup library - https://www.crummy.com/software/BeautifulSoup/


### Setting up

1. Map your DITA file names to their corresponding Help Center ids. To do so, create a yml file called **ditamap.yml**. Enter the following information for each article: DITA filename without the file extension, Help Center subdomain, and article id.

    Example:

    ```yml
    - dita: zug_placeholders
      hc: support
      id: 203662116
    - dita: zug_markdown
      hc: support
      id: 203661586
    ```

    Make sure to follow the format in the example.

    You can keep adding mappings to the same yml file. You don't need to create a yml file each time you publish.

    Make sure each article id is unique in the yml file.

    Don't include the .dita file extension.

    Save the file anywhere on your computer.

2. In the zpu project files, update the **auth.py** file with your Zendesk username and API token. Example:

    ```
    def get_auth():
        return '{}/token'.format('jdoe@example.com'), '9a8b7c6d5e4f3g2h1'
    ```

3. In the **[HC]** section of the **settings.ini** file, specify your Help Center settings. Example:

    ```text
    [HC]
    subdomain=support
    locale=en-us
	```

4. In the **[MAP]** section of the **settings.ini** file, specify the path to the **ditamap.yml** file. Example:

    ```text
    [MAP]
    path=/Volumes/GoogleDrive/Team Drives/Documentation/Production/ditamap.yml
    ```


### Publishing files

1. Use your DITA authoring tool to batch transform the DITA files to HTML.

2. Copy the transformed HTML files to the **zpu/transformed_dita_files** folder.

3. In your command line interface, navigate to your **zpu** folder on your computer.

4. Run the following command:

    ```bash
    $ python3 publish_files.py
    ```

    The tool parses each HTML file and publishes it to HC.

5. When you're done, move or delete the HTML files in the **zpu/transformed_dita_files** folder to prepare for your next batch of files.


### Terms of use

This project is open source. It's not officially supported by Zendesk. See the license for the terms of use.
