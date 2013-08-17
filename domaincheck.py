from string import ascii_lowercase
from multiprocessing import Pool
import whois
import sys


def whois_lookup(url):
    try:
        whois.whois(url)
        sys.stderr.write('unavailable domain: %s\n' % (url))
        sys.stderr.flush()
    except Exception:
        print('available domain: %s' % (url))


def gendomain():
    for i in ascii_lowercase:
        for j in ascii_lowercase:
            for k in ascii_lowercase:
                for l in ascii_lowercase:
                    yield '%s%s%s%s.com' % (i, j, k, l)


if __name__ == '__main__':
    query = gendomain()
    p = Pool(processes=1)
    p.map(whois_lookup, query)
