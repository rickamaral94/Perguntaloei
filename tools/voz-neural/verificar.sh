#!/usr/bin/env bash
# Baixa a voz neural opcional exatamente como o app faz (mesma versão fixa do Hugging Face,
# mesmos arquivos e SHA-256 de NeuralVoicePack.kt), confere os hashes e gera áudio de verdade
# em um PC Linux x86_64. Útil para conferir a voz sem celular.
# Uso: tools/voz-neural/verificar.sh "Texto a falar" saida.wav
set -euo pipefail
cd "$(dirname "$0")"
V=v1.13.8
BASE=https://jitpack.io/com/github/k2-fsa/sherpa-onnx
mkdir -p build
[ -f build/jvm.jar ] || curl -sSL -o build/jvm.jar "$BASE/sherpa-onnx-jvm/$V/sherpa-onnx-jvm-$V.jar"
[ -f build/native.jar ] || curl -sSL -o build/native.jar "$BASE/sherpa-onnx-native-lib-linux-x64/$V/sherpa-onnx-native-lib-linux-x64-$V.jar"
KT=../../app/src/main/java/br/com/perguntaloei/voice/NeuralVoicePack.kt
URL=$(grep -oE 'https://huggingface.co/[^"]+' "$KT")
mkdir -p build/voz
grep -oE 'VoiceFile\((MODEL_FILE|"[^"]+"), [0-9_]+, "[0-9a-f]{64}"' "$KT" | while read -r line; do
  path=$(echo "$line" | sed -E 's/VoiceFile\(("?)([^",]+)"?, .*/\2/')
  [ "$path" = MODEL_FILE ] && path=pt_BR-faber-medium.onnx
  sha=$(echo "$line" | grep -oE '[0-9a-f]{64}')
  mkdir -p "build/voz/$(dirname "$path")"
  if ! echo "$sha  build/voz/$path" | sha256sum -c --status 2>/dev/null; then
    curl -sSL -o "build/voz/$path" "$URL/$path"
  fi
  echo "$sha  build/voz/$path" | sha256sum -c --quiet
done
echo "ok: arquivos da voz conferidos"
CP=build/jvm.jar:build/native.jar
javac -cp "$CP" -d build TtsDemo.java
java -cp "$CP:build" TtsDemo build/voz pt_BR-faber-medium.onnx "${2:-amostra.wav}" "${1:-Atenção, Paula! Qual é a capital do Brasil?}" 2>&1 | grep -E "^ok|rror"
