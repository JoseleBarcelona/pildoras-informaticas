package Swing.JFrame;

import javax.swing.*;
import java.awt.*;

public class CreandoMarcoCentrado {
    public static void main(String[] args) {

        MarcoCentrado miMarco = new MarcoCentrado();
        miMarco.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        miMarco.setVisible(true);
    }
}
class MarcoCentrado extends JFrame{
    public MarcoCentrado() {

        Toolkit miPantalla = Toolkit.getDefaultToolkit();//Guardamos en la variable  miPantalla nuestro sistema nativo de ventana
        Dimension tamañoPantalla = miPantalla.getScreenSize(); //Nos dice el tamaño (Resolución) que tiene nuestra pantalla y la almacenamos en una variable

        int alturaPantalla = tamañoPantalla.height; //Extraemos la altura de la pantalla y la almacenamos en  una variable int
        int anchoPantalla = tamañoPantalla.width;

        setSize(anchoPantalla/2, alturaPantalla/2); //Le damos a la ventana unas dimensiones a la mitad de nuestra pantalla.
        setLocation(anchoPantalla/4, alturaPantalla/4); //El punto x/y lo ponemos a la cuarta parte de mi pantalla
        setTitle("Mazinger Z");

        Image miIcono = miPantalla.getImage("src/Swing/JFrame/Mazinger.jpg"); //Almaceno en la variable miIcono una imagen.
        setIconImage(miIcono);


    }
}
