package Swing.Imagenes;

import javax.imageio.ImageIO;
import javax.swing.*;
import java.awt.*;
import java.io.File;
import java.io.IOException;

public class PruebaImagenes2 {
    public static void main(String[] args) {

        MarcoImagen2 miImagen2 = new MarcoImagen2();
        miImagen2.setVisible(true);
    }
}
class MarcoImagen2 extends JFrame {
    public MarcoImagen2() {

      setBounds(100, 100, 850, 900);
      setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      setTitle("NO ME TOQUES LAS PELOTAS");

      LaminaConImagen2 miLamina = new LaminaConImagen2();
      add(miLamina);
    }

    }
    class LaminaConImagen2 extends JPanel {

    public void paintComponent(Graphics g) {

        super.paintComponent(g);

        File miImagen = new File ("src/Swing/Imagenes/pelota.gif");

        try {
            imagen = ImageIO.read(miImagen);
        } catch (IOException e) {
            System.out.println("La imagen no se encuentra");
        }
        int anchuraImagen = imagen.getWidth(this);
        int alturaImagen = imagen.getHeight(this);

        g.drawImage(imagen, 0, 0, null);

        for (int i = 0; i <300; i++) {
            for (int j = 0; j <200; j++) {
                g.copyArea(0, 0, anchuraImagen, alturaImagen, anchuraImagen*i, alturaImagen*j);
            }
        }
        //g.copyArea(0, 0, 200, 200, 300, 300);
    }
    private Image imagen;
    }

