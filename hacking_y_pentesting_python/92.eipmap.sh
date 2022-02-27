#!/bin/bash
dateUTC=$(date -u)

# $1 host, $2 primer puerto, $3 ultimo puerto

echo "EIPmap desarrollado por el estudiante Víctor Luque"
echo "Hora de Ejecución: $dateUTC"
echo "Parametos necesarios: host, primer puerto, ultimo puerto"
echo ""

# Declaración de parametros a integers
declare -i first=$2
declare -i last=$3

# Primera línea del csv resultante
echo "host,port,status;" >> "$1.csv"

# Bucle for de los dos parametros introducidos
for port in $(seq $first $last);
do
    timeout 1 bash -c "</dev/tcp/$1/$port" && resultado="true" || resultado="false"
    if [ $resultado = "true" ]; then
        echo "$1,$port,open;" >> "$1.csv"
    else
        echo "$1,$port,closed;" >> "$1.csv"
    fi
# En caso de error de conexión silenciar el error e indicar el puerto cerrado
done 2>/dev/null && echo "Finished"