# __author__ = 'Chris Eby'

from configparser import ConfigParser
from os import path
from subprocess import Popen, PIPE
import shlex


def main():
    config_file = 'settings.ini'

    # Check if the ini file exists, create if not
    if not path.isfile(config_file):
        create_ini(config_file)
        print(config_file, ' not found, a default one has been created.  Set it up and then re-run.')
        quit()

    # Read in all the settings
    config = ConfigParser()
    config.read(config_file)
    user = config.get('mysql', 'user')
    password = config.get('mysql', 'password')
    destination = config.get('mysql', 'destination')
    file_name = 'mysql_dump'

    print('Running mysqldump')
    cmd = 'mysqldump --events --add-drop-table --all-databases --single-transaction --user=' + user + \
          ' --password="' + password + '" --result-file="' + file_name + '.sql"'
    print(cmd)
    run_cmd(cmd)

    print('Creating tarball')
    run_cmd('tar -cf ' + file_name + '.tar ' + file_name + '.sql')

    print('Zipping tarball')
    run_cmd('gzip -f ' + file_name + '.tar')

    print('Removing dump file')
    run_cmd('rm ' + file_name + '.sql')

    print('Moving zipped tarball to destination')
    run_cmd('mv ' + file_name + '.tar.gz ' + destination)


def run_cmd(cmd):
    process = Popen(shlex.split(cmd), stdout=PIPE)
    dump_output = process.communicate()[0]
    exit_code = process.wait()
    if exit_code != 0:
        print(dump_output)
        raise Exception(str(exit_code) + ' - Error executing command.  Please review output.')


def create_ini(config_file):
    config = ConfigParser()
    config['mysql'] = {
        'user': 'some_user',
        'password': 'default',
        'destination': '/mnt/data/backups/mysql/current/'
    }
    with open(config_file, 'w') as configfile:
        config.write(configfile)


if __name__ == '__main__':
    main()