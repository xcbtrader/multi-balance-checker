# multi-balance-checker
Comprobar el saldo de  direcciones bitcoin contenidas en fichero de texto utilizando múltiples APIs

El programa permite comprobar el saldo de tantas direcciones bitcoin como tengamos en el fichero de texto que nos pide al iniciar el programa. Para comprobar el saldo se utilizan hasta 14 APIs diferentes, y así evitar ser baneados por el proveedor.

Entre comprobación y comprobación se establece un tiempo de pausa, guardado en la variable pausa, que puede ser modificado.

Hay que tener en cuenta que si un proveedor detecta muchas llamadas a su API en poco tiempo, baneará la IP y ya no se podrá utilizar más durante un cierto tiempo.


EJEMPLO: direcciones.txt

12dfkjgh dfghfhjkdh76ythh......

1hhGGfRgtbnkioUhkjui....

1YYggFfrrHB545hnM08........

El fichero debe contener direcciones bitcoin válidas y una en cada línea (sin espacios en blanco)

Para que el programa funcione se debe tener instalada la libreria requests.

El programa está pensado para python3, no para python 2.7

