import torch
import itertools

embeddings_str = []
labels = []

def parse_embedding(embedding_str):
    # Assuming embeddings are enclosed in square brackets and comma-separated
    values = [float(val.strip('[],')) for val in embedding_str.split()]
    return torch.tensor(values)

embeddings_str.append(open("/Users/rohithpallamreddy/Documents/NONSTS/Amrutham.txt", "r", encoding="utf-8").read())
embeddings_str.append(open("/Users/rohithpallamreddy/Documents/NONSTS/WirallyR.txt", "r", encoding="utf-8").read())
embeddings_str.append(open("/Users/rohithpallamreddy/Documents/NONSTS/Mahathali.txt", "r", encoding="utf-8").read())
embeddings_str.append(open("/Users/rohithpallamreddy/Documents/NONSTS/ChillMama.txt", "r", encoding="utf-8").read())
embeddings_str.append(open("/Users/rohithpallamreddy/Documents/NONSTS/WirallyJ.txt", "r", encoding="utf-8").read())
embeddings_str.append(open("/Users/rohithpallamreddy/Documents/NONSTS/TV9.txt", "r", encoding="utf-8").read())
embeddings_str.append(open("/Users/rohithpallamreddy/Documents/NONSTS/ETV.txt", "r", encoding="utf-8").read())
embeddings_str.append(open("/Users/rohithpallamreddy/Documents/NONSTS/TTD.txt", "r", encoding="utf-8").read())
embeddings_str.append(open("/Users/rohithpallamreddy/Documents/NONSTS/Vahchef.txt", "r", encoding="utf-8").read())
embeddings_str.append(open("/Users/rohithpallamreddy/Documents/NONSTS/FoodReviewer.txt", "r", encoding="utf-8").read())
embeddings_str.append(open("/Users/rohithpallamreddy/Documents/NONSTS/AST.txt", "r", encoding="utf-8").read())
embeddings_str.append(open("/Users/rohithpallamreddy/Documents/NONSTS/PrasadTech.txt", "r", encoding="utf-8").read())
embeddings_str.append(open("/Users/rohithpallamreddy/Documents/NONSTS/KarthikaDeepam.txt", "r", encoding="utf-8").read())
embeddings_str.append(open("/Users/rohithpallamreddy/Documents/NONSTS/Brahmamudi.txt", "r", encoding="utf-8").read())
embeddings_str.append(open("/Users/rohithpallamreddy/Documents/NONSTS/MEK1.txt", "r", encoding="utf-8").read())
embeddings_str.append(open("/Users/rohithpallamreddy/Documents/NONSTS/MEK2.txt", "r", encoding="utf-8").read())
embeddings_str.append(open("/Users/rohithpallamreddy/Documents/NONSTS/BigBoss1.txt", "r", encoding="utf-8").read())
embeddings_str.append(open("/Users/rohithpallamreddy/Documents/NONSTS/BiggBoss2.txt", "r", encoding="utf-8").read())
embeddings_str.append(open("/Users/rohithpallamreddy/Documents/NONSTS/Aha1.txt", "r", encoding="utf-8").read())
embeddings_str.append(open("/Users/rohithpallamreddy/Documents/NONSTS/Aha2.txt", "r", encoding="utf-8").read())
labels.append("Amr")
labels.append("WR")
labels.append("Maha")
labels.append("Chill")
labels.append("WJ")
labels.append("TV9")
labels.append("ETV")
labels.append("TTD")
labels.append("Vah")
labels.append("Food")
labels.append("AST")
labels.append("Tech")
labels.append("KD")
labels.append("BrMu")
labels.append("MEK1")
labels.append("MEK2")
labels.append("BB1")
labels.append("BB2")
labels.append("Aha1")
labels.append("Aha2")

embeddings = [parse_embedding(embedding_str) for embedding_str in embeddings_str]

# Calculate cosine similarity for every combination
similarities = []
combinations = list(itertools.combinations(zip(labels, embeddings), 2))
for (label1, emb1), (label2, emb2) in combinations:
    similarity = torch.nn.functional.cosine_similarity(emb1.unsqueeze(0), emb2.unsqueeze(0)).item()
    similarities.append((label1, label2, similarity))

# Print out the results
label = ""
for label1, label2, similarity in similarities:
    if label != label1:
        print()
    print(f"{similarity:.2f}")
    label = label1