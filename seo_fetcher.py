import random

def fetch_seo_metrics(keyword):
    return {
        "keyword": keyword,
        "search_volume": random.randint(500, 50000),
        "keyword_difficulty": random.randint(10, 100),
        "avg_cpc": round(random.uniform(0.3, 6.5), 2)         
    }
