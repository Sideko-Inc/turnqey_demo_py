import enum


class Environment(enum.Enum):
    """Pre-defined base URLs for the API"""

    PRODUCTION = "https://api2.turnqey.xyz/api"
    SANDBOX = "https://turnqeyapi-sandbox.azurewebsites.net/api"
    MOCK_SERVER = "https://api.sideko.dev/v1/mock/public/turnkey-demo/0.1.1"
