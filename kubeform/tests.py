from django import forms
from django.test import TestCase
from django.template import Template, Context


class TestKubeForm(forms.Form):
    text = forms.CharField(label='label_text')


class FilterTest(TestCase):
    def setUp(self):
        self.context = Context({'form': TestKubeForm()})

    def test_base_render(self):
        template = Template('{% load kube %}{{ form|kubecolumn }}')
        rendered = template.render(self.context)
        self.assertIn('<p>', rendered)

    def test_inline_filter(self):
        template = Template('{% load kube %}{{ form|kubeinline }}')
        rendered = template.render(self.context)
        self.assertIn('class="units-row"', rendered)

    def test_field_render(self):
        template = Template('{% load kube %}{{ form.text|kubewidth:"50" }}')
        rendered = template.render(self.context)
        self.assertIn('class="width-50"', rendered)