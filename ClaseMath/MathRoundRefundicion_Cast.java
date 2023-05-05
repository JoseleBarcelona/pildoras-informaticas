package ClaseMath;

public class MathRoundRefundicion_Cast {
    public static void main(String[] args) {
        double num1 = 5.85;
        int resultado = (int) Math.round(num1); //Aquí hemos hecho un cast o refundición
        /*el método Math.round tiene dos métodos:
        round(float a):int .Recibe un float y devuelve un int
        round(double a): long .Recibe un double y devuelve un long
        Lo que se puede hacer es cambiar las variables a lo que el método te pide
        o hacer un cast (refundición) y decirle que lo que se te devuelva, se almacene en una
        variable del tipo indicado, en este caso int resultado = (int) Math.round(num1);
        en un int. La pega es que puedes perder parte de la información, aunque en el caso
        de round no hay problema en que se pierdan los decimales, ya que le pedimos que redondee
        por lo que daría 6 en este caso.
         */
        System.out.println(resultado); // =6
         float num2 = 5.85f; //En este caso se le pasa el tipo de dato que te pide el método a través de la API de java.
         int result = Math.round(num2);
        System.out.println(result); // =6


    }
}
