from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """Тестирует CRUD привычек"""

    def setUp(self):
        self.user = User.objects.create(username="test_user", password="testtest")
        self.user2 = User.objects.create(username="test_user2", password="testtest2")
        self.habit = Habit.objects.create(
            place="вокруг квартала",
            author=self.user,
            action="выходить на прогулку",
            time="сразу после ужина",
        )
        self.habit2 = Habit.objects.create(
            place="по дороге на работу",
            author=self.user2,
            action="ездить на велосипеде",
            time="по утрам",
            is_pleasant=True,
        )

    def test_habit_retrieve(self):
        url = reverse("habits:habits-detail", args=(self.habit.pk,))
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), self.habit.action)

    def test_habit_retrieve_forbidden(self):
        url = reverse("habits:habits-detail", args=(self.habit.pk,))
        self.client.force_authenticate(user=self.user2)
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_habit_list(self):
        url = reverse("habits:habits-list")
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(data.get("results")), Habit.objects.filter(author=self.user).count()
        )

    def test_habit_create(self):
        url = reverse("habits:habits-list")
        self.client.force_authenticate(user=self.user)
        habit_data = {
            "action": "Выпивать 10 стаканов воды",
            "place": "на работе",
            "time": "днем",
        }
        response = self.client.post(url, data=habit_data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data.get("action"), habit_data.get("action"))

    def test_habit_update(self):
        url = reverse("habits:habits-detail", args=(self.habit.pk,))
        self.client.force_authenticate(user=self.user)
        habit_data = {
            "action": "Выпивать 10 стаканов воды",
            "place": "на работе",
            "time": "днем",
        }
        response = self.client.patch(url, data=habit_data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), habit_data.get("action"))

        response = self.client.patch(url, data={"periodicity": 8})
        data = response.json()
        self.assertEqual(
            data,
            {
                "periodicity": [
                    "значение периодичности выполнения привычки должно быть не больше 7 дней"
                ]
            },
        )

        response = self.client.patch(url, data={"execution_time": 130})
        data = response.json()
        self.assertEqual(
            data,
            {
                "execution_time": [
                    "Значение времени выполнения привычки должно быть не больше 120 секунд"
                ]
            },
        )

        response = self.client.patch(
            url, data={"related_pleasant_habit": self.habit.pk}
        )
        data = response.json()
        self.assertEqual(
            data,
            {
                "related_pleasant_habit": [
                    "В связанные привычки можно добавлять только привычки с "
                    "признаком приятной привычки"
                ]
            },
        )

        response = self.client.patch(
            url, data={"related_pleasant_habit": self.habit2.pk, "reward": "Мороженое"}
        )
        data = response.json()
        self.assertEqual(
            data,
            {
                "non_field_errors": [
                    "Не допустим одновременный выбор связанной привычки и указание вознаграждения"
                ]
            },
        )

    def test_habit_update_pleasant(self):
        url = reverse("habits:habits-detail", args=(self.habit.pk,))
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(
            url, data={"is_pleasant": True, "reward": "Мороженое"}
        )
        data = response.json()
        self.assertEqual(
            data,
            {
                "non_field_errors": [
                    "У приятной привычки не может быть вознаграждения или связанной привычки"
                ]
            },
        )

    def test_habit_delete(self):
        self.client.force_authenticate(user=self.user)
        url = reverse("habits:habits-detail", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.count(), 1)
