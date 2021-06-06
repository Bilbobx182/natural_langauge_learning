from util import deEmojify,clean

def load_whatsapp_data():
        """
        Clean up the data.txt
        - lower to standardise  what we have.
        - remove special characters
        :return: data.txt
        """
        with open('data.txt', 'r') as file:
            data = file.read()

        cleansed_emoji = deEmojify(data)
        return clean(cleansed_emoji)


