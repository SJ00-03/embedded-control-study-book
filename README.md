# Embedded Control Study Book

한국어 임베디드 제어 소프트웨어 학습서 생성 프로젝트입니다. Python, C, STM32, ROS 2, MATLAB/Control을 기초부터 실무형 프로젝트까지 단계적으로 학습하도록 구성합니다.

## 대상 독자

- 전기/전자공학 전공 지식을 바탕으로 임베디드 제어 SW 직무를 준비하는 사람
- 로봇 소프트웨어, 모터 제어, 센서 처리, 안전 중요 소프트웨어 개발에 관심 있는 사람
- 한국의 임베디드, 로봇, 방산 관련 SW 직무를 목표로 포트폴리오를 만들고 싶은 사람

## 저장소 운영 방식

이 저장소는 한 번에 전체 책을 생성하지 않습니다. Codex Web을 사용해 한 PR에서 하나의 lesson 또는 하나의 lab을 생성·검토·병합하는 장기 프로젝트로 운영합니다.

- `book/`: 본문 lesson
- `labs/`: 빌드 또는 실행 가능한 실습
- `quizzes/`: 확인 문제 모음
- `solutions/`: 해설 및 예시 답안
- `prompts/`: Codex Web에 사용할 반복 작업 프롬프트
- `scripts/`: 품질 검사 자동화 스크립트
- `progress_state.yml`: 다음에 생성할 콘텐츠 상태

## 학습 트랙

1. Python: 자동화, 데이터 처리, 신호 분석, 테스트 도구
2. C: 메모리 모델, 포인터, 비트 조작, 상태기계, 방어적 코딩
3. STM32: GPIO, 타이머, PWM, ADC, UART, 인터럽트, DMA, RTOS 개념
4. ROS 2: 노드, 토픽, 서비스, 액션, QoS, tf2, launch, lifecycle
5. MATLAB/Control: 시스템 모델링, PID, 상태공간, 이산화, 구현 제약
6. Integrated Projects: PC-임베디드-분석 도구를 연결한 미니 프로젝트

## Lesson 표준 구조

모든 lesson은 다음 12개 절을 포함합니다.

1. 학습 목표
2. 왜 이 개념이 임베디드 제어 SW에서 중요한가
3. 기초 개념
4. 공식 또는 이론의 유도/직관
5. 간단한 예시
6. 실무형 예시
7. 직접 구현 실습
8. 디버깅 포인트
9. 방산/로봇 SW 관점에서의 주의점
10. 확인 문제
11. 심화 과제
12. 포트폴리오 연결 아이디어

## 시작하기

샘플 lesson과 lab을 먼저 확인합니다.

```bash
python3 scripts/check_lesson_quality.py book/02_c/01_memory_pointer_basics.md
cd labs/c/01_pointer_memory_lab && make && ./main
```

## 안전 및 저작권 원칙

- 본문, 예제, 문제는 원본으로 작성합니다.
- 방산 관련 내용은 신뢰성, 안전, 테스트, 문서화, 코딩 표준 수준으로 제한합니다.
- 무기 표적화, 회피, 공격적 알고리즘, 위해 가능 운용 지침은 다루지 않습니다.
