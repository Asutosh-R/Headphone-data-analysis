

from urllib import robotparser

def check_robots_txt(url):
    rp = robotparser.RobotFileParser()
    rp.set_url(url + '/robots.txt')
    rp.read()
    return rp

# Example usage
rp = check_robots_txt('https://www.amazon.in/')
print(rp.can_fetch('*', 'https://example.com/page1')) 