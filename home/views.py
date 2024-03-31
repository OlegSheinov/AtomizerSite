import base64
import os
import tempfile

import cv2
from django.http import HttpResponse, JsonResponse
from django.views import View


class GetFrameView(View):

    def post(self, request, *args, **kwargs):
        try:
            video = request.FILES.get('videoFile')
            if video:
                with tempfile.TemporaryDirectory() as tmp_path:
                    video_path = os.path.join(tmp_path, video.name)
                    with open(video_path, 'wb') as temp_file:
                        for chunk in video.chunks():
                            temp_file.write(chunk)
                    # открываем видео файл и получаем первый кадр
                    cap = cv2.VideoCapture(video_path)
                    ret, frame = cap.read()
                    # преобразуем первый кадр в формат base64
                    ret, buffer = cv2.imencode('.jpg', frame)
                    jpg_as_text = base64.b64encode(buffer).decode('utf-8')
                return JsonResponse({"first_frame": jpg_as_text}, status=200)
            else:
                return JsonResponse({"message": "not video"}, status=401)
        except BaseException as err:
            print(err)
