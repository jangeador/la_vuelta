import random


def intro():
    print("\nBienvenidos al Juego de Aventuras de los Dominicanos!")
    print(
        "Ustedes son un grupo de amigos dominicanos tratando de llegar a los Estados Unidos."
    )
    print(
        "El viaje comenzará en la República Dominicana, pasando por Colombia y luego atravesando Panamá, Costa Rica, Nicaragua, Honduras, Guatemala, y finalmente México desde Chiapas hasta San Luis Río Colorado para llegar a San Luis, Arizona.\n"
    )
    print(
        "Prepárate para una aventura llena de retos, decisiones difíciles y sorpresas!\n"
    )


class Player:
    def __init__(self, name):
        self.name = name
        self.energy = 100
        self.money = 500
        self.morale = 100
        self.location = "Dominican Republic"

    def update_status(self, energy_change, money_change, morale_change):
        self.energy = max(0, min(self.energy + energy_change, 100))
        self.money = max(0, self.money + money_change)
        self.morale = max(0, min(self.morale + morale_change, 100))

    def status(self):
        print(f"\nEstado de {self.name}:")
        print(f" Energía: {self.energy}")
        print(f" Dinero: ${self.money}")
        print(f" Moral: {self.morale}\n")

    def is_alive(self):
        return self.energy > 0 and self.morale > 0 and self.money > 0


def challenge(player, location):
    location_challenges = {
        "Colombia": [
            (
                "Las autoridades colombianas están revisando papeles en el aeropuerto. ¿Intentan hablar con ellos o se escabullen?",
                "Hablar con las autoridades",
                "Escabullirse",
            ),
            (
                "Hay una tormenta inesperada y los vuelos se cancelan. ¿Esperan la tormenta o buscan otra forma de continuar el viaje?",
                "Esperar la tormenta",
                "Buscar otra forma",
            ),
        ],
        "Panamá": [
            (
                "Tienen que cruzar la selva del Darién. ¿Contratan un guía local o intentan cruzar solos?",
                "Contratar un guía",
                "Cruzar solos",
            ),
            (
                "La policía panameña está pidiendo documentos. ¿Los enfrentan o intentan esconderse?",
                "Enfrentar a la policía",
                "Esconderse",
            ),
        ],
        "Costa Rica": [
            (
                "El grupo se encuentra con problemas al cruzar la frontera. ¿Intentan sobornar a la autoridad o buscan otra ruta?",
                "Sobornar a la autoridad",
                "Buscar otra ruta",
            ),
            (
                "Los recursos están bajos. ¿Piden ayuda a los locales o siguen adelante sin descanso?",
                "Pedir ayuda a los locales",
                "Seguir adelante",
            ),
        ],
        "Nicaragua": [
            (
                "Se encuentran con manifestantes que bloquean el camino. ¿Se unen a la manifestación o buscan una ruta alternativa?",
                "Unirse a la manifestación",
                "Buscar una ruta alternativa",
            ),
            (
                "Hay soldados en la carretera. ¿Cooperan con ellos o intentan pasar desapercibidos?",
                "Cooperar con los soldados",
                "Pasar desapercibidos",
            ),
        ],
        "Honduras": [
            (
                "Unos asaltantes los rodean y les piden dinero. ¿Intentan negociar o huyen corriendo?",
                "Negociar",
                "Huir",
            ),
            (
                "La policía los detiene para revisar. ¿Sobornan a los oficiales o intentan explicar su situación?",
                "Sobornar a los oficiales",
                "Explicar la situación",
            ),
        ],
        "Guatemala": [
            (
                "Al cruzar la frontera, hay problemas con los papeles falsos. ¿Sobornan a la autoridad o buscan una ruta alternativa?",
                "Sobornar a la autoridad",
                "Buscar otra ruta",
            ),
            (
                "El grupo está agotado. ¿Descansan y pierden tiempo o siguen adelante para llegar a tiempo a la siguiente parada?",
                "Descansar",
                "Seguir adelante",
            ),
        ],
        "México": [
            (
                "En Chiapas, un grupo de hombres armados les exige dinero. ¿Negocian con ellos o intentan escapar?",
                "Negociar",
                "Escapar",
            ),
            (
                "Al cruzar el desierto hacia San Luis Río Colorado, se están quedando sin agua. ¿Deciden buscar un oasis o racionar lo que queda?",
                "Buscar un oasis",
                "Racionar el agua",
            ),
            (
                "En el estado de Veracruz, encuentran un retén ilegal. ¿Pagan el peaje o intentan tomar un camino alternativo?",
                "Pagar el peaje",
                "Tomar un camino alternativo",
            ),
            (
                "En Sinaloa, se encuentran con un grupo sospechoso que les ofrece 'protección'. ¿Aceptan la oferta o la rechazan?",
                "Aceptar la protección",
                "Rechazar la oferta",
            ),
            (
                "Cerca de Sonora, la policía local los detiene y exige un soborno. ¿Pagan o intentan convencerlos de que los dejen ir?",
                "Pagar el soborno",
                "Intentar convencer a la policía",
            ),
        ],
    }
    challenge_text, option_a, option_b = random.choice(location_challenges[location])
    print(f"\nDesafío en {location}: {challenge_text}")
    print(f" 1. {option_a}")
    print(f" 2. {option_b}")
    decision = input("Elige (1 para opción A / 2 para opción B): ")
    if decision == "1":
        outcome = random.choice(["success", "fail"])
        if outcome == "success":
            print(
                f"\n¡Buena decisión! {option_a} funcionó bien. Ganaste algo de moral y perdiste un poco de energía y dinero."
            )
            player.update_status(-10, -50, 5)
        else:
            print(
                f"\nLa situación no salió como esperaban... {option_a} tuvo consecuencias negativas. Perdiste energía, dinero y algo de moral."
            )
            player.update_status(-30, -100, -10)
    elif decision == "2":
        outcome = random.choice(["success", "fail"])
        if outcome == "success":
            print(
                f"\nLa decisión alternativa de {option_b} funcionó, aunque perdieron algo de moral. Ganaste algo de energía, pero no ganaste dinero."
            )
            player.update_status(-15, 0, -5)
        else:
            print(
                f"\nLa situación salió mal y {option_b} resultó ser complicado. Perdiste energía, dinero y mucha moral."
            )
            player.update_status(-20, -100, -20)
    else:
        print("\nDecisión inválida. Perdiste energía por la indecisión.")
        player.update_status(-10, 0, -5)


def main():
    intro()
    num_players = int(input("¿Cuántos jugadores son en el grupo? (1-4): "))
    players = []

    for i in range(num_players):
        name = input(f"Nombre del jugador {i+1}: ")
        players.append(Player(name))

    journey_complete = False
    locations = [
        "Colombia",
        "Panamá",
        "Costa Rica",
        "Nicaragua",
        "Honduras",
        "Guatemala",
        "México",
    ]
    current_location_index = 0

    while not journey_complete:
        for player in players:
            if player.is_alive():
                player.status()
                challenge(player, locations[current_location_index])
                if not player.is_alive():
                    print(f"\n{player.name} no pudo continuar el viaje...")
            else:
                print(f"\n{player.name} ya no está en condiciones de seguir adelante.")

        alive_players = [player for player in players if player.is_alive()]
        if not alive_players:
            print("\nEl grupo no pudo completar el viaje. Fin del juego.")
            journey_complete = True
        else:
            if current_location_index < len(locations) - 1:
                cont = input("¿Quieren seguir el viaje? (s/n): ")
                if cont.lower() != "s":
                    print(
                        "\nDecidieron abandonar el viaje. ¡Esperamos que hayan disfrutado la aventura!\n"
                    )
                    journey_complete = True
                else:
                    for player in players:
                        player.update_status(
                            10, -50, 5
                        )  # Recuperan algo de energía, pero el dinero disminuye
                    current_location_index += 1
                    print(f"\nAvanzan hacia {locations[current_location_index]}...\n")
            else:
                print(
                    "\n¡Felicidades! Han llegado a San Luis, Arizona. ¡Han completado el viaje con éxito!\n"
                )
                journey_complete = True


if __name__ == "__main__":
    main()
