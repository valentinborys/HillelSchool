# CREATE TABLE categories (
#     id SERIAL PRIMARY KEY,
#     categories_name VARCHAR(100),
#     categories_description VARCHAR(150)
# );
#
# CREATE TABLE products (
#     id SERIAL PRIMARY KEY,
#     product_name VARCHAR(100),
#     product_description VARCHAR(150),
#     price INTEGER,
#     category_id INTEGER,
#     FOREIGN KEY (category_id) REFERENCES categories(id)
# );
#
# INSERT INTO products (product_name, product_description, price, category_id) VALUES
# ('Ноутбук', 'Високопродуктивний ноутбук', 1200, 1),
# ('Смартфон', 'Остання модель смартфона', 800, 1),
# ('Стіл', 'Офісний стіл', 150, 2),
# ('Стілець', 'Ергономічний офісний стілець', 100, 2),
# ('Футболка', 'Бавовняна футболка', 20, 3),
# ('Джинси', 'Сині джинси', 40, 3);
#
#
# INSERT INTO categories (categories_name, categories_description) VALUES
# ('Електроніка', 'Пристрої та гаджети'),
# ('Меблі', 'Домашні та офісні меблі'),
# ('Одяг', 'Одяг та аксесуари');
#
# SELECT products.product_name, products.product_description, products.price, categories.categories_name
# from products
# JOIN categories ON products.category_id = categories.id;