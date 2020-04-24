from django.test import TestCase
from reports.models import Report
from django.contrib.auth.models import User

class ReportTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username="TestUser")
        self.report1 = Report.objects.create(title="Match 1", content="The report from the match", date="10th January 2020", author=self.user1)

    def test_user_saved(self):
        self.assertGreater(self.user1.pk, 0)

    def test_report_saved(self):
        self.assertGreater(self.report1.pk, 0)

    def test_post_fk(self):
        self.assertEqual(self.report1.author.pk, self.user1.pk)
