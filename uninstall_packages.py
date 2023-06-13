import subprocess
import pkg_resources

# Obtém a lista de pacotes instalados
installed_packages = [pkg.key for pkg in pkg_resources.working_set]

# Desinstala cada pacote individualmente
for package in installed_packages:
    subprocess.check_call(['pip', 'uninstall', '-y', package])
    print('Todos pacotes foram desinstalados ')
