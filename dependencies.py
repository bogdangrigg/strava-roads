import pip

def install(package):
    pip.main(['install', package])

# Example
if __name__ == '__main__':
    install('BeautifulSoup4')
    install('numpy')
    install('simplejson')
    install('matplotlib')
    install('scipy')
