import toml


class AccountConfig:
    username: str
    password: str
    server: str
    site_id: str

    def __init__(
        self,
        username: str = "",
        password: str = "",
        server: str = "",
        site_id: str = "",
        filePath: str = None
    ):
        # try read config file first
        if filePath is not None:
            if "toml" in filePath:
                # toml compose
                # [account]
                # username = "xxx"
                # ...
                parsedToml = toml.load(f=filePath)
                self.username = parsedToml["account"]["username"]
                self.password = parsedToml["account"]["password"]
                self.server = parsedToml["account"]["server"]
                self.site_id = parsedToml["account"]["site_id"]
                return
        self.username = username
        self.password = password
        self.server = server
        self.site_id = site_id


def getAccountSetting(file: str) -> AccountConfig:
    return AccountConfig(filePath=file)


