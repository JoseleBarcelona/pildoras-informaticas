package Swing.Eventos;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;

import static javax.swing.text.StyleConstants.setBackground;

public class PruebaAcciones {
    public static void main(String[] args) {

        MarcoAccion marco = new MarcoAccion();
        marco.setVisible(true);
        marco.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
class MarcoAccion extends JFrame {

    public MarcoAccion() {
        setTitle("Prueba acciones");
        setBounds(600, 350, 600, 300);
        PanelAccion lamina = new PanelAccion();
        add(lamina);
    }
}
class PanelAccion extends JPanel {

    public PanelAccion() {

        AccionColor accionamarillo = new AccionColor("Amarillo", Color.yellow);
        AccionColor accionazul = new AccionColor("Azul", Color.blue);
        AccionColor accionrojo = new AccionColor("Rojo", Color.red);

        add(new JButton(accionamarillo));
        add(new JButton(accionazul));
        add(new JButton(accionrojo));

        InputMap mapaEntrada = getInputMap(JComponent.WHEN_IN_FOCUSED_WINDOW);
        mapaEntrada.put(KeyStroke.getKeyStroke("ctrl A"), "fondoamarillo");
        mapaEntrada.put(KeyStroke.getKeyStroke("ctrl Y"), "fondoamarillo"); //Se pueden aplicar varias combinaciones, para una misma acción
        mapaEntrada.put(KeyStroke.getKeyStroke("ctrl B"), "fondoazul");
        mapaEntrada.put(KeyStroke.getKeyStroke("ctrl R"), "fondorojo");

        ActionMap mapaAccion = getActionMap();

        mapaAccion.put("fondoamarillo", accionamarillo);
        mapaAccion.put("fondoazul", accionazul);
        mapaAccion.put("fondorojo", accionrojo);


    }
    private class AccionColor extends AbstractAction{

        public AccionColor(String nombre, Color colorboton) {
            putValue(Action.NAME, nombre);
            putValue(Action.SHORT_DESCRIPTION, "Poner la lámina de color" + nombre);
            putValue("Color de fondo", colorboton);
        }
        @Override
        public void actionPerformed(ActionEvent e) {

            Color c = (Color) getValue("Color de fondo");
            setBackground(c);
            System.out.println("Nombre: " + getValue(Action.NAME) + "\nDescripción: " + getValue(Action.SHORT_DESCRIPTION));
        }
    }
}
