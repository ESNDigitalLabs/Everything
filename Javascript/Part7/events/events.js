// Gathering the paragraph
let p1 = document.getElementById('p1');
let p2 = document.getElementById('p2');
let p3 = document.getElementById('p3');
let p4 = document.getElementById('p4');
let p3Btn = document.getElementById('p3Btn');


//Creating the Event and Event Listener
//          (event type, functon)
p1.addEventListener('mouseover' ,function run(){
    p1.style.backgroundColor = "orange"
})

p1.addEventListener('mouseleave' ,function run(){
    p1.style.backgroundColor = "white"
})
// Create event that changes the second paragraph on click
p2.addEventListener('mouseover' , function run(){
    p2.style.backgroundColor = "red"
});
p2.addEventListener('click', function run(){
    p2.style.backgroundColor = "yellow"
})

// Create event that reverts the second paragraph on mouseout
p2.addEventListener('mouseout', function run(){
    p2.style.backgroundColor = "white"
})

//p3
p3.style.color = "blue"
p3Btn.addEventListener('click', function run(){
 
    if (p3.style.display != "block") {
        p3.style.display = "block";
        console.log("showing")
        p4.style.display = "none"
    } else {
        p3.style.display = "none";
        console.log("p3 hidden")
        p4.style.display = "block"
    }

})
//p4
p4.style.color = "crimson"


//THE START OF MY CODING//
//function change()

// Create event that changes the second paragraph on click
 
p2.addEventListener('mouseover' , function run(){
    p2.style.backgroundColor = "red"
});

p2.addEventListener('mouseout' , function run(){
    p2.style.backgroundColor = "blue"
}); 


// Create event that reverts the second paragraph on mouseout

p2.addEventListener('click' , function run(){
    p2.style.backgroundColor = 'yellow'
});
p2.addEventListener('mouseout' , function run(){
    p2.style.backgroundColor = 'white'
});

let h1 = document.getElementById('head');
h1.addEventListener( 'click' , function run(){
    h1.innerHTML = "JavaScript HAS changed the HTML";
    h1.style.backgroundColor = 'green'
});
//Task: Apply an event using the "on" method, you will need to build  function to supply this with.

function changeBackground(){
    p5.style.backgroundColor = "pink" 
};
if (p5.style.color){
    p5.style.color = "";
} else{
    p5.style.color = "yellow";
};
