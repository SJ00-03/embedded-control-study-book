# ROADMAP

이 문서는 임베디드 제어 SW 취업 준비를 위한 전체 커리큘럼입니다. 각 항목은 향후 독립 lesson 또는 lab으로 확장됩니다.

## 00. Orientation

- 학습 환경: Codex Web, GitHub, Linux cloud 중심 워크플로
- 임베디드 제어 SW 직무 지도
- 로봇 SW와 안전 중요 SW의 공통 역량
- 포트폴리오 구성 전략

## 01. Python

1. Python 문법과 실행 모델
2. 리스트, 튜플, 딕셔너리, 집합
3. 함수, 스코프, 모듈
4. 파일 입출력과 CSV/JSON 로그 처리
5. 예외 처리와 로깅
6. NumPy 배열 기초
7. 샘플링 데이터와 신호 통계
8. Matplotlib 기반 플로팅
9. 간단한 필터링과 FFT 직관
10. 시리얼 통신 개념과 로그 포맷 설계
11. pytest 기반 테스트 자동화
12. 임베디드/로봇 개발 보조 도구 만들기
13. Python serial monitor 프로젝트

## 02. C

1. 메모리 모델과 포인터 기초
2. 빌드 과정: 전처리, 컴파일, 어셈블, 링크
3. 배열과 문자열의 메모리 표현
4. 구조체, enum, union
5. 포인터와 const 정확히 읽기
6. static, extern, translation unit
7. volatile과 메모리 접근 의미
8. 비트 조작과 레지스터 스타일 코드
9. 링 버퍼 구현
10. 상태기계 패턴
11. 패킷 파서 설계
12. 고정소수점 연산
13. 방어적 C 코딩
14. 유닛 테스트 스타일 C 예제
15. C ring buffer and packet parser 프로젝트

## 03. STM32

1. MCU와 주변장치 개념: 보드 독립 관점
2. GPIO 입력/출력
3. 타이머와 시간 기준
4. PWM과 듀티비
5. ADC와 센서 샘플링
6. UART 통신
7. I2C와 SPI 개념 비교
8. 인터럽트 설계
9. DMA 개념과 주의점
10. FreeRTOS 태스크, 큐, 타이머 기초
11. 센서 읽기 아키텍처
12. 모터 제어 기초
13. PID 구현 시 고려사항
14. 디버깅 전략: 로그, 핀 토글, 계측
15. STM32 PWM motor controller 프로젝트

## 04. ROS 2

1. ROS 2 계산 그래프와 워크스페이스 개념
2. node와 topic
3. service
4. action
5. parameter
6. launch
7. QoS 정책과 센서 데이터
8. tf2 좌표계 기초
9. URDF 기본 구조
10. lifecycle node
11. sensor message flow
12. embedded controller bridge 개념
13. logging, bagging, debugging
14. ROS 2 velocity command node 프로젝트

## 05. MATLAB / Control

1. 행렬과 벡터 기초
2. 플로팅과 신호 분석
3. 1차 시스템 직관
4. 2차 시스템 직관
5. 전달함수와 블록 다이어그램
6. PID 제어
7. 상태공간 기초
8. 연속시간과 이산시간의 직관
9. 샘플링 시간 선택
10. 포화, 잡음, 양자화
11. DC 모터 모델
12. simulation-to-implementation workflow
13. MATLAB PID simulation 프로젝트

## 06. Integrated Projects

1. Python serial monitor
2. C ring buffer and packet parser
3. STM32 PWM motor controller
4. MATLAB PID simulation
5. ROS 2 velocity command node
6. Full mini project: ROS 2 PC node + STM32 controller + Python logging tool + MATLAB response analysis

## 반복 생성 순서

1. `progress_state.yml`의 `next_lesson`을 확인합니다.
2. `prompts/create_next_lesson.md`를 사용해 lesson을 생성합니다.
3. `scripts/check_lesson_quality.py`로 구조를 검사합니다.
4. 필요한 경우 `prompts/review_lesson.md`로 리뷰합니다.
5. lesson과 연결되는 실습은 `prompts/create_lab.md`로 별도 PR에서 생성합니다.
