# GlyphFormer: Sub-character Decomposition Tool for Japanese Language Processing

This repository contains the code for sub-character decomposition in Japanese text, specifically designed for use in language models like GlyphFormer. The tool supports both radical-based and element-based decomposition methods.

## Introduction

This project focuses on enhancing Japanese language models by breaking down kanji characters into smaller, meaningful sub-components. The tool provided here allows for easy decomposition of kanji characters into radicals and elements.

## How to Use

To use the tool, follow these steps:

```bash
python GlyphFormer.py [radical|element] 'text to decompose'
```

Replace `[radical|element]` with your desired decomposition method and `'text to decompose'` with the text you want to process.

## Examples

Here are some examples of how the text is decomposed:

```
Character-based: 親譲り の 無鉄砲 で 小 供 の 時 から 損 ばかり し て いる 。
Radical-based: 立 木 見 言 襄 り の 丿 一 灬 金 失 石 包 で 小 亻 共 の 日 寺 か ら 扌 員 ば か り し て い る 。
Element-based: 立 木 見 亠 目 言 六 衣 八 一 亠 口 襄 三 り の 灬 一 丿 金 大 夫 失 丿 己 包 石 丿 口 勹 で 小 八 共 亻 の 日 寸 土  寺 か ら 員 口 目 貝 扌 ば か り し て い る 。
```

## License

This project is licensed under the terms of the MIT License. See the [LICENSE.md](LICENSE.md) file for details.

## References

- Original JSON files for kanji decomposition are sourced from [KanjiVG-radical](https://github.com/yagays/kanjivg-radical/tree/master).

## Related Paper

For a detailed explanation of the underlying research and methodology, please refer to the associated paper: [GlyphFormer: Improving Japanese Language Models with Sub-character Tokenization](https://www.vixra.org/pdf/2408.0083v1.pdf).
