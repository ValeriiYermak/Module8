from collections import Counter

IP = [
    "85.157.172.253",
    "85.157.171.253",
    "85.157.172.253",
    "85.157.172.253",
    "85.157.171.253",
    "85.157.173.253",
    "85.157.175.253",
    "85.157.173.253",
    "85.157.172.253"
]

def get_count_visits_from_ip(ips):
    key_ip = Counter(ips)
    return (key_ip)

  
def get_frequent_visit_from_ip(ips):
    key_ip = Counter(ips)
    often_use = key_ip.most_common(1)
    return often_use[0]

