package Matrices;

public class Array4 {
    public static void main(String[] args) {
        int[] array_Aleatoria = new int[150];

        for (int i =0; i < array_Aleatoria.length; i++){
            array_Aleatoria[i] = (int)Math.round(Math.random() * 100);
        }
        for (int numeros : array_Aleatoria){
            System.out.print(numeros + " ");
        }
    }
}
