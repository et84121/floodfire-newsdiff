from crawler import Crawler


def test_NTK():
    c = Crawler(['none', 'ntk', 'list'])
    c.main()
    c = Crawler(['none', 'ntk', 'page'])
    c.main()


def test_NOW():
    c = Crawler(['none', 'now', 'list'])
    c.main()
    c = Crawler(['none', 'now', 'page'])
    c.main()
