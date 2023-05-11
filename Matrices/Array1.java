package Matrices;

public class Array1 {
    public static void main(String[] args) {
        int[] array = new int[5];
        int[] array2 = {5, 98, 57, -87, -32};

        array[0] = 15;
        array[1] = 22;
        array[2] = -17;
        array[3] = 100;
        array[4] = -5;
        
        for (int i = 0; i < array.length; i++){
            System.out.println("En en índice " + i + " El valor del array es " + array[i]);
        }
        System.out.println(" ");
        for (int i = 0; i < array2.length; i++){
            System.out.println("En en índice " + i + " El valor del array es " + array[i]);

        }
    }
}
