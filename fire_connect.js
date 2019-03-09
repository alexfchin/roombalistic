var refFire = firebase.database();

document.getElementById("left").addEventListener("mousedown", leftDown);
document.getElementById("left").addEventListener("mouseup", leftUp);

document.getElementById("right").addEventListener("mousedown", rightDown);
document.getElementById("right").addEventListener("mouseup", rightUp);

document.getElementById("up").addEventListener("mousedown", upDown);
document.getElementById("up").addEventListener("mouseup", upUp);

document.getElementById("down").addEventListener("mousedown", downDown);
document.getElementById("down").addEventListener("mouseup", downUp);

function leftDown(){
    var leftChild = refFire.ref();
    var obj = {
        Left: "yes",
    };
    leftChild.update(obj);
}

function leftUp(){
    var leftChild = refFire.ref();
    var obj = {
        Left: "no",
    };
    leftChild.update(obj);
}

function rightDown(){
    var rightChild = refFire.ref();
    var obj = {
        Right: "yes",
    };
    rightChild.update(obj);
}

function rightUp(){
    var rightChild = refFire.ref();
    var obj = {
        Right: "no",
    };
    rightChild.update(obj);
}

function upDown(){
    var upChild = refFire.ref();
    var obj = {
        Up: "yes",
    };
    upChild.update(obj);
}

function upUp(){
    var upChild = refFire.ref();
    var obj = {
        Up: "no",
    };
    upChild.update(obj);
}

function downDown(){
    var downChild = refFire.ref();
    var obj = {
        Down: "yes",
    };
    downChild.update(obj);
}

function downUp(){
    var downChild = refFire.ref();
    var obj = {
        Down: "no",
    };
    downChild.update(obj);
}
