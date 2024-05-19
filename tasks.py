from src.crawler_latimes import  LATimesCrawler

if __name__ == '__main__':
    with LATimesCrawler() as crawler:
        crawler.main("money", "example topic", 0)