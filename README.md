
## DITA transformation publish tool

This tool batch-publishes transformed DITA files to Help Center.

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
    ...
    ```

    Make sure to follow the format above.

    Make sure the article id is unique in the yml file.

    Don't include the .dita extension.

    Save the file anywhere on your computer.


2. In the zpu files, update the **auth.py** file with your Zendesk username and API token:

    ```
    def get_auth():
        return '{}/token'.format('jdoe@example.com'), '9a8b7c6d5e4f3g2h1'
    ```

3. Specify your Help Center settings in the **[HC]** section of the **settings.ini** file:

    ```text
    [HC]
    subdomain=support
    locale=en-us
	```

4. Specify the path to the **ditamap.yml** file the **[MAP]** section of the **settings.ini** file:
    
    ```text
    [MAP]
path=/Volumes/GoogleDrive/Team Drives/Documentation/All products/production/ditamap.yml
    ```


### Publishing files


1. Batch transform the DITA files to HTML.

2. Copy the transformed HTML files to the **zpu/transformed_dita_files** folder.

3. Run the following script to parse each file and publish it to HC:

    ```bash
    $ python publish_files.py
    ```

4. When you're done, move or delete the HTML files in the **zpu/transformed_dita_files** folder to prepare for your next batch of transformed DITA files.


### Terms of use

This project is open source. It's not officially supported by Zendesk. See the license for the terms of use.