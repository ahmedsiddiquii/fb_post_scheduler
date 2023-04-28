from django import forms
from .models import *

class post_form(forms.ModelForm):
    username = forms.CharField(required=False)
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        self.fields['every'].widget.attrs.update({'style': 'background-color:white;\
        	height:40px;\
        	margin-left: 50px;\
        	width:200px;\
        	border-radius:6px;\
        	color:black;\
        box-shadow: 0px 0px 30px 0px rgb(190, 190, 190);\
        '})
        # self.fields['post_as'] = forms.ChoiceField(choices=())
        if user:
            choices=self.instance.update_choices(user=user)
            self.fields['post_as'] = forms.ChoiceField(choices=choices)
        self.fields['post_as'].widget.attrs.update({'style': 'background-color:white;\
                	height:40px;\
                	margin-left: 50px;\
                	width:200px;\
                	border-radius:6px;\
                	color:black;\
                box-shadow: 0px 0px 30px 0px rgb(190, 190, 190);\
                '})
        # self.fields['post_as'] = for
    class Meta:
        model = PostModel
        fields = ['title', 'text', 'post_as',"every","time","image","username"]
        widgets = {
            'title': forms.TextInput(attrs={'style':'background-color:white;\
	height:40px;\
	margin-left: 50px;\
	width:1000px;\
	border-radius:6px;\
	color:black;\
box-shadow: 0px 0px 30px 0px rgb(190, 190, 190);\
',"name":"title"}),
            'text': forms.Textarea(attrs={'style':'background-color:white;\
	height:80px;\
	margin-left: 50px;\
	width:1000px;\
	border-radius:6px;\
	color:black;\
box-shadow: 0px 0px 30px 0px rgb(190, 190, 190);\
'}),
#             'post_as': forms.TextInput(attrs={'style':'background-color:white;\
# 	height:40px;\
# 	margin-left: 50px;\
# 	width:200px;\
# 	border-radius:6px;\
# 	color:black;\
# box-shadow: 0px 0px 30px 0px rgb(190, 190, 190);\
# '}),
        #     'every': forms.TextInput(attrs={'style': 'background-color:white;\
        # 	height:40px;\
        # 	margin-left: 50px;\
        # 	width:200px;\
        # 	border-radius:6px;\
        # 	color:black;\
        # box-shadow: 0px 0px 30px 0px rgb(190, 190, 190);\
        # '}),
            'time': forms.TimeInput(attrs={'style': 'background-color:white;\
        	height:40px;\
        	margin-left: 50px;\
        	width:200px;\
        	border-radius:6px;\
        	color:black;\
        box-shadow: 0px 0px 30px 0px rgb(190, 190, 190);\
        ','type':'time'}),
        #     'image': forms.(attrs={'style': 'background-color:white;\
        # 	height:40px;\
        # 	margin-left: 50px;\
        # 	width:1000px;\
        # 	border-radius:6px;\
        # 	color:black;\
        # box-shadow: 0px 0px 30px 0px rgb(190, 190, 190);\
        # '}),
            'group': forms.TextInput(attrs={'style': 'background-color:white;\
        	height:40px;\
        	margin-left: 50px;\
        	width:400px;\
        	border-radius:6px;\
        	color:black;\
        box-shadow: 0px 0px 30px 0px rgb(190, 190, 190);\
        '})
        }
