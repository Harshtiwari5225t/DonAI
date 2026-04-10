
from flask import Flask, request, jsonify, send_from_directory
import pyjokes
import wikipedia

app=Flask(__name__, static_folder='.', static_url_path='')





def search_for_meaning(word_query):
    word = word_query.replace("meaning of", "").replace("search for", "").replace("what is", "").strip()
    if not word:
        return "Please specify a word you want the meaning for."
        
    try:
        summary = wikipedia.summary(word, sentences=3)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        # Handle cases where the search term is ambiguous (multiple options)
        return f"There are multiple results for {word}. Could you be more specific?"
    except wikipedia.exceptions.PageError:
        return f"Sorry, I couldn't find a clear definition for {word} on Wikipedia."
    except Exception as e:
        return f"An error occurred during the search: {e}"

def Dora(user_input):
    
        query=user_input.lower()
    
        if "bye" in query:
            return "Dora:Good Bye!! Have a nice day"
        elif "joke" in query:
            return pyjokes.get_joke()
        elif "dora" in query or "hi" in query:
            return "Dora: Yes BOSS!! Tell me what to do"
        elif "name" in query:
            return "Dora: Dora, A ChatBot knows as DonAI named Dora"
        elif "what" in query or "who" in query or "what" in query:
            return "Dora: "+search_for_meaning(query)
        elif "help" in query:
            return "Dora: Tell me what is the problem"

        elif "flight" in query  or "book" in query  :
            return "Dora: Sure! can you please please tell me whether you want a domestic or international flight?"

        elif "domestic" in query or "dome" in query:
            return "Dora: Enter your Source and Destination"
        elif "from" in query:
            return "LOL !! Fool I can only have a chat with you"
        elif "inter" in query or "international" in query:
            return "Dora: Sorry I cant help you with international flight booking"
        elif "gadget" in query:
            return "dukkan thodi khol rakhi hai meine!!! bada aaya shizuka ko impress krne wala>>"
        else:
            return "Dora: Can't understand what are you asking!!!"




@app.route("/")
def home():
    return send_from_directory('.','DonAI.html')

@app.route("/chat",methods=["POST"])
def chat():
    data=request.json
    user_message=data.get("message")
    response=Dora(user_message)
    
    return jsonify({"response": response})

if __name__=="__main__":
    print("Doraemon is running!! Visit http://127.0.0.1:5500/DonAI.html  in your browser")
    print("Serving DonAI.html file")
    app.run(debug=True)

