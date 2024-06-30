#forms.py
from django import forms
from .models import Post # Post 모델 import

class PostBasedForm(forms.Form):
    image = forms.ImageField()
    content = forms.CharField(widget=forms.Textarea)

# Model Forms
class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post # Post 모델(models.py에 정의) 사용
        fields = '__all__' # Post 클래스의 모든 항목 가져오기

class PostCreateForm(PostModelForm):
    class Meta(PostModelForm.Meta):
        fields = ['image', 'content']

class PostUpdateForm(PostModelForm):
    class Meta(PostModelForm.Meta):
        fields=['image', 'content']

class PostDetailForm(PostModelForm):
    def __init__(self, *args, **kwargs):
        super(PostDetailForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].widget.attrs['disabled']=True
