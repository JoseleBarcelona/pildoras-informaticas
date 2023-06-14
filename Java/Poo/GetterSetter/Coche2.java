package Poo.GetterSetter;

public class Coche2 {
    private int ruedas; //Variables globales
    private int largo;
    private int ancho;
    private int motor;
    private int peso_plataforma;
    private int peso_total;
    private String color; //De aquí abajo son atributos diferentes para cada coche
    private boolean asientos_cuero, climatizador;

    public Coche2(){ //CONSTRUCTOR (Declaramos unas variables comunes para todos los coches que creemos)
        ruedas = 4;
        largo = 2000;
        ancho = 300;
        motor = 1600;
        peso_plataforma = 500;
    }
    public String dime_datos_generales(){ //GETTER
        return "La plataforma del vehículo tiene " + ruedas + " ruedas, mide " + largo/1000 +
                " metros con un ancho de " + ancho + "cm y con un peso de plataforma de " + peso_plataforma + "kg";
    }
    public void establece_color(String color_coche){ //SETTER
        color = color_coche; //Iniciamos la variable color y le asignamos un valor pasado por parámetros
    }
    public String dime_color(){ //GETTER
        return "El color del coche es " + color;
    }
    public void configura_asientos(String asientos_cuero){ //SETTER
        if (asientos_cuero.equalsIgnoreCase("si")){ //Las cadenas de caracteres se comparan con el método equals()
            this.asientos_cuero = true;
        }else {
            this.asientos_cuero = false;
        }
    }
    public String dime_asientos(){ //GETTER
        if (asientos_cuero == true){
            return "El coche tiene asientos de cuero";

        }else {
            return "El coche tiene asientos de serie";
        }
    }
    public void configura_climatizador(String climatizador){ //SETTER
        if (climatizador.equalsIgnoreCase("si")){
            this.climatizador = true;
        }else {
            this.climatizador = false;
        }
    }
    public String dime_climatizador(){ //GETTER
        if (climatizador == true){
            return "El coche incorpora climatizador";
        }
        else {
            return "El coche lleva aire acondicionado";
        }
    }
    public String dime_peso(){ //Poner un setter y getter como aquí en un único método, no es recomendable

        int peso_carroceria = 500; //variable local, (Solo se puede instanciar dentro de este método).

        peso_total = peso_carroceria + peso_plataforma;

        if (asientos_cuero == true){
            peso_total = peso_total + 50;
        }
        if (climatizador == true){
            peso_total = peso_total + 20;
        }
        return "El peso total del coche es de " + peso_total + "kg";
    }
    public int dime_precio(){ //GETTER y SETTER juntos
        int precio_final = 10000;
        if (asientos_cuero == true){
            precio_final += 2000;
        }
        if (climatizador == true){
            precio_final += 1500;
        }
        return precio_final;
    }

}
/*
La plataforma del vehículo tiene 4 ruedas, mide 2 metros con un ancho de 300cm y con un peso de plataforma de 500kg
El color del coche es azul
El coche tiene asientos de cuero
El coche incorpora climatizador
El peso total del coche es de 1070kg
El precio total del coche, es de 13500€
 */
