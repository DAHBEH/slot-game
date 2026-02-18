// Game Variables
let gameState = {
    balance: 100,
    isSpinning: false,
    totalSpins: 0,
    totalWins: 0,
    currentSymbols: ['tofu', 'kwek-kwek', 'sauce'],
    spinningIntervals: []
};

// Symbols - Custom Food Items
const SYMBOLS = ['tofu', 'kwek-kwek', 'sauce'];
const SYMBOL_DISPLAY = {
    'tofu': 'Tofu',
    'kwek-kwek': 'Kwek-Kwek',
    'sauce': 'Sauce'
};

// DOM Elements
const spinBtn = document.getElementById('spinBtn');
const stopBtn = document.getElementById('stopBtn');
const balanceDisplay = document.getElementById('balance');
const winMessage = document.getElementById('winMessage');
const spinAudio = document.getElementById('spinSound');
const winAudio = document.getElementById('winSound');
const loseAudio = document.getElementById('loseSound');

const reel1 = document.getElementById('reel1');
const reel2 = document.getElementById('reel2');
const reel3 = document.getElementById('reel3');

const img1 = document.getElementById('img1');
const img2 = document.getElementById('img2');
const img3 = document.getElementById('img3');

const text1 = document.getElementById('text1');
const text2 = document.getElementById('text2');
const text3 = document.getElementById('text3');

const totalSpinsDisplay = document.getElementById('totalSpins');
const totalWinsDisplay = document.getElementById('totalWins');
const winRateDisplay = document.getElementById('winRate');

// Initialize
function init() {
    updateDisplay();
    spinBtn.addEventListener('click', handleSpin);
    stopBtn.addEventListener('click', handleStop);
    stopBtn.disabled = true;

    // Show initial symbols
    displaySymbol(reel1, text1, img1, gameState.currentSymbols[0]);
    displaySymbol(reel2, text2, img2, gameState.currentSymbols[1]);
    displaySymbol(reel3, text3, img3, gameState.currentSymbols[2]);
}

// Update Display
function updateDisplay() {
    balanceDisplay.textContent = gameState.balance;
    totalSpinsDisplay.textContent = gameState.totalSpins;
    totalWinsDisplay.textContent = gameState.totalWins;

    const winRate = gameState.totalSpins > 0
        ? Math.round((gameState.totalWins / gameState.totalSpins) * 100)
        : 0;
    winRateDisplay.textContent = winRate + '%';
}

// Display Symbol
function displaySymbol(element, textElement, imageElement, symbol) {
    if (textElement) {
        textElement.textContent = SYMBOL_DISPLAY[symbol];
    }
    imageElement.src = `images/${symbol}.png`;
    imageElement.onerror = () => {
        // Fallback if image not found
        imageElement.classList.remove('show');
    };
    imageElement.onload = () => {
        imageElement.classList.add('show');
    };
    imageElement.classList.remove('show');
}

// Play Sound
function playSound(audio) {
    audio.currentTime = 0;
    audio.play().catch(e => console.log('Could not play sound:', e));
}

// Get random symbol
function getRandomSymbol() {
    return SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)];
}

// Handle SPIN button - start spinning
function handleSpin() {
    if (gameState.isSpinning) return;

    gameState.isSpinning = true;
    spinBtn.disabled = true;
    stopBtn.disabled = false;
    winMessage.classList.remove('show');

    // Count spin
    gameState.totalSpins++;
    updateDisplay();

    // Play spin sound on loop while spinning
    spinAudio.loop = true;
    playSound(spinAudio);

    // Start spinning animation
    reel1.classList.add('spinning');
    reel2.classList.add('spinning');
    reel3.classList.add('spinning');

    // Cycle through symbols continuously
    const spinSpeed = 100; // ms per symbol change

    const interval1 = setInterval(() => {
        const newSymbol = getRandomSymbol();
        gameState.currentSymbols[0] = newSymbol;
        displaySymbol(reel1, text1, img1, newSymbol);
    }, spinSpeed);

    const interval2 = setInterval(() => {
        const newSymbol = getRandomSymbol();
        gameState.currentSymbols[1] = newSymbol;
        displaySymbol(reel2, text2, img2, newSymbol);
    }, spinSpeed);

    const interval3 = setInterval(() => {
        const newSymbol = getRandomSymbol();
        gameState.currentSymbols[2] = newSymbol;
        displaySymbol(reel3, text3, img3, newSymbol);
    }, spinSpeed);

    gameState.spinningIntervals = [interval1, interval2, interval3];
}

// Handle STOP button - stop all reels and check for win
function handleStop() {
    if (!gameState.isSpinning) return;

    // Clear all intervals to stop spinning
    gameState.spinningIntervals.forEach(interval => clearInterval(interval));
    gameState.spinningIntervals = [];

    // Stop spinning animation
    reel1.classList.remove('spinning');
    reel2.classList.remove('spinning');
    reel3.classList.remove('spinning');

    // Stop spin sound
    spinAudio.pause();
    spinAudio.currentTime = 0;
    spinAudio.loop = false;

    gameState.isSpinning = false;
    spinBtn.disabled = false;
    stopBtn.disabled = true;

    // Check if all 3 symbols match
    const [sym1, sym2, sym3] = gameState.currentSymbols;
    const isWin = (sym1 === sym2 && sym2 === sym3);

    if (isWin) {
        gameState.totalWins++;
        updateDisplay();
        playSound(winAudio);
        showMessage('CONGRATULATIONS YOU WIN', 'win');
    } else {
        playSound(loseAudio);
        showMessage('Try Again', 'lose');
    }

    updateDisplay();
}

// Show Message
function showMessage(message, type) {
    winMessage.textContent = message;
    winMessage.className = `win-message show ${type}`;

    setTimeout(() => {
        winMessage.classList.remove('show');
    }, 3000);
}

// Start Game
document.addEventListener('DOMContentLoaded', init);
