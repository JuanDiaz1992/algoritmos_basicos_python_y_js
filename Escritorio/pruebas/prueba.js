function getUrl(){
    fetch("https://fakestoreapi.com/products")
    .then(response=>response.json())
    .then(data=>{
        let datos = data.sort((a,b)=> a.price - b.price)
        console.log(datos.filter(item => item.category === "electronics" && item.price<70))
    })
}

function palindromos(text){
    let palabra = ""
    for (let i = text.length-1; i >= 0; i--) {
        palabra += text[i] 
    }
    if (palabra === text ) {
        console.log("true")
    }else{
        console.log("false")
    }
}
function numberMax(array){
    array.sort((a,b)=>a-b)
    console.log(array[array.length-1])
}

numberMax([2,5,2,6,7,5,4,70,8,4,3])