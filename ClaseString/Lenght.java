package ClaseString;

public class Lenght {
    public static void main(String[] args) {
        String nombre = "Mariano";
        System.out.println("Mi nombre es: " + nombre);
        System.out.println("Mi nombre tiene " + nombre.length() + " letras ");
        System.out.println("la primera letra de " + nombre + " es la " + nombre.charAt(0));

        int ultima_letra;
        ultima_letra = nombre.length();
        System.out.println("La última letra de " + nombre + " es la " + nombre.charAt(ultima_letra-1));
        // decimos nombre.charAt(ultima_letra-1) porque chartAt te da el índice de la cadena, por eso le restamos 1
        //indice 0=M, 1=a, 2=r, 3=i, 4=a, 5=n, 6=o, dado que la longitud es de 7 contando el 0.
        /*
        Mi nombre es: Mariano
        Mi nombre tiene 7 letras
        la primera letra de Mariano es la M
        La última letra de Mariano es la o
         */
    }
}
