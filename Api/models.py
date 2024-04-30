from django.db import models


class Department(models.Model):
    dept_name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)

    def __str__(self):
        return self.dept_name


class Service(models.Model):
    STATUS_CHOICES = [
        ('Manual', 'Manual'),
        ('Digital', 'Digital'),
    ]
    ECITIZEN_CHOICES = [
        ('yes', 'Yes'),
        ('No', 'No'),
    ]
    ENHANCEMENT_CHOICES = [
        ('yes', 'Yes'),
        ('No', 'No'),
    ]
    YEAR_CHOICES = [
        ('none', 'None'),
        ('Y1-2023/24', 'Y1-2023/24'),
        ('Y2-2024/25', 'Y2-2024/25'),
        ('Y3-2025/26', 'Y3-2025/26'),
        ('Y4-2026/27', 'Y4-2026/27'),
    ]

    service_name = models.CharField(max_length=100)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    timeline = models.CharField(
        max_length=20, choices=YEAR_CHOICES, blank=True, null=True)
    ecitizen = models.CharField(max_length=3, choices=ECITIZEN_CHOICES)
    enhancement = models.CharField(max_length=3, choices=ENHANCEMENT_CHOICES)
    legal_instrument = models.ForeignKey(
        'LegalInstrument', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.service_name


class LegalInstrument(models.Model):
    name = models.CharField(max_length=100)
    requires_change = models.BooleanField(default=False)
    change_text = models.TextField()

    def __str__(self):
        return self.name
