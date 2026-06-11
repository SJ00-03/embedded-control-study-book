# C Lab 01. 포인터와 메모리 기초

## 1. 실습 목표

이 실습은 `book/02_c/01_memory_pointer_basics.md`와 연결됩니다. Linux cloud 환경에서 GCC와 Makefile만으로 포인터의 기본 동작을 확인합니다.

- 포인터로 원본 변수를 수정합니다.
- 배열 시작 주소와 길이를 함수에 전달합니다.
- 입력 전용 포인터에 `const`를 사용합니다.
- 출력 포인터와 오류 코드를 함께 사용하는 방식을 연습합니다.

## 2. 선행 지식

- C 함수 호출
- `int`, 배열, `size_t`
- `printf` 기본 사용법
- 터미널에서 `make` 실행하기

## 3. 파일 구성

```text
labs/c/01_pointer_memory_lab/
├─ README.md
├─ main.c
├─ Makefile
└─ expected_output.txt
```

## 4. 빌드/실행 방법

```bash
make -C labs/c/01_pointer_memory_lab
make -C labs/c/01_pointer_memory_lab run
```

정리하려면 다음을 실행합니다.

```bash
make -C labs/c/01_pointer_memory_lab clean
```

## 5. 예상 출력 또는 검증 방법

실행 결과는 `expected_output.txt`와 같아야 합니다.

```bash
make -C labs/c/01_pointer_memory_lab run > /tmp/pointer_lab_output.txt
diff -u labs/c/01_pointer_memory_lab/expected_output.txt /tmp/pointer_lab_output.txt
```

## 6. 디버깅 포인트

- `average_i32`에 배열 길이 `count`를 잘못 넘기면 평균이 달라집니다.
- `out_avg`가 `NULL`이면 결과를 저장할 수 없으므로 함수가 실패해야 합니다.
- 배열 범위를 넘어 읽는 코드는 운 좋게 동작하는 것처럼 보여도 올바른 C 코드가 아닙니다.
- `-Wall -Wextra -Wpedantic` 경고를 무시하지 마세요.

## 7. 확장 과제

1. 평균뿐 아니라 최솟값과 최댓값을 계산하는 함수를 추가하세요.
2. 샘플 배열을 `int16_t`로 바꾸고 overflow 가능성을 검토하세요.
3. 잘못된 입력에 대한 테스트 케이스를 2개 더 추가하세요.
4. `Makefile`에 AddressSanitizer 빌드 타깃을 추가해 보세요.

## 8. 포트폴리오 연결 아이디어

이 lab을 확장해 “센서 샘플 통계 모듈”로 만들 수 있습니다. README에 함수 인터페이스, 방어 코드, 빌드 명령, 예상 출력, 향후 STM32 ADC 버퍼와 연결할 계획을 정리하면 임베디드 C 기본기를 보여 주는 작은 포트폴리오가 됩니다.
