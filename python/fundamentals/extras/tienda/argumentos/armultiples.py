def varargs(arg1, *args):
    print("Tengo ", arg1, " and ", args)
varargs("uno") 			# salida: Tengo uno y ()
varargs("uno", "dos") 	# salida: Tengo uno y ('dos',)
varargs("uno", "dos", "tres") # salida: Tengo uno y ('dos', 'tres' )

