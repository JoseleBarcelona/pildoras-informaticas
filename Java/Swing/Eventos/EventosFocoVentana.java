package Swing.Eventos;

import javax.swing.*;
import java.awt.event.WindowEvent;
import java.awt.event.WindowFocusListener;

public class EventosFocoVentana extends JFrame implements WindowFocusListener {

    public static void main(String[] args) {

        EventosFocoVentana miventana = new EventosFocoVentana();
        miventana.iniciar();
    }
    public void iniciar(){

        marco1 = new EventosFocoVentana();
        marco2 = new EventosFocoVentana();
        marco1.setVisible(true);
        marco2.setVisible(true);
        marco1.setBounds(300, 200, 600, 350);
        marco2.setBounds(900, 200, 600, 350);
        marco1.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        marco2.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        marco1.addWindowFocusListener(this);
        marco2.addWindowFocusListener(this);
    }

    @Override
    public void windowGainedFocus(WindowEvent e) {

        if (e.getSource() == marco1) {
            marco1.setTitle("Tengo el foco");
        }else {
            marco2.setTitle("Tengo el foco");
        }
    }

    @Override
    public void windowLostFocus(WindowEvent e) {

        if (e.getSource() == marco1) {
            marco1.setTitle("");
        }else {
            marco2.setTitle("");
        }
    }
    EventosFocoVentana marco1;
    EventosFocoVentana marco2;
}
