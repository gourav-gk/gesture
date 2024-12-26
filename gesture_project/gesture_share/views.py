from django.shortcuts import render, get_object_or_404
from .models import Image
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import SharedImage
import json
from django.utils.timezone import now


def home(request):
    images = Image.objects.all()
    return render(request, 'gallery/home.html', {'images': images})


def image_detail(request, pk):
    image = get_object_or_404(Image, pk=pk)
    return render(request, 'gallery/image_detail.html', {'image': image})


@csrf_exempt
def get_user_ip(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        image_name = data.get('imageName', '')
        user_ip = get_client_ip(request)

        # Save to database
        SharedImage.objects.create(image_name=image_name, user_ip=user_ip)

        return JsonResponse({'status': 'success', 'imageName': image_name, 'userIP': user_ip})
    return JsonResponse({'status': 'failed'}, status=400)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def receiver_view(request):
    return render(request, 'gallery/receiver.html')


def check_image(request):
    if request.method == 'GET':
        user_ip = request.META.get('REMOTE_ADDR')
        #image_record = SharedImage.objects.filter(user_ip=user_ip).last()  # Get the latest image for this IP
        image_record = SharedImage.objects.last()
        if image_record:
            image_record.delete()
            return JsonResponse({'image_name': image_record.image_name}, status=200)
        else:
            return JsonResponse({'message': 'No image found'}, status=404)


def capture_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        uploaded_image = request.FILES['image']
        title = f"Captured on {now().strftime('%Y-%m-%d %H:%M:%S')}"

        # Save the image to the database
        image = Image.objects.create(title=title, image=uploaded_image)
        return JsonResponse({'success': True, 'message': 'Image uploaded successfully', 'image_name': image.image.name})

    return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)


def camera_view(request):
    return render(request, 'gallery/camera.html')