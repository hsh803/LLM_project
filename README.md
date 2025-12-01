# Research and development project
- R&D course project from Language Technology Mater's program, Uppsala university
- Subject of the project: Eror Propagation in STT Pipelines: Investigating Language Model Limitations and Amplification Effects

## Data
- Each 500 English audio files from Librispeech and Common Voice

## Models
- ASR (Automatic Speech Recognition) model: Kaldi
- Language model for post correction : LLaMA 3.2-1B (llama.py), 3-gram model (3g.py)

## Evaluation
- WER (Word Error rate): wer.py
- SeMaScore (Sasindran et al., 2024): Semascore.py is modified by using the original SeMaScore code from https://github.com/zenlab-edgeASR/SeMaScore/tree/main/codes
  
