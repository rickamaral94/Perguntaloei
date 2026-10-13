import com.k2fsa.sherpa.onnx.*;

public class TtsDemo {
    public static void main(String[] args) {
        String dir = args[0];
        String model = args[1];
        String out = args[2];
        String text = args[3];
        OfflineTtsVitsModelConfig vits = OfflineTtsVitsModelConfig.builder()
            .setModel(dir + "/" + model).setTokens(dir + "/tokens.txt").setDataDir(dir + "/espeak-ng-data")
            .setNoiseScale(0.667f).setNoiseScaleW(0.8f).setLengthScale(1.0f).build();
        OfflineTtsModelConfig mc = OfflineTtsModelConfig.builder().setVits(vits).setNumThreads(2).setDebug(false).build();
        OfflineTtsConfig cfg = OfflineTtsConfig.builder().setModel(mc).build();
        OfflineTts tts = new OfflineTts(cfg);
        long t0 = System.currentTimeMillis();
        GeneratedAudio audio = tts.generate(text, 0, 1.0f);
        long ms = System.currentTimeMillis() - t0;
        audio.save(out);
        float[] s = audio.getSamples();
        double rms = 0; for (float x : s) rms += x * x; rms = Math.sqrt(rms / s.length);
        System.out.printf("ok %s: %d amostras, %d Hz, %.2fs de áudio em %d ms, rms=%.3f%n", out, s.length, audio.getSampleRate(), s.length / (double) audio.getSampleRate(), ms, rms);
        tts.release();
    }
}
