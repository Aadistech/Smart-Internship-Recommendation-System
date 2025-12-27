import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import CountVectorizer

# Load dataset
data = pd.read_csv("internship_dataset.csv")

# Convert skills text into numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data['skills'])

# Train KNN model
knn = NearestNeighbors(n_neighbors=2, metric='cosine')
knn.fit(X)

def recommend_internship(student_skills):
    student_vector = vectorizer.transform([student_skills])
    distances, indices = knn.kneighbors(student_vector)

    recommendations = []
    for i in indices[0]:
        recommendations.append(data.iloc[i]['domain'])

    return recommendations
