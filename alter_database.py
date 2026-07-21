from app import db

def upgrade():
    with db.engine.connect() as connection:
        connection.execute('ALTER TABLE member ADD COLUMN membership_level STRING')
        connection.execute('ALTER TABLE member ADD COLUMN company STRING')
        connection.execute('ALTER TABLE member ADD COLUMN phone_number STRING')
        connection.execute('ALTER TABLE member ADD COLUMN date_joined DATE')
        connection.execute('ALTER TABLE member ADD COLUMN current_balance_due FLOAT')

if __name__ == '__main__':
    upgrade()
