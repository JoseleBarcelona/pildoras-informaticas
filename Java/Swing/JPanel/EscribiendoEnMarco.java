package Swing.JPanel;

import javax.swing.*;
import java.awt.*;

public class EscribiendoEnMarco {
    public static void main(String[] args) {

        MarcoConTexto miMarco = new MarcoConTexto(); //Instanciamos la clase que contiene el marco para inicializar sus métodos
        miMarco.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

    }
}
class MarcoConTexto extends JFrame {

    public MarcoConTexto() {

        setVisible(true);
        setSize(600, 450);
        setLocation(400, 200);
        setTitle("Primer Texto");
        Lamina miLamina = new Lamina(); //Instanciamos la clase Lamina para poner un panel sobre el marco y escribir sobre ella.
        add(miLamina); //Agregamos el panel sobre el marco.
    }
}
class Lamina extends JPanel{

    public void paintComponent(Graphics g) { //Este método permite escribir, colorear y poner gráficos sobre el panel

        super.paintComponent(g); //super llama al constructor de paintComponent, para aplicar sus métodos.
        g.drawString("Estamos aprendiendo Swing", 100, 100);
    }
}