package Poo.GetterSetter;

public class Coche {
    private int ruedas;
    private int largo;
    private int ancho;
    private int motor;
    private int peso;

    public Coche() { //Método constructor sin parámetros

    }

    public int getRuedas() { //Método getter
        return ruedas;
    }

    public void setRuedas(int ruedas) { //Método setter
        this.ruedas = ruedas;
    }

    public int getLargo() {
        return largo;
    }

    public void setLargo(int largo) {
        this.largo = largo;
    }

    public int getAncho() {
        return ancho;
    }

    public void setAncho(int ancho) {
        this.ancho = ancho;
    }

    public int getMotor() {
        return motor;
    }

    public void setMotor(int motor) {
        this.motor = motor;
    }

    public int getPeso() {
        return peso;
    }

    public void setPeso(int peso) {
        this.peso = peso;
    }
}
