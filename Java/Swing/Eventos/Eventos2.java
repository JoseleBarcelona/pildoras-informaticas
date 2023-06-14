package Swing.Eventos;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import static javax.swing.text.StyleConstants.setBackground;

public class Eventos2 {
    public static void main(String[] args) {
        MarcoBotones2 mimarco = new MarcoBotones2();
        mimarco.setVisible(true);
    }
}
class MarcoBotones2 extends JFrame{
    public MarcoBotones2() {

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setTitle("Botones y Eventos");
        setBounds(700, 300, 500, 300);
        LaminaBotones2 milamina = new LaminaBotones2();
        add(milamina); //Agregamos el panel al marco
    }

}
class LaminaBotones2 extends JPanel {

    JButton botonAzul = new JButton("Azul");
    JButton botonAmarillo = new JButton("Amarillo");
    JButton botonRojo = new JButton("Rojo");
    public LaminaBotones2() {

        add(botonAzul); //Agregamos el botón al panel
        add(botonAmarillo); //Agregamos el botón al panel
        add(botonRojo); //Agregamos el botón al panel

        ColorFondo amarillo = new ColorFondo(Color.YELLOW);
        ColorFondo azul = new ColorFondo(Color.BLUE);
        ColorFondo rojo = new ColorFondo(Color.RED);
        botonAzul.addActionListener(azul);
        botonAmarillo.addActionListener(amarillo);
        botonRojo.addActionListener(rojo);
    }
    private class ColorFondo implements ActionListener{

        public ColorFondo(Color c){
            colorDeFondo = c;
        }
        private Color colorDeFondo;
        @Override
        public void actionPerformed(ActionEvent e) {

            setBackground(colorDeFondo);
        }
    }
}
