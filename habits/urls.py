from rest_framework.routers import SimpleRouter

from habits.apps import HabitsConfig
from habits.views import HabitViewSet

app_name = HabitsConfig.name

router = SimpleRouter()
router.register(r"habits", HabitViewSet, basename="habits")

urlpatterns = []

urlpatterns += router.urls
