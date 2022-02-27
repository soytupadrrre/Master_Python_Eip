require 'open-uri'
# Mostrar el contenido de una web
URI.open("http://www.ruby-lang.org/en") {|f|
    f.each_line {|line| p line}
}
