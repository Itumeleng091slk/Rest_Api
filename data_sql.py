import psycopg2

connection = psycopg2.connect(database="data_sql",user="user",password="pass", host="localhost",port=5432)
cursor = connection.cursor()

query = """INSERT INTO Computers(computer_name,hard_drive,processor,ram_amount,maximum_ram,hard_drive_space,form_factor) 
VALUES
('Dell','Dell 500GB 7,200 RPM SATA 2.5in Hard Drive','Intel Core i9 processor',8,8,'512GB','18.3 cm (mini)'),
('LG','HDD','Intell Pentium II 350Hz',60,512,'2000GB','63.5 cm(max)'),
('Acer','Solid State Drive (SSD)','Intel i5','4','64','30GB','SFF(small form factor)')"""

cursor.execute(query)
connection.commit()