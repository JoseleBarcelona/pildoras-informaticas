package Swing.Eventos;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Eventos1 {
    public static void main(String[] args) {
        MarcoBotones mimarco = new MarcoBotones();
        mimarco.setVisible(true);
    }
}
class MarcoBotones extends JFrame{
    public MarcoBotones() {

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setTitle("Botones y Eventos");
        setBounds(700, 300, 500, 300);
        LaminaBotones milamina = new LaminaBotones();
        add(milamina); //Agregamos el panel al marco
    }

}
class LaminaBotones extends JPanel implements ActionListener {

    JButton botonAzul = new JButton("Azul");
    JButton botonAmarillo = new JButton("Amarillo");
    JButton botonRojo = new JButton("Rojo");
    public LaminaBotones() {

        add(botonAzul); //Agregamos el botón al panel
        add(botonAmarillo); //Agregamos el botón al panel
        add(botonRojo); //Agregamos el botón al panel

        botonAzul.addActionListener(this);
        botonAmarillo.addActionListener(this);
        botonRojo.addActionListener(this);
    }

    @Override
    public void actionPerformed(ActionEvent e) {

        Object botonPulsado = e.getSource(); //Este método nos devuelve quién es la fuente (botonAzul, botonAmarillo, botonRojo)

        if (botonPulsado == botonAzul){
            setBackground(Color.BLUE);
        }
        else if (botonPulsado == botonAmarillo){
            setBackground(Color.YELLOW);
        }
        else {
            setBackground(Color.RED);
        }
    }
}