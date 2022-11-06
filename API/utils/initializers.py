from elasticsearch import Elasticsearch

from utils.feature_extraction import FeatureExtractor

INDEX_NAME = 'open-image'
SOURCE_NO_VEC = ['ImageID', 'OriginalURL', 'AuthorID', 'Title', 'tags','labels']
es = Elasticsearch(["http://localhost:9200"])
fe = FeatureExtractor("Data/pca.pkl")