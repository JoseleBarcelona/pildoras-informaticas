package ClaseString;

public class SubstringEquals {
    public static void main(String[] args) {
        String frase = "Hoy es un día estupendo para aprender a programar en Java";
        String frase_resumen = frase.substring(29, 57) + " e irnos a la playa";
        System.out.println(frase);
        System.out.println(frase_resumen);

        String alumno1, alumno2;
        alumno1 = "David";
        alumno2 = "david";
        System.out.println(alumno1.equals(alumno2)); //Java es case sensitive, distingue entre mayúsculas y minúsculas
        System.out.println(alumno1.equalsIgnoreCase(alumno2)); //Ignorecase da la instrucción de que no distinga entre mayúsculas y minúsculas.

        /*
        Hoy es un día estupendo para aprender a programar en Java
        aprender a programar en Java e irnos a la playa
        false
        true
         */

    }


}
