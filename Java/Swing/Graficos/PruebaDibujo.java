package Swing.Graficos;

import javax.swing.*;
import java.awt.*;

public class PruebaDibujo {
    public static void main(String[] args) {

        MarcoConDibujo miMarco = new MarcoConDibujo();
        miMarco.setVisible(true);
        miMarco.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
class MarcoConDibujo extends JFrame {
    public MarcoConDibujo() {
        setTitle("Dibujo");
        setSize(400, 400);
        LaminaConFiguras miLamina = new LaminaConFiguras();
        add(miLamina);

    }

}
class LaminaConFiguras extends JPanel {
    public void paintComponent(Graphics g) {

        super.paintComponent(g);
        g.drawRect(50, 50, 200, 200);
        g.drawLine(100, 100, 300, 200);
        g.drawArc(100, 100,100,100,120, 150);
    }
}
