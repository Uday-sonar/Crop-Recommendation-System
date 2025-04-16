import pickle

# Load the trained model from pickle
with open('crop1.pkl', 'rb') as f:
    model = pickle.load(f)

def crop_model(K, N, P, H, M, R, T):
    input_data = [[K, N, P, H, M, R, T]]
    prediction = model.predict(input_data)
    return prediction  