#!/usr/bin/env bash
# Gera áudio de verdade com a voz neural, usando exatamente os arquivos embutidos no app
# (app/src/main/assets/tts), em um PC Linux x86_64. Útil para conferir a voz sem celular.
# Uso: tools/voz-neural/verificar.sh "Texto a falar" saida.wav
set -euo pipefail
cd "$(dirname "$0")"
V=v1.13.8
BASE=https://jitpack.io/com/github/k2-fsa/sherpa-onnx
mkdir -p build
[ -f build/jvm.jar ] || curl -sSL -o build/jvm.jar "$BASE/sherpa-onnx-jvm/$V/sherpa-onnx-jvm-$V.jar"
[ -f build/native.jar ] || curl -sSL -o build/native.jar "$BASE/sherpa-onnx-native-lib-linux-x64/$V/sherpa-onnx-native-lib-linux-x64-$V.jar"
CP=build/jvm.jar:build/native.jar
javac -cp "$CP" -d build TtsDemo.java
java -cp "$CP:build" TtsDemo ../../app/src/main/assets/tts pt_BR-faber-medium.onnx "${2:-amostra.wav}" "${1:-Atenção, Paula! Qual é a capital do Brasil?}" 2>&1 | grep -E "^ok|rror"
