import math
an = float(input('Digite o ângulo que você deseja:'))
seno = math.sin(math.radians(an))
print('O ângulo de {} tem o SENO de {:.2f}'.format(an, seno))
tangente = math.tan(math.radians(an))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(an,tangente))
