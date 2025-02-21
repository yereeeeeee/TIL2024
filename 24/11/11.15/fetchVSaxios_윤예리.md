커리어리 보고있는데 "왜 fetch를 쓰지 않을까?"라는 글이 있길래 공부해봄

## 공통점

- 서버에 요청하는 함수
- promise 기반 (요청하면 promise를 반환)

## 차이점

### 시작방법

- axios: 서드파티 라이브러리 (그래서 import 해서 사용해야 함) (근데 현업에서 많이 써서 주로 axios를 쓴대요.)
- fetch: 자체 내장함수 (RN과 같이 잦은 업데이트가 있는 경우 용이함)

### 사용법

- 거의 비슷함
- 둘 다 method를 붙이지 않으면 get 요청임

1. axios

```js
axios.get({
  url: url,
  headers: {},
  data: {},
  responseType: "json", // 'arraybuffer', 'document', 'blob', 'text', 'stream'도 가능
});

// fetch처럼 method를 지정해서 사용도 가능
```

2. fetch

```js
fetch(url, {
  method: "GET",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({}),
});

// body에서 stringify를 해줘야 함
```

### 데이터 처리

1. axios

```js
axios.get(url).then((response) => console.log(response.data));
```

2. fetch

```js
fetch(url)
  // fetch는 받아오는 response가 json 타입이 아님
  .then((response) => response.json())
  // 따라서 한번 더 호출하여 json화 시킨 값을 console에 찍어야 함
  .then(console.log);
```

### 데이터 요청

1. axios

- `request body`의 내용을 `data`프로퍼티에 할당하며 기본 `Content-Type: application/json`임

2. fetch

- `request body`의 내용을 `body`프로퍼티에 할당하며 `JSON.stringify(body)`의 형식처럼 객체를 문자열로 변환한 뒤 할당하여야 함

### 에러 처리

1. axios

```js
// promise의 상태코드가 200대를 넘어가면 자동으로 error로 처리됨
axios
  .get(url)
  .then((response) => console.log(response.data))
  .catch((err) => {
    console.log(err.message);
  });
```

2. fetch

```js
fetch(url)
  .then((response) => {
    // response에 ok라는 boolean값이 있음
    // 이게 true면 서버로 잘 전송됐다는 의미
    // false면 잘못된 주소로 요청했다는 의미
    if (!response.ok) {
      throw new Error(
        // 404에러와 같이 200대가 아닐 때 error로 throw
        `${response.status}`
      );
    }
    return response.json();
  })
  .then(console.log)
  .catch((err) => {
    console.log(err.message);
  });
```
