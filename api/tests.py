from rest_framework.test import APITestCase
from .models import Company, Employee


class CompanyEmployeeAPITest(APITestCase):

    def setUp(self):
        self.company = Company.objects.create(
            name="Test Company",
            location="Pune",
            company_type="startup"
        )

        Employee.objects.create(
            name="Test Employee",
            email="test@company.com",
            employee_position="intern",
            company=self.company
        )

    def test_employee_list(self):
        response = self.client.get("/api/v1/employees/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)

    def test_company_list(self):
        response = self.client.get("/api/v1/companies/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)

