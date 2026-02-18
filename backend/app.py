from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import random
import json
import os

app = Flask(__name__, 
            template_folder='../frontend',
            static_folder='../frontend',
            static_url_path='')
CORS(app)

# Default slot machine symbols - Custom food items
SYMBOLS = ['tofu', 'kwek-kwek', 'sauce']
SYMBOL_EMOJIS = {
    'tofu': '',
    'kwek-kwek': '',
    'sauce': ''
}

@app.route('/')
def index():
    """Serve the main game page"""
    return render_template('index.html')

@app.route('/api/spin', methods=['POST'])
def spin():
    """Process a spin and return results"""
    try:
        # Generate random results for 3 reels
        result1 = random.choice(SYMBOLS)
        result2 = random.choice(SYMBOLS)
        result3 = random.choice(SYMBOLS)
        
        # Check for win (all 3 same)
        win = (result1 == result2 == result3)
        
        return jsonify({
            'results': [result1, result2, result3],
            'win': win,
            'symbols': SYMBOLS,
            'message': f'🎉 JACKPOT! 3 {result1}s!' if win else f'{result1} {result2} {result3}'
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/symbols', methods=['GET'])
def get_symbols():
    """Get available symbols"""
    return jsonify({
        'symbols': SYMBOLS,
        'emojis': SYMBOL_EMOJIS
    }), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
