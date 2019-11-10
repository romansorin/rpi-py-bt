#!/usr/local/bin/python3
from flask import Flask, render_template, request
from selenium import webdriver
import vlc
import time

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["OS"] = 'Windows'

DRILL = 'drill'
BASS = 'bass'

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
        driver.get('https://www.youtube.com/watch?v=fc7XA4bo4bc&t=2683s')
    elif sound_type == BASS:
        driver.get('https://www.youtube.com/watch?v=H8pZmH5DHnQ&t=408s')

    driver.find_element_by_class_name('ytp-play-button').click()
    return 'Started.'


@app.route('/end', methods=['POST'])
def end_sounds():
    driver.quit()

    return 'Ended.'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
