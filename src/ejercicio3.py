
def censurar(spoilers):
    #guardo la review aca, el usuario no deberia de verlo sin censura
    review = """La película sigue a un grupo de astronautas que
        viajan a Marte
        en una misión de rescate. El capitán Torres lidera al equipo
        a través
        de tormentas solares y fallos en el sistema de navegación. Al
        llegar
        a Marte descubren que la base está abandonada y los
        suministros
        destruidos. Torres decide sacrificar la nave nodriza para
        salvar
        al equipo y logran volver a la Tierra en una cápsula de
        emergencia.
        El final revela que Torres sobrevivió gracias a un pasaje
        secreto."""

    def censurar_palabra(palabra, lista):
        rew = palabra.strip(".,\n") 
        
        if rew.lower() in lista:
            asteriscos = "*" * len(rew)
            return palabra.replace(rew, asteriscos)
        
        return palabra

    clean_rw = [censurar_palabra(pal, spoilers) for pal in review.split()]

    review_censurada = " ".join(clean_rw)
    print(review_censurada)