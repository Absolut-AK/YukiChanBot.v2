from .data_base import DataBase
d = DataBase()

#user table
d.dataRequest('''CREATE TABLE IF NOT EXISTS users(
    id INTEGER, 
    coin INTEGER,
    exp INTEGER,
    class TEXT,
    casino_pass BIT,
    UNIQUE(id))
    ''')
#inventory table
d.dataRequest('''CREATE TABLE IF NOT EXISTS inventory(
            id INTEGER,
            name TEXT,
            ammount INTEGER,
            UNIQUE(id))
            ''')
#user stats
d.dataRequest('''CREATE TABLE IF NOT EXISTS stats(
            id INTEGER,
            name TEXT,
            power INTEGER,
            attack INTEGER,
            speed INTEGER,
            agility INTEGER,
            critchance INTEGER,
            critdamage INTEGER,
            burn INTEGER,
            shock INTEGER,
            poison INTEGER,
            freeze INTEGER,
            abilityslot1 TEXT,
            abilityslot2 TEXT,
            abilityslot3 TEXT,
            abilityslot4 TEXT,
            abilityslot5 TEXT,
            passiveSlot1 TEXT,
            passiveSlot2 TEXT,
            passiveSlot3 TEXT,
            passiveSlot4 TEXT,
            passiveSlot5 TEXT,
            passiveSlot6 TEXT,
            UNIQUE(id))
            ''')

#equipments
d.dataRequest('''CREATE TABLE IF NOT EXISTS weapon(
            id INTEGER,
            name TEXT,
            power INTEGER,
            attack INTEGER,
            speed INTEGER,
            agility INTEGER,
            critchance INTEGER,
            critdamage INTEGER,
            UNIQUE(id))
            ''')

d.dataRequest('''CREATE TABLE IF NOT EXISTS helmet(
            id INTEGER,
            name TEXT,
            power INTEGER,
            attack INTEGER,
            speed INTEGER,
            agility INTEGER,
            critchance INTEGER,
            critdamage INTEGER,
            UNIQUE(id))
            ''')

d.dataRequest('''CREATE TABLE IF NOT EXISTS chest(
            id INTEGER,
            name TEXT,
            power INTEGER,
            attack INTEGER,
            speed INTEGER,
            agility INTEGER,
            critchance INTEGER,
            critdamage INTEGER,
            UNIQUE(id))
            ''')

d.dataRequest('''CREATE TABLE IF NOT EXISTS pants(
            id INTEGER,
            name TEXT,
            power INTEGER,
            attack INTEGER,
            speed INTEGER,
            agility INTEGER,
            critchance INTEGER,
            critdamage INTEGER,
            UNIQUE(id))
            ''')

d.dataRequest('''CREATE TABLE IF NOT EXISTS boots(
            id INTEGER,
            name TEXT,
            power INTEGER,
            attack INTEGER,
            speed INTEGER,
            agility INTEGER,
            critchance INTEGER,
            critdamage INTEGER,
            UNIQUE(id))
            ''')

d.dataRequest('''CREATE TABLE IF NOT EXISTS redGem(
            id INTEGER,
            power INTEGER,
            attack INTEGER,
            critchance INTEGER,
            critdamage INTEGER,
            UNIQUE(id))
            ''')

d.dataRequest('''CREATE TABLE IF NOT EXISTS blueGem(
            id INTEGER,
            mana INTEGER,
            stamina INTEGER,
            UNIQUE(id))
            ''')

d.dataRequest('''CREATE TABLE IF NOT EXISTS greenGem(
            id INTEGER,
            agility INTEGER,
            endurance INTEGER,
            UNIQUE(id))
            ''')

#enemys
d.dataRequest('''CREATE TABLE IF NOT EXISTS enemy1(
            id INTEGER,
            name TEXT,
            power INTEGER,
            attack INTEGER,
            speed INTEGER,
            agility INTEGER,
            critchance INTEGER,
            critdamage INTEGER,
            abilityslot1 TEXT,
            abilityslot2 TEXT,
            abilityslot3 TEXT,
            abilityslot4 TEXT,
            abilityslot5 TEXT,
            passiveSlot1 TEXT,
            passiveSlot2 TEXT,
            passiveSlot3 TEXT,
            passiveSlot4 TEXT,
            passiveSlot5 TEXT,
            passiveSlot6 TEXT,
            UNIQUE(id))
            ''')

d.dataRequest('''CREATE TABLE IF NOT EXISTS enemy2(
            id INTEGER,
            name TEXT,
            power INTEGER,
            attack INTEGER,
            speed INTEGER,
            agility INTEGER,
            critchance INTEGER,
            critdamage INTEGER,
            abilityslot1 TEXT,
            abilityslot2 TEXT,
            abilityslot3 TEXT,
            abilityslot4 TEXT,
            abilityslot5 TEXT,
            passiveSlot1 TEXT,
            passiveSlot2 TEXT,
            passiveSlot3 TEXT,
            passiveSlot4 TEXT,
            passiveSlot5 TEXT,
            passiveSlot6 TEXT,
            UNIQUE(id))
            ''')

d.dataRequest('''CREATE TABLE IF NOT EXISTS enemy3(
            id INTEGER,
            name TEXT,
            power INTEGER,
            attack INTEGER,
            speed INTEGER,
            agility INTEGER,
            critchance INTEGER,
            critdamage INTEGER,
            abilityslot1 TEXT,
            abilityslot2 TEXT,
            abilityslot3 TEXT,
            abilityslot4 TEXT,
            abilityslot5 TEXT,
            passiveSlot1 TEXT,
            passiveSlot2 TEXT,
            passiveSlot3 TEXT,
            passiveSlot4 TEXT,
            passiveSlot5 TEXT,
            passiveSlot6 TEXT,
            UNIQUE(id))
            ''')

d.dataRequest('''CREATE TABLE IF NOT EXISTS enemy4(
            id INTEGER,
            name TEXT,
            power INTEGER,
            attack INTEGER,
            speed INTEGER,
            agility INTEGER,
            critchance INTEGER,
            critdamage INTEGER,
            abilityslot1 TEXT,
            abilityslot2 TEXT,
            abilityslot3 TEXT,
            abilityslot4 TEXT,
            abilityslot5 TEXT,
            passiveSlot1 TEXT,
            passiveSlot2 TEXT,
            passiveSlot3 TEXT,
            passiveSlot4 TEXT,
            passiveSlot5 TEXT,
            passiveSlot6 TEXT,
            UNIQUE(id))
            ''')

d.dataRequest('''CREATE TABLE IF NOT EXISTS enemy5(
            id INTEGER,
            name TEXT,
            power INTEGER,
            attack INTEGER,
            speed INTEGER,
            agility INTEGER,
            critchance INTEGER,
            critdamage INTEGER,
            abilityslot1 TEXT,
            abilityslot2 TEXT,
            abilityslot3 TEXT,
            abilityslot4 TEXT,
            abilityslot5 TEXT,
            passiveSlot1 TEXT,
            passiveSlot2 TEXT,
            passiveSlot3 TEXT,
            passiveSlot4 TEXT,
            passiveSlot5 TEXT,
            passiveSlot6 TEXT,
            UNIQUE(id))
            ''')

d.dataRequest('''CREATE TABLE IF NOT EXISTS enemy6(
            id INTEGER,
            name TEXT,
            power INTEGER,
            attack INTEGER,
            speed INTEGER,
            agility INTEGER,
            critchance INTEGER,
            critdamage INTEGER,
            abilityslot1 TEXT,
            abilityslot2 TEXT,
            abilityslot3 TEXT,
            abilityslot4 TEXT,
            abilityslot5 TEXT,
            passiveSlot1 TEXT,
            passiveSlot2 TEXT,
            passiveSlot3 TEXT,
            passiveSlot4 TEXT,
            passiveSlot5 TEXT,
            passiveSlot6 TEXT,
            UNIQUE(id))
            ''')