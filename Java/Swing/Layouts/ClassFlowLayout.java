package Swing.Layouts;

import javax.swing.*;
import java.awt.*;


public class ClassFlowLayout {
    public static void main(String[] args) {
        MarcoLayout marco = new MarcoLayout();
        marco.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
class MarcoLayout extends JFrame {
    public MarcoLayout() {
        setVisible(true);
        setBounds(600, 350, 600, 300);
        setTitle("Prueba Layouts");

        PanelLayout lamina = new PanelLayout();
        add(lamina);

    }
}
class PanelLayout extends JPanel {
    public PanelLayout() {

        setLayout(new FlowLayout(FlowLayout.CENTER, 75, 100)); //Establece la posición de los componmentes en la lámina
        add(new JButton("Amarillo"));
        add(new JButton("Azul"));
        add(new JButton("Rojo"));
    }
}
