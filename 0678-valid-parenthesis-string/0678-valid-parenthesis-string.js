/**
 * @param {string} s
 * @return {boolean}
 */
var checkValidString = function (s) {
    let balance = 0;
    let n = s.length;

    for (let i = 0; i < n; ++i) {
        if (s[i] !== ')') {
            balance++;
        } else if (balance > 0) {
            balance--;
        } else {
            return false;
        }
    }

    if (balance === 0) {
        return true;
    }

    balance = 0;
    for (let i = n - 1; i >= 0; --i) {
        if (s[i] !== '(') {
            balance++;
        } else if (balance > 0) {
            balance--;
        } else {
            return false;
        }
    }

    return true;
};