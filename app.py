from flask import Flask
import multiprocessing
import GetChat

app = Flask(__name__)

current_process = None

def run_getLiveData(video_id):
    try:
        GetChat.getLiveData(video_id)
    except Exception as error:
        print(f'Error {error}')

@app.route('/<video_id>')
def post_videoid(video_id):
    global current_process

    if current_process and current_process.is_alive():
        current_process.terminate()
        current_process.join()

    current_process = multiprocessing.Process(target=run_getLiveData, args=(video_id,))
    current_process.start()
    
    return "LiveStream processing in the background"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
