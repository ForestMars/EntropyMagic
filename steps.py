import numpy as np
import math
from collections import Counter
import random

# Step 1: Define the deck of cards
def create_deck():
    # Full deck of 52 cards
    suits = ['♠', '♣', '♦', '♥']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [rank + suit for suit in suits for rank in ranks]
    return deck

# Step 2: Shannon entropy calculation
def shannon_entropy(probabilities):
    """Calculates Shannon entropy for a given probability distribution."""
    return -sum(p * math.log2(p) for p in probabilities if p > 0)

# Step 3: Bayesian update function
def bayesian_update(prior, likelihood):
    """Updates the belief using Bayes' Theorem."""
    posterior = np.multiply(likelihood, prior)
    posterior /= np.sum(posterior)  # Normalize to get a valid probability distribution
    return posterior

# Step 4: Compute entropy decay curve
def entropy_decay_curve(deck_order):
    """Computes the entropy decay curve for a given deck order."""
    prior = np.ones(len(deck_order)) / len(deck_order)
    entropy_curve = []
    
    for revealed_card in deck_order:
        likelihood = np.ones(len(deck_order))
        likelihood[deck_order.index(revealed_card)] = 0  # Eliminating revealed card
        posterior = bayesian_update(prior, likelihood)
        entropy_curve.append(shannon_entropy(posterior))
        prior = posterior
    
    return entropy_curve

# Step 5: Generate new deck order with hidden cards removed
def remove_hidden_cards(deck, hidden_cards):
    return [card for card in deck if card not in hidden_cards]

# Step 6: Run entropy analysis on a structured and random deck
def entropy_analysis():
    deck = create_deck()
    hidden_cards = ['7♦', 'Q♥']  # Fixed volunteer selections
    remaining_deck = remove_hidden_cards(deck, hidden_cards)
    
    # New deck order with missing cards
    structured_deck = remaining_deck.copy()
    random_deck = remaining_deck.copy()
    random.shuffle(random_deck)
    
    # Calculate entropy decay curves
    structured_entropy_curve = entropy_decay_curve(structured_deck)
    random_entropy_curve = entropy_decay_curve(random_deck)
    
    # Store results in a data structure
    deck_analysis = [
        {"deck_order": structured_deck, "entropy_curve": structured_entropy_curve},
        {"deck_order": random_deck, "entropy_curve": random_entropy_curve}
    ]
    
    print("Entropy Decay (Structured Deck):", structured_entropy_curve)
    print("Entropy Decay (Random Deck):", random_entropy_curve)
    
    return deck_analysis

# Run the entropy analysis
deck_analysis_results = entropy_analysis()
