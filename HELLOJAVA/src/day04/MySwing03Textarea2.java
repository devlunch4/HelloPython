package day04;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextArea;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import javax.swing.JTextField;
import javax.swing.SwingConstants;

public class MySwing03Textarea2 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing03Textarea2 frame = new MySwing03Textarea2();
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
	public MySwing03Textarea2() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 220, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);

		JTextArea ta1 = new JTextArea();
		ta1.setText("Text Area");
		ta1.setBounds(12, 10, 180, 23);
		contentPane.add(ta1);

		tf = new JTextField();
		tf.setHorizontalAlignment(SwingConstants.RIGHT);
		tf.setBounds(12, 43, 180, 21);
		contentPane.add(tf);
		tf.setColumns(10);

		JButton b1 = new JButton("1");
		b1.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {

				String str_old = tf.getText();
				String str_new = ((JButton) e.getSource()).getText();
				System.out.println(str_old + str_new);
				tf.setText(str_old + str_new);

			}
		});
		b1.setBounds(12, 80, 50, 23);
		contentPane.add(b1);

		JButton b2 = new JButton("2");
		b2.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String str_old = tf.getText();
				String str_new = ((JButton) e.getSource()).getText();
				System.out.println(str_old + str_new);
				tf.setText(str_old + str_new);
			}
		});
		b2.setBounds(76, 80, 50, 23);
		contentPane.add(b2);

		JButton b3 = new JButton("3");
		b3.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String str_old = tf.getText();
				String str_new = ((JButton) e.getSource()).getText();
				System.out.println(str_old + str_new);
				tf.setText(str_old + str_new);
			}
		});
		b3.setBounds(142, 80, 50, 23);
		contentPane.add(b3);

		JButton b4 = new JButton("4");
		b4.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String str_old = tf.getText();
				String str_new = ((JButton) e.getSource()).getText();
				System.out.println(str_old + str_new);
				tf.setText(str_old + str_new);
			}
		});
		b4.setBounds(12, 113, 50, 23);
		contentPane.add(b4);

		JButton b5 = new JButton("5");
		b5.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String str_old = tf.getText();
				String str_new = ((JButton) e.getSource()).getText();
				System.out.println(str_old + str_new);
				tf.setText(str_old + str_new);
			}
		});
		b5.setBounds(76, 113, 50, 23);
		contentPane.add(b5);

		JButton b6 = new JButton("6");
		b6.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String str_old = tf.getText();
				String str_new = ((JButton) e.getSource()).getText();
				System.out.println(str_old + str_new);
				tf.setText(str_old + str_new);
			}
		});
		b6.setBounds(142, 113, 50, 23);
		contentPane.add(b6);

		JButton b7 = new JButton("7");
		b7.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String str_old = tf.getText();
				String str_new = ((JButton) e.getSource()).getText();
				System.out.println(str_old + str_new);
				tf.setText(str_old + str_new);
			}
		});
		b7.setBounds(12, 146, 50, 23);
		contentPane.add(b7);

		JButton b8 = new JButton("8");
		b8.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String str_old = tf.getText();
				String str_new = ((JButton) e.getSource()).getText();
				System.out.println(str_old + str_new);
				tf.setText(str_old + str_new);
			}
		});
		b8.setBounds(76, 146, 50, 23);
		contentPane.add(b8);

		JButton b9 = new JButton("9");
		b9.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String str_old = tf.getText();
				String str_new = ((JButton) e.getSource()).getText();
				System.out.println(str_old + str_new);
				tf.setText(str_old + str_new);
			}
		});
		b9.setBounds(142, 146, 50, 23);
		contentPane.add(b9);

		JButton b0 = new JButton("0");
		b0.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String str_old = tf.getText();
				String str_new = ((JButton) e.getSource()).getText();
				System.out.println(str_old + str_new);
				tf.setText(str_old + str_new);
			}
		});
		b0.setBounds(12, 179, 50, 23);
		contentPane.add(b0);

		JButton bc = new JButton("Call");
		bc.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String str_old = tf.getText();
				String str_new = ((JButton) e.getSource()).getText();
				String calltxt = str_old + str_new + " -call(전화중)";
				System.out.println(str_old + str_new);

				tf.setText(calltxt);

				JOptionPane.showMessageDialog(null, calltxt);
				tf.setText("");
			}
		});
		bc.setBounds(76, 179, 115, 23);
		contentPane.add(bc);

		JButton breset = new JButton("Reset");
		breset.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				tf.setText("");
			}
		});
		breset.setBounds(12, 212, 180, 23);
		contentPane.add(breset);

	}

}
