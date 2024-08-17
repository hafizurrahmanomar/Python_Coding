//for loop
const productsList1 = ["pen", "paper", "soap", "oil"];

for (let i = 0; i < productsList1.length; i++) {
  console.log(`Item ${i + 1} is ${productsList1[i]}`);
}

// forEach easy way

const productsList2 = ["pen", "paper", "soap", "oil"];
function showItem(item) {
  console.log(item);
}
productsList2.forEach(showItem);

// forEach for project use for best option
const productsList3 = ["pen", "paper", "soap", "oil"];

productsList3.forEach(function (item, index) {
  console.log(`Item ${index + 1} is ${item}`);
});

//For in
const products4 = ["pen", "paper", "soap", "oil"];

for (let x in products4) {
  //console.log(x);
  //console.log(person[x]);
  // console.log(x,products4[x]);
  console.log(`Item ${x} is ${products4[x]}`);
}
// for of
const products = ["pen", "paper", "soap", "oil"];

for (let item of products) {
  console.log(`Item  is ${item}`);
}
