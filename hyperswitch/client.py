class HyperSwitchClient:
    def __init__(self, base_url: str, api_key: str = None):
        """
        Initialize the HyperSwitch client with the base URL.

        :param base_url: The base URL for the HyperSwitch API.
        """
        self.base_url = base_url
        self.api_key = api_key
