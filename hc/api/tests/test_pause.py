from hc.api.models import Check
from hc.test import BaseTestCase


class PauseTestCase(BaseTestCase):

    def test_it_works(self):
        check = Check(user=self.alice, status="up")
        check.save()

        url = "/api/v1/checks/%s/pause" % check.code
        r = self.client.post(url, "", content_type="application/json",
                             HTTP_X_API_KEY="abc")

        ### Assert the expected status code and check's status
        check.refresh_from_db()
        self.assertEqual(200, r.status_code)
        self.assertEqual('paused', check.status)

    def test_it_validates_ownership(self):
        check = Check(user=self.bob, status="up")
        check.save()

        url = "/api/v1/checks/%s/pause" % check.code
        r = self.client.post(url, "", content_type="application/json",
                             HTTP_X_API_KEY="abc")
        self.assertEqual(r.status_code, 400)

        ### Test that it only allows post requests
        r = self.client.get(url, "", content_type="application/json",
                            HTTP_X_API_KEY="abc")

        self.assertEqual(r.status_code, 405)

        r = self.client.put(url, "", content_type="application/json",
                            HTTP_X_API_KEY="abc")

        self.assertEqual(r.status_code, 405)

        r = self.client.patch(url, "", content_type="application/json",
                              HTTP_X_API_KEY="abc")

        self.assertEqual(r.status_code, 405)

        r = self.client.delete(url, "", content_type="application/json",
                               HTTP_X_API_KEY="abc")

        self.assertEqual(r.status_code, 405)

        r = self.client.options(url, "", content_type="application/json",
                                HTTP_X_API_KEY="abc")

        self.assertEqual(r.status_code, 405)
