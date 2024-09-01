# GlyphFormer: Sub-character Decomposition Tool for Japanese Language Processing

This repository contains the code for sub-character decomposition in Japanese text, specifically designed for use in language models like GlyphFormer. The tool supports both radical-based and element-based decomposition methods.

## Introduction

This project focuses on enhancing Japanese language models by breaking down kanji characters into smaller, meaningful sub-components. The tool provided here allows for easy decomposition of kanji characters into radicals and elements.

### Visualization of Character Decomposition

Below are three images illustrating the differences in kanji decomposition:

- Character-based: The kanji character "親" in its normal form.
  
  ![normal_親](https://github.com/user-attachments/assets/f04828a9-16fc-4572-a687-de35f4304ce7)


- Radical-based: The kanji "親" broken down into its radicals: "立", "木", and "見". Each radical is color-coded.
  
  ![radical_親](https://github.com/user-attachments/assets/2ee0fef1-c9a5-4108-87a4-758679e34f79)


- Element-based: The kanji "親" further decomposed into its elements: "立", "木", "見", "亠", and "目". This version includes the radicals plus additional finer elements, all of which are color-coded to differentiate the components.

  ![element_親](https://github.com/user-attachments/assets/03ad95e9-00f9-4c70-be49-0a90061efd2d)


## How to Use

To use the tool, follow these steps:

```bash
python3 GlyphFormer.py [radical|element] 'text to decompose'
```

Replace `[radical|element]` with your desired decomposition method and `'text to decompose'` with the text you want to process.


## Examples

Here are some examples of how the text is decomposed:

```
Character-based: 親譲り の 無鉄砲 で 小 供 の 時 から 損 ばかり し て いる 。
Radical-based: 立 木 見 言 襄 り の 丿 一 灬 金 失 石 包 で 小 亻 共 の 日 寺 か ら 扌 員 ば か り し て い る 。
Element-based: 立 木 見 亠 目 言 六 衣 八 一 亠 口 襄 三 り の 灬 一 丿 金 大 夫 失 丿 己 包 石 丿 口 勹 で 小 八 共 亻 の 日 寸 土  寺 か ら 員 口 目 貝 扌 ば か り し て い る 。
```

```bash
python3 GlyphFormer.py radical 親譲りの無鉄砲で小供の時から損ばかりしている。
立 木 見 言 襄 り の 丿 一 灬 金 失 石 包 で 小 亻 共 の 日 寺 か ら 扌 員 ば か り し て い る 。
```

## Perplexity Results

Perplexity is a common metric used to evaluate language models, reflecting how well a model predicts a sequence of words. A lower Perplexity score indicates better performance.

### Experimental Setup

The Perplexity of the ALBERT model was evaluated using the GlyphFormer tool on a dataset from the Boccia domain. The dataset was processed using the sub-character decomposition methods provided in this repository.

### Results

The results of the experiments are summarized in the following table. As shown, sub-character tokenization methods significantly improved perplexity compared to traditional character-based tokenization.

| Tokenization Method | Perplexity | Improvement (%) |
|----------------------|------------|-----------------|
| Character-based | 3.85 | - |
| Radical-based | 2.90 | 24.68 |
| Element-based | 2.82 | 26.75 |

These results indicate that sub-character decomposition significantly aids the model in handling the complexity of kanji in Japanese, leading to better performance as measured by Perplexity. 

## License

This project is licensed under the terms of the MIT License. See the [LICENSE](LICENSE) file for details.

## References

- Original JSON files for kanji decomposition are sourced from [KanjiVG-radical](https://github.com/yagays/kanjivg-radical/tree/master).

## Related Paper

For a detailed explanation of the underlying research and methodology, please refer to the associated paper: [GlyphFormer: Improving Japanese Language Models with Sub-character Tokenization](https://www.vixra.org/pdf/2408.0083v1.pdf).
