const boxes = [1, 2, 3, 4, 5, 6]

function logFirstTwoBoxes(boxes) {
    console.log(boxes[0]);  //O(1)
    console.log(boxes[1]);  //O(1)
}

logFirstTwoBoxes(boxes) //O(2)