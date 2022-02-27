def getRanges(array)
    # Conversion de los arrays de Integers en arrays de Integers en IPs válidas para la lectura
    cont = 0
    ip = ''
    array.each do |value|
        if value < 100
            # Es necesario incluir los 2 ceros delante del número ya que de lo contrario el bucle es eterno
            value = "00"+(value).to_s
        else
            value = (value).to_s
        end

        # Contador para incluir los "." de las IP
        if cont < 3
            ip += value+ "."
        else
            ip += value
        end
        cont += 1
    end
    return ip
end

def func(ip)

    first = 1
    last = 254

    ip = ip.gsub("\n", "")
    numeros = ip.split(".")
    arrayNum = Array.new
    numeros.each {|numero| arrayNum.push(Integer(numero))}
    
    arrayLess = Array.new
    arrayHigh = Array.new

    finalArray = Array.new
    finalArray.push(arrayNum)
    cont = 0

    # Creación de arrays con el valor mínimo, X.X.X.1 y el máximo X.X.X.254
    while cont < 3
        if cont == 1
            contador = 1
            arrayNum.each do |value|
                if contador == 4
                    arrayLess.push(001)
                else
                    arrayLess.push(value)
                end
                contador += 1
            end
        elsif cont == 2
            contador = 1
            arrayNum.each do |value|
                if contador == 4
                    arrayHigh.push(254)
                else
                    arrayHigh.push(value)
                end
                contador += 1
            end
        end
        cont += 1
    end
    
    cont = 0
    # Obtención de String IPs
    low = getRanges(arrayLess)
    high = getRanges(arrayHigh)

    # Es importante que los 3 números de la IP estén rellenos
    # los formatos del tipo 192.168.1.1 generan rangos muy grandes.
    range = (low..high).to_a

    range.each do |value|
        puts "IP ["+ String(range.index(value) + 1)+"] -> " + value
    end
end


print "Indique la IP\n"
func(gets)