import pkg.setting as setting
import pkg.job as job
import tableauserverclient as TSC


def getTableauConnection(username: str, password: str, site_id: str, server: str) -> TSC.Server:
    tableau_auth = TSC.TableauAuth(
        username=username, password=password, site_id=site_id)
    tscServer = TSC.Server(
        server, use_server_version=True)
    tscServer.auth.sign_in(tableau_auth)
    return tscServer


def getRootProjectID(server: TSC.Server) -> {str: str}:
    all_project_items, _ = server.projects.get()
    return {proj.name: proj.id for proj in all_project_items}


def main():
    account = setting.getAccountSetting("./config.toml")
    conn = getTableauConnection(account.username, account.password,
                                account.site_id, account.server)

    jb = job.getJobSetting("./job/test.toml")


if __name__ == '__main__':
    main()
