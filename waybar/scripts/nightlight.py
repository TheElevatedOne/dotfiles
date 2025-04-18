import json
import sys
import os.path as op
import subprocess


cdir = op.join(op.dirname(op.realpath(__file__)), "nl-config.json")

r_cfg = open(cdir, "r", encoding="utf-8")
r_dict = json.load(r_cfg)
r_cfg.close()

w_cfg = open(cdir, "w", encoding="utf-8")

alt = "off"
temp = "~6500"

argv = sys.argv[-1]

match argv:
    case "return":
        match r_dict["active"]:
            case True:
                alt = "on"
                temp = r_dict["saved"]

            case False:
                alt = alt
                temp = temp

    case "toggle":
        match r_dict["active"]:
            case True:
                # Config Writing
                r_dict["active"] = False
                r_dict["saved"] = 0

                # Hyprctl
                subprocess.run(["hyprctl", "hyprsunset", "identity"])

                # Return value
                alt = "off"
                temp = temp

            case False:
                # Config Writing
                r_dict["active"] = True
                r_dict["saved"] = r_dict["default"]

                # Hyprctl
                subprocess.run(
                    ["hyprctl", "hyprsunset", "temperature", str(r_dict["saved"])]
                )

                # Return value
                alt = "on"
                temp = f"{r_dict['saved']}"


json.dump(r_dict, w_cfg, indent=4)
w_cfg.close()

print(json.dumps({"text": temp, "alt": alt}))
