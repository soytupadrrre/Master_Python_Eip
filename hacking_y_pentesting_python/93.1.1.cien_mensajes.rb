def mensajes(input)
    
    rango = 1..100

    rango.each {|numero| puts input}

    # metodo .gsub para eliminar caracteres de un string, (Similar al metodo strip() de Python,)
    # acepta expresiones regulares
    print "Numero de palabras "+ input.gsub("\n", "") + ": " + String(rango.size)

end

mensajes(gets)