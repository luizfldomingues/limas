document.addEventListener('DOMContentLoaded', function (){
  const filterInput = document.getElementById("filter-products-input");
  const clearFiltersButton = document.getElementById("clear-filter-button");
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

  function clearFilters(){
    filterInput.value = '';
    filterProducts.call(filterInput);
  }


  filterInput.addEventListener("input", filterProducts);
  clearFiltersButton.addEventListener("click", clearFilters);

})
