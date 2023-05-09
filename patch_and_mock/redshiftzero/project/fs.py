from subprocess import check_output


def print_contents():
    return check_output(['ls']).split()

