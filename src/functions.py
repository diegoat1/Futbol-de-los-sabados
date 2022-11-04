from pulp import *
import sqlite3
from io import *
import os
from datetime import datetime
import math
from flask import *

### FUNCIÓN QUE AGREGA LOS PERFILES ###

def creadordeperfil(perfil):
    # Base de datos
    basededatos = sqlite3.connect("src/Basededatos")
    cursor = basededatos.cursor()
    try:
        cursor.execute("CREATE TABLE JUGADORES (NOMBRE_APELLIDO VARCHAR(50)")
    except sqlite3.OperationalError:
        pass
    try:
        cursor.execute("INSERT INTO JUGADORES (NOMBRE, PUNTOS, PRESENTE, GOLES) VALUES(?, ?, ?, ?)", perfil)
        basededatos.commit()
        nameuser = perfil[0]
        success_message = 'El usuario {} ha sido creado.'.format(nameuser)
        flash(success_message)
    except sqlite3.IntegrityError:
        nameuser = perfil[0]
        warning_message = 'El usuario {} ya ha sido creado con anterioridad.'.format(nameuser)
        flash(warning_message)
        pass

## FUNCIÓN QUE EDITA LOS PERFILES ESTATICOS ###

def actualizarplayer(datos):
    #Base de datos
    basedatos = sqlite3.connect("src/Basededatos")
    cursor = basedatos.cursor()
    try:
        cursor.execute("UPDATE JUGADORES SET NOMBRE=? WHERE ID=?", (datos[0], datos[1]))
        basedatos.commit()
        nameuser = datos[0]
        success_message = 'El usuario {} ha sido actualizado.'.format(nameuser)
        flash(success_message)
    except sqlite3.IntegrityError:
        nameuser = datos[0]
        warning_message = 'El usuario {} ya ha sido creado con anterioridad.'.format(
            nameuser)
        flash(warning_message)
    
def listadejugadores():
    basededatos=sqlite3.connect("src/Basededatos")
    cursor=basededatos.cursor()
    cursor.execute("SELECT NOMBRE FROM JUGADORES ORDER BY NOMBRE ASC")
    lista=[('','')]
    for i in cursor.fetchall():
        i=[i[0],i[0]]
        lista.append(i)
    return lista

def match(match):
    lista=list(match.data.values())
    basededatos=sqlite3.connect('src/Basededatos')
    cursor=basededatos.cursor()
    for i in range(0,60,3):
        if lista[i]!="":
            cursor.execute("SELECT * FROM JUGADORES WHERE NOMBRE=?", [lista[i]])
            datos=cursor.fetchall()[0]
            puntos=datos[2]+lista[i+1]
            presente=datos[3]+1
            goles=datos[4]+lista[i+2]
            cursor.execute("UPDATE JUGADORES SET PUNTOS=?, PRESENTE=?, GOLES=? WHERE NOMBRE=?", (puntos, presente, goles, datos[1]))
        else:
            pass
        pass
    basededatos.commit()

def team(team):
    lista=list(team.data.values())
    basededatos=sqlite3.connect('src/Basededatos')
    cursor=basededatos.cursor()
    jugadores=[]
    promedios=[]
    presente=[]
    for i in range(0,60,2):
        if lista[i]!="":
            jugadores.append(lista[i])
            cursor.execute("SELECT * FROM JUGADORES WHERE NOMBRE=?", [lista[i]])
            datos=cursor.fetchall()[0]
            try:
                p=datos[2]/datos[3]
            except:
                p=0
            promedios.append(p)
            presente.append(datos[3])
        else:
            pass
        pass

    def reparte2(promedios):
        prom = sorted([(x, i) for i, x in enumerate(promedios)], reverse=True)
        teamA = []
        teamB = []
        sumA = 0
        sumB = 0
        for x, i in prom:
            if sumA > sumB:
                teamB.append(i)
                sumB += x
            else:
                teamA.append(i)
                sumA += x
        return (teamA, sumA), (teamB, sumB)

    def reparte3(promedios):
        prom = sorted([(x, i) for i, x in enumerate(promedios)], reverse=True)
        teamA = []
        teamB = []
        teamC = []
        sumA = 0
        sumB = 0
        sumC = 0
        for x, i in prom:
            if sumA > sumB:
                if sumB > sumC:
                    teamC.append(i)
                    sumC += x
                else:
                    teamB.append(i)
                    sumB += x
            else:
                teamA.append(i)
                sumA += x
        return (teamA, sumA), (teamB, sumB), (teamC, sumC)

    def ordenar(equipo):
        jugadoresquipo=[]
        presenteequipo=[]
        for i in equipo:
            jugadoresquipo.append(jugadores[i])
            presenteequipo.append(presente[i])
        ordn = sorted([(x, i) for i, x in enumerate(presenteequipo)], reverse=True)
        return  jugadoresquipo, ordn

    if len(promedios)>=24:
        teamA, teamB, teamC = reparte3(promedios)
        ordn=ordenar(teamA[0])[1]
        jugadoresquipo=ordenar(teamA[0])[0]
        flash("\nFuerza equipo A: "+str(round(teamA[1])) + " número de jugadores: " + str(len(teamA[0])),"block-title mb-0")
        for i in ordn:
            flash("· " + str(jugadoresquipo[i[1]]), "mb-0 font-w500")
        ordn=ordenar(teamB[0])[1]
        jugadoresquipo=ordenar(teamB[0])[0]
        flash("\nFuerza equipo B: "+str(round(teamB[1])) + " número de jugadores: " + str(len(teamB[0])),"block-title mb-0")
        for i in ordn:
            flash("· " + str(jugadoresquipo[i[1]]), "mb-0 font-w500")
        ordn=ordenar(teamC[0])[1]
        jugadoresquipo=ordenar(teamC[0])[0]
        flash("\nFuerza equipo C: "+str(round(teamC[1])) + " número de jugadores: " + str(len(teamC[0])),"block-title mb-0")
        for i in ordn:
            flash("· " + str(jugadoresquipo[i[1]]), "mb-0 font-w500")
    else:
        teamA, teamB = reparte2(promedios)
        ordn=ordenar(teamA[0])[1]
        jugadoresquipo=ordenar(teamA[0])[0]
        flash("\nFuerza equipo A: "+str(round(teamA[1])) + " número de jugadores: " + str(len(teamA[0])),"block-title mb-0")
        for i in ordn:
            flash("· " + str(jugadoresquipo[i[1]]), "mb-0 font-w500")
        ordn=ordenar(teamB[0])[1]
        jugadoresquipo=ordenar(teamB[0])[0]
        flash("\nFuerza equipo B: "+str(round(teamB[1])) + " número de jugadores: " + str(len(teamA[0])),"block-title mb-0")
        for i in ordn:
            flash("· " + str(jugadoresquipo[i[1]]), "mb-0 font-w500")
    
            # show final objective
    #solver(promedios)