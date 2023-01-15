from Enzyme import Enzyme

# Seulement en µmol pour le substrat et µmol/L/min pour Vi pour le moment

enzyme = Enzyme([0.1, 2, 20, 40, 60, 100, 200],[0.27, 5, 40, 64, 80, 100, 120])

enzyme.graphe()