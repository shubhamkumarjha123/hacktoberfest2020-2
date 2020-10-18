var ask = true;
while(ask){
  var user = prompt("Pilih :\n- Gunting\n- Batu\n- Kertas");

  var com = Math.random();

  if(com < 0.34){
    com = "Gunting";
  } else if(com >= 0.34 && com < 0.67){
    com = "Batu";
  } else {
    com = "Kertas";
  }

  var result = "";

  if (user == com){
    result = "SERI";

  } else if(user == "Gunting"){
    result = (com == "Batu") ? "KALAH" : "MENANG";

  } else if(user == "Batu"){
    result = (com == "Kertas") ? "KALAH" : "MENANG";

  } else if (user == "Kertas"){
    result = (com == "Gunting") ? "KALAH" : "MENANG";
  } else {
    result = "Masukkan pilihan yang benar";
  }

  alert(`User memilih : ${user} dan Computer memilih ${com} \nMaka hasilnya : ${result}`);

  ask = confirm("Ingin bermain lagi?");
}
alert("Terima kasih sudah bermain")