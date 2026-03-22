import hashlib


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha_hash = self._gerar_hash(senha)

    def _gerar_hash(self, senha):
        return hashlib.sha256(senha.encode()).hexdigest()

    def validar_senha(self, senha):
        return self.senha_hash == self._gerar_hash(senha)

    def to_dict(self):
        return {
            "nome": self.nome,
            "email": self.email
        }


class GerenciadorUsuarios:
    def __init__(self):
        self.usuarios = []

    def cadastrar_usuario(self, nome, email, senha):
        if self.buscar_usuario_por_email(email):
            raise ValueError("Email já cadastrado.")

        usuario = Usuario(nome, email, senha)
        self.usuarios.append(usuario)

    def buscar_usuario_por_email(self, email):
        for usuario in self.usuarios:
            if usuario.email == email:
                return usuario
        return None

    def fazer_login(self, email, senha):
        usuario = self.buscar_usuario_por_email(email)
        if usuario and usuario.validar_senha(senha):
            return True
        return False

    def listar_usuarios(self):
        return [usuario.to_dict() for usuario in self.usuarios]
