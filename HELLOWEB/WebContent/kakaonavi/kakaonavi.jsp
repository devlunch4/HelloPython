<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<%-- <script src="<%=request.getContextPath()%>/js/kakao.js"></script> --%>
<script src="//developers.kakao.com/sdk/js/kakao.min.js"></script>
<script
	src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
</head>
<body>



	<a id="navi" href="#" onclick="navi();"> <img
		src="https://developers.kakao.com/assets/img/about/buttons/navi/kakaonavi_btn_medium.png" />
	</a>
	<script type="text/javascript">
	
    // 사용할 앱의 JavaScript 키를 설정
    Kakao.init('71c959dae2a4fb40829db6f796a1f9b6');
    // 카카오 내비 버튼을 생성합니다.
  function navi() {
    Kakao.Navi.start({
      name: '현대백화점 판교점',
      x: 127.11205203011632,
      y: 37.39279717586919,a
      coordType: 'wgs84',
    })
  }
</script>
</body>
</html>