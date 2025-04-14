def handle_text_query(query):
    if 'yellow' in query and 'leaf' in query:
        return "Possible Nitrogen Deficiency. Suggest adding compost or urea."
    elif 'brown spots' in query:
        return "Could be fungal infection. Try a copper-based fungicide."
    else:
        return "Sorry, I need more info to help you. Try uploading an image."
