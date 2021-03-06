__author__ = 'dmitriydmitrienko'
from django.template import Context
from django.template.loader import get_template
from django.template import Library


register = Library()


def get_context_template(element):
    template = get_template("kubeform/kube_form.html")
    context = Context({'form': element})
    return template, context


@register.filter
def kubecolumn(element):
    template, context = get_context_template(element)
    return template.render(context)


@register.filter
def kubeinline(element):
    template, context = get_context_template(element)
    context.update({'inline': True})
    return template.render(context)


@register.filter
def kubewidth(element, size):
    element_type = element.__class__.__name__.lower()
    if element_type == 'boundfield':
        try:
            attrs_field = element.field.widget.attrs
            attr_size = "width-%s" % size
            if 'class' in attrs_field:
                class_attr = element.field.widget.attrs['class']
                element.field.widget.attrs['class'] = class_attr + ' ' + attr_size
            element.field.widget.attrs.update({
                'class': attr_size
            })
        except Exception:
            return element
    return element
