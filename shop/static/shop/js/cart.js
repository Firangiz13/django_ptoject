if(localStorage.getItem('cart')==null){
    var cart = {};
}
else{
    cart = JSON.parse(localStorage.getItem('cart'));   
}

$(document).on('click', '.atc', function(){
    console.log('hello')
    var item_id = this.id.toString();
    console.log(item_id);

    if(cart[item_id]!=undefined){
        quantity = cart[item_id][0] + 1;
        cart[item_id][0] = quantity;
    }
    else{
        quantity = 1;
        title = document.getElementById("ttl"+item_id).innerHTML;
        cart[item_id] = [quantity, title];
    }
    console.log(cart);
    localStorage.setItem('cart', JSON.stringify(cart));

    document.getElementById('cart').innerHTML ="Cart("+Object.keys(cart).length +")";
});