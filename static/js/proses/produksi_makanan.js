const jumlah = document.getElementsByName("jumlah")[0];
const xp = document.getElementsByName("xp")[0];

const add_jumlah = () => {
  // console.log(jumlah.value);
  // console.log(xp.value);

  xp.value = jumlah.value * 5;
};
