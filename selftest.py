"""Local tester for server.py - not the hidden grader.

    python3 selftest.py

Starts your server.py in the background, runs the given client.py twice and prints the answers.
"""
import os
import subprocess
import sys
import time


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    server = subprocess.Popen([sys.executable, os.path.join(here, "server.py")], cwd=here)
    try:
        time.sleep(1)
        for message, expected in (("meow", "woem"), ("Kululu", "ululuK")):
            result = subprocess.run(
                [sys.executable, os.path.join(here, "client.py"), message],
                capture_output=True, text=True, timeout=5,
            )
            answer = result.stdout.strip()
            if result.returncode != 0:
                print("the client crashed:", result.stderr.strip().splitlines()[-1])
                continue
            print("sent", repr(message), "- the server answered", repr(answer))
            print("OK" if answer == expected else f"expected {expected!r}")
    finally:
        server.kill()


if __name__ == "__main__":
    main()
