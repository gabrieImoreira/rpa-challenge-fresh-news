from src.crawler_latimes import  LATimesCrawler

if __name__ == '__main__':

    crawler = LATimesCrawler().main("Facebook", "California", 3)
    # crawler = LATimesCrawler().main("Biden", "Politics", 1)
    # print(crawler)