# Review My Answer Prompt

학습자가 작성한 `study_notes/` 답안을 검토하고, `feedback/`에는 피드백을, `solutions/`에는 별도 모범 답안을 생성하세요.

## 입력

- 원본 lesson 경로: `book/<track>/<lesson>.md`
- 내 답안 경로: `study_notes/<track>/<lesson>_my_answer.md`
- 피드백 경로: `feedback/<track>/<lesson>_feedback.md`
- 모범 답안 경로: `solutions/<track>/<lesson>_solution.md`
- 연결된 lab 경로가 있으면 함께 지정합니다.

## 검토 순서

1. `study_notes/` 파일이 실제로 존재하고 학습자가 작성한 내용이 있는지 확인합니다.
2. 답안이 비어 있으면 피드백과 모범 답안을 만들지 말고, 먼저 답안을 작성하라고 안내합니다.
3. 원본 lesson과 lab 요구사항을 기준으로 개념 이해, 구현 정확성, 디버깅 관점, 안전한 코딩 습관을 검토합니다.
4. `feedback/`에는 문항별 강점, 보완점, 다시 풀어볼 질문, 오답노트에 옮길 내용을 작성합니다.
5. `solutions/`에는 학습자가 비교할 수 있는 모범 답안을 작성하되, `book/`에는 절대 넣지 않습니다.
6. 가능하면 lab 빌드/실행 명령을 수행하고 결과를 피드백에 기록합니다.

## 피드백 작성 형식

- 전체 요약
- 문항별 피드백
- 실습 및 실행 결과 검토
- 자주 헷갈린 개념
- 오답노트로 옮길 항목
- 다음 복습 계획

## 주의 사항

- `study_notes/`의 원문은 명시 요청 없이 수정하거나 덮어쓰지 않습니다.
- `feedback/`은 Codex 리뷰 결과, `solutions/`는 모범 답안으로 분리합니다.
- 학습자가 답을 작성하기 전에는 full solution을 생성하지 않습니다.
