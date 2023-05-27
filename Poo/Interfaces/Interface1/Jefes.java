package Poo.Interfaces.Interface1;

public interface Jefes extends Trabajadores {
    String tomarDecisiones(String decision);

    //Los métodos en una interface se definen, no se declaran.
    //Los métodos de las interfaces son siempre Public Abstract, por lo que Java lo obvia y no hace falta ponerlo

}
