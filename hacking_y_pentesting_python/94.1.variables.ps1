[string]$string1 = "123"
[string]$string2 = "456"

[string]$concat = $string1 + $string2

$concat

If($string2 -like "*$string1*"){
    'Contiene'
}
Else{
    'No contiene'
}
