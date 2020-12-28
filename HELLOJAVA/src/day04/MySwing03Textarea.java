package day04;

import java.awt.EventQueue;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextArea;
import javax.swing.border.EmptyBorder;

public class MySwing03Textarea extends JFrame {

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private JPanel contentPane;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing03Textarea frame = new MySwing03Textarea();
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
	public MySwing03Textarea() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 220, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);

		JTextArea ta = new JTextArea();
		ta.setBounds(12, 10, 180, 60);
		contentPane.add(ta);

		JButton b1 = new JButton("1");
		b1.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				ta.setText(ta.getText() + 1);
			}
		});
		b1.setBounds(12, 80, 50, 23);
		contentPane.add(b1);

		JButton b2 = new JButton("2");
		b2.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				ta.setText(ta.getText() + 2);
			}
		});
		b2.setBounds(76, 80, 50, 23);
		contentPane.add(b2);

		JButton b3 = new JButton("3");
		b3.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				ta.setText(ta.getText() + 3);
			}
		});
		b3.setBounds(142, 80, 50, 23);
		contentPane.add(b3);

		JButton b4 = new JButton("4");
		b4.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				ta.setText(ta.getText() + 4);
			}
		});
		b4.setBounds(12, 113, 50, 23);
		contentPane.add(b4);

		JButton b5 = new JButton("5");
		b5.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				ta.setText(ta.getText() + 5);
			}
		});
		b5.setBounds(76, 113, 50, 23);
		contentPane.add(b5);

		JButton b6 = new JButton("6");
		b6.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				ta.setText(ta.getText() + 6);
			}
		});
		b6.setBounds(142, 113, 50, 23);
		contentPane.add(b6);

		JButton b7 = new JButton("7");
		b7.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				ta.setText(ta.getText() + 7);
			}
		});
		b7.setBounds(12, 146, 50, 23);
		contentPane.add(b7);

		JButton b8 = new JButton("8");
		b8.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				ta.setText(ta.getText() + 8);
			}
		});
		b8.setBounds(76, 146, 50, 23);
		contentPane.add(b8);

		JButton b9 = new JButton("9");
		b9.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				ta.setText(ta.getText() + 9);
			}
		});
		b9.setBounds(142, 146, 50, 23);
		contentPane.add(b9);

		JButton b0 = new JButton("0");
		b0.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				ta.setText(ta.getText() + 0);
			}
		});
		b0.setBounds(12, 179, 50, 23);
		contentPane.add(b0);

		JButton bc = new JButton("Call");
		bc.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String calltxt  = ta.getText() + " -call(전화중)";
				ta.setText(calltxt);
				JOptionPane.showMessageDialog(null, calltxt);
				ta.setText("");
			}
		});
		bc.setBounds(76, 179, 115, 23);
		contentPane.add(bc);
		
		JButton breset = new JButton("Reset");
		breset.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				ta.setText("");
			}
		});
		breset.setBounds(12, 212, 180, 23);
		contentPane.add(breset);
	}

}
