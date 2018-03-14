#!/usr/bin/python3
import pandas

from graphviz import Digraph

# unix.py - http://www.graphviz.org/content/unix
# http://graphviz.readthedocs.io/en/stable/examples.html
u1 = Digraph('procesos', filename='procesos.gv')
u1.attr(size='126,6')
u1.node_attr.update(color='lightblue2', style='filled')

u2 = Digraph('incumbencias', filename='incumbencias.gv')
u2.attr(size='26,6')
u2.node_attr.update(color='lightblue2', style='filled')

u3 = Digraph('resumen', filename='resumen.gv')
u3.attr(size='26,6')
u3.node_attr.update(color='lightblue2', style='filled')

in_df = pandas.read_csv('incumbencias.csv', sep = ',')

incumbencia = ''
proceso = ''
for index, row in in_df.iterrows():
    #print(row['INCUMBENCIA'], row['DEPENDENCIAS'])
    if type(row['INCUMBENCIA']) is str:
        incumbencia = row['INCUMBENCIA']
    if type(row['PROCESOS']) is str:
        proceso = row['PROCESOS']

    #print('DEPENDENCIAS', row['DEPENDENCIAS'])
    dependencias = row['DEPENDENCIAS']
    #print(type(dependencias))
    if type(dependencias) is float:
        continue
    dependencias = dependencias.split(' / ')
    firstTime = True
    for dependencia in dependencias:
        print('dependencia: ', dependencia, '; incumbencia: ', incumbencia, '; proceso: ', proceso)
        u1.edge(dependencia, proceso)
        u2.edge(dependencia, incumbencia)

        u3.edge(dependencia, proceso)
        ## se puede evitar qué se repita
        if firstTime:
            u3.edge(proceso, incumbencia)
            firstTime = False


u1.render()
u2.render()
u3.render()
