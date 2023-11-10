import subprocess


def upgrade_command(model_name):

    command1 = f'alembic revision --autogenerate -m "Create {model_name} model"'
    command2 = 'alembic upgrade heads'

    result1 = subprocess.check_output(command1, shell=True, universal_newlines=True)
    print("command 1 result", result1)

    result2 = subprocess.check_output(command2, shell=True, universal_newlines=True)
    print("command 2 result", result2)