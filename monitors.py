import subprocess


def screens():
    output = [l for l in subprocess.check_output(
        ["xrandr"]).decode("utf-8").splitlines()]
    return [l.split()[0] for l in output if " connected " in l]


if 'HDMI2' in screens():
    bashCommand = "xrandr --auto --output HDMI2 --right-of eDP1 --mode 1920x1080 --rate 60"
    process = subprocess.run(bashCommand, shell=True, check=True)
