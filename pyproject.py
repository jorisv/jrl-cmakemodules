#!/usr/bin/env python3
import sys

try:
    import tomlkit
except ImportError as e:
    print(
        "tomlkit not found. Please make sure to install the package. If it is already installed, make sure that it is included in the search path."
    )
    raise e


def update_pyproject_version(version):
    with open("pyproject.toml") as f:
        doc = tomlkit.load(f)
    doc["project"]["version"] = version
    with open("pyproject.toml", "w") as f:
        tomlkit.dump(doc, f)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        update_pyproject_version(sys.argv[1])
    else:
        print("you must provide the version as argument.")
        exit(1)
