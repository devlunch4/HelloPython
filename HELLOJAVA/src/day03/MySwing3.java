package day03;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing3 extends JFrame {

	private JPanel contentPane;
	private JTextField txtGoodMoring;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing3 frame = new MySwing3();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MySwing3() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		txtGoodMoring = new JTextField();
		txtGoodMoring.setText("Good Moring");
		txtGoodMoring.setBounds(12, 61, 130, 21);
		contentPane.add(txtGoodMoring);
		txtGoodMoring.setColumns(10);
		
		JButton btnNewButton = new JButton("click");
		btnNewButton.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				txtGoodMoring.setText("Good Evening");
			}
		});
		btnNewButton.setBounds(154, 60, 97, 23);
		contentPane.add(btnNewButton);
	}

}
