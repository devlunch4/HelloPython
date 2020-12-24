package day04;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JLabel;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing02Textarea extends JFrame {

	private JPanel contentPane;
	private JTextField tf;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing02Textarea frame = new MySwing02Textarea();
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
	public MySwing02Textarea() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);

		JTextArea ta = new JTextArea();
		ta.setBounds(12, 10, 180, 241);
		contentPane.add(ta);

		tf = new JTextField();
		tf.setBounds(204, 12, 80, 21);
		contentPane.add(tf);
		tf.setColumns(10);

		JButton btn = new JButton("출력");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {

				// 값 가져오기
				String dan = tf.getText();
				int danx = Integer.parseInt(dan);
				String danprint = "";
				for (int i = 1; i < 10; i++) {
					danprint += danx + " x " + i + " = " + (danx * i) + "\n";
				}

				ta.setText(danprint);

			}
		});
		btn.setBounds(325, 11, 97, 23);
		contentPane.add(btn);

		JLabel lblNewLabel = new JLabel("단");
		lblNewLabel.setBounds(296, 15, 30, 15);
		contentPane.add(lblNewLabel);
	}
}
