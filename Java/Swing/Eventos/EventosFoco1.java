package Swing.Eventos;

import javax.swing.*;
import java.awt.*;
import java.awt.event.FocusEvent;
import java.awt.event.FocusListener;

public class EventosFoco1 {
    public static void main(String[] args) {
        MarcoFoco mimarco = new MarcoFoco();
        mimarco.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
class MarcoFoco extends JFrame {
    public MarcoFoco() {
        setVisible(true);
        setBounds(300, 300, 600, 450);
        add(new LaminaFoco());
    }
}
class LaminaFoco extends JPanel {
    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        setLayout(null); //invalidamos el Layout (La colocación por defecto)

        cuadro1 = new JTextField();
        cuadro2 = new JTextField();
        cuadro1.setBounds(120, 10, 150, 20);
        cuadro2.setBounds(120, 50, 150, 20);
        add(cuadro1);
        add(cuadro2);

        LanzaFoco elFoco = new LanzaFoco();
        cuadro1.addFocusListener(elFoco); //Ponemos al objeto cuadro1 a la escucha
    }
    JTextField cuadro1;
    JTextField cuadro2;
   private class LanzaFoco implements FocusListener {  //Clase interna para acceder a los objetos cuadro1 y cuadro2
        @Override
        public void focusGained(FocusEvent e) {

        }

        @Override
        public void focusLost(FocusEvent e) {
            String email = cuadro1.getText();
            boolean comprobacion = false;
            for (int i = 0; i < email.length(); i++) {
                if (email.charAt(i) == '@') {
                    comprobacion = true;
                }

            }
            if(comprobacion){
                System.out.println("El email es correcto");
            }else{
                System.out.println("El email es incorrecto");
            }
        }
    }
}

