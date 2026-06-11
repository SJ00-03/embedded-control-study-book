# Create Lab Prompt

지정된 lesson과 연결되는 실습 디렉터리를 `labs/` 아래에 생성하세요.

## 공통 원칙

- README는 한국어로 작성합니다.
- 실습은 클라우드/Linux 환경에서 가능한 한 재현 가능해야 합니다.
- C 실습은 GCC와 Makefile로 빌드 가능하게 구성합니다.
- STM32 실습은 보드 독립 개념, 의사 코드, 인터페이스 설계를 먼저 제시하고 보드별 구현은 선택 사항으로 분리합니다.
- ROS 2 실습은 특정 로봇 플랫폼을 가정하지 않습니다.
- MATLAB 실습은 MATLAB Online 호환성을 우선합니다.

## 권장 lab 구조

```text
labs/<track>/<nn_lab_name>/
├─ README.md
├─ source files
├─ Makefile 또는 실행 스크립트
└─ expected_output.txt 또는 검증 방법
```

## README 필수 내용

1. 실습 목표
2. 선행 지식
3. 파일 구성
4. 빌드/실행 방법
5. 예상 출력 또는 검증 방법
6. 디버깅 포인트
7. 확장 과제
8. 포트폴리오 연결 아이디어

## 완료 조건

1. lab 파일을 생성합니다.
2. 가능한 빌드/실행 검사를 수행합니다.
3. PR 설명에 lesson과 lab의 연결 관계를 적습니다.
