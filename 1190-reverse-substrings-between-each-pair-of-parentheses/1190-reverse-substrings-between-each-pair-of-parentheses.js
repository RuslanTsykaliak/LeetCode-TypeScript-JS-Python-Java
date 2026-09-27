/**
 * @param {string} s
 * @return {string}
 */
var reverseParentheses = function (s) {
    let paranRegex = /\((\w*)\)/, m, pattern = "", extract = "";

    while (s.includes('(')) {
        m = s.match(paranRegex);
        extract = m[1].split('').reverse().join('');
        pattern = m[0];
        s = s.replaceAll(pattern, extract);
    }
    return s;
};