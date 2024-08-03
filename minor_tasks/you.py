from pytube import YouTube

YouTube('https://youtu.be/57ATmXx-uUk?si=m92TboYQ5iv2Uwfv').streams.first().download()