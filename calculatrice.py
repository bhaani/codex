"""Calculatrice simple en ligne de commande."""

from __future__ import annotations


def calculer(a: float, operateur: str, b: float) -> float:
    """Retourne le résultat de l'opération demandée."""
    if operateur == "+":
        return a + b
    if operateur == "-":
        return a - b
    if operateur == "*":
        return a * b
    if operateur == "/":
        if b == 0:
            raise ZeroDivisionError("Division par zéro impossible.")
        return a / b
    raise ValueError(f"Opérateur non pris en charge: {operateur}")


def parser_expression(expression: str) -> tuple[float, str, float]:
    """Parse une expression simple de type 'nombre opérateur nombre'."""
    morceaux = expression.strip().split()
    if len(morceaux) != 3:
        raise ValueError("Format attendu: <nombre> <opérateur> <nombre>")

    gauche, operateur, droite = morceaux
    return float(gauche), operateur, float(droite)


def main() -> None:
    """Point d'entrée de la calculatrice."""
    expression = input("Entrez une expression (ex: 2 + 3) : ")
    a, operateur, b = parser_expression(expression)
    resultat = calculer(a, operateur, b)
    print(f"Résultat : {resultat}")


if __name__ == "__main__":
    main()
