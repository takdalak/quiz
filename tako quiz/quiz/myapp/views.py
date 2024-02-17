from django.shortcuts import render
from .db.mock_data import mock_db

def employees(request):
    employees = []

    for employee in mock_db:
        employees.append({
            'id': employee['id'],
            'name': employee['name'],
            'surname': employee['surname'],
            'stack': employee['stack'],
            'team_lead': employee['team_lead'],
        })

    return render(request, 'employees.html', {'employees': employees})

def stacks(request):
    stacks_set = set()
    stacks = []

    for employee in mock_db:
        stack = employee['stack']
        if stack not in stacks_set:
            stacks_set.add(stack)
            stack_users = [{'name': employee['name'], 'surname': employee['surname']}]
            stacks.append({'stack': stack, 'users': stack_users})
        else:
            for stack_data in stacks:
                if stack_data['stack'] == stack:
                    stack_data['users'].append({'name': employee['name'], 'surname': employee['surname']})
                    break

    return render(request, 'stacks.html', {'stacks': stacks})


def team_leads(request):
    team_leads_set = set()
    team_leads = []

    for employee in mock_db:
        if employee['team_lead'] not in team_leads_set:
            team_leads_set.add(employee['team_lead'])
            users = []
            for emp in mock_db:
                if emp['team_lead'] == employee['team_lead']:
                    users.append({'name': emp['name'], 'surname': emp['surname']})
            team_leads.append({
                'name': employee['team_lead'], 
                'users': users
            })

    return render(request, 'team_leads.html', {'team_leads': team_leads})


def home(request):
    return render(request, 'home.html')
