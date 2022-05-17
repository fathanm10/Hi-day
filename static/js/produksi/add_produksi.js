addBahan = document.getElementsByName("add")[0];
bahanList = document.getElementsByClassName("list-bahan")[0];
bahan = document.getElementsByName("bahan")[0];
jumlahBahan = document.getElementsByName("jumlahbahan")[0];
addProduct = document.getElementsByName("add-product")[0];

addBahan.addEventListener("click", () => {
  const newRow = document.createElement("tr");
  const newBahan = document.createElement("input");
  const newJumlahBahan = document.createElement("input");
  const newBahanRow = document.createElement("td");
  const newJumlahBahanRow = document.createElement("td");
  const newAction = document.createElement("td");

  newBahan.value = bahan.options[bahan.selectedIndex].text;
  newJumlahBahan.value = jumlahBahan.value;
  newBahanRow.appendChild(newBahan);
  newJumlahBahanRow.appendChild(newJumlahBahan);

  newBahan.setAttribute("name", "bahan" + bahanList.childElementCount);
  newBahan.readOnly = true;
  newJumlahBahan.setAttribute(
    "name",
    "jumlahbahan" + bahanList.childElementCount
  );
  newJumlahBahan.readOnly = true;
  newRow.setAttribute("name", "row" + bahanList.childElementCount);

  const remove = document.createElement("input");
  remove.setAttribute("type", "button");
  remove.setAttribute("value", "Hapus Bahan");
  remove.setAttribute("name", "row" + bahanList.childElementCount);
  remove.addEventListener("click", () => {
    const element = document.getElementsByName(remove.name)[0];
    element.remove();
    if (bahanList.childElementCount <= 1) {
      addProduct.disabled = true;
    }
  });
  newAction.appendChild(remove);

  newRow.appendChild(newBahanRow);
  newRow.appendChild(newJumlahBahanRow);
  newRow.appendChild(newAction);

  bahanList.appendChild(newRow);

  if (addProduct.disabled == true) {
    addProduct.disabled = false;
  }
});
