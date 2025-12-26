from sklearn.metrics.pairwise import cosine_similarity

def cosine_sim(vec1, vec2):
    return cosine_similarity(vec1, vec2)[0][0]

