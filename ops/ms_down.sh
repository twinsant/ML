#!/bin/bash
# Download models from modelscope to /Volumes/S8/models/Qwen3-TTS/$1
uv run modelscope download --model Qwen/$1  --local_dir /Volumes/S8/models/Qwen3-TTS/$1