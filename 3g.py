# -*- coding: utf-8 -*-

import kenlm
import numpy as np

# Load the KenLM 3-gram model
lm_model = kenlm.Model('3-gram.bin')

def preprocess_line(line):
    """Remove <UNK> token from the end of the line if present."""
    if line.endswith(" <UNK>"):
        line = line[:-6]  # Remove the last 6 characters
    return line.strip()  # Return the processed line without trailing spaces

def get_alternative_words(word, context, model):
    """Generate alternative words based on context and language model scoring."""
    # Load the vocabulary
    vocabulary = set()
    with open('librispeech-voca.txt', 'r') as f:
        for line in f:
            vocabulary.add(line.strip())

    alternatives = []
    for candidate in vocabulary:
        # Create the new context with the candidate word
        new_context = ' '.join(context.split()[:-1] + [candidate])
        score = model.score(new_context)
        alternatives.append((candidate, score))

    # Sort alternatives based on their scores (higher is better)
    alternatives.sort(key=lambda x: x[1], reverse=True)
    return alternatives[:5]  # Return top 5 alternatives

def correct_line(line, model):
    # Split the line into parts (ID and sentence)
    parts = line.split(' ', 1)  # Split into ID and sentence
    if len(parts) != 2:
        return line  # Return original line if it doesn't have ID and sentence

    id, sentence = parts  # Unpack ID and sentence
    words = sentence.split()  # Split sentence into words
    corrected_words = []

    # Iterate through each word in the line and check context using 3-grams
    for i in range(len(words)):
        if words[i] == "<UNK>":  # Handle <UNK> tokens specifically
            # Ensure we have a 3-gram context
            if i >= 2:
                context = ' '.join(words[i-2:i+1])
                # Get alternatives for <UNK>
                alternatives = get_alternative_words(words[i], context, model)
                if alternatives:
                    corrected_words.append(alternatives[0][0])  # Use the highest scoring alternative
                else:
                    corrected_words.append(words[i])  # No alternative found, keep <UNK>
            else:
                corrected_words.append(words[i])  # Keep <UNK> if insufficient context
        else:
            if i >= 2:  # Ensure we have a 3-gram context
                context = ' '.join(words[i-2:i+1])
                # Check the score of the current context
                score = model.score(context)

                if score < -10:  # Threshold for unlikely sequences
                    # Get alternatives for the last word
                    alternatives = get_alternative_words(words[i], context, model)
                # Choose the highest scoring alternative or keep the original word if no better options
                    if alternatives:
                        corrected_words.append(alternatives[0][0])  # Append the best alternative
                    else:
                        corrected_words.append(words[i])  # No alternatives found, keep original
                else:
                    corrected_words.append(words[i])  # Keep original word

            else:
                corrected_words.append(words[i])  # Use as is if insufficient context

    # Join the corrected words and keep the ID
    corrected_sentence = ' '.join(corrected_words)
    return corrected_sentence  # Return ID with the corrected sentence

# Read ASR output and apply corrections
with open('/Downloads/kaldi/egs/librispeech/s5/common_500_lm_9.1.0.txt') as f:
    lines = [line.strip() for line in f]

# Preprocess each line to remove <UNK> tokens
preprocessed_lines = [preprocess_line(line) for line in lines]

# Apply KenLM-based correction and keep IDs
corrected_lines = [correct_line(line, lm_model) for line in preprocessed_lines]

# Write out corrected ASR output
with open('common_500_lm_corr_9.1.0.txt', 'w') as f:
    f.write('\n'.join(corrected_lines))

