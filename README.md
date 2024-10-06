A minimum viable product for a flask web application.

Users can enter their queries through a web interface and receive responses output on the screen from the LLM in the flask backend.

**Dependencies - `requirements.txt`**
<ul>
<li>flask</li>
<li>flask_cors</li>
<li>transformers</li>
</ul>


**Usage - `start.sh`**<br>
Clone the repository and run `./start.sh` in the bash terminal to install the required packages and launch the app.<br>
The app will be available at `localhost:3000`.<br>

A different model from the transformers library can easily be substituted in by amending this line of the code in `app.py`:<br>
`llm = pipeline("text-generation", model="gpt2")`
