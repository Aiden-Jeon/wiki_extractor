# wiki_extractor

위키피디아의 문장을 추출합니다.

## 1. Install
깃을 통해 설치를 진행합니다.
```bash
git clone https://github.com/Aiden-Jeon/wiki_extractor.git
cd wiki_extractor
pip install -e .
```

## 2. Wikiextractor
1. [링크](https://dumps.wikimedia.org/kowiki/latest/kowiki-latest-pages-articles-multistream.xml.bz2)를 통해 위키의 전체 덤프 파일을 다운로드 받습니다.
2. wikiextractor를 통해 xml 파일을 txt형태로 추출합니다.
  ```bash
  wikiextractor data/kowiki-latest-pages-articles-multistream.xml.bz2 -o contents/
  ```

## 3. idxbook 생성
문장 추출을 위한 `idxbook.tsv`을 생성합니다.
```bash
wikiextract idxbook extract --data-dir contents/
```

생성된 `idxbook.tsv`은 다음과 같이 생겼습니다.
```
name    folder  wiki    line_start      line_end
백수왕 고라이온 AC      wiki_73 0       20
오수연 (작가)   AC      wiki_73 21      27
가나안농군학교  AC      wiki_73 28      33
실데나필        AC      wiki_73 34      50
```

각 column의 의미입니다.
- name: aritcle의 이름
- folder: wikiextractor에서 추출된 폴더 중 name의 article 내용이 들어있는 폴더
- wiki: wikiextractor에서 추출된 폴더의 텍스트 중 name의 article 내용이 들어있는 파일 이름
- line_start: 해당 파일에서 name의 article 내용이 시작하는 줄
- line_end: 해당 파일에서 name의 article 내용이 끝나는 줄

## 4. 문장 추출
name argument를 통해 원하는 토픽의 문장을 추출합니다.
```bash
wikiextract sentence extract --name="백수왕 고라이온" --data-dir contents/ --idxbook idxbook.tsv --save-dir results/
```

`--line-length` 를 통해 주어진 값보다 character 수가 작은 문장은 추출하지 않고 넘어갈 수 있습니다.  
default 값은 `10`입니다.
```bash
wikiextract sentence extract --name="백수왕 고라이온" --data-dir contents/ --idxbook idxbook.tsv --save-dir results/ --line-length 10
```

추출된 데이터는 `--save-dir` 을 통해 입력된 곳에 `name.txt`로 저장됩니다.  
위의 예시에서는 `백수왕 고라이온.txt`로 저장됩니다.  
추출된 `백수왕 고라이온.txt`의 내용은 다음과 같습니다.
```
백수왕 고라이온(百獣王ゴライオン)은 1981년 3월 4일부터 1982년 2월 24일까지 일본 TV도쿄와 도에이에서 방영한 애니메이션이다.
야츠데 사부로의 원작을 애니화 하였고 타구치 가츠히코가 감독을, 타카히사 스스무가 각색하였다.
총 52편으로 구성되어 있으며, 영미권에서는 《볼트론》으로 알려져 있다.
대한민국에서는 미래용사 볼트론이라는 제목으로 1993년에 MBC에서 방영되었다.
고라이온은 우주에 내려오는 전설 속 동물 로봇왕으로 검정, 빨강, 녹색, 파랑, 노란 사자가 합체된 모습으로서 자신의 힘을 과시하고 상대가 많지 않자 과감하게 신(神)에게 도전하다가 오히려 신의 노여움을 받아 벌을 받은 대가로 5개로 분리, 아르티나 행성(국내명 : 아루스 왕국)에 봉인된다.
...
```
