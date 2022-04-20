
# Creación funcion números primos
primos <- function(n){
    # n es el número de primos que se quieren encontrar
    n <- as.integer(n)
    # Si n es menor que 2, devuelve el primo 1
    if(n < 2)
        return(1)
    else
        # Creación de vector/lista inicial de números primos
        primes <- c(2)
        # Recorrer números desde 2 hasta n        
        for(i in 2:n){
            is_prime <- TRUE
            # recorrer los primos anteriores
            for(j in primes){
                # calcular si el número actual es divisible por alguno de los anteriores
                if(i %% j == 0){
                    is_prime <- FALSE
                    break
                }
            }
            # Si el número actual es primo, se añade a la lista de primos
            if(is_prime)
                primes <- c(primes, i)
        }
        # Devolver la lista de primos incluyendo el número 1
        primes <- append(primes, 1, after=0)
        return(primes)
    }
