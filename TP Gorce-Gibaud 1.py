import mysql.connector

con= mysql.connector.connect(host='127.0.0.1 ',database='France',user='root',password='')
cursor=con.cursor()

req='select * from departement'
cursor.execute(req)

tableau=cursor.fetchall()

req2='select * from  villes_france_free'
cursor.execute(req2)
tableau2=cursor.fetchall()

con.close()


class departement:
    def __init__(self):
        self.id =""
        self.code =""
        self.nom =""
        self.nom_uppercase =""
        self.slug =""
        self.nom_soundex =""
        self.Voisins=[]


    def attribut (self,x):
        self.id = tableau[x][0]
        self.code = tableau[x][1]
        self.nom = tableau[x][2]
        self.nom_uppercase = tableau[x][3]
        self.slug = tableau[x][4]
        self.nom_soundex = tableau[x][5]

    def Oui(self):
        for i in range(len(tableau2)):
            if self.code==L_Villes[i].departement:
                self.Voisins.append(L_Villes[i].nom)



class ville:
    def __init__(self):
        self.id = ""
        self.departement = ""
        self.slug = ""
        self.nom = ""
        self.nom_simple = ""
        self.nom_reel = ""
        self.nom_soundex = ""
        self.nom_metaphone = ""
        self.code_postal = ""
        self.commune = ""
        self.code_commune = ""
        self.arrondissement = ""
        self.canton = ""
        self.amdi = ""
        self.popu2010 = ""
        self.popu1999 = ""
        self.popu2012 = ""
        self.densite2010 = ""
        self.surface = ""
        self.longitude_deg = ""
        self.latitude_deg = ""
        self.longitude_drg = ""
        self.latitude_grd = ""
        self.longitude_dms = ""
        self.latitude_dms = ""
        self.zmin = ""
        self.zmax = ""
        L=[]


    def attribut(self,x):
        self.id = tableau2[x][0]
        self.departement = tableau2[x][1]
        self.slug = tableau2[x][2]
        self.nom = tableau2[x][3]
        self.nom_simple = tableau2[x][4]
        self.nom_reel = tableau2[x][5]
        self.nom_soundex = tableau2[x][6]
        self.nom_metaphone = tableau2[x][7]
        self.code_postal = tableau2[x][8]
        self.commune = tableau2[x][9]
        self.code_commune = tableau2[x][10]
        self.arrondissement = tableau2[x][11]
        self.canton = tableau2[x][12]
        self.amdi = tableau2[x][13]
        self.popu2010 = tableau2[x][14]
        self.popu1999 = tableau2[x][15]
        self.popu2012 = tableau2[x][16]
        self.densite2010 = tableau2[x][17]
        self.surface = tableau2[x][18]
        self.longitude_deg = tableau2[x][19]
        self.latitude_deg = tableau2[x][20]
        self.longitude_drg = tableau2[x][21]
        self.latitude_grd = tableau2[x][22]
        self.longitude_dms = tableau2[x][23]
        self.latitude_dms = tableau2[x][24]
        self.zmin = tableau2[x][25]
        self.zmax = tableau2[x][26]
    def Migration(self,ville,n):
        ville.popu2012+=n
        self.popu2012-=n


L_Villes=[]
for j in range(len(tableau2)):
    var= ville()
    var.attribut(j)
    L_Villes.append(var)


L_Departements=[]
for i in range(len(tableau)):
    var = departement()
    var.attribut(i)
    var.Oui()
    L_Departements.append(var)



