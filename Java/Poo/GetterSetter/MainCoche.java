package Poo.GetterSetter;

public class MainCoche {
    public static void main(String[] args) {

        Coche Renault = new Coche();
        Renault.setRuedas(8);
        Renault.setAncho(3);
        Renault.setLargo(6);
        Renault.setMotor(1800);
        Renault.setPeso(2200);

        System.out.println("El coche Renault tiene " + Renault.getRuedas() + " ruedas, mide " + Renault.getAncho() + " metros de ancho, " +
                Renault.getLargo() + " metros de largo, tiene un motor de " + Renault.getMotor() + " centímetros cúbicos" +
                " y pesa " + Renault.getPeso() + "kg");
    }
}
