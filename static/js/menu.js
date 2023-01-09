var tipo_ids = [];


function addMenu(tipo_id, tipo_producto, tipo_nombre) {
    let tablaB = document.getElementById('resumen');
    let tr = document.createElement('tr');

    let td_producto = document.createElement('td');
    td_producto.innerHTML = tipo_producto;

    let td_nombre = document.createElement('td');
    td_nombre.innerHTML = tipo_nombre;
    tr.appendChild(td_producto);
    tr.appendChild(td_nombre);
  
    tablaB.appendChild(tr);
    tipo_ids.push(tipo_id);

}




function limpiarProductos() {
  var table = document.getElementById('resumen');
  while (table.firstChild) {
    table.removeChild(table.firstChild);
  }
  producto_ids = [];
}



function postMenu(url) {
  data = {
    'tipo_ids' : tipo_ids,
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