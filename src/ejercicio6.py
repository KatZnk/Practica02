#6. Análisis de hashtags
#Dadas las siguientes publicaciones de una red social, extraiga todos los
#hashtags (palabras que comienzan con #), cuente la frecuencia de cada uno, y
#muestre los hashtags trending (los que aparecen más de una vez).

def analisis(posts):
    count = {}
    
    for post in posts:
        words = post.split()
        hashtags = [h.lower().strip(",.!") for h in words if h.startswith('#')] 

        for w in hashtags:
            count[w] = count.get(w, 0) + 1

    trending = [(k, v) for k, v in count.items() if v > 1]
    trending.sort(key=lambda x: x[1], reverse=True)
        
    for tag, cant in trending:
        print(f"{tag}: {cant}")