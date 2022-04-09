import subprocess


def layout():
    output = subprocess.check_output(
        "setxkbmap -query | grep layout",
        stderr=subprocess.STDOUT,
        shell=True).decode("utf-8").split(' ')
    if "us\n" in output:
        bashCommand = "setxkbmap -layout es"
    else:
        bashCommand = "setxkbmap -layout us"

    return bashCommand


bashCommand = layout()
process = subprocess.run(bashCommand, shell=True, check=True)


layout()
