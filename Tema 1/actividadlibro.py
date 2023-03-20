def main():
	print ("Convierte medidas inglesas a sistema metrico")
	millas = int(input("Cuantas millas?:"))
	pies = int (input("Y cuantos pies?:"))
	pulgadas = int(input("Y cuantas pulgadas?:"))
	metros = 1609.344 * millas + 0.3048 * pies + 0.0254 * pulgadas
	print ("La longitud es de", metros, "metros")
main()