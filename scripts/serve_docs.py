#!/usr/bin/env python3
import argparse
import os
import subprocess
import sys
import webbrowser

def main():
    p = argparse.ArgumentParser(description="Serve Sphinx HTML docs with python -m http.server")
    p.add_argument("--dir", "-d", default="../docs/build/html", help="Directory to serve")
    p.add_argument("--port", "-p", type=int, default=8000, help="Port to serve on")
    p.add_argument("--bind", default="127.0.0.1", help="Address to bind to (use 0.0.0.0 to expose)")
    p.add_argument("--open", action="store_true", help="Open the served URL in the default browser")
    args = p.parse_args()

    path = os.path.abspath(args.dir)
    if not os.path.isdir(path):
        print(f"Directory `{path}` does not exist")
        sys.exit(1)

    url = f"http://{args.bind}:{args.port}/"
    cmd = [sys.executable, "-m", "http.server", str(args.port), "--directory", path, "--bind", args.bind]

    print(f"Serving {url} from `{path}` (Ctrl-C to stop)")
    if args.open:
        webbrowser.open(url)

    try:
        subprocess.run(cmd, check=True)
    except KeyboardInterrupt:
        print("\nStopped.")
    except subprocess.CalledProcessError as e:
        print(f"Server exited with code {e.returncode}")
        sys.exit(e.returncode)

if __name__ == "__main__":
    main()
