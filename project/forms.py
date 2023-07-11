from django import forms
from django.core.exceptions import ValidationError
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "slug",
            "description",
        ]

    def clean_name(self):
        name = self.cleaned_data.get('name')
        # Validar que el nombre no esté vacío
        if not name:
            raise ValidationError("El nombre es obligatorio.")
        # Validar longitud mínima
        if len(name) < 3:
            raise ValidationError("El nombre debe tener al menos 3 caracteres.")
        return name

    def clean_slug(self):
        slug = self.cleaned_data.get('slug')
        # Validar que el slug no esté vacío
        if not slug:
            raise ValidationError("El slug es obligatorio.")
        # Validar que el slug sea único
        if Project.objects.filter(slug=slug).exists():
            raise ValidationError("El slug ya está en uso.")
        # Validar que el slug esté en minúsculas
        if not slug.islower():
            raise ValidationError("El slug debe estar en minúsculas.")
        return slug

    def clean_description(self):
        description = self.cleaned_data.get('description')
        # Validar que la descripción no esté vacía
        if not description:
            raise ValidationError("La descripción es obligatoria.")
        # Validar longitud máxima
        if len(description) > 200:
            raise ValidationError("La descripción debe tener menos de 200 caracteres.")
        return description