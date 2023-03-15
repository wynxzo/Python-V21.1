x = 12
if x > 50:
    	print("mayor que 50")
else:
	print("menor que 50")
    # ya que x es menor que 50, la segunda sentencia print es la única que se ejecutará.
    
x = 55
if x > 10:
    	print("mayor que 10")
elif x > 50:
    	print("mayor que 50")
else:
    	print("menor que 10")
    # aunque x es mayor que 10 y 50, la primera sentencia verdadera es la única que se ejecutará, por lo que solo veremos 'mayor que 10'
    
if x < 10:
    	print("menor que 10")
    # no pasa nada, porque la sentencia es falsa