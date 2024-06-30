import subprocess


def install_package(package):
    try:
        subprocess.check_call(["pip", "install", package])
    except subprocess.CalledProcessError:
        print(f"Failed to install package: {package}")


def main():
    with open("sys_requirements.txt", "r") as f:
        for line in f:
            package = line.strip()
            if package and not package.startswith("#"):
                install_package(package)


if __name__ == "__main__":
    main()
