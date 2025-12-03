# Research and development project
- R&D course project from Language Technology Mater's program, Uppsala university
- Subject of the project: Eror Propagation in STT Pipelines: Investigating Language Model Limitations and Amplification Effects

## Introduction
- This project specifically examines the impact of LMs (Language models) during the post-correction phase of the ASR (Automatic Speech Recognition) workflow.

## Data
- Each 500 English audio files from Librispeech (OpenSLR) and Common Voice (Mozilla community)

## Models
- ASR model: Kaldi (https://kaldi-asr.org)
- Language model for post correction : LLaMA 3.2-1B (llama.py), 3-gram model (3g.py)

## Evaluation
- WER (Word Error rate): wer.py
- SeMaScore (Sasindran et al., 2024): Semascore.py is modified by using the original SeMaScore code from https://github.com/zenlab-edgeASR/SeMaScore/tree/main/codes

## Experiments
1. Process each 500 audio file through the ASR model with/withouwt using LM for decoding
2. After decoding, the post-correction process is applied using both the 3-gram and the LLaMA model for each case (with and without the LM for decoding).

## Conclustion
- Incorporating the LM during the decoding stage improved significantly transcription accuracy, as evidenced by lower WER and higher SeMaScore.
- Both the 3-gram and LLaMA models exhibit notable limitations in post-correction tasks.
- LLaMA model showed marginal improvements compared to the 3-gram model ,however, it proved insufficient to meaningfully enhance transcription quality overall.
- These findings highlight the inevitability of error propagation in ASR pipelines and the critical need to address the limitations of LMs.
- This project can provide a valuable foundation for future research aimed at improving various ASR systems, including E2E ap-
proaches, by refining the role and application of language models.
  
