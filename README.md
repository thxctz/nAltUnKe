class RafnixG:

    def __init__(self):
        self.username = 'rafnixg'
        self.name = 'Rafnix Guzmán'
        self.web = 'https://rafnixg.dev'
        self.twitter = '@rafnixg'
        self.code = {
            'frontend': ['HTML', 'CSS', 'JavaScript', 'ReactJS', 'Svelte', 'Boostrap', 'TailWind'],
            'backend': ['Python', 'PHP', 'Flask', 'Django', 'Laravel', 'NodeJS', 'Odoo'],
            'database': ['PostgreSQL', 'MySQL', 'SQLite3', 'Mongo DB'],
            'devops': ['Docker', 'Nginx', 'Jenkins', 'GitHub Actions', 'AWS', 'Heroku'],
            'tools': ['GIT', 'GitHub', 'GitLab', 'Pandas', 'Jupyter notebook', 'SQLAlchemy', 'Redis', 'Celery'],
            'misc': ['Firebase', 'TDD', 'SCRUM', 'SOLID', 'GNU/Linux']
        }
        self.architecture = ['SPA', 'MVC', 'Serverless', 'microservices']

    def __str__(self):
        return self.name


if __name__ == '__main__':
    me = RafnixG()

