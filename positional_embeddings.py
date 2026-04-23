import math
import numpy as np

"""
In the transformer architecture, positional embeddings are added to each token so the model knows their respective 
postion within the sequence. Below I have created a program that creates the positional embeddings for all tokens 
in a sequence. In the embeddings variable near the bottom, input the dimension for all tokens as well as the number 
of tokens in the sequence. 
"""


def create_embedding(position, dimension):
	"""
	Creates a positional embedding for a token within a sequence. Within the sine and cosine calls below the position 
	is divided by 10000^(2 * (vector position within sequence) / (dimension of all tokens)). As this increases it will 
	go from 1 to 100 to 1,000 to 10,000 ....
	position: position within the sequence
	dimension: 
	"""
	vector = np.array([])
	for i in range(int(dimension/2)):
    	vector = np.append(vector, math.sin(position / 10000**(2*i/dimension)))
    	vector = np.append(vector, math.cos(position / 10000**(2*i/dimension)))
	return vector 
  
def create_embedding_list(dimension, num_tokens):
  """
  Creates a numpy array populated with all positional embeddings for a sequence. 
  embedding_length: length of each individual embedding for a token
  num_tokens: number of tokens in the sequence
  """
  embedding_list = np.array([create_embedding(0,dimension)])
  
  for i in range(1,num_tokens):
      vector = create_embedding(i,dimension)
      embedding_list = np.vstack((embedding_list,vector))
    
  return embedding_list

# create the embeddings list with 10 tokens, each with a dimension of 4
embeddings = create_embedding_list(4,10)

# print out all of the embeddings 
for j in range(len(embeddings)):
  print(f"{j}: {embeddings[j]}")




