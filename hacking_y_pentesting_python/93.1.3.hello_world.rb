def saludo(palabra)
    puts palabra
end

def displaystring(*args)
   args.each{|string|puts string}
end

def multiply(val1, val2)
    result = val1 * val2
    return result
end

# Permite crear un duplicado de una función
alias docalc multiply

# rangos
# Rango de 1 a 10 inclusive
(1..10).to_a
#Rango de 1 a 9
(1...10).to_a

# Rango tambien de letras
('a'..'i').to_a
words = 'cab'..'car'

# words.min
# words.max

# Contiene can?
words.include?('can')

words.reject {|subrange| subrange < 'cal'} # Rechaza valores por debajo de cierto valor

#words.each {|word| puts "Hello " + word} # Recorrer lista 


=begin
# Bucle condicional, cuando se introduce start o end aparece el mensaje triggered

while input = gets
    puts input + " triggered" if input =~ /start/ .. input =~ /end/
end
=end

# Comprobar si algo está dentro de un rango
(1..20) === 15


#Arrays
dias_semana = Array["Lun", 11, "Mart", 12, "Mier"]
dias_semana.slice (1..3)


print ("192.168.001.001".."192.168.001.010").to_a


