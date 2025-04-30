import os
import json


def main() -> None:
    wal = os.path.join(os.path.expanduser("~"), ".cache/hellwal/colors.json")
    cava = os.path.join(os.path.expanduser("~"), ".config/cava")
    preset = os.path.join(cava, "config-preset")
    config = os.path.join(cava, "config")

    with open(wal) as f:
        wal_raw = json.load(f)

    colors = wal_raw["colors"]

    with open(preset, "r") as temp:
        with open(config, "w") as conf:
            for line in temp:
                line = line.replace("$color1", colors["color1"])
                line = line.replace("$color2", colors["color2"])
                line = line.replace("$color3", colors["color3"])
                line = line.replace("$color4", colors["color4"])
                line = line.replace("$color5", colors["color5"])
                line = line.replace("$color6", colors["color6"])
                conf.write(line)
    os.system("killall -s SIGUSR1 cava")


if __name__ == "__main__":
    main()
