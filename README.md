# wiki_extractor

위키피디아의 문장을 추출합니다.

## 1. Install
깃을 통해 설치를 진행합니다.
```bash
git clone https://github.com/Aiden-Jeon/wiki_extractor.git
cd wiki_extractor
pip install -e .
```

## 2. Wikiextract
wikiextractor를 통해 xml 파일을 추출합니다.
우선 [링크](https://dumps.wikimedia.org/kowiki/latest/kowiki-latest-pages-articles-multistream.xml.bz2)를 통해위키의 덤프 파일은 다운로드 받습니다. 

wikiextractor를 통해 해제합니다.
```bash
wikiextractor data/kowiki-latest-pages-articles-multistream.xml.bz2 -o contents/
```

## 3. idxbook 생성
idxbook을 생성합니다.
```bash
wikiextract idxbook extract --data-dir contents/
```

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
