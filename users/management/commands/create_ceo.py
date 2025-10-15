"""
Management command to create a CEO user for the three-tier approval system
"""
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from users.models import Department

User = get_user_model()


class Command(BaseCommand):
    help = 'Create a CEO user for the three-tier approval system'

    def add_arguments(self, parser):
        parser.add_argument('--username', type=str, help='Username for the CEO (will be derived from email if not provided)')
        parser.add_argument('--email', type=str, default='ceo@company.com', help='Email for the CEO')
        parser.add_argument('--first-name', type=str, default='Chief', help='First name')
        parser.add_argument('--last-name', type=str, default='Executive Officer', help='Last name')
        parser.add_argument('--employee-id', type=str, default='CEO001', help='Employee ID')
        parser.add_argument('--password', type=str, help='Custom password (optional, defaults to ChangeMe123!)')

    def handle(self, *args, **options):
        email = options['email']
        first_name = options['first_name']
        last_name = options['last_name']
        employee_id = options['employee_id']
        custom_password = options.get('password', 'ChangeMe123!')
        
        # Extract username from email (everything before @)
        username = options.get('username')
        if not username:
            username = email.split('@')[0]
            
        self.stdout.write(f'Creating CEO with username: {username} and email: {email}')

        # Check if CEO user already exists
        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING(f'CEO user with username "{username}" already exists!')
            )
            return

        if User.objects.filter(email=email).exists():
            self.stdout.write(
                self.style.WARNING(f'User with email "{email}" already exists!')
            )
            return

        if User.objects.filter(employee_id=employee_id).exists():
            self.stdout.write(
                self.style.WARNING(f'User with employee ID "{employee_id}" already exists!')
            )
            return

        # Get or create Executive department
        executive_dept, created = Department.objects.get_or_create(
            name='Executive',
            defaults={'description': 'Executive leadership team'}
        )
        if created:
            self.stdout.write(f'Created Executive department')

        # Create CEO user
        ceo_user = User.objects.create_user(
            username=username,
            email=email,
            password=custom_password,
            first_name=first_name,
            last_name=last_name,
            employee_id=employee_id,
            role='ceo',
            department=executive_dept,
            is_staff=True,  # CEO should have admin access
            annual_leave_entitlement=30,  # CEO gets more leave
            is_active_employee=True
        )

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created CEO user:\n'
                f'  Username: {username}\n'
                f'  Email: {email}\n'
                f'  Employee ID: {employee_id}\n'
                f'  Password: {custom_password}\n'
                f'  Role: {ceo_user.role}\n'
                f'  Department: {ceo_user.department.name}\n\n'
                f'IMPORTANT: You can now login using email "{email}" and the password above!'
            )
        )