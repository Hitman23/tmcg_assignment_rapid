from django.test import TestCase
from models import Groups


# Create your tests here.
class TestCharacter(TestCase):
    def setUp(self):
        Groups.objects.create(name='TMCG', number_of_contacts=3)

    def test_if_group_exists(self):
        groups = Groups.objects.first()
        self.assertEquals(groups.name, "TMCG")

    def test_if_number_exists(self):
        groups = Groups.objects.first()
        self.assertEquals(groups.number_of_contacts, 3)

    def test_if_number_is_int(self):
        groups = Groups.objects.first()
        numtype = type(groups.number_of_contacts)
        self.assertTrue(numtype, int)
