def calcularMinutos()
    dias_al_agno = 365
    horas_al_dia = 24

    horas_al_agno = dias_al_agno * horas_al_dia

    minutos_al_agno = horas_al_agno * 60

    return minutos_al_agno
end

print "Hay " + (calcularMinutos).to_s + " minutos al año"