# gem install launchy
require 'launchy'

def primera(url)
    Launchy.open(url)
end

def segunda(url)
    url = "http://stackoverflow.com"
    Launchy.open(url)
end

url = gets
primera(url)
segunda(url)