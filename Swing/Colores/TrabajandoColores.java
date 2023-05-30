package Swing.Colores;

import javax.swing.*;
import java.awt.*;
import java.awt.geom.Ellipse2D;
import java.awt.geom.Rectangle2D;

public class TrabajandoColores {
    public static void main(String[] args) {
        MarcoConColores miMarco = new MarcoConColores();
        miMarco.setVisible(true);
        miMarco.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

    }
}
class MarcoConColores extends JFrame{
    public MarcoConColores() {
        setTitle("Prueba con colores");
        setSize(400, 400);
        LaminaConColor miLamina = new LaminaConColor();
        add(miLamina);
        miLamina.setBackground(Color.PINK);
        //miLamina.setBackground(SystemColor.window); //Te da el color de la interfaz por defecto del sistema operativo windows

    }
}
class LaminaConColor extends JPanel{
    public void paintComponent(Graphics g){

        super.paintComponent(g);
        Graphics2D g2d = (Graphics2D) g;

        //Dibujamos rectángulo
        Rectangle2D rectangulo = new Rectangle2D.Double(100, 100, 200, 150);

        g2d.setPaint(Color.BLACK);//Color del trazo perimetral del rectángulo
        g2d.draw(rectangulo);
        g2d.setPaint(Color.RED); //Constante estática de clase RED
        g2d.fill(rectangulo); //fill rellena el color de una figura

        //Dibujamos una elipse
        Ellipse2D ellipse = new Ellipse2D.Double();
        ellipse.setFrame(rectangulo);


        //Color miColor = new Color(155, 155, 255); //Otra manera de instanciar un color fuera del método
        //g2d.setColor(miColor);


        //g2d.setPaint(Color.BLUE); //Establecemos el color con una constante estática
        g2d.setPaint(new Color(155, 155, 255).darker()); //Establecemos el color con un constructor RGB
        //g2d.setPaint(new Color(155, 255, 255).brighter()); //Establecemos el color con un constructor RGB

        g2d.fill(ellipse);
    }
}
