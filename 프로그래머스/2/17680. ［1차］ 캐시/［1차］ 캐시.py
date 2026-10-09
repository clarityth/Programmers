def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities :
        city = city.lower()
        if city in cache : # Cache Hit
            answer += 1
            cache.remove(city)
            cache.append(city)
        else : # Cache Miss
            answer += 5
            cache.append(city)
            if cacheSize < len(cache) :
                cache = cache[1:]
    return answer