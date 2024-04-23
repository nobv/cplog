import * as fs from "fs";

const inputs = fs.readFileSync(0, "utf8");
const inputArray = inputs.split("\s")

let currentIndex = 0;
function next() {
    return inputArray[currentIndex++]
}
