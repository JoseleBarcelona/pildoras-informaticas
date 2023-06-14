package Poo.Interfaces.ClaseInternaLocal;


import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Date;

public class PruebaTemporizador2 {
    public static void main(String[] args) {
        Reloj miReloj = new Reloj();
        miReloj.enMarcha(3000, true);
        JOptionPane.showMessageDialog(null, "Pulsa ok para terminar");
        System.exit(0);

    }
}
class Reloj{

    public void enMarcha(int intervalo, boolean sonido){
        class DameLaHora implements ActionListener{

            @Override
            public void actionPerformed(ActionEvent e) {
                Date ahora = new Date();
                System.out.println("Te pongo la hora cada 3 segundos " + ahora);

                if (sonido){
                    Toolkit.getDefaultToolkit().beep();
                }


            }
        }
        ActionListener oyente = new DameLaHora();
        Timer miTemporizador = new Timer(intervalo, oyente);
        miTemporizador.start();
    }


}
