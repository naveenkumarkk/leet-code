// # Thought Process
// # To find the length of continuous alphabetical substring
// # initialize the given alphabets in the string
// # get the input string
// # iterate all the characters in the string
// # initialize the counter as 1
// # after identifying the continuous substring increment the counter

// # edge case:
// # the given character might start in the middle of the alphabetical order as 
// # To fix this case I need to check and start every character with the alphabet array        

function longestContinuousSubstring(inputStr) {
    let inputStringLength = inputStr.length;
    var counter = 1
    let resultCounter = 1;
    for (let i = 0; i < inputStringLength - 1; i++) {
        let checkCondition = checkTheCurrentAndNextChar(inputStr.charAt(i), inputStr.charAt(i + 1));
        if (checkCondition) {
            counter++;
        } else {
            counter = 1;
        }

        if (counter > resultCounter) {
            resultCounter = counter
        }
    }

    return resultCounter;
}

function checkTheCurrentAndNextChar(currentChar, nextChar) {
    let alphabets = "abcdefghijklmnopqrstuvwxyz";
    let currentCharIndex = alphabets.indexOf(currentChar);
    let nextCharIndex = currentCharIndex + 1
    return alphabets.charAt(nextCharIndex) === nextChar
}




