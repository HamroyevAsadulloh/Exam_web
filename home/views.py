import requests
from django.shortcuts import render
from django.views import View



class IndexView(View):
    def get(self, request):
        services = requests.get('http://127.0.0.1:8000/api/service-web/').json()
        businesses = requests.get('http://127.0.0.1:8000/api/busines-web/').json()
        users = requests.get('http://127.0.0.1:8000/api/users-web/').json()
        clients = requests.get('http://127.0.0.1:8000/api/client-web/').json()
        comments = requests.get('http://127.0.0.1:8000/api/comment-web/').json()
        faqs = requests.get('http://127.0.0.1:8000/api/faqs-web/').json()
        context = {
            'services':services,
            'businesses': businesses,
            'users': users,
            'clients': clients,
            'comments': comments,
            'faqs': faqs,
        }
        return render(request, 'index.html', context)


class ServiceView(View):
    def get(self, request):
        services = requests.get('http://127.0.0.1:8000/api/service-web/').json()
        clients = requests.get('http://127.0.0.1:8000/api/client-web/').json()
        context = {
            'services':services,
            'clients': clients,
        }
        return render(request, 'service.html',context)


class ClientView(View):
    def get(self, request):
        clients = requests.get('http://127.0.0.1:8000/api/client-web/').json()
        context = {
            'clients': clients,
        }
        return render(request, 'testimonial.html',context)



class AboutView(View):
    def get(self, request):
        businesses = requests.get('http://127.0.0.1:8000/api/busines-web/').json()
        users = requests.get('http://127.0.0.1:8000/api/users-web/').json()
        context = {
            'businesses': businesses,
            'users': users,
        }
        return render(request, 'about.html')






class BusinesView(View):
    def get(self, request):
        businesses = requests.get('http://127.0.0.1:8000/api/busines-web/').json()
        context = {
            'businesses':businesses,
        }
        return render(request, 'feature.html',context)

class UsersView(View):
    def get(self, request):
        users = requests.get('http://127.0.0.1:8000/api/users-web/').json()
        context = {
            'users':users,
        }
        return render(request, 'team.html',context)


# class CommentView(View):
#     def get(self, request):
#         users = requests.get('http://127.0.0.1:8000/api/comment-web//').json()
#         context = {
#             'comment':comment,
#         }
#         return render(request, 'blog.html',context)





class FaqsView(View):
    def get(self, request):
        faqs = requests.get('http://127.0.0.1:8000/api/faqs-web/').json()
        context = {
            'faqs': faqs,
        }
        return render(request, 'FAQs.html')





class BlogView(View):
    def get(self, request):
        comments = requests.get('http://127.0.0.1:8000/api/comment-web/').json()
        context = {
            'comments': comments,
        }

        return render(request, 'blog.html',context)


















#
#
#

#
#
# class ServiceView(View):
#     def get(self, request):
#         service = requests.get('http//:localhost:8000/api/service-web').json()
#         context = {
#             'service':service
#         }
#         return render(request, 'service.html')
#
#
# class BusinesView(View):
#     def get(self, request):
#         busines = requests.get('http//:localhost:8000/api/busines-web').json()
#         context = {
#             'busines':busines
#         }
#         return render(request, 'feature.html')
#
#
# class UserView(View):
#     def get(self, request):
#         users = requests.get('http//:localhost:8000/api/users-web').json()
#         context = {
#             'users':users
#         }
#         return render(request, 'team.html')
#
#
# class ClientView(View):
#     def get(self, request):
#         client = requests.get('http//:localhost:8000/api/client-web').json()
#         context = {
#             'client':client
#         }
#         return render(request, 'testimonial.html')
#
#
# class CommentView(View):
#     def get(self, request):
#         comment = requests.get('http//:localhost:8000/api/comment-web').json()
#         context = {
#             'comment':comment
#         }
#         return render(request, 'blog.html')
#
#
# class FaqView(View):
#     def get(self, request):
#         faq = requests.get('http//:localhost:8000/api/faqs-web').json()
#         context = {
#             'faq':faq
#         }
#         return render(request, 'FAQ.html')