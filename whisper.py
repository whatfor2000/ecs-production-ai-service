from transformers import WhisperForConditionalGeneration, WhisperProcessor
import librosa

import torch
from transformers import WhisperForConditionalGeneration, WhisperProcessor
import librosa
import gc

def Speechtotext(path: str) -> str:
    """
    Get the transcription from audio path
    
    Args:
        path(str): path to audio file (can be load with librosa)
        
    Returns:
        str: transcription
    """
    print(f"Loading Whisper model for {path}...")
    device = "cpu" # Force CPU for quantization compatibility
    
    try:
        # Load processor
        processor = WhisperProcessor.from_pretrained("juierror/whisper-base-thai", language="Thai", task="transcribe")
        
        # Load model
        model = WhisperForConditionalGeneration.from_pretrained("juierror/whisper-base-thai")
        
        # Quantize model to reduce memory usage
        print("Quantizing Whisper model...")
        model = torch.quantization.quantize_dynamic(
            model, {torch.nn.Linear}, dtype=torch.qint8
        )
        
        # Load and process audio
        audio, sr = librosa.load(path, sr=16000)
        input_features = processor(audio, sampling_rate=16000, return_tensors="pt").input_features
        
        # Generate transcription
        generated_tokens = model.generate(
            input_features=input_features,
            max_new_tokens=255,
            language="Thai"
        )
        
        transcriptions = processor.tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
        result = transcriptions[0]
        
        return result
        
    except Exception as e:
        print(f"Error in Speechtotext: {e}")
        return ""
        
    finally:
        # Cleanup to free memory
        print("Cleaning up Whisper model...")
        if 'model' in locals():
            del model
        if 'processor' in locals():
            del processor
        if 'input_features' in locals():
            del input_features
        if 'generated_tokens' in locals():
            del generated_tokens
        
        gc.collect()

