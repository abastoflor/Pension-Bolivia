var id_productos = [];
var cantidad = [];
var id_cantidades = {};

function agregarProducto(producto_id, producto_nombre, producto_cantidad) {
    let tablaB = document.getElementById('resumen');
    let tr = document.createElement('tr');

    let td_nombre = document.createElement('td');
    td_nombre.innerHTML = producto_nombre;

    let td_cantidad = document.createElement('input');
    td_cantidad.type = 'number';
    td_cantidad.style.width = '80px';
    td_cantidad.setAttribute('class', 'cantidad float-right text-center bg-primary border-0 mt-2');
    td_cantidad.setAttribute('min', 1);
    td_cantidad.value = 1;
    td_cantidad.innerHTML = producto_cantidad;
    tr.appendChild(td_nombre);
    tr.appendChild(td_cantidad);
  
    tablaB.appendChild(tr);
    id_productos.push(producto_id);

}


function limpiarItems() {
    var tabla = document.getElementById('resumen');
    while (tabla.firstChild) {
      tabla.removeChild(tabla.firstChild);
    }
    id_productos = [];
    cantidad = []; 
  }



function postOrden(url, cuenta_id) {
    var canti = document.getElementsByClassName('cantidad');
    var cantidades = [].map.call(canti, function(input){
      return input.value;
    }).join('');
    cantidad = cantidades;
    id_productos.forEach((k, i) => {id_cantidades[k] = cantidad[i]})

    data = {
      'cuenta_id': cuenta_id,
      'id_cantidades':id_cantidades,
    };
    let csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0];
    let form = document.createElement('form');
    form.action = url;
    form.method = "POST";
    let inp = document.createElement('input');
    inp.type = 'hidden';
    inp.name = 'data';
    inp.value = JSON.stringify(data);
    form.appendChild(csrftoken);
    form.appendChild(inp);
  
    document.body.appendChild(form);
    form.submit();
}