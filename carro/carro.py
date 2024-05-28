class Carro:
    def __init__(self, request):
        self.request = request
        self.ssesion = request.session
        carro = self.ssesion.get('carro')
        if not carro:
            carro = self.ssesion['carro'] = {}
        else:
            self.carro = carro

    def agregar(self, producto):
        if(str(producto.id) not in self.carro.keys()):
            self.carro[producto.id]={
                'producto_id' : producto.id,
                'nombre' : producto.nombre,
                'precio' : producto.precio,
                'cantidad' : 1,
                'imagen' : producto.imagen.url
            }
        else:
            for key, value in self.carro.items():
                if key==str(producto.id):
                    value['cantidad'] = value['cantidad']+1
                    break
        self.guardar_carro()

    def guardar_carro(self):
        self.ssesion['carro'] = self.carro
        self.ssesion.modified=True

    def eliminar(self, producto):
        producto.id=str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()

    def restar_producto(self, producto):
        for key, value in self.carro.items():
            if key == str(producto.id):
                value['cantidad'] = value['cantidad']-1
                if value['cantidad'] < 1:
                    self.eliminar(producto)
                break
        self.guardar_carro()

    def limpiar_carro(self):
        self.ssesion['carro']={}
        self.ssesion.modified=True