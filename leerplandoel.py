import sqlite3
import os

db_filename = 'leerplandoelen_db.sqlite3'

def create_db():

    conn = sqlite3.connect(db_filename)
    c = conn.cursor()

    c.execute("CREATE TABLE Competenties(nummer text primary key, omschrijving text)")
    c.execute("CREATE TABLE Deelcompetenties(nummer text primary key, omschrijving text, competentie text)")
    c.execute("CREATE TABLE Leerplandoelen(nummer text primary key, omschrijving text, competentie text, deelcompetentie text)")

    with open('leerplandoelen_text.txt', 'r') as f:
        for line in f:
            if line.startswith('Competentie'):
                dash_pos = line.index('-')
                nummer = line[len('Competentie'):dash_pos].strip()
                omschrijving = line[dash_pos+1:].strip() 
                c.execute('INSERT INTO Competenties VALUES(?,?)', (nummer, omschrijving))           
                #print(f'{nummer} {omschrijving}')
            elif line.startswith('Deelcompetentie'):
                dash_pos = line.index('-')
                nr = line[len('Deelcompetentie'):dash_pos].strip()
                omschr = line[dash_pos+1:].strip() 
                comp,deelcomp = nr.split('.')
                c.execute('INSERT INTO Deelcompetenties VALUES(?,?,?)', (nr, omschr, comp))
                print(f' {nr} {omschr} {deelcomp}')
                
            else:
                if line.strip() == "":
                    pass
                else:
                    dash_post = line.index(' ')
                    n = line[len(''):dash_post].strip()
                    o = line[dash_post+1:].strip()
                    p,d,e = n.split('.')
                    c.execute('INSERT INTO Leerplandoelen VALUES(?,?,?,?)', (n, o, p, d))

    conn.commit()
    c.close()

if __name__ == '__main__':
    if os.path.isfile(db_filename):
        os.remove(db_filename)
    create_db()