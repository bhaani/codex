# Calculatrice

Cette application propose maintenant **deux interfaces** :
- une interface en ligne de commande (Python)
- une interface web simple (HTML/JS)

## 1) Interface en ligne de commande

```bash
python calculatrice.py
```

Exemple d'entrée :

```text
2 + 3
```

## 2) Interface utilisateur (web)

Depuis la racine du projet, lancez un serveur statique :

```bash
python -m http.server 8000
```

Puis ouvrez :

```text
http://localhost:8000/ui/
```

## Tests Python

```bash
python -m unittest -v
```
