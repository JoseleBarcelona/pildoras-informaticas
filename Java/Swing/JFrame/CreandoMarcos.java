package Swing.JFrame;

import javax.swing.*;

public class CreandoMarcos {
    public static void main(String[] args) {

        miMarco marco1 = new miMarco();
        marco1.setVisible(true);
        marco1.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
class miMarco extends JFrame{ //Heredo de JFrame para poder usar todos sus métodos, tanto propios como sus heredados.

    public miMarco(){ //Constructor

        setBounds(500, 300, 400, 400); //Es una suma de setSize y setLocation
        setTitle("MAZINGER Z");

        //setSize(500, 300); //Método de heredado de JFrame que establece el tamaño de la ventana.
        //setLocation(500, 300);
        //setResizable(false); //Evitamos que se pueda redimensionar.
        //setExtendedState(Frame.MAXIMIZED_BOTH);//Amplia la ventana al tamaño de la pantalla.

    }
}
