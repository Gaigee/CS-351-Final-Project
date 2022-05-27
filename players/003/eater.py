# Name: Neil Schneringer
# ID: 004810739
# Project: Assignment #3, Battle Dots
# Description: This dot only looks for food. That's it.

def init():
    return ("🍴")


def run(db_cursor, state):
    rows = db_cursor.execute(
        f"select x,y from main_game_field as gf, owner  where is_flag = FALSE and gf.owner_id = owner.owner_id and owner.name = '{state['NAME']}'")  # get all my dots
    for row in rows.fetchall():  # iterate this loop for each dot

        # FIND FOOD
        offsetX = 0
        offsetY = 0
        bestDistance = 10000000
        meat = db_cursor.execute(
            f"select x,y from main_game_field as gf where gf.owner_id = '0' ")  # get the location of food
        for target in meat.fetchall():  # for each food on the map
            distX = target[0] - row[0]
            distY = target[1] - row[1]
            distance = distX * distX + distY * distY
            if distance < bestDistance:
                bestDistance = distance
                if distX < 0:
                    offsetX = -1
                elif distX > 0:
                    offsetX = 1
                else:
                    offsetX = 0
                if distY < 0:
                    offsetY = -1
                elif distY > 0:
                    offsetY = 1
                else:
                    offsetY = 0
        db_cursor.execute(
            f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + offsetX}, {row[1] + offsetY}, 'MOVE')")

        # END FIND FOOD
