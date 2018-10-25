from mongoengine import Document, EmbeddedDocument, fields

# Create your fields here.
class Choferes (Document):
    nombre = fields.StringField(max_length=200, blank=False, required=True)
    rut = fields.StringField(max_length=150, blank=False, required=True)

    def __str__(self):
        return self.nombre

class Pasajeros (Document):
    nombre = fields.StringField(max_length=200, blank=False, required=True)
    rut = fields.StringField(max_length=20, blank=False, required=True)

    def __str__(self):
        return self.nombre

class AsientoAsignado (EmbeddedDocument):
    pasajero_id = fields.ReferenceField(Pasajeros, blank=False, required=True, dbref=True)
    numeroAsiento = fields.IntField(blank=False, required=True)

    class Meta:
        abstract = True

class Buses (Document):
    matricula = fields.StringField(max_length=100, blank=False, required=True)
    choferes = fields.ReferenceField(Choferes, blank=False, required=True, dbref=True)
    asientoAsignado = fields.EmbeddedDocumentListField(AsientoAsignado)
    
    def __str__(self):
        return self.id

class Trayectos (Document):
    origen = fields.StringField(max_length=150, blank=False, required=True)
    destino = fields.StringField(max_length=150, blank=False, required=True)
    horario = fields.DateTimeField(blank=False, required=True)
    subida = fields.StringField(max_length=150, blank=False, required=True)
    buses = fields.ReferenceField(Buses, blank=True, required=False, null=True, dbref=True)

    def __str__(self):
        return self.destino