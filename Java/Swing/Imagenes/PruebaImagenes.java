package Swing.Imagenes;

import javax.imageio.ImageIO;
import javax.swing.*;
import java.awt.*;
import java.io.File;
import java.io.IOException;

public class PruebaImagenes {
    public static void main(String[] args) {

        MarcoImagen miImagen = new MarcoImagen();
        miImagen.setVisible(true);
    }
}
class MarcoImagen extends JFrame {
    public MarcoImagen() {

      setBounds(100, 100, 500, 500);
      setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      setTitle("EL CONEJO DE LA LOLE");

      LaminaConImagen miLamina = new LaminaConImagen();
      add(miLamina);
    }

    }
    class LaminaConImagen extends JPanel {

    public void paintComponent(Graphics g) {

        super.paintComponent(g);

        File miImagen = new File ("src/Swing/Imagenes/Mazinger.jpg");

        try {
            imagen = ImageIO.read(miImagen);
        } catch (IOException e) {
            System.out.println("La imagen no se encuentra");
        }
        g.drawImage(imagen, 5, 5, null);
    }
    private Image imagen;
    }

