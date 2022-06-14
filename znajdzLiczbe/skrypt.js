function liczbaZakres(){
    var ilosc=document.getElementById('zakres').value;
    document.getElementById('wyborLiczby').value=ilosc;
}
var wylosowanaLiczba=Math.floor(Math.random()*100+1);
function sprawdz(){
    let podanaLiczba = document.getElementById('liczba').value;
    if(podanaLiczba == wylosowanaLiczba){
        alert("Wygrałeś");
    }else if(podanaLiczba<wylosowanaLiczba){
        alert("Podałeś za małą liczbę");
    }else{
        alert("Podałeś za dużą liczbę");
    }

}