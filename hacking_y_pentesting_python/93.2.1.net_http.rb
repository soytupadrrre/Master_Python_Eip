require 'net/http'
# GET request
puts "GET REQUEST\n\n"

uri = URI('http://example.com/index.html?count=10')
res = Net::HTTP.get_response(uri) # => String
puts res.body

puts "\nPOST REQUEST\n\n"

# POST request
uri = URI('http://www.example.com/search.cgi')
res = Net::HTTP.post_form(uri, 'q' => 'ruby', 'max' => '50')
puts res.body