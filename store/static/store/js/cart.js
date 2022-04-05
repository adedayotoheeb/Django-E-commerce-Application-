let updateBtns = document.getElementsByClassName("update-cart");

for (let j = 0; j < updateBtns.length; j++) {
  updateBtns[j].addEventListener("click", function () {
    let productId = this.dataset.single_product;
    let action = this.dataset.action;
    console.log(`productId: ${productId}, action: ${action}`);
  });
}
