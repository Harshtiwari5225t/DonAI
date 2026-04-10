import pandas as pd

from flask import Flask, request, jsonify, send_from_directory
import pyjokes
df=pd.read_csv("airlines_flights_data.csv")

app=Flask(__name__, static_folder='.', static_url_path='')


def Dora(user_input):
    
        query=user_input.lower()
    
        if "bye" in query:
            return "Dora: Dora ra Dora ra"
        elif "joke" in query:
            return pyjokes.get_joke()
        elif "dora" in query or "hi" in query:
            return "Dora: Kya hua nobita"

        elif "name" in query:
            return "Dora: Doraemon hu yaar"
         
        
        elif "help" in query:
            return "Dora: Gian ne fir mara kya?? AA gya fir se pit ke!!!"

        elif "flight" in query  or "book" in query  :
            return "Dora: Sure! can you please please tell me whether you want a domestic or international flight?"

            

        elif "domestic" in query or "dome" in query:
            return "Dora: Enter your Source and Destination"

                # Source=input("Dora: Enter the Nearest airport or the source airport: ").capitalize()
                # dest=input("Dora: Enter the Destination: ").capitalize
                # clas=input("Dora: Enter the class? economy or bussiness  :  ").capitalize()

                # if clas!="Economy":
                #     print("Dora: Sorry!!! We cant help you")
                #     return "Sorry we cant do it"

                # #day=input("Enter the days left for flight booking:  ")
                # stop=input("Dora: Enter the minimum stops you can take during flight? zero or one or two like that:  ").lower()
               
                # arrival=input("Dora:Enter the arrival time? Evening or Night or Morning or Early_Morning:  ").capitalize()
                
                # filter_df=df.query('source_city==@Source & destination_city==@dest  & stops==@stop & arrival_time==@arrival')

                # print(filter_df)
                
                # print()
                # print("Dora: This is the list of available flights suitable for you!!")

        elif "inter" in query or "international" in query:
            return "Dora: Sorry I cant help you with international flight booking"
        elif "gadget" in query:
            return "dukkan thodi khol rakhi hai meine!!! bada aaya shizuka ko impress krne wala>>"
        else:
            return "Dora: ye kya bakk rhe ho!!!"

# DoraFlight() 


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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)