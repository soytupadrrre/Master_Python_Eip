class TestClase
    def initialize
    end

    def elementos
        @elementos = [1,2,3,4,5]
    end

    def addNew(array)
        begin
            return array.insert(0,60)
        rescue
            print "Unable to modify: " + array.to_s
        end
    end
end

ejemplo = TestClase.new()
puts "Actual object: " + ejemplo.inspect.to_s
puts "La clase es: " + ejemplo.class.to_s

array1 = ejemplo.elementos
# to_enum method se usa para no modificar arrays por metodos dentro de clases
ejemplo.addNew(array1.to_enum)

print array1
puts
ejemplo.addNew(array1)
puts "\nArray modificado"
print array1


if ejemplo.object_id == 60
    puts "\nLa clase tiene id: " + ejemplo.object_id.to_s
else
    puts "\nLa clase tiene otro id que no es el esperado: " + ejemplo.object_id.to_s
end
