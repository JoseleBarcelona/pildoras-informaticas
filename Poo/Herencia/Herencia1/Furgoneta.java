package Poo.Herencia.Herencia1;


public class Furgoneta extends Coche1 {
    //Clase hija
    private int capacidad_carga;
    private int plazas_extra;
    public Furgoneta(int plazas_extra, int capacidad_carga) { //Constructor

        //inicializamos las variables (Damos un estado inicial)

        super(); //con la palabra súper, llamamos al constructor de la clase padre e inicializamos sus variables en esta clase hija
        this.capacidad_carga = capacidad_carga;
        this.plazas_extra = plazas_extra;

    }
    public String dimeDatosFurgoneta() { //Getter

        return "la capacidad de carga es: " + this.capacidad_carga + " y las plazas son: " + this.plazas_extra;
    }
}
