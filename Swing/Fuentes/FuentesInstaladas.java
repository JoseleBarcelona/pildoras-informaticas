package Swing.Fuentes;

import java.awt.*;

public class FuentesInstaladas {
    public static void main(String[] args) {

        String[] nombresDeFuentes = GraphicsEnvironment.getLocalGraphicsEnvironment().getAvailableFontFamilyNames();
        for (String nombredelafuente : nombresDeFuentes) {
            System.out.println(nombredelafuente);

        }
    }
}
