document.addEventListener('DOMContentLoaded', function() {
    const productSearch = document.getElementById('product-search');
    const productCatalogBody = document.getElementById('product-catalog-body');
    const currentOrderBody = document.getElementById('current-order-body');
    const totalPriceEl = document.getElementById('total-price');
    const orderForm = document.getElementById('order-form');

    let currentOrder = {};

    // Filter products
    productSearch.addEventListener('input', function() {
        const searchTerm = this.value.toLowerCase();
        const productRows = productCatalogBody.querySelectorAll('.product-row');
        const typeHeaders = productCatalogBody.querySelectorAll('.product-type-header');

        let visibleTypes = new Set();

        productRows.forEach(row => {
            const name = row.dataset.name;
            const type = row.dataset.type;
            const isVisible = name.includes(searchTerm) || type.includes(searchTerm);
            row.style.display = isVisible ? '' : 'none';
            if (isVisible) {
                visibleTypes.add(type);
            }
        });

        typeHeaders.forEach(header => {
            const type = header.querySelector('th').textContent.toLowerCase().trim();
            header.style.display = visibleTypes.has(type) ? '' : 'none';
        });
    });

    // Add product to order
    productCatalogBody.addEventListener('click', function(e) {
        if (e.target.classList.contains('add-product-btn')) {
            const button = e.target;
            const id = button.dataset.id;
            const name = button.dataset.name;
            const price = parseFloat(button.dataset.price);

            if (currentOrder[id]) {
                currentOrder[id].quantity++;
            } else {
                currentOrder[id] = {
                    name: name,
                    price: price,
                    quantity: 1
                };
            }
            renderCurrentOrder();
        }
    });

    // Render the current order table
    function renderCurrentOrder() {
        currentOrderBody.innerHTML = '';
        let totalPrice = 0;

        for (const id in currentOrder) {
            const item = currentOrder[id];
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${item.name}</td>
                <td>${item.price.toFixed(2)}</td>
                <td>
                    <input type="number" class="form-control form-control-sm quantity-input" value="${item.quantity}" min="1" data-id="${id}" style="width: 60px;">
                </td>
                <td>
                    <button class="btn btn-sm btn-danger remove-item-btn" data-id="${id}">&times;</button>
                </td>
            `;
            currentOrderBody.appendChild(row);
            totalPrice += item.price * item.quantity;
        }

        totalPriceEl.textContent = totalPrice.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
    }

    // Update quantity or remove item
    currentOrderBody.addEventListener('change', function(e) {
        if (e.target.classList.contains('quantity-input')) {
            const id = e.target.dataset.id;
            const quantity = parseInt(e.target.value);
            if (quantity > 0) {
                currentOrder[id].quantity = quantity;
            } else {
                delete currentOrder[id];
            }
            renderCurrentOrder();
        }
    });

    currentOrderBody.addEventListener('click', function(e) {
        if (e.target.classList.contains('remove-item-btn')) {
            const id = e.target.dataset.id;
            delete currentOrder[id];
            renderCurrentOrder();
        }
    });

    // Handle form submission
    orderForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const formData = new FormData(this);

        for (const id in currentOrder) {
            formData.append(id, currentOrder[id].quantity);
        }

        fetch(this.action, {
            method: 'POST',
            body: formData
        }).then(response => {
            if (response.ok) {
                window.location.href = response.url;
            } else {
                // Handle error
                console.error('Form submission failed');
            }
        });
    });
});