import ThaiserEmotionModel

input_path = "test/0Anger.wav"  # Replace with your test audio file path
result = ThaiserEmotionModel.Thaiser(input_path)
print("Emotion Prediction Result:")
print(result)

