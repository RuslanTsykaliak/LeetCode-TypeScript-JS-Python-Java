/**
 * @param {string} s
 * @return {number}
 */
var minAddToMakeValid = function (s) {
    let queue = [];

    for (let char of s) {
        if (char === ")") {
            if (queue[queue.length - 1] === "(") {
                queue.pop();
            } else {
                queue.push(char);
            }
        } else {
            queue.push(char);
        }
    }

    return queue.length;
};