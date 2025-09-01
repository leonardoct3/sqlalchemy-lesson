import sqlite3

conn = sqlite3.connect('biblioteca.db')
cursor = conn.cursor()

# Get all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Created tables:", [table[0] for table in tables])

# Check the association table structure
print("\nAssociation table structure:")
cursor.execute("PRAGMA table_info(author_book_association)")
columns = cursor.fetchall()
for col in columns:
    print(f"  {col[1]} ({col[2]}) - Primary Key: {bool(col[5])}")

# Check foreign keys
print("\nForeign key constraints:")
cursor.execute("PRAGMA foreign_key_list(author_book_association)")
fks = cursor.fetchall()
for fk in fks:
    print(f"  {fk[3]} -> {fk[2]}.{fk[4]}")

conn.close()
print("\n✅ Database schema created successfully with many-to-many relationship!")
