package Swing.Layouts;

import javax.swing.*;
import java.awt.*;

public class ClassBorderLayout3 {
    public static void main(String[] args) {
        MarcoLayout3 marco = new MarcoLayout3();
        marco.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
class MarcoLayout3 extends JFrame {
    public MarcoLayout3() {
        setVisible(true);
        setBounds(600, 350, 600, 300);
        setTitle("Prueba Layouts");

        PanelLayout3 lamina = new PanelLayout3();
        PanelLayout4 lamina2 = new PanelLayout4();
        add(lamina, BorderLayout.NORTH);
        add(lamina2, BorderLayout.SOUTH);

    }
}
class PanelLayout3 extends JPanel {
    public PanelLayout3() {

        setLayout(new FlowLayout(FlowLayout.LEFT));
        add(new JButton("Amarillo"));
        add(new JButton("Azul"));

    }
}
class PanelLayout4 extends JPanel {
    public PanelLayout4() {
        setLayout(new BorderLayout());
        add(new JButton("Rojo"), BorderLayout.WEST);
        add(new JButton("Verde"), BorderLayout.EAST);
        add(new JButton("Negro"), BorderLayout.CENTER);
    }
}

