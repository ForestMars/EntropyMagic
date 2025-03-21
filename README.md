# Card Deck Entropy Analyzer

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-orange.svg)

A Python-based tool to analyze the entropy decay of a card deck under Bayesian updates as cards are revealed. This project simulates deck ordering (structured vs. random), computes Shannon entropy, and tracks the decay curve as information is revealed.

It takes the form of a magic trick, where 2 volunteers each select a card, and the magicians volunteer puts them back in the deck, and arranges it in any order she likes (to help the magician "guess" the card in as few reveals as possible) and then the magician views the deck, one card at a time, until he has reduced the entropy enough to guess the volunteers' cards. 

---

## ✨ Features

- **Deck Generation**: Creates a standard 52-card deck with suits and ranks.
- **Entropy Calculation**: Computes Shannon entropy for probability distributions.
- **Bayesian Updates**: Applies Bayes' theorem to update beliefs as cards are revealed.
- **Entropy Decay Curves**: Visualizes how entropy decreases with structured and random deck orders.
- **Hidden Card Removal**: Simulates real-world scenarios by removing specific cards.

---

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- Required libraries: `numpy`

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/card-deck-entropy-analyzer.git
   cd card-deck-entropy-analyzer

## Usage

The script runs an entropy analysis on a 52-card deck with two
pre-selected hidden cards (**7♦** and **Q♥**). It compares entropy decay
between a structured deck (original order) and a randomized deck.

### Example Output

    Entropy Decay (Structured Deck): [5.672425341971495, 5.655351828612337, ...]
    Entropy Decay (Random Deck): [5.672425341971495, 5.655351828612337, ...]

To customize:

- Modify *hidden_cards* in the *entropy_analysis()* function.
- Adjust deck ordering logic in *create_deck()* or *entropy_analysis()*.

## How It Works

1.  **Deck Creation**: Generates a standard 52-card deck using suits
    (♠♣♦♥) and ranks (2-10, J, Q, K, A).
2.  **Entropy Calculation**: Uses Shannon entropy (*H = -∑ p log₂(p)*)
    to measure uncertainty.
3.  **Bayesian Updates**: Updates probability distributions as cards are
    revealed, normalizing posteriors.
4.  **Decay Curve**: Tracks entropy reduction over time for structured
    and random decks.
5.  **Analysis**: Compares entropy decay between deterministic and
    shuffled deck orders.

## Results

The output includes:

- **Structured Deck**: Entropy decay for the remaining deck in its
  original order.
- **Random Deck**: Entropy decay for a shuffled version of the remaining
  deck.
- **Data Structure**: A list of dictionaries containing deck orders and
  their entropy curves.

## Testing

Run the script directly to see results. For unit tests (coming soon),
use:

    pytest tests/

## Contributing

Contributions are welcome! Here's how to get started:

1.  Fork the repository.
2.  Create a feature branch: *git checkout -b feature/amazing-idea*.
3.  Commit your changes: *git commit -m "Add amazing idea"*.
4.  Push to the branch: *git push origin feature/amazing-idea*.
5.  Open a Pull Request.

## Roadmap

- [ ] Add visualization with Matplotlib or Plotly.
- [ ] Implement CLI for custom hidden card inputs.
- [ ] Support multiple deck sizes (e.g., 32-card decks).
- [ ] Add statistical comparison of decay curves.
- [ ] Optimize Bayesian updates with NumPy vectorization.

## License

⚖️ This project is licensed under the MIT License.

## Acknowledgments

- Inspired by information theory and Bayesian inference.
- Built with ♥ using Python and NumPy.

## Stargazers

If you find this project useful, give it a ★ on GitHub!

## Questions?

Open an issue or reach out via
\[Discussions\|<https://github.com/yourusername/card-deck-entropy-analyzer/discussions>\].