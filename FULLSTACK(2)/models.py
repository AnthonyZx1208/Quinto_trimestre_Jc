from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Rol(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False, unique=True)

    #Relación inversa: un rol tiene muchos usuarios
    usuarios = relationship("Usuario", back_populates="rol")

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    telefono = Column(String(20), nullable=False)
    edad = Column(Integer, nullable=False)

    #Llave foránea que referencia la tabla roles
    rol_id = Column(Integer, ForeignKey("roles.id", ondelete="RESTRICT"), nullable=False)

    #Relaciones
    rol = relationship("Rol", back_populates="usuarios")
    matriculas = relationship("Matricula", back_populates="programa")

class Programa(Base):
    __tablename__ = "programas"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    codigo = Column(String(20), nullable=False, unique=True)

    #Relación inversa
    matriculas = relationship("Matricula", back_populates="programa")

class Matricula(Base):
    __tablename__ = "matriculas"
    id = Column(Integer, primary_key=True, index=True)

    #Llaves foraneas
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"), nullable=False)
    programa_id = Column(Integer, ForeignKey("programas.id", ondelete="RESTRICT"), nullable=False)
    fecha_matricula = Column(String(20), nullable=False)

    #Relaciones y back-references
    usuario = relationship("Usuario", back_populates="matriculas")
    programa = relationship("Programa", back_populates="matriculas")
    asistencias = relationship("Asistencia", back_populates="matriculas")

class Asistencia(Base):
    __tablename__ = "asistencias"
    id = Column(Integer, primary_key=True, index=True)

    #Llave foránea hacia matricula
    matricula_id = Column(Integer, ForeignKey("matriculas.id", ondelete="CASCADE"), nullable=False)
    fecha = Column(String(20), nullable=False)
    estado = Column(String(20), nullable=False)

    #Relación
    matricula = relationship("Matricula", back_populates="asistencias")