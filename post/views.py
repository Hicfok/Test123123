from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404

# Получить все посты
class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

# Получить пост по ID
class PostDetail(APIView):
    def get(self, request, id):
        post = get_object_or_404(Post, id=id)
        serializer = PostSerializer(post)
        return Response(serializer.data)

# Создать новый пост
class PostCreate(APIView):
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Удалить пост по ID
class PostDelete(APIView):
    def delete(self, request, id):
        post = get_object_or_404(Post, id=id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post-list')  # Перенаправление на страницу с постами
    else:
        form = PostForm()
    return render(request, 'post/create_post.html', {'form': form})