package ClaseMath;

public class MathPotencia {
    public static void main(String[] args) {
        double base = 5;
        double exponente = 3;
        int resultado = (int) Math.pow(base, exponente); //hacemos un cast si nos interesa guadarlo en una variable entera
        double resultado1 = Math.pow(base, exponente); //lo guardamos en un double ya que es lo que pide el método si no necesitamos recibir un entero
        System.out.println("5 elevado a 3 es: " + resultado + "\n" + "5 elevado a 3 es: " + resultado1);
    }
}
/*
5 elevado a 3 es: 125
5 elevado a 3 es: 125.0
 */