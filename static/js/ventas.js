var producto_ids = [];
var precio_total = 0;

function addVenta(producto_id, producto_nombre, producto_precio){
  var tbody = document.getElementById('resumen');
  var tr = document.createElement('tr');

  var td_nombre = document.createElement('td');
  td_nombre.innerHTML = producto_nombre;

  var td_precio = document.createElement('td');
  td_precio.setAttribute('class', 'text-right');
  td_precio.innerHTML = 'Bs. ' + producto_precio;

  precio_total += producto_precio;

  tr.appendChild(td_nombre);
  tr.appendChild(td_precio);

  limpiarTotal();

  tbody.appendChild(tr);
  tbody.append(getTotal());
  producto_ids.push(producto_id);

}

function limpiarProductos() {
  var table = document.getElementById('resumen');
  while (table.firstChild) {
    table.removeChild(table.firstChild);
  }

  producto_ids = [];
  precio_total = 0;

  table.appendChild(getTotal());
}

function limpiarTotal() {
  var total_tr = document.getElementById("total-tr");
  if (total_tr !== null) {
    total_tr.parentNode.removeChild(total_tr);
  }
}

function getTotal(){
  var tr_total = document.createElement('tr');
  tr_total.setAttribute('id', 'total-tr')

  var td_total_display = document.createElement('td');
  td_total_display.setAttribute('class', 'thick-line text-right');
  td_total_display.innerHTML = "<strong>Total en Bolivianos: </strong>";

  var td_precio_total = document.createElement('td');
  td_precio_total.setAttribute('class', 'thick-line text-right');
  td_precio_total.setAttribute('id', 'total')
  td_precio_total.innerHTML = "<strong>" + precio_total + " </strong>";

  tr_total.appendChild(td_total_display);
  tr_total.appendChild(td_precio_total);

  return tr_total;
}


function postOrden(url) {
  data = {
    'producto_ids' : producto_ids,
    'precio_total' : precio_total,
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