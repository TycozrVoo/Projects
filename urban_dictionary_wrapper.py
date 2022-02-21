import requests
import re


def urbandict(query):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
    data = requests.get(f"https://www.urbandictionary.com/define.php?term={requests.utils.quote(query)}", headers=headers).text
    definition = re.search('name="Description" property="og:description"><meta content="(.*?)" name="twitter:description">', data).group(1)

    if "&quot;" in definition:
        definition = definition.replace("&quot;", "\"", definition.count("&quot;"))
    elif "&apos;" in definition:
        definition = definition.replace("&apos;", "'", definition.count("&apos;"))

    return definition
