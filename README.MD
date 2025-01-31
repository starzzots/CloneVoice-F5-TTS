firstly this is the original repo im using on this project if anything goes wrong refer to this https://github.com/swivid/F5-TTS/


https://github.com/JarodMica/F5-TTS this is the repo used in youtube. Repo is most up to date 
- https://www.youtube.com/watch?v=GmketyZW2c4&ab_channel=JarodsJourney this video is for the people who dont like walls of text to figure this out <3 

pip install -r requirements.txt so you can use helper scripts I made if you dont want to use them you can skip this part 

-strip_audio.py is a script to help strip a video into just audio form so you can use to train on F5-TTS faster
-combine.py combines multiple audio files you create from the F5-TTS model into one audio file

-sample_clone_of_me.wave is a sample of my voice clone snippets and then combines them together to make one long audio file. 
I noticed the F5-TTS does really well at getting the voice clone better when you make it say less at a time. Also you can make different emotions for each sentence before combining making the clone of you feel more alive.

First) go to https://github.com/swivid/F5-TTS/ and go through there set up of F5-TTS if you're too lazy I got you 

F5-TTS: Diffusion Transformer with ConvNeXt V2, faster trained and inference.

E2 TTS: Flat-UNet Transformer, closest reproduction from paper.

Sway Sampling: Inference-time flow step sampling strategy, greatly improves performance
Thanks to all the contributors !
News

    2024/10/08: F5-TTS & E2 TTS base models on 🤗 Hugging Face, 🤖 Model Scope, 🟣 Wisemodel.

Installation

# Create a python 3.10 conda env (you could also use virtualenv)
conda create -n f5-tts python=3.10
conda activate f5-tts

# NVIDIA GPU: install pytorch with your CUDA version, e.g.
pip install torch==2.3.0+cu118 torchaudio==2.3.0+cu118 --extra-index-url https://download.pytorch.org/whl/cu118

# AMD GPU: install pytorch with your ROCm version, e.g. (Linux only)
pip install torch==2.5.1+rocm6.2 torchaudio==2.5.1+rocm6.2 --extra-index-url https://download.pytorch.org/whl/rocm6.2

# Intel GPU: install pytorch with your XPU version, e.g.
# Intel® Deep Learning Essentials or Intel® oneAPI Base Toolkit must be installed
pip install --pre torch torchaudio --index-url https://download.pytorch.org/whl/nightly/xpu

Then you can choose from a few options below:
1. As a pip package (if just for inference)

pip install git+https://github.com/SWivid/F5-TTS.git

2. Local editable (if also do training, finetuning)

git clone https://github.com/SWivid/F5-TTS.git
cd F5-TTS
# git submodule update --init --recursive  # (optional, if need bigvgan)
pip install -e .

3. Docker usage

# Build from Dockerfile
docker build -t f5tts:v1 .

# Or pull from GitHub Container Registry
docker pull ghcr.io/swivid/f5-tts:main

Inference
1. Gradio App

Currently supported features:

    Basic TTS with Chunk Inference
    Multi-Style / Multi-Speaker Generation
    Voice Chat powered by Qwen2.5-3B-Instruct
    Custom inference with more language support

# Launch a Gradio app (web interface)
f5-tts_infer-gradio

# Specify the port/host
f5-tts_infer-gradio --port 7860 --host 0.0.0.0

# Launch a share link
f5-tts_infer-gradio --share

2. CLI Inference

# Run with flags
# Leave --ref_text "" will have ASR model transcribe (extra GPU memory usage)
f5-tts_infer-cli \
--model "F5-TTS" \
--ref_audio "ref_audio.wav" \
--ref_text "The content, subtitle or transcription of reference audio." \
--gen_text "Some text you want TTS model generate for you."

# Run with default setting. src/f5_tts/infer/examples/basic/basic.toml
f5-tts_infer-cli
# Or with your own .toml file
f5-tts_infer-cli -c custom.toml

# Multi voice. See src/f5_tts/infer/README.md
f5-tts_infer-cli -c src/f5_tts/infer/examples/multi/story.toml

3. More instructions

    In order to have better generation results, take a moment to read detailed guidance.
    The Issues are very useful, please try to find the solution by properly searching the keywords of problem encountered. If no answer found, then feel free to open an issue.

Training
1. Gradio App

Read training & finetuning guidance for more instructions.

# Quick start with Gradio web interface
f5-tts_finetune-gradio

Evaluation
Development

Use pre-commit to ensure code quality (will run linters and formatters automatically)

pip install pre-commit
pre-commit install

When making a pull request, before each commit, run:

pre-commit run --all-files

Note: Some model components have linting exceptions for E722 to accommodate tensor notation
Acknowledgements

    E2-TTS brilliant work, simple and effective
    Emilia, WenetSpeech4TTS, LibriTTS, LJSpeech valuable datasets
    lucidrains initial CFM structure with also bfs18 for discussion
    SD3 & Hugging Face diffusers DiT and MMDiT code structure
    torchdiffeq as ODE solver, Vocos and BigVGAN as vocoder
    FunASR, faster-whisper, UniSpeech, SpeechMOS for evaluation tools
    ctc-forced-aligner for speech edit test
    mrfakename huggingface space demo ~
    f5-tts-mlx Implementation with MLX framework by Lucas Newman
    F5-TTS-ONNX ONNX Runtime version by DakeQQ

Citation

If our work and codebase is useful for you, please cite as:

@article{chen-etal-2024-f5tts,
      title={F5-TTS: A Fairytaler that Fakes Fluent and Faithful Speech with Flow Matching}, 
      author={Yushen Chen and Zhikang Niu and Ziyang Ma and Keqi Deng and Chunhui Wang and Jian Zhao and Kai Yu and Xie Chen},
      journal={arXiv preprint arXiv:2410.06885},
      year={2024},
}

License
Our code is released under MIT License. The pre-trained models are licensed under the CC-BY-NC license due to the training data Emilia, which is an in-the-wild dataset. Sorry for any inconvenience this may cause.
