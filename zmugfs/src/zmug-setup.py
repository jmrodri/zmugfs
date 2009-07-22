from config import Config

def get_input(msg, default):
    val = raw_input(msg % default)
    if val is None or val == "":
        val = default

    return val

def main():
    config = Config('/etc/zmugfs/zmugfs.conf', '.zmugfs/zmugfsrc')
    username = get_input("smugmug username [%s]: ", config['smugmug.username'])
    password = get_input("smugmug username [%s]: ", config['smugmug.password'])
    disk_cache = get_input("smugmug username [%s] MB: ",
                          config['image.disk.cache'])
    mem_cache = get_input("smugmug username [%s] images: ",
                          config['image.memory.cache'])

if __name__ == '__main__':
    main()
