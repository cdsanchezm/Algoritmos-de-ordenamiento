def ordenamientoPorSeleccion(unaLista):
   for llenarRanura in range(len(unaLista)-1,0,-1):
       posicionDelMayor=0
       for ubicacion in range(1,llenarRanura+1):
           if unaLista[ubicacion]>unaLista[posicionDelMayor]:
               posicionDelMayor = ubicacion

       temp = unaLista[llenarRanura]
       unaLista[llenarRanura] = unaLista[posicionDelMayor]
       unaLista[posicionDelMayor] = temp
