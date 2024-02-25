from flask import Flask, request, render_template, jsonify
from google.generativeai import GenerativeModel, configure

app = Flask(__name__)

# Set up the AI model
configure(api_key="AIzaSyAQO8sBlnCZYvAU-h4Pg6Pna5vPVcbsRY8")

# Initialize the model
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

model = GenerativeModel(
    model_name="gemini-pro",
    generation_config=generation_config,
    safety_settings=safety_settings
)

# Define routes to serve static HTML pages
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bookanappointment')
def book_an_appointment():
    return render_template('bookanappointment.html')

@app.route('/bodymassindex')
def body_mass_index():
    return render_template('bodymassindex.html')

@app.route('/cycle')
def cycle():
    return render_template('cycle.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/userprofile')
def user_profile():
    return render_template('userprofile.html')

@app.route('/waterdrop')
def water_drop():
    return render_template('waterdrop.html')

@app.route('/homepage')
def home_page():
    return render_template('homepage.html')

@app.route('/contactus')
def contact_us():
    return render_template('contactus.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/virtualmeet')
def virtual_meet():
    return render_template('virtualmeet.html')

# Define route to handle AI response generation
@app.route('/generate_response', methods=['POST'])
def generate_response():
    # Get the prompt from the request data
    prompt = request.json.get('prompt')

    # List of allowed keywords
    allowed_keywords = [
        "fit", "health", "fitness", "cardio", "strength", "aerobic", "anaerobic",
        "interval", "core", "flexibility", "balance", "agility", "endurance", 
        "power", "speed", "recovery", "muscle", "fat", "bone", "skin", "organs", 
        "systems", "metabolism", "hormones", "nutrients", "energy", "weight", 
        "physique", "appearance", "nutrition", "food", "eating", "macronutrients", 
        "micronutrients", "calories", "carbohydrates", "proteins", "fats", "fiber", 
        "vitamins", "minerals", "water", "supplements", "meal", "portion", "calorie", 
        "junk", "healthy", "processed", "unprocessed", "workout", "routine", 
        "schedule", "duration", "progression", "abs", "ripped", "shredded", "v-cut", 
        "adonis", "washboard", "six-pack", "eight-pack", "ten-pack", "ldl", "hdl", 
        "triglycerides", "atherosclerosis", "heart", "stroke", "saturated", 
        "unsaturated", "monounsaturated", "polyunsaturated", "omega-3", "omega-6", 
        "trans", "well-being", "wellness", "vitality", "longevity", "disease", 
        "prevention", "chronic", "management", "mental", "emotional", "social", 
        "environmental", "beneficial", "positive", "favorable", "desirable", 
        "optimal", "ideal", "appearance", "physique", "body", "composition", 
        "muscle", "definition", "skin", "tone", "hair", "eyes", "smile", 
        "posture", "confidence", "amino", "essential", "non-essential", 
        "complete", "incomplete", "synthesis", "degradation", "breakdown", 
        "sugars", "starches", "fiber", "glucose", "fructose", "sucrose", 
        "lactose", "maltose", "dextrin", "glycogen", "polysaccharide", 
        "polymer", "amylose", "amylopectin", "diet", "eating", "improve"
    ]

    # Check if any of the allowed keywords are present in the prompt
    if any(keyword in prompt.lower() for keyword in allowed_keywords):
        # Generate the response using the AI model
        result = model.generate_content([prompt])
        response_parts = [part.text for part in result.parts]
        response = ' '.join(response_parts)
        return jsonify({'response': response})
    else:
        # Return a message indicating that the prompt is not related to the allowed topics
        return jsonify({'response': "Sorry, I'm not supposed to answer prompts that are not related to physical body, fitness, and diet."})

if __name__ == '__main__':
    app.run(debug=True)
