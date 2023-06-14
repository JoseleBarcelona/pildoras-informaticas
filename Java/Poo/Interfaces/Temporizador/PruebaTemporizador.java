package Poo.Interfaces.Temporizador;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Date;
import javax.swing.*;

public class PruebaTemporizador {
    public static void main(String[] args) {

        DameLaHora oyente = new DameLaHora();
        Timer miTemporizador = new Timer(5000, oyente);
        miTemporizador.start();
        JOptionPane.showMessageDialog(null, "Pulsa ok para detener");
        System.exit(0);

    }
}
class DameLaHora implements ActionListener{

    @Override
    public void actionPerformed(ActionEvent e) {

        Date ahora = new Date();

        System.out.println("Muestro hora cada 5 segundos " + ahora);

        Toolkit.getDefaultToolkit().beep();
    }
}
