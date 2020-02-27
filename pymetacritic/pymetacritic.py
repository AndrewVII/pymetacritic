"""This is a module to get album ratings from metacritic.

Raises:
    ValueError: If the requested album is not found on metacritic
"""

import requests
from bs4 import BeautifulSoup


class Album():
    """Class which gets metacritic scores for albums

    Arguments:
        album_name {string} -- the name of the album

    Raises:
        ValueError: If the requested album is not found on metacritic
    """

    def __init__(self, album_name):
        self.name = album_name
        self.link = None
        self.critic_score = None
        self.user_score = None
        self.get_album_data()

    def get_album_data(self):
        """Gets the album scores from the name associated with the Album class

        Raises:
            ValueError: If the requested album is not found on metacritic
        """

        album_in_link = '-'.join(self.name.split(' '))
        self.link = f'https://www.metacritic.com/music/{album_in_link}'
        headers = {
            'User-Agent': (
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/80.0.3987.122 Safari/537.36'
                )
        }
        page = requests.get(self.link, headers=headers)

        if page.status_code == 404:
            raise ValueError(f'{self.link} returned a 404 Error')

        soup = BeautifulSoup(page.text, 'html.parser')
        self.critic_score = soup.find(
            "div",
            {"class": "metascore_w xlarge album positive"}
        ).getText()
        self.user_score = soup.find(
            "div",
            {"class": "metascore_w user large album positive"}
        ).getText()
        self.user_score = str(int(float(self.user_score) * 10))

    def change_album(self, new_album_name):
        """Changes the data for this object to align with the new album name

        Arguments:
            new_album_name {string} -- name of the new album
        """
        self.name = str(new_album_name)
        self.get_album_data()
