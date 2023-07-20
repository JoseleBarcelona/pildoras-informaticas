package Swing.Eventos;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class MultiplesOyentes {
    public static void main(String[] args) {
        MarcoPrincipal mimarco = new MarcoPrincipal();
        mimarco.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        mimarco.setVisible(true);
    }
}
class MarcoPrincipal extends JFrame {
    public MarcoPrincipal(){
        setTitle("Prueba Varios");
        setBounds(1300, 100, 300, 200);

        LaminaPrincipal lamina = new LaminaPrincipal();
        add(lamina);
    }
}
class LaminaPrincipal extends JPanel {
    public LaminaPrincipal(){
        JButton botonNuevo = new JButton("Nuevo");
        add(botonNuevo);
        botonCerrar = new JButton("Cerrar todo");
        add(botonCerrar);

        OyenteNuevo miOyente = new OyenteNuevo();
        botonNuevo.addActionListener(miOyente);

    }
    private class OyenteNuevo implements ActionListener {

        @Override
        public void actionPerformed(ActionEvent e) {

            MarcoEmergente marco = new MarcoEmergente(botonCerrar);
            marco.setVisible(true);
        }
    }
    JButton botonCerrar;
}
class MarcoEmergente extends JFrame {
    public MarcoEmergente(JButton botonPrincipal){

        contador ++;
        setTitle("Ventana" + contador);
        setBounds(40 * contador, 40 * contador, 300, 150);

        CierraTodos oyenteCerrar = new CierraTodos();
        botonPrincipal.addActionListener(oyenteCerrar);

    }
    private class CierraTodos implements ActionListener {

        @Override
        public void actionPerformed(ActionEvent e) {

            dispose();
        }
    }
    private static int contador = 0;
}
