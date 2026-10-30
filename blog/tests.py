from django.test import SimpleTestCase


class ErrorPageDemoTests(SimpleTestCase):
    def test_404_demo_displays_page_with_not_found_status(self):
        response = self.client.get("/test-404/")

        self.assertEqual(response.status_code, 404)
        self.assertContains(response, "Page Not Found", status_code=404)

    def test_500_demo_displays_page_with_server_error_status(self):
        response = self.client.get("/test-500/")

        self.assertEqual(response.status_code, 500)
        self.assertContains(response, "Server Error", status_code=500)
