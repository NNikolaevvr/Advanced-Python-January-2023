class Player:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills.keys():
            return f'Skill already added'
        else:

            self.skills[skill_name] = mana_cost
            return f'Skill {skill_name} added to the collection of the player {self.name}'


    def player_info(self):
        dict = '\n'.join([f"==={skill} - {mana}" for skill, mana in self.skills.items()])
        return f'Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n{dict}\n'
