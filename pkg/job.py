import toml


class JobTask:
    typ: str
    projectName: str
    workbookName: str
    csv: {str: str}


class JobConfig:
    task: [JobTask]

    def __init__(
        self,
        filePath: str
    ):
        if "toml" in filePath:
            parsedToml = toml.load(f=filePath)
            print(parsedToml)


def getJobSetting(file: str) -> JobConfig:
    return JobConfig(file)
