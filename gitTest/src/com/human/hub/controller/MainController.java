package com.human.hub.controller;

import java.io.IOException;
import javax.servlet.*;
import javax.servlet.annotation.*;
import javax.servlet.http.*;

@WebServlet("/main.ghub")
public class MainController extends HttpServlet {
	public void service(HttpServletRequest req, HttpServletResponse resp) 
						throws ServletException, IOException{
		RequestDispatcher rd = req.getRequestDispatcher("/WEB-INF/views/main.jsp");
		rd.forward(req, resp);
	}

}
