# tkinter-translation-app

<p align="center">
  <br> Simple Translation Application in Python using Tkinter <br><br>
  <img src="https://user-images.githubusercontent.com/80552425/174131604-437ccc50-fab0-445d-a567-6957098ac2a1.jpg" width="500" title="hover text">
</p>

# About

By default the program will detect korean language (hangul) and translate it into english.
<br> You can also adjust and costumize it into your desired language.

<p align="justify">This program consist of 2 main function: text detection & text translation. 
<br> To detect the text from image i used EasyOCR & OpenCV. 
  After detecting the text, first you need to change it from list to string datatype (deep_translator can't process list) which you can see it on our sub function listToString(). After it you can finally translate the text. 
  For text translation i used deep translator, a free and unlimited tool to translate between languages (no need to build a RNN architecture again). 
  From there i import 2 translator which are GoogleTranslator and MyMemory. 
  You may change the translator type and also see the documentation <a href="https://pypi.org/project/deep-translator">here</a>. 
  I'm using tkinter to make the GUI that can you freely edit the frames, buttons, and labels according to your taste. I also already included the jupyter notebook file to show the whole processes.</p>


# Library Used:
- TKinter
- PIL
- Numpy
- EasyOCR
- OpenCV (CV2)
- Matplotlib
- Deep_Translator

# Image Used
I used image from a comic named "백작가의 사생아가 결혼하면" on KakaoWebtoon episode 3 (You can read the first 3 episodes for free <a href="https://webtoon.kakao.com/content/%EB%B0%B1%EC%9E%91%EA%B0%80%EC%9D%98-%EC%82%AC%EC%83%9D%EC%95%84%EA%B0%80-%EA%B2%B0%ED%98%BC%ED%95%98%EB%A9%B4/2824">here</a>).
