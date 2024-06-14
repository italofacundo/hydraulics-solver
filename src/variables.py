from models.Variable import Variable
from sympy.physics.units import meter, kilogram, second, newton

# Comprimento
za = Variable("zᴀ", "Cota do ponto A", meter)
zb = Variable("zʙ", "Cota do ponto B", meter)
z = Variable("z", "Cota", meter)
delta_h = Variable("ΔH", "Perda de carga entre A e B", meter)
cpa = Variable("CPᴀ", "Cota piezométrica do ponto A", meter)
cpb = Variable("CPʙ", "Cota piezométrica do ponto B", meter)

# Massa

# Tempo

# Velocidade
va = Variable("vᴀ", "Velocidade no ponto A", meter / second)
vb = Variable("vʙ", "Velocidade no ponto B", meter / second)
v = Variable("v", "Velocidade", meter / second)

# Pressão
pa = Variable("pᴀ", "Pressão interna no ponto A", newton / meter**2)
pb = Variable("pʙ", "Pressão interna no ponto B", newton / meter**2)
p = Variable("p", "Pressão interna", newton / meter**2)

# Peso Específico
gama = Variable("γ", "Peso específico", newton / meter**3)

# Aceleração
g = Variable("g", "Gravidade", meter / second**2)
