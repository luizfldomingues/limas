SELECT products.id, products.product_name, products.price, product_types.product_type
FROM products
INNER JOIN product_types ON products.product_type_id=product_types.id;
