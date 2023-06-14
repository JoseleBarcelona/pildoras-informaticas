package Poo.Interfaces.InterfaceclaseInterna;


import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Date;

public class PruebaTemporizador2 {
    public static void main(String[] args) {
        Reloj miReloj = new Reloj(3000, true);
        miReloj.enMarcha();
        JOptionPane.showMessageDialog(null, "Pulsa ok para terminar");
        System.exit(0);

    }
}
class Reloj{

    public Reloj(int intervalo, boolean sonido){
        this.intervalo = intervalo;
        this.sonido = sonido;

    }
    public void enMarcha(){
        ActionListener oyente = new DameLaHora();
        Timer miTemporizador = new Timer(intervalo, oyente);
        miTemporizador.start();
    }
    private int intervalo;
    private boolean sonido;
    private class DameLaHora implements ActionListener{

        @Override
        public void actionPerformed(ActionEvent e) {
            Date ahora = new Date();
            System.out.println("Te pongo la hora cada 3 segundos " + ahora);

            if (sonido){
                Toolkit.getDefaultToolkit().beep();
            }


        }
    }
}
