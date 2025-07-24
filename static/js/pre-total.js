document.addEventListener('DOMContentLoaded', function () {

  const quantities = document.querySelectorAll('.quantity-input');
  const display_total = document.querySelector('#pre-total');

  function update_total() {
    let total = 0
    console.log(quantities);
    for (quantity of quantities) {
      console.log(quantity)
      total += quantity.value * quantity.dataset.price;
    }
    display_total.innerHTML = formatBRL(total);
  }
  quantities.forEach(quantity => quantity.addEventListener('input', update_total));
});
