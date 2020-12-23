package day03;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JLabel;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing5 extends JFrame {

	private JPanel contentPane;
	private JTextField tf1;
	private JTextField tf2;
	private JTextField tf3;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing5 frame = new MySwing5();
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
	public MySwing5() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);

		tf1 = new JTextField();
		tf1.setBounds(12, 43, 80, 21);
		contentPane.add(tf1);
		tf1.setColumns(10);

		tf2 = new JTextField();
		tf2.setBounds(145, 43, 80, 21);
		contentPane.add(tf2);
		tf2.setColumns(10);

		tf3 = new JTextField();
		tf3.setBounds(306, 43, 80, 21);
		contentPane.add(tf3);
		tf3.setColumns(10);

		JLabel lbl1 = new JLabel("\uC5D0\uC11C");
		lbl1.setBounds(104, 46, 57, 15);
		contentPane.add(lbl1);

		JLabel lbl2 = new JLabel("\uAE4C\uC9C0 \uD569\uC740");
		lbl2.setBounds(237, 46, 57, 15);
		contentPane.add(lbl2);

		JButton btnNewButton = new JButton("\uACC4\uC0B0 \uBC84\uD2BC");
		btnNewButton.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				int a = Integer.parseInt(tf1.getText());
				int b = Integer.parseInt(tf2.getText());
				int sum = 0;
				for (int i = a; i < b + 1; i++) {
					sum += i;
				}
				tf3.setText(Integer.toString(sum));
			}
		});
		btnNewButton.setBounds(306, 74, 100, 23);
		contentPane.add(btnNewButton);

	}

}
