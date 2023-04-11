from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService

class RobotsManagingApp:

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type, name):
        if service_type not in ["MainService", "SecondaryService"]:
            raise Exception("Invalid service type!")

        service = [s for s in self.services if s.name == name]

        if service:
            raise Exception(f"{name} already exists.")

        if service_type == "MainService":
            service = MainService(name)
        else:
            service = SecondaryService(name)

        self.services.append(service)
        return f"{service_type} is successfully added."


    def add_robot(self,robot_type, name, kind, price):

        if robot_type not in ["MaleRobot", "FemaleRobot"]:
            raise Exception("Invalid robot type!")

        if robot_type == "MaleRobot":
            robot = MaleRobot(name, kind, price)

            self.robots.append(robot)
        elif robot_type == "FemaleRobot":
            robot = FemaleRobot(name, kind, price)

            self.robots.append(robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name, service_name):
        robot = next((r for r in self.robots if r.name == robot_name), None)
        service = next((s for s in self.services if s.name == service_name), None)

        if (isinstance(robot, MaleRobot) and not isinstance(service, MainService)) or \
            (isinstance(robot, FemaleRobot) and not isinstance(service, SecondaryService)):
            return "Unsuitable service."

        if service.capacity <= len(service.robots):
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."


    def remove_robot_from_service(self, robot_name, service_name):

        service = next((s for s in self.services if s.name == service_name), None)
        robot = next((r for r in service.robots if r.name == robot_name), None)

        if robot is None:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."


    def feed_all_robots_from_service(self, service_name):

        service = next((s for s in self.services if s.name == service_name), None)
        robots_fed = 0

        for robot in service.robots:
            robot.eating()
            robots_fed += 1

        return f"Robots fed: {robots_fed}."

    def service_price(self,service_name):
        service = next((s for s in self.services if s.name == service_name), None)

        total_price = sum(r.price for r in service.robots)

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):

        result = []

        for s in self.services:
            result.append(s.details())

        return '\n'.join(result)

