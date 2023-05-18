package Poo.Herencia;
/*
Diseño de la herencia. La regla tiene que responder a "Es un"
Furgoneta "Es un..." coche, como no es así, la herencia está mal diseñada aunque nos sirva
para ilustrar el ejemplo. Lo correcto sería haber hecho unas clases de esta manera:

                                         VEHICULO
                                            |
                              ______________|_______________
                              |         |          |        |
                           COCHE    FURGONETA    MOTO    CAMION

                           Furgoneta "Es un..." Vehiculo
 */
public class MainVehiculo {
    public static void main(String[] args) {

        //Simplemente por utilizar el operador new, junto con el nombre del constructor, le estamos dando un estado inicial
        //a los objetos. (obtienen una copia de las variables de los constructores).

        Coche1 micoche1 = new Coche1();
        micoche1.establece_color("Rojo");

        Furgoneta mifurgoneta1 = new Furgoneta(7, 580);

        mifurgoneta1.establece_color("Azul");
        mifurgoneta1.configura_asientos("Si");
        mifurgoneta1.configura_climatizador("Si");

        System.out.println(micoche1.dime_datos_generales() + "\n" + micoche1.dime_color() + "\n");
        System.out.println(mifurgoneta1.dime_datos_generales() + ", " + mifurgoneta1.dimeDatosFurgoneta());

    }
}
/*
La plataforma del vehículo tiene 4 ruedas
Mide 2 metros con un ancho de 300cm
Tiene un peso de plataforma de 500kg
El color del coche es Rojo

La plataforma del vehículo tiene 4 ruedas
Mide 2 metros con un ancho de 300cm
Tiene un peso de plataforma de 500kg, la capacidad de carga es: 580 y las plazas son: 7
 */
