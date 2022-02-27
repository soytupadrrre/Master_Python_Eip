require 'openssl'

# Generación de claves públicas y privadas
key = OpenSSL::PKey::RSA.new 2048

open 'private_key.pem', 'w' do |io| io.write key.to_pem end
open 'public_key.pem', 'w' do |io| io.write key.public_key.to_pem end