def tipo_dato
    int = 5
    float = 23.0
    str = "esto_es_un_string"
    range = (1..4)
    hash = {"nombre" => "German", "edad" => 34}
    array = Array.new(2, "test")

    puts "Integer: Valor de numeros enteros -> Clase: '" + String(int.class) + "', Valor: " + String(int)
    puts "Los integer puedes ser FixNum o Bignum, los Fixnum son aquellos que se representan en una palabra nativa (menos de 1 bit)"
    puts ""
    puts "Float: Valores de números con decimales -> Clase: '" + String(float.class) + "', Valor: " + String(float)
    puts ""
    puts "String: Cadenas de texto -> Clase: '" + String(str.class) + "', Valor: " + str
    puts ""
    puts "Range: Rangos, pueden ser números (del 1 al 10) o de palabras/letras (a,b,c ...), se declaran con 'n..m' o 'n...m' -> Clase: '" + String(range.class) + "', Valor: " + String((range).to_a)
    puts ""
    puts "Hashes: se tratan de una colección de datos asignados a una llave, son parecidos a un JSON o a un diccionario de Python-> Clase: '" + String(hash.class) + "', Valor: " + String(hash)
    puts "Para crear un par clave-valor es necesario utilizar el simbolo '=>', que serían los ':' de los archivos JSON."
    puts ""
    puts "Arrays: Se tratan de objetos que permiten almacenar otros tipos de datos. Som similares a las listas en Python -> Class: '" + String(array.class) + "', Valor: " + String(array)
end


tipo_dato