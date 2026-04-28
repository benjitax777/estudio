{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Vamos a ver el orden cronologico de las siguientes fechas\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Ingrese una fecha (DD/MM/AAAA)  12/01/2880\n",
      "Ingrese otra fecha (DD/MM/AAAA) 12/01/2003\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "la fecha: 2003-01-12 es anterior a : 2880-01-12\n"
     ]
    }
   ],
   "source": [
    "print(\"Vamos a ver el orden cronologico de las siguientes fechas\")\n",
    "from datetime import datetime\n",
    "fecha1 = (input(\"Ingrese una fecha (DD/MM/AAAA) \"))\n",
    "fecha = datetime.strptime(fecha1, \"%d/%m/%Y\").date()\n",
    "fecha2= (input(\"Ingrese otra fecha (DD/MM/AAAA)\"))\n",
    "Fecha2 = datetime.strptime(fecha2, \"%d/%m/%Y\").date()\n",
    "from datetime import date\n",
    "if fecha ==date.today() or Fecha2 == date.today():\n",
    "    fecha_actual =fecha if fecha == date.today() else Fecha2\n",
    "    print(f\"esta es la fecha actual {fecha_actual}\")\n",
    "elif fecha < Fecha2:\n",
    "    print(f\"La fecha : {fecha} es anterior a : {Fecha2}\")\n",
    "elif fecha > Fecha2:\n",
    "    print (f\"la fecha: {Fecha2} es anterior a : {fecha}\")\n",
    "else:\n",
    "    print(\"Las fechas son iguales\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.1+"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
