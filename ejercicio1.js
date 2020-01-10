function calcularPasaje(distancia, estancia) {
  let precioPasaje = 0;
  let precioKm = 35;
  let precioDescuento = 0;

  if (distancia > 1000 && estancia > 7) {
    precioPasaje = precioKm * distancia;
    precioDescuento = precioPasaje - precioPasaje * 0.3;
    return precioDescuento;
  } else {
    precioPasaje = precioKm * distancia;
    return precioPasaje;
  }
}
console.log(calcularPasaje(1000, 7));
