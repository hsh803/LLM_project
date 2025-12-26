# Research and development project
- R&D course project from Language Technology Mater's program, Uppsala university
- Eror Propagation in STT Pipelines: Investigating Language Model Limitations and Amplification Effects

## Keywords
\# Speech to text (STT) \# ASR (Automatic Speech Recognition) \# post correction

## Introduction
- This project specifically examines the impact of LMs during the post-correction phase of the ASR workflow.

## Data
- Each 500 English audio files from Librispeech (OpenSLR) and Common Voice (Mozilla community)
<img width="798" height="337" alt="image" src="https://github.com/user-attachments/assets/103b6ad0-8870-4beb-92fb-b92ae5554c35" />


## Models
- ASR model: Kaldi (https://kaldi-asr.org)
- Language model for post correction : LLaMA 3.2-1B (https://huggingface.co/meta-llama/Llama-3.2-1B), 3-gram model ()

## Evaluation
- WER (Word Error rate)
- SeMaScore (Sasindran et al., 2024): semascore.py is modified by using the original SeMaScore code from the source (https://github.com/zenlab-edgeASR/SeMaScore/tree/main/codes)

## Experiments
- Process each 500 audio file through the ASR model with/withouwt using LM for decoding
- After decoding, the post-correction process is applied using both the LLaMA model and the 3-gram for each case (with and without the LM for decoding): llama.py, 3g.py
- Evaluate the performance of post-correction: wer.py, semascore.py

## Conclustion
- Incorporating the LM during the decoding stage improved significantly transcription accuracy, as evidenced by lower WER and higher SeMaScore.
- Both the 3-gram and LLaMA models exhibit notable limitations in post-correction tasks.
- LLaMA model showed marginal improvements compared to the 3-gram model ,however, it proved insufficient to meaningfully enhance transcription quality overall.
- These findings highlight the inevitability of error propagation in ASR pipelines and the critical need to address the limitations of LMs.
- This project can provide a valuable foundation for future research aimed at improving various ASR systems, including E2E ap-
proaches, by refining the role and application of language models.
  
