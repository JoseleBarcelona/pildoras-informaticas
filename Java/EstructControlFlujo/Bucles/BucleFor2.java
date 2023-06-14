package EstructControlFlujo.Bucles;

import javax.swing.*;

//EVALÚA SI LA DIRECCIÓN DE E-MAIL ES VÁLIDA O NO
public class BucleFor2 {
    public static void main(String[] args) {
        String  mail = JOptionPane.showInputDialog("Digite su e-mail");
        int arroba = 0;
        boolean punto = false;

       for (int i = 0; i < mail.length(); i++) {
           if (mail.charAt(i) == '@'){
               arroba ++;

           }if (mail.charAt(i) == '.'){
               punto = true;
           }
       }
        if (arroba == 1 && punto == true){
            System.out.println("El e-mail es correcto");
        }
        else {
            System.out.println("El e-mail es incorrecto");
        }

    }
}
