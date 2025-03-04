from flask import Flask, render_template, request, redirect, url_for
import time
app = Flask(__name__)

keystroke_count = 0
last_typing_time = time.time()
inactivity_threshold = 5

def on_key_event(event):
        global last_typing_time
        last_typing_time = time.time()
    

@app.route('/', methods=['GET', 'POST'])
def index():
    global keystroke_count, last_typing_time
    typing_status = "No typing detected."

    if request.method == 'POST':
        user_input = request.form['text_input']
        
        keystroke_count += len(user_input)
        last_typing_time = time.time()
        return redirect(url_for('index'))
    
    
    current_time = time.time()
    if current_time - last_typing_time > inactivity_threshold:
        
        typing_status = "No typing detected for the last 5 seconds."
    else:
        typing_status = "Typing detected."
    time.sleep(1)

    return render_template('index.html', status=typing_status, keystrokes=keystroke_count)

if __name__ == '__main__':
    app.run(debug=True)
