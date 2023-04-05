from gptcache.utils import import_sbert
import_sbert()

import numpy as np
from sentence_transformers import SentenceTransformer


class SBERT:
    """Generate sentence embedding for given text using pretrained models of Sentence Transformers.

    Example:
        .. code-block:: python
        
            from gptcache.embedding import SBERT
            
            test_sentence = "Hello, world." 
            encoder = SBERT("paraphrase-albert-small-v2")
            embed = encoder.to_embeddings(test_sentence)
    """
    def __init__(self, model: str="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model)
        self.model.eval()
        self.__dimension = None

    def to_embeddings(self, data, **kwargs):
        if not isinstance(data, list):
            data = [data]
        emb = self.model.encode(data).squeeze(0)

        if not self.__dimension:
            self.__dimension = len(emb)
        return np.array(emb).astype('float32')
    
    @property
    def dimension(self):
        if not self.__dimension:
            self.__dimension == self.to_embeddings("foo")
        return self.__dimension