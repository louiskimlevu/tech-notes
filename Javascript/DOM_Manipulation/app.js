const body = document.body;
// body object
let button = (document.querySelector("button.body").onclick = () => {
  console.log(body);
});

// body-append object
button = document.querySelector("button.append").onclick = () => {
  const h2 = document.querySelector("h2.this_h2_to_move");
  const div = document.querySelector("div.div_append_h2");
  div.append("Hello World!", h2.innerText);
};

// body-append-child object
button = document.querySelector("button.append_child").onclick = () => {
  const toMove = document.querySelector(".to-move");
  const moveHere = document.querySelector(".move-here");
  moveHere.appendChild(toMove);
};

// create element
button = document.querySelector("button.create_element").onclick = () => {
  const destination = document.querySelector(".add_sthg_here_div");
  const newDiv = document.createElement("div");
  newDiv.innerText = "Created via InnerText";
  destination.appendChild(newDiv);
  const salut = document.createTextNode("Created via createTextNode");
  destination.appendChild(salut);
};

// innerText-vs-textContent
button = document.querySelector(
  "button.innertext_vs_textcontent__btn"
).onclick = () => {
  const div = document.querySelector("div.innertext_vs_textcontent__div");
  console.log(div.innerText);
  console.log(div.textContent);
};

// innerHTML
button = document.querySelector("button.innerhtml__button").onclick = () => {
  const div = document.querySelector("div.innerhtml__div");

  // Method1: createElement + innerText +appendChild
  // newH1= document.createElement("h1");
  // newH1.innerText = "New content with innerHTML";
  // div.appendChild(newH1);

  // Method2: innerHTML
  div.innerHTML = "<h1>New content added with innerHTML</h1>";
};

// delete an element
button = document.querySelector("button.delete_element").onclick = () => {
  const div = document.querySelector("#delete_element");
  div.remove();
};

// delete child
button = document.querySelector("button.delete_child").onclick = () => {
  const div = document.querySelector("#delete_child_div");
  const h2 = document.querySelector("#delete_child_h2");
  div.removeChild(h2);
};

// change style attribute
button = document.querySelector("button.change_attr").onclick = () => {
  const span = document.querySelector("#change_my_style");
  console.log(span.getAttribute("style"));
  console.log(span.style.color);
  span.setAttribute("style", "color: green");
};

// data attributes
button = document.querySelector("button.change_data_attr").onclick = () => {
  const span = document.querySelector("#data_attr_span");
  console.log(span.dataset);
  span.innerText = span.dataset.firstName;
  span.dataset.myNewAttribute = "from js to css";
};

// class list
button = document.querySelector("button.btn_class_list").onclick = () => {
  const div = document.querySelector("#class_list");
  const classList = div.classList;
  console.log(classList);
  classList.add("superclass");
  classList.remove("hi1");
  classList.toggle("hi3");
  console.log(classList);
};

// change css
button = document.querySelector("button.change.css").onclick = () => {
  const button = document.querySelector("button.change.css");
  button.style.color = "red";
};
