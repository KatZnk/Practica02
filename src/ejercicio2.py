
def evaluar_playlist(playlist):
    total_segundos = sum(int(m) * 60 + int(s) for m, s in (c['duration'].split(":") for c in playlist))

    min_total, sec_total = divmod(total_segundos, 60)

    print(f"Duración total: {min_total}m {sec_total}s")

    mas_larga = max(playlist, key=lambda c: int(c['duration'].split(":")[0]) * 60 + int(c['duration'].split(":")[1]))
    mas_corta = min(playlist, key=lambda c: int(c['duration'].split(":")[0]) * 60 + int(c['duration'].split(":")[1]))

    print(f"Canción más larga: \"{mas_larga['title']}\" {mas_larga['duration']}")
    print(f"Canción más corta: \"{mas_corta['title']}\" {mas_corta['duration']}")

