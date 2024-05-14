from Task import TeamLead

team_lead = TeamLead("Валентин", 100000, "QA", "Python", 5)

assert hasattr(team_lead, 'name')
assert hasattr(team_lead, 'salary')
assert hasattr(team_lead, 'department')
assert hasattr(team_lead, 'programming_language')
assert hasattr(team_lead, 'team_size')

print("")
print("Вітаю! Тест пройдено, всі атрибути в класі \"TeamLead\" є:)")