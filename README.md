# 📚 알고리즘 스터디

LeetCode 75 기반 코딩테스트 스터디 풀이 공유 사이트

## 🔗 사이트
https://seongkyu-lim.github.io/algo-study/

## 🏗 동작 방식

```
┌─────────────────────────┐        ┌─────────────────────────┐
│  leetcode-algorithms    │        │  algo-study (Pages)     │
│  (private, 풀이 데이터)   │        │  (public, 정적 사이트)    │
│                         │        │                         │
│  0001-two-sum/          │  push  │  index.html             │
│    README.md            │ ─────► │  data/solutions.json    │
│    0001-two-sum.kt      │        │  scripts/generate-data  │
│  0283-move-zeroes/      │        │                         │
│    ...                  │        │                         │
└─────────────────────────┘        └─────────────────────────┘
```

### 자동 배포 흐름

1. **`leetcode-algorithms`에 풀이 push**
2. GitHub Actions (`trigger-pages.yml`)가 `algo-study` 레포에 dispatch 이벤트 발송
3. `algo-study`의 Actions (`deploy.yml`)가 실행:
   - `leetcode-algorithms` 레포를 clone (토큰 인증)
   - `scripts/generate-data.py`로 전체 풀이를 파싱 → `data/solutions.json` 생성
   - GitHub Pages로 배포
4. **1~2분 후 사이트에 반영**

> ⚠️ 데이터는 **빌드 시점에 복사**됩니다. leetcode-algorithms를 실시간으로 바라보는 게 아니라, push할 때마다 스냅샷을 떠서 정적 파일(`solutions.json`)로 변환 후 배포합니다.

### 자동 파싱 항목

| 항목 | 소스 |
|------|------|
| 문제 설명 | `{폴더}/README.md` (HTML) |
| 풀이 코드 | `{폴더}/*.kt`, `*.py`, `*.java` 등 |
| 작성자 | Git commit author 또는 코드 내 `@author` 주석 |
| 시간복잡도 | 코드 내 `// Time Complexity: O(n)` 주석 |
| 공간복잡도 | 코드 내 `// Space Complexity: O(1)` 주석 |
| 언어 | 파일 확장자 자동 감지 |

## 📝 풀이 올리는 법

1. [leetcode-algorithms](https://github.com/seongkyu-lim/leetcode-algorithms) 레포에 풀이 push
2. 폴더 구조: `NNNN-problem-slug/파일명.확장자`
3. Push하면 자동으로 사이트에 반영 (1~2분)

### 폴더 구조 예시
```
leetcode-algorithms/
├── 0001-two-sum/
│   ├── README.md              # 문제 설명 (자동 생성 또는 수동)
│   ├── 0001-two-sum.kt        # 성규 풀이
│   └── 0001-two-sum-철수.py   # 철수 풀이
├── 0283-move-zeroes/
│   ├── README.md
│   └── 0283-move-zeroes.kt
└── ...
```

### 복잡도 & 작성자 표시 (선택)
코드 주석에 추가하면 사이트에 자동 표시:
```kotlin
// @author 성규
// Time Complexity: O(n)
// Space Complexity: O(1)
class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray { ... }
}
```

## 🛠 Setup (관리자)

### Secrets 설정
| 레포 | Secret 이름 | 용도 |
|------|-------------|------|
| `algo-study` | `DATA_REPO_TOKEN` | leetcode-algorithms 읽기용 PAT |
| `leetcode-algorithms` | `PAGES_DISPATCH_TOKEN` | algo-study dispatch 트리거용 PAT |

### 수동 배포
GitHub Actions 탭 → "Deploy Pages" → "Run workflow" 클릭

## 🌐 기능

- **📅 커리큘럼 뷰**: Day별 문제 + 알고리즘 유형 표시
- **📝 전체 풀이 뷰**: 모든 문제 목록 + 풀이 수 표시  
- **👥 멤버 뷰**: 멤버별 풀이 통계 + 진행률
- **🔗 LeetCode 링크**: 각 문제에서 바로 LeetCode로 이동
- **🎨 코드 하이라이팅**: Kotlin, Python, Java 등 지원
- **↩️ 브라우저 네비게이션**: 뒤로가기/앞으로가기 지원 (hash routing)
