package Swing.Fuentes;

import javax.swing.*;
import java.awt.*;

public class TrabajandoConFuentes {
    public static void main(String[] args) {

        MarcoConFuentes miMarco = new MarcoConFuentes();
        miMarco.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        miMarco.setVisible(true);
    }
}
class MarcoConFuentes extends JFrame {
    public MarcoConFuentes() {
        setTitle("Prueba con fuentes");
        setSize(400, 400);
        LaminasConFuentes miLamina = new LaminasConFuentes();
        add(miLamina);
        miLamina.setBackground(Color.PINK);
        //miLamina.setForeground(Color.CYAN);
    }
}
class LaminasConFuentes extends JPanel{
    public void paintComponent(Graphics g){

        super.paintComponent(g);
        Graphics2D g2 = (Graphics2D) g; //Refundición o Casting

        Font miFuente = new Font("Monaco", Font.BOLD, 26);
        g2.setFont(miFuente);
        g2.setColor(Color.BLUE);
        g2.drawString("José", 150, 150);

        g2.setFont(new Font("Monaco", Font.BOLD, 26));
        g2.setColor(new Color(128, 45, 54).brighter());
        g2.drawString("Núria", 150, 100);
    }


}