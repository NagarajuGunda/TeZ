import os
import sys
import yaml

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import app_mods


def main():
    r = app_mods.get_systemCfg()
    print(r)

    mo = app_mods.get_system_info("MARKET_TIMING", "OPEN")
    print(mo)

    gsheet_info = app_mods.get_system_info("TIU", "GOOGLE_SHEET")
    print(gsheet_info)

    cred_file = app_mods.get_system_info("TIU", "CRED_FILE")
    print(cred_file)

    with open(cred_file) as f:
        cred = yaml.load(f, Loader=yaml.FullLoader)

    session_id = app_mods.get_session_id_from_gsheet(cred,
                                                     gsheet_client_json=gsheet_info['CLIENT_SECRET'],
                                                     url=gsheet_info['URL'],
                                                     sheet_name=gsheet_info['NAME'])

    print(f'session_id:{session_id}')


if __name__ == "__main__":
    main()
