usuario = {"login": "joaosilva"}
senha = usuario.get("senha")
if not(senha):
    usuario["senha"] = 123456

print(usuario)