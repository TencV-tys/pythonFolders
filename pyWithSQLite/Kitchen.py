import database as db

conn = db.setup()
#db.add_recipes(conn, 'Pasta', 20)
#db.add_recipes(conn,'Pizza',30)

all_recipes = db.get_recipes(conn)

for recipes in all_recipes:
    print(f"#{recipes[0]}: {recipes[1]} - {recipes[2]} mins")
conn.close()