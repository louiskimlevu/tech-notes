animal = {
  alive: "yes",
};

human = {
  gender: "man",
  name: "patrick",
};

Object.setPrototypeOf(human, animal);
console.log(human);
console.log(Object.getPrototypeOf(human));

const { gender, name:myname } = human;

console.log(gender, myname);


console.log(human.caca)