import datetime

import faker

from domain.entities.actions import ActionAt, ActionType


class UserFactory:
    def __init__(self, user_role):
        self.user_role = user_role
        self.fake = faker.Faker()

    def dump(self):
        return {
            "id": self.fake.pyint(),
            "username": self.fake.user_name(),
            "role": self.user_role,
            "created_at": datetime.datetime.now(),
            "updated_at": datetime.datetime.now(),
        }


class ActionFactory:
    def __init__(self):
        self.fake = faker.Faker()

    def dump_create(self):
        return {
            "action_at": self.action_at.value,
            "action_type": self.action_type.value,
            "name": self.name,
        }

    def dump(self):
        return {
            "action_at": self.action_at.value,
            "action_type": self.action_type.value,
            "name": self.name,
            "id": self.id,
            "user_id": self.user_id,
            "created_at": self.created_at,
        }

    @property
    def id(self):
        return self.fake.name()

    @property
    def user_id(self):
        return self.fake.pyint()

    @property
    def name(self):
        return self.fake.user_name()

    @property
    def action_at(self):
        return ActionAt.sheet

    @property
    def action_type(self):
        return ActionType.done

    @property
    def created_at(self):
        return int(datetime.datetime.utcnow().timestamp())
