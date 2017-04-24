from models import Base, engine
from controllers import insert_skill, insert_team, insert_mentor
from _requests import skills, teams, mentors


def insert_all_skills(skills):
    for item in skills.json():
        insert_skill(item['name'])


def insert_all_teams(teams):
    for item in teams.json():
        insert_team(item['name'], item['idea_description'], item['repository'],
                    item['need_more_members'], item['members_needed_desc'],
                    item['room'], item['technologies_full'])


def insert_all_mentors(mentors):
    for item in mentors.json():
        insert_mentor(item['name'], item['description'],
                      item['picture'], item['teams'])


def main():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    insert_all_skills(skills)
    insert_all_teams(teams)
    insert_all_mentors(mentors)


if __name__ == '__main__':
    main()
