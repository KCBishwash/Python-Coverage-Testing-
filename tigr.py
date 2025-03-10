"""Tigr.

Usage:
  tigr.py [FILES ...] [-c c.ini] [-e tkinter] [-s 5] [-p regex] [--pencolor black] [--pensize 1] [-i]

You can also run all the unittest by this command: python -m unittest discover tigr/test
You can also run all the doc-test by this command: python -m doctest -v tigr/drawer/tkinter_worker.py

Options:
  -h --help                  Show this screen.
  -c 1.ini --config 1.ini    Specify the ini config file name
  -e turtle --engine turtle  Specify the drawer engine, tkinter or turtle. [default: turtle]
  -s 5 --speed 5             Specify the drawer speed, 1 slowest, 9 fastest [default: 5]
  -p regex --parser regex    Specify the instruction parser [default: peg]
  --pencolor black           Specify pen color [default: black]
  --pensize 1                Specify pen size [default: 1]
  -i --interactive           Specify if enter interactive mode when the script files were executed done [default: 0]
  --version                  Show version

Attention:

If an option is found in config file and command line arguments at the same time,
this program will use the value from the ini file.
"""
from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Tigr 1.0')

    if arguments['--config'] is not None:
        import os.path
        import configparser as cp
        config = cp.ConfigParser()

        config_file = arguments['--config']
        if os.path.exists(config_file):
            name, ext = os.path.splitext(config_file)
            if ext.lower() == '.ini':
                config.read(config_file)
                for section in config.sections():
                    for option in config.options(section):
                        arguments['--' + option] = config.get(section, option)
            elif ext.lower() in ['.yml', '.yaml']:
                import yaml
                with open(config_file, 'r') as stream:
                    try:
                        config = yaml.safe_load(stream)
                        for section in config:
                            for option in config[section]:
                                arguments['--' + option] = config[section][option]
                    except yaml.YAMLError as e:
                        print(e)
            else:
                print(f'invalid config file: {config_file}', 'unrecognized ext name')
        else:
            print(f'config file does not exist: {config_file}')

    import tigr
    tigr.main(arguments)
