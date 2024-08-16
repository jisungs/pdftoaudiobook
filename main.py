
from gtts import gTTS
from PyPDF2 import PdfReader

def pdf_to_audio(pdf_file, output_audio, output_text):
    with open(pdf_file, 'rb') as file:

        reader = PdfReader(file)
        text = ""

        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
        
        # 텍스트 파일로 저장
        with open(output_text, 'w', encoding='utf-8') as text_file:
            text_file.write(text)
        print(f"Text saved as {output_text}")

        print('오디오북 저장이 시작됩니다.')
        tts = gTTS(text, lang='ko')
        tts.save(output_audio)
        print(f"오디오 북이 저장되었습니다. {output_audio}")

pdf_to_audio('little_prince.pdf', 'little_prince.mp3', 'output_text.txt')