/**
 * @param {string} s
 * @return {number}
 */
var maxDepth = function (s) {
    let maxDepth = 0; // This will keep track of the maximum depth encountered
    let currentDepth = 0; // This will keep track of the current depth

    // Iterate over each character in the input string
    for (const char of s) {
        // If the character is an opening parenthesis, increase the current depth
        if (char === '(') {
            currentDepth++;
            // Update the maximum depth if the curren depth exceeds it
            maxDepth = Math.max(maxDepth, currentDepth)
        } else if (char === ')') {
            // If the character is a closing parenthesis, decrease the current depth
            currentDepth--;
        }
        // We ignore all other characters
    }
    return maxDepth; // Return the maximum depth encountered
};