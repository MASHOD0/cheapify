"""
Queries for the database.
"""
create_tables = """
                CREATE TABLE "Product" (
                "id" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
                "asin" varchar(20),
                "name" varchar(80),
                "link" varchar(100),
                "img_link" varchar(100),
                "website" varchar(80),
                "description" varchar(200),
                "tag" varchar(50),
                "price" int
                );
               
                """

insert_product = """INSERT INTO "Product" (asin, name, link, img_link, website, description, tag, price)
VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', {});"""
fetch_products = 'SELECT * FROM "Product";'
#drop table "Product_search_Mapping"; = 'DROP TABLE "Product_search_Mapping";'