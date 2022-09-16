from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register('category', CategoryViewset, basename='CategoryViewset')
router.register('profession', ProfessionViewset, basename='ProfessionViewset')
router.register('skill', SkillViewset, basename='SkillViewset')
