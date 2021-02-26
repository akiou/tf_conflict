package aoka.sample;

import java.nio.file.Paths;
import org.tensorflow.SavedModelBundle;

public class Sample {
    public Sample() {
        String modelPath = "model/";
        SavedModelBundle savedModel = SavedModelBundle.load(
                Paths.get(modelPath).toFile().getAbsolutePath(), "serve");
    }
}
