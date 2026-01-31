document.addEventListener('DOMContentLoaded', function (){
  const filterInput = document.getElementById("filter-products-button")
  const tbodies = document.querySelectorAll(".product-type-body");
  const productRows = document.querySelectorAll('.product-row');
 
  function removeAccents(str){
    return str.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
  }

  function filterProducts(){
    const inputValue = removeAccents(this.value.toLowerCase());

    for(row of productRows){
      if(String(removeAccents(row.getAttribute("data-product-name"))).indexOf(inputValue) == -1){
        row.classList.add('d-none');
      } else {
        row.classList.remove('d-none');
      }
    }
  };

  filterInput.addEventListener("input", filterProducts);

})
