def func(ip)

    ip = ip.gsub("\n", "")
    numeros = ip.split(".")
    arrayNum = Array.new
    numeros.each {|numero| arrayNum.push(Integer(numero))}
    contador = 1

    finalArray = Array.new
    finalArray.push(arrayNum)
    value4 = arrayNum[0]
    value3 = arrayNum[1]
    value2 = arrayNum[2]
    value1 = arrayNum[3]

    # Bucle para realizar el incremento de las IPs en +10, en caso de llegar a 255 se resetea el valor a 0
    # Se toma como referencia el número más a la derecha hasta la izquierda
    while contador <= 10
        if value1 < 255
            value1 += 1
        else
            value1 = 0
            if value2 < 255
                value2 += 1
            else
                value2 = 0
                if value3 < 255
                    value3 += 1
                else
                    value3 = 0
                    if value4 < 255
                        value4 += 1
                    else
                        value4 = 0
                    end
                end
            end
        end

        finalArray.push([value4, value3, value2, value1])

        contador += 1
    end

    # Impresion bonita por pantalla
    finalArray.each do |ip|
        if finalArray.index(ip) == 0
            print "Tu IP: "
        else
            print "IP [" + String(finalArray.index(ip)) + "]: "   
        
        end
        cont = 0
        ip.each do |value|
            if cont < 3
                print (value).to_s + "."
            else
                print (value).to_s
            end
            cont += 1
        end
        print("\n")
    end

end

printf "Escriba una IP\n"
func(gets)