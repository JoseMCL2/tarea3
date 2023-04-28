sueldo_base=int,float(input("ingrese sueldo base:"))
comision=int,(input("ingrese comision:"))
venta1=int,float(input("ingrese cantidad de venta 1:"))
venta2=int,float(input("ingrese cantidad de venta 2:"))
venta3=int,float(input("ingrese cantidad de venta 3:"))
total_ventas=venta1+venta2+venta3
comisiones=total_ventas*comision
salario_mensual=sueldo_base+comisiones
print("el salario mensual es:$"+str(salario_mensual))