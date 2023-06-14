package Swing.Graficos;

import javax.swing.*;
import java.awt.*;
import java.awt.geom.Ellipse2D;
import java.awt.geom.Line2D;
import java.awt.geom.Rectangle2D;

public class PruebaDibujo2D {
    public static void main(String[] args) {
        MarcoConDibujo2D mimarco2D = new MarcoConDibujo2D();
        mimarco2D.setVisible(true);
        mimarco2D.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
class MarcoConDibujo2D extends JFrame{
    public MarcoConDibujo2D() {
        setTitle("Dibujo2D");
        setSize(400, 400);
        LaminaConFiguras2D lamina2D = new LaminaConFiguras2D();
        add(lamina2D);

    }
}
class LaminaConFiguras2D extends JPanel{
    public void paintComponent(Graphics g) {
        super.paintComponent(g);

        Graphics2D g2d = (Graphics2D) g; //Hacemos una refundición de la clase Graphics para convertirla en graphics2D usando su objeto g

        Rectangle2D rectangulo = new Rectangle2D.Double(100, 100, 200, 150);
        //Instanciamos las clase Rectangle2D
        //Polimorfismo, llamamos al constructor de Rectangle2D.Double que hereda de Rectangle2D, la cual es abstracta

        g2d.draw(rectangulo); //a draw le pasamos por parámetro el objeto que implemente la interfaz shape, en este caso la clase Rectangle2D

        Ellipse2D ellipse = new Ellipse2D.Double(); //Instanciamos la clase Ellipse2D
        ellipse.setFrame(rectangulo); //le decimos que la elipse está dentro del rectángulo
        //Llamamos a uno de los constructores del método setFrame y le pasamos los parámetros
        g2d.draw(ellipse);

        g2d.draw(new Line2D.Double(100,100,300,250)); //Instanciamos directamente el objeto Line2D

        double centroX = rectangulo.getCenterX();
        double centroY = rectangulo.getCenterY();
        double radio = 125;

        Ellipse2D circulo = new Ellipse2D.Double();
        circulo.setFrameFromCenter(centroX, centroY, centroX+radio, centroY+radio);
        g2d.draw(circulo);

    }
}
