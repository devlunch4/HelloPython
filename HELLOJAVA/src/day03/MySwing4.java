package day03;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing4 extends JFrame {

	private JPanel contentPane;
	private JTextField tf1;
	private JTextField tf2;
	private JTextField tf3;
	private JLabel lbl;
	private JButton btn;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing4 frame = new MySwing4();
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
	public MySwing4() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);

		tf1 = new JTextField();
		tf1.setBounds(12, 40, 60, 21);
		contentPane.add(tf1);
		tf1.setColumns(10);

		tf2 = new JTextField();
		tf2.setColumns(10);
		tf2.setBounds(84, 40, 60, 21);
		contentPane.add(tf2);

		tf3 = new JTextField();
		tf3.setColumns(10);
		tf3.setBounds(265, 40, 60, 21);
		contentPane.add(tf3);

		lbl = new JLabel("+");
		lbl.setBounds(74, 43, 15, 15);
		contentPane.add(lbl);

		btn = new JButton("=");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				int a = Integer.parseInt(tf1.getText());
				int b = Integer.parseInt(tf2.getText());
				int c = a + b;

				tf3.setText(Integer.toString(c));
			}
		});
		btn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		btn.setBounds(156, 39, 97, 23);
		contentPane.add(btn);
	}
}
