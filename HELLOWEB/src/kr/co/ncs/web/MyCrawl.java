package kr.co.ncs.web;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

@WebServlet("/mycrawl")
public class MyCrawl extends HttpServlet {
	private static final long serialVersionUID = 1L;

	public MyCrawl() {
		super();
	}

	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		response.setContentType("text/html;charset=UTF-8");
		response.setCharacterEncoding("UTF-8");
		
		try {
			HttpSession session = request.getSession();
			String user_name = session.getAttribute("user_name").toString();
			response.getWriter().append("<table><tr><td>안녕</td><td>111-1111-1111</td></tr></table>");
			System.out.println(user_name);

		} catch (Exception e) {
			response.getWriter().append("페이지에 권한이없습니다.");
			response.getWriter().append("you do not have permission");
		}

	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		doGet(request, response);
	}

}
