from nltk.stem import WordNetLemmatizer

lemmatizer =WordNetLemmatizer()

print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("clean"))
print(lemmatizer.lemmatize("tries"))
print(lemmatizer.lemmatize("Sun"))
print("---------------------------")
print(lemmatizer.lemmatize("better",pos="a"))
print(lemmatizer.lemmatize("better"))
print(lemmatizer.lemmatize("worse",pos="a"))
print(lemmatizer.lemmatize("run",'v'))