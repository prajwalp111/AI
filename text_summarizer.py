# preview : https://colab.research.google.com/drive/1oDTfGizrk3HE3MPb-gaVictHG1Tukrx-#scrollTo=4dKrycxCIjbH



from transformers import pipeline
summarizer = pipeline("summarization")

def summarize_text(text):
	summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
	return summary[0]['summary_text']
text =input('enter the texy u want to summarize') 
summarized_text = summarize_text(text)

print("Original Text:\n", text)
print("\nSummarized Text:\n", summarized_text)
