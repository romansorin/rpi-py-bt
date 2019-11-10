#!/usr/local/bin/python3
from flask import Flask, render_template, request
from selenium import webdriver
from subprocess import call

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["OS"] = 'Windows'
app.config["HOST"] = '0.0.0.0'
app.config["PORT"] = '8090'

DRILL = 'drill'
DRILL_URL = 'https://www.youtube.com/watch?v=fc7XA4bo4bc'
BASS = 'bass'
BASS_URL = 'https://www.youtube.com/watch?v=H8pZmH5DHnQ'

options = webdriver.FirefoxOptions()
options.headless = True

if app.config["OS"] == 'Windows':
    executable_path = './geckodriver.exe'
elif app.config["OS"] == 'Linux':
    executable_path = '/home/pi/gecko-dev/target/armv7-unknown-linux-gnueabihf/release/geckodriver'

driver = webdriver.Firefox(
    executable_path=executable_path, options=options)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/start', methods=['POST'])
def start_sounds():
    sound_type = request.form['sound_type']

    if sound_type == DRILL:
        # driver.get(DRILL_URL)
        call(['cd %PROGRAMFILES%/VideoLAN/VLC/ && vlc.exe', DRILL_URL], shell=True)
    elif sound_type == BASS:
        driver.get(BASS_URL)

    # driver.find_element_by_class_name('ytp-play-button').click()
    return 'Started.'


@app.route('/end', methods=['POST'])
def end_sounds():
    driver.quit()

    return 'Ended.'


if __name__ == '__main__':
    app.run(host=app.config["HOST"], port=app.config["PORT"])
