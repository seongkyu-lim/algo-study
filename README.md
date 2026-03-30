# 📚 알고리즘 스터디

LeetCode 75 기반 코딩테스트 스터디 풀이 공유 사이트

## 🔗 사이트
https://seongkyu-lim.github.io/algo-study/

## 📝 풀이 올리는 법

1. [leetcode-algorithms](https://github.com/seongkyu-lim/leetcode-algorithms) 레포에 풀이 push
2. 폴더 구조: `NNNN-problem-slug/파일명.kt` (또는 .py, .java 등)
3. Push하면 자동으로 사이트에 반영됩니다!

### 복잡도 자동 인식
코드 주석에 아래 형식으로 작성하면 사이트에 자동 표시:
```
// Time Complexity: O(n)
// Space Complexity: O(1)
```

### 작성자 표시
코드 주석에 `@author 이름` 추가:
```
// @author 성규
```

## 🛠 Setup
- `algo-study` 레포 Settings → Secrets에 `DATA_REPO_TOKEN` 추가 (leetcode-algorithms 읽기 권한)
- `leetcode-algorithms` 레포 Settings → Secrets에 `PAGES_DISPATCH_TOKEN` 추가 (algo-study dispatch 권한)
