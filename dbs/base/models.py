from django.db import models
from accounts.models import CustomUser

class BaseModel(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, 
								related_name="%(app_label)s_%(class)s_created_by", blank=True, null=True)
	updated_at = models.DateTimeField(auto_now=True)
	manual_updated_at = models.DateTimeField(blank=True, null=True)
	updated_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
								related_name="%(app_label)s_%(class)s_updated_by", blank=True, null=True)
	deleted_at = models.DateTimeField(blank=True, null=True)
	deleted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
								related_name="%(app_label)s_%(class)s_deleted_by", blank=True, null=True)

	class Meta:
		abstract = True