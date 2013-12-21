django-kube-form
================

Reusable Django app for display [kube forms](http://imperavi.com/kube/forms/ "kube forms")

## Installation
Install with pip: `pip install kubeform`

Add `'kubeform',` to INSTALLED_APPS

## Usage

Simple column form:

```html
{% load kube %}

<h2>Form</h2>
<form method="POST">
    {{ form|kubecolumn }}
    <p>
		  <input type="submit" class="btn" value="Send">
	  </p>
</form>
```

Simple inline form:

```html
{% load kube %}

<h2>Form</h2>
<form method="POST">
    {{ form|kubeinline }}
   <input type="submit" class="btn" value="Send">
</form>
```

Width fields:
```html
{% load kube %}

<h2>Form</h2>
<form method="POST">
  {{ form.title|kubewidth:"50" }}
  <input type="submit" class="btn" value="Send">
</form>
```
