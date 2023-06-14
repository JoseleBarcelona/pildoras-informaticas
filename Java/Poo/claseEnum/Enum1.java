package Poo.claseEnum;
/*La clase enum se utiliza en el caso de que necesitemos aseguraros de almacenar en una variable, una serie de determinados valores.
Por ejemplo para definir diversas tallas de ropa:
talla pequeña, talla mediana, talla grande. Si alguien en la variable pusiera por ejemplo talla azul, la clase enum la descartaría.
Siempre se declara en una clase, pero fuera de la clase main.*/

public class Enum1 {

    enum Talla {mini, mediana, grande, extra_grande} //Así se declara.
    public static void main(String[] args) {
        /*Se llama con el nombre de la clase variable al ser enum un método static
        Un método static no permite poner Talla s = new Talla(); */

        Talla s = Talla.mini;
        Talla l = Talla.mediana;
        Talla x = Talla.grande;
        Talla xl = Talla.extra_grande;

        System.out.println("La talla s es la " + s + "\nLa talla l es la " + l + "\nLa talla x es la "
                + x + "\nLa talla xl es la " + xl);
    }
}
