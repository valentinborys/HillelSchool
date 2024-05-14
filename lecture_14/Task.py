class Employee:
    def name(self):
        pass

    def salary(self):
        pass



class Manager(Employee):
    def __init__(self, name, salary, department):
        self._name = name
        self._salary = salary
        self._department = department

    def name(self):
        return self._name

    def salary(self):
        return self._salary

    def department(self):
        return self._department


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        self._name = name
        self._salary = salary
        self._programming_language = programming_language

    def name(self):
        return self._name

    def salary(self):
        return self._salary

    def programming_language(self):
        return self._programming_language



class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self._team_size = team_size

    def team_size(self):
        return self._team_size



team_lead = TeamLead("Валентин", 100000, "QA", "Python", 5)

print(team_lead.name())
print(team_lead.salary())
print(team_lead.department())
print(team_lead.programming_language())

