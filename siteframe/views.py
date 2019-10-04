from django.shortcuts import render
from django.views.generic import View


class TestSiteframeView(View):
    def get(self, request):
        return render(request, 'siteframe/testsiteframe.html', {})
