from evaluate import load

bertscore = load("bertscore")
predictions_text =  """
#add predictions here
"""
predictions = [line.strip() for line in predictions_text.strip().split('\n') if line.strip()]

references_text =  """
#add references here
"""
references = [line.strip() for line in references_text.strip().split('\n') if line.strip()]

results = bertscore.compute(predictions=predictions, references=references, lang="pl", model_type="distilbert-base-uncased")
print(results)