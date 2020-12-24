package day04;

import java.awt.EventQueue;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.border.EmptyBorder;

public class MySwing01Textarea extends JFrame {

	private JPanel contentPane;
	private JTextField tf;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing01Textarea frame = new MySwing01Textarea();
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
	public MySwing01Textarea() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);

		JTextArea ta = new JTextArea();
		ta.setBounds(12, 10, 130, 241);
		contentPane.add(ta);

		tf = new JTextField();
		tf.setBounds(154, 12, 116, 21);
		contentPane.add(tf);
		tf.setColumns(10);

		JButton btn = new JButton("전송");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String inputtxt = tf.getText();
				if (ta.getText().equals("")) {
					ta.setText(inputtxt);
				} else {
					ta.setText(ta.getText() + "\n" + inputtxt);
				}
				tf.setText("");

			}
		});
		btn.setBounds(173, 43, 97, 23);
		contentPane.add(btn);
	}
}
