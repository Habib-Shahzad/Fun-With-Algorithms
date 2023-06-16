class Dictionary {
  dict: Object;

  constructor(wordsArray: string[]) {
    this.dict = wordsArray.reduce((acc, word) => {
      acc[word] = true;

      word.split("").map((_, index) => {
        const start = word.slice(0, index);
        const end = word.slice(index + 1);
        const partialWord = `${start}*${end}`;
        acc[partialWord] = true;
      });

      return acc;
    }, {});
  }

  isInDict(word: string) {
    return !!this.dict[word];
  }
}

const words = ["cat", "car", "bar"];
const dict = new Dictionary(words);

console.log(dict.isInDict("cat")); // true
console.log(dict.isInDict("cal")); // false
console.log(dict.isInDict("*at")); // true
console.log(dict.isInDict("c*t")); // true
