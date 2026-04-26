class Usuario:
    def __init__(self, user_id, username, password, edad, horas): #! CONSTRUCTOR 
        self.id =  user_id
        self.username = username
        self.__password = password
        self.edad = edad
        self._horas =horas
        
        
    def es_mayor_de_edad(self):
        return self.edad >= 18
    
    def es_usuario_intensivo(self):
        return self.horas >= 10

    
    def resumen(self):
        return f"{self.username} tiene {self.horas} horas"
    
    # comentrario para merge
    
    def usuario_admin(self):
        return self.username == "admin"
    
    def get_password_hash(self):
        return self.__password
    
    def mensaje_bienvenido(self):
        if self.usuario_admin():        
            return (f"bienvenido administrador{self.username}")
        else:
            print(f"bienvenido {self.username}")
            
    @property
    def horas(self):
        return self._horas

    @horas.setter
    def horas(self, value):
        if value < 0 or value >168:
            raise ValueError("horas in validas")
        self._horas = value
    
    
    def __str__(self):
        return f"{self.username} |  {self.edad} años | {self.horas} hrs"
    


    
    def __repr__(self):
        return f"Usuario(id={self.id}), username={self.username})"
    
    
    def __len__(self):
        return self.horas


    def __eq__(self, other):
        return isinstance(other, Usuario) and self. username == other.username
    
    
    def __gt__(self, other):
        if not isinstance(other,Usuario):
            return NotImplemented
        return self.horas > other.horas
    
    
    def nivel_actividad(self):
        if self.horas >= 50:
            return "Ultra activo"
        elif self.horas >= 25:
            return "Activo"
        else:
            return "casual"


