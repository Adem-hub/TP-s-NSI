import mysql.connector

con= mysql.connector.connect(host='127.0.0.1 ',database='videotheque',user='root',password='')
cursor=con.cursor()

request= 'select * from user'
cursor.execute(request)
users=cursor.fetchall()

request2='select * from film '
cursor.execute(request2)
films=cursor.fetchall()

request3='select * from acteur '
cursor.execute(request3)
acteurs=cursor.fetchall()

request4='select * from jouer '
cursor.execute(request4)
jouer=cursor.fetchall()

request5='select * from realisateur '
cursor.execute(request5)
realisateurs=cursor.fetchall()


def exo1():
    a=str(input('votre nom: ' ))
    b=str(input('Votre mail: '))
    for i in range(len(users)):
        if a and b in users[i]:
            return 'tu est dans la BDD !'
    return "tu n'est pas reférencé dans la BDD"

def exo2():
    a=str(input('votre nom: ' ))
    b=str(input('Votre prenom: '))
    c=str(input('Votre mail: '))
    d=str(input('Votre mdp: '))

    sql = "INSERT INTO user (nom,prenom,mail,mdp) VALUES (%s,%s,%s,%s)"
    data_man=(a,b,c,d)
    print(data_man)
    cursor.execute(sql,data_man)
    con.commit()

def exo3():
    var=str(input('donnez une chaine de caractères: '))
    for i in range(len(films)):
        if var in films[i][1]:
            print(films[i][1]+', realisé par: '+nom_real)

def exo4():
    var=str(input('donnez une chaine de caractères: '))
    for i in range(len(films)):
        if var in films[i][1]:
            id_real=films[i][5]
            nom_real=''
            for j in range(len(realisateurs)):
                if id_real in realisateurs[j]:
                    nom_real=realisateurs[j][1]+' '+ realisateurs[j][2]
            print(films[i][1]+', realisé par: '+nom_real)

def exo5():
    var=str(input('donnez une chaine de caractères: '))
    for i in range(len(films)):
        if var in films[i][1]:
            id_real=films[i][5]
            nom_real=''
            for j in range(len(realisateurs)):
                if id_real in realisateurs[j]:
                    nom_real=realisateurs[j][1]+' '+ realisateurs[j][2]
            L=[]
            for k in range(len(jouer)):
                if jouer[k][0]==films[i][0]:
                    L.append(jouer[k][1])
            P=[]
            for m in range(len(L)):
                for n in range(len(acteurs)):
                    if L[m]== acteurs[n][0]:
                        ac=acteurs[n][1]+ ' '+acteurs[n][2]
                        P.append(ac)

            print(films[i][1]+', realisé par: '+nom_real+', avec comme acteurs: '+str(P))


