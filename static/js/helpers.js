function formatBRL(price) {
  price = Math.round(price);
  if (price < 0) {
    sign = '-'
  }
  else {
    sign = ''
  }
  price = Math.abs(price);
  return 'R$' + sign + Math.floor(price / 100) + ',' + String(Math.floor(Math.abs(price) % 100)).padStart(2, '0');
}
