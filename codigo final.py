import sys
def mostrar_encabezado():
    print("=" * 60)
    print("      DIAGRAMA DE FLUJO - GUARDIANES DEL REINO PERDIDO")
    print("=" * 60)
    print("\n[PRESENTACIÓN DEL JUEGO]")
    print("Nombre: Guardianes del Reino Perdido")
    print("\n[DESCRIPCIÓN]")
    print("Es un juego de aventura y acción donde los jugadores exploran,")
    print("enfrentan enemigos, resuelven acertijos y protegen un reino mágico.")
    print("Desbloquean nuevas habilidades, herramientas y personajes.\n")
def mostrar_objetivos():
    print("-" * 50)
    print("OBJETIVOS DEL JUEGO")
    print("-" * 50)
    print("• Explorar todos los escenarios del reino.")
    print("• Derrotar a los enemigos y jefes finales.")
    print("• Completar misiones principales y secundarias.")
    print("• Recolectar monedas, gemas y objetos especiales.")
    print("• Salvar el Reino Perdido y restaurar la paz.")
    input("\nPresiona Enter para continuar...")
def mostrar_herramientas():
    print("-" * 50)
    print("HERRAMIENTAS DISPONIBLES")
    print("-" * 50)
    herramientas = [
        ("Espada Legendaria", "Atacar."),
        ("Escudo Protector", "Reduce daño."),
        ("Arco Mágico", "Ataque a distancia."),
        ("Poción de Vida", "Recupera salud."),
        ("Mapa Encantado", "Muestra caminos ocultos y tesoros."),
        ("Llave Dorada", "Abre puertas secretas y cofres."),
        ("Antorcha", "Ilumina cuevas.")
    ]
    for item, desc in herramientas:
        print(f"• {item}: {desc}")
    input("\nPresiona Enter para continuar...")
def mostrar_personajes():
    print("-" * 50)
    print("PERSONAJES DEL JUEGO")
    print("-" * 50)
    personajes = [
        ("Alex (Héroe)", "Valiente y fuerte. Combate cuerpo a cuerpo."),
        ("Luna (Arquera)", "Muy rápida y precisa. Ataques a distancia."),
        ("Leo (Mago)", "Controla magia elemental (hechizos de fuego, hielo y electricidad)."),
        ("Nara (Sanadora)", "Cura a los compañeros. Aumenta la defensa del equipo."),
        ("Rey Oscuro (Villano)", "Enemigo principal. Gran poder mágico y controla criaturas oscuras.")
    ]
    for nombre, desc in personajes:
        print(f"• {nombre}: {desc}")
    input("\nPresiona Enter para continuar...")
def jugar_niveles():
    print("-" * 50)
    print("PROGRESIÓN DE NIVELES")
    print("-" * 50)
    niveles = [
        {
            "nombre": "Nivel 1: Bosque Encantado",
            "pasos": ["Aprender controles.", "Encontrar la espada inicial.", "Derrotar primeros enemigos."]
        },
        {
            "nombre": "Nivel 2: Cueva Misteriosa",
            "pasos": ["Resolver acertijos.", "Obtener la Llave Dorada.", "Enfrentar al Guardián de la Cueva."]
        },
        {
            "nombre": "Nivel 3: Montaña de Hielo",
            "pasos": ["Superar obstáculos de hielo.", "Conseguir el Escudo Protector.", "Derrotar al Gigante de Hielo."]
        },
        {
            "nombre": "Nivel 4: Castillo Oscuro",
            "pasos": ["Encontrar las gemas mágicas.", "Derrotar al ejército enemigo.", "Llegar al jefe final."]
        },
        {
            "nombre": "Nivel 5: Reino Perdido",
            "pasos": ["Enfrentar al Rey Oscuro.", "Recuperar la Corona de la Luz.", "Salvar el reino y completar el juego."]
        }
    ]
    for lvl in niveles:
        print(f"\n--- {lvl['nombre']} ---")
        for paso in lvl['pasos']:
            print(f" [ ] {paso}")
        opcion = input("\n¿Deseas completar este nivel y avanzar? (s/n): ").strip().lower()
        if opcion != 's':
            print("\nHas decidido pausar la aventura.")
            return False
        print(f"¡{lvl['nombre']} COMPLETADO CON ÉXITO!")
    return True
def mostrar_premios_y_reglas():
    print("-" * 50)
    print("PREMIOS Y RECOMPENSAS")
    print("-" * 50)
    premios = [
        "Monedas de oro.", "Gemas mágicas.", "Nuevas armas y armaduras.",
        "Habilidades especiales.", "Personajes desbloqueables.",
        "Trofeos por completar cada nivel.", "Medalla de Guardián del Reino al finalizar el juego al 100%."
    ]
    for p in premios:
        print(f"• {p}")
    print("\n" + "-" * 50)
    print("REGLAS DEL JUEGO")
    print("-" * 50)
    reglas = [
        "1. No abandonar la partida durante una misión importante.",
        "2. Administrar correctamente la salud y los recursos.",
        "3. Completar los objetivos de cada nivel para avanzar.",
        "4. Trabajar en equipo en modo multijugador.",
        "5. Derrotar al jefe final para completar la aventura."
    ]
    for r in reglas:
        print(f"  {r}")
    input("\nPresiona Enter para continuar...")
def mostrar_conclusion():
    print("-" * 50)
    print("CONCLUSIÓN")
    print("-" * 50)
    print("Guardianes del Reino Perdido ofrece una experiencia de aventura llena de")
    print("exploración, acción y desafíos. Gracias a sus personajes, herramientas,")
    print("niveles y recompensas, los jugadores pueden desarrollar estrategias para")
    print("superar cada reto y disfrutar de una experiencia entretenida.")
    print("\n¡GRACIAS POR JUGAR!")
    print("=" * 60)
def main():
    mostrar_encabezado()
    # Exploración de módulos principales según el diagrama de flujo
    mostrar_objetivos()
    mostrar_herramientas()
    mostrar_personajes()
    # Sección de Niveles
    juego_completado = jugar_niveles()
    # Premios, Reglas y Conclusión
    if juego_completado:
        mostrar_premios_y_reglas()
        mostrar_conclusion()
    else:
        print("\nPuedes reanudar el juego cuando quieras. ¡Hasta la próxima!")
if __name__ == "__main__":
    main()
 