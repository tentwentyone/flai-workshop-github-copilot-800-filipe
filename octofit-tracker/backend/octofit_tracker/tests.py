from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            name='Test User',
            email='testuser@example.com',
            password='testpass123'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.name, 'Test User')
        self.assertEqual(self.user.email, 'testuser@example.com')

    def test_user_str(self):
        self.assertEqual(str(self.user), 'Test User')


class TeamModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(
            name='Team Alpha',
            members=['user1', 'user2']
        )

    def test_team_creation(self):
        self.assertEqual(self.team.name, 'Team Alpha')

    def test_team_str(self):
        self.assertEqual(str(self.team), 'Team Alpha')


class ActivityModelTest(TestCase):
    def setUp(self):
        self.activity = Activity.objects.create(
            user='Test User',
            activity_type='Running',
            duration='30 minutes',
            date='2024-01-01'
        )

    def test_activity_creation(self):
        self.assertEqual(self.activity.activity_type, 'Running')

    def test_activity_str(self):
        self.assertEqual(str(self.activity), 'Test User - Running')


class LeaderboardModelTest(TestCase):
    def setUp(self):
        self.entry = Leaderboard.objects.create(
            user='Test User',
            score=100
        )

    def test_leaderboard_creation(self):
        self.assertEqual(self.entry.score, 100)

    def test_leaderboard_str(self):
        self.assertEqual(str(self.entry), 'Test User: 100')


class WorkoutModelTest(TestCase):
    def setUp(self):
        self.workout = Workout.objects.create(
            name='Morning Run',
            description='A quick morning run to start the day',
            duration='30 minutes'
        )

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, 'Morning Run')

    def test_workout_str(self):
        self.assertEqual(str(self.workout), 'Morning Run')


class UserAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            name='API User',
            email='apiuser@example.com',
            password='apipass123'
        )

    def test_list_users(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        data = {'name': 'New User', 'email': 'newuser@example.com', 'password': 'newpass123'}
        response = self.client.post('/api/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_user(self):
        response = self.client.get(f'/api/users/{self.user.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TeamAPITest(APITestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team', members=[])

    def test_list_teams(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_team(self):
        data = {'name': 'New Team', 'members': []}
        response = self.client.post('/api/teams/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ActivityAPITest(APITestCase):
    def setUp(self):
        self.activity = Activity.objects.create(
            user='Test User',
            activity_type='Cycling',
            duration='45 minutes',
            date='2024-01-01'
        )

    def test_list_activities(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_activity(self):
        data = {
            'user': 'Test User',
            'activity_type': 'Swimming',
            'duration': '60 minutes',
            'date': '2024-01-02'
        }
        response = self.client.post('/api/activities/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LeaderboardAPITest(APITestCase):
    def setUp(self):
        self.entry = Leaderboard.objects.create(user='Top User', score=500)

    def test_list_leaderboard(self):
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_leaderboard_entry(self):
        data = {'user': 'Another User', 'score': 250}
        response = self.client.post('/api/leaderboard/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class WorkoutAPITest(APITestCase):
    def setUp(self):
        self.workout = Workout.objects.create(
            name='Yoga Session',
            description='Relaxing yoga session',
            duration='60 minutes'
        )

    def test_list_workouts(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_workout(self):
        data = {
            'name': 'HIIT Training',
            'description': 'High intensity interval training',
            'duration': '20 minutes'
        }
        response = self.client.post('/api/workouts/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class APIRootTest(APITestCase):
    def test_api_root(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_root_via_api_path(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
