import logging

# 로거명 설정
mylogger = logging.getLogger("my")
# 로거 레벨 설정
mylogger.setLevel(logging.DEBUG)

# 포맷 설정 변수
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 정보 출력위치 설정 >> streamHandler는 콘솔에 출력
stream_hander = logging.StreamHandler()
# 출력 포맷 설정
stream_hander.setFormatter(formatter)
# 로거명에 핸들러 적용
mylogger.addHandler(stream_hander)

# 로그 저장될 파일 설정 파일명 설정
file_handler = logging.FileHandler('my.log')
# 로그저장시 포맷 설정
file_handler.setFormatter(formatter)
# 로거명에 파일핸들러 적용
mylogger.addHandler(file_handler)

# 단계에 따른 로거 출력
mylogger.info("I am info")
mylogger.debug("I am debug")
mylogger.warning("I am warning")
mylogger.error("I am error")
mylogger.critical("I am critical")

# 출처: https://hamait.tistory.com/880 [HAMA 블로그]
