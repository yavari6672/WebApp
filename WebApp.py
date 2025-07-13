#!/usr/bin/env python3

'''WebApp'''

import argparse
import subprocess
import sys
import platform
import os
import Apps


def show_system_info():
    print(BN := '='*20, "System Info", BN)
    print(f"Python Version : {platform.python_version()}")
    print(f"OS             : {platform.system()} {platform.release()}")
    print('='*53, "\n")


def run_django(host: str, port: str, verbose: bool):
    command = ["python", "WebApp/manage.py", "runserver", f"{host}:{port}"]

    if verbose:
        command.append("--verbosity=2")

    print(f"Running command: {' '.join(command)}")
    print(f"\n🌐 Server will be available at: http://{host}:{port}\n")

    try:
        subprocess.run(command)
    except KeyboardInterrupt:
        print("\nServer stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    show_system_info()

    parser = argparse.ArgumentParser(
        prog=__doc__, description='Web Application')
    parser.add_argument('-WA', '--WebApp', action='store_true',
                        help='Launch the web application.')
    parser.add_argument('-L', '--local', action='store_true',
                        help='Run on localhost (127.0.0.1).')
    parser.add_argument('-V', '--verbose', action='store_true',
                        help='Enable verbose logging.')
    parser.add_argument('-P', '--port', type=str, default="8000",
                        help='Specify custom port (default: 8000).')
    parser.add_argument('-APP', "--AllApps",
                        help="Print all apps", action='store_true')

    args = parser.parse_args()

    if args.WebApp:
        if not os.path.isfile("WebApp/manage.py"):
            print("❌ Error: 'manage.py' not found in the current directory.")
            sys.exit(1)

        host = "127.0.0.1" if args.local else "0.0.0.0"
        run_django(host, args.port, args.verbose)
    elif args.AllApps:
        Apps.print_apps_table()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
