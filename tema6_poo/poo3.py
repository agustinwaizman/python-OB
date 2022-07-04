class Categorias:
    idcategoria = 0
    nombre = ""

class Proveedores:
    idproveedor = 0
    nombre = ""

class Productos:
    idproducto = 0
    categoriaproducto = Categorias()
    precio = 0
    tamaño = 0
    tipodeproducto = 0
    CIFProveedor = Proveedores()

p = Productos()
p.CIFProveedor.nombre
p.categoriaproducto.idcategoria