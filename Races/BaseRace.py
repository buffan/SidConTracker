import abc
import Resources.Resources as Resources


class BaseRace(abc.ABC):
    resources = {Resources.Cylinder: 0,
                 Resources.Yellow: 0,
                 Resources.Black: 0,
                 Resources.Blue: 0,
                 Resources.Green: 0,
                 Resources.Brown: 0,
                 Resources.White: 0,
                 Resources.Ship: 0
                 }

    @property
    def temporary_converters(self):
        return []

    @property
    @abc.abstractmethod
    def converters(self):
        raise NotImplementedError

    @property
    def colonies(self):
        return []

    @property
    def research_teams(self):
        return []

    def add_resources(self, resources):
        for resource_type, amount in resources.items():
            self.resources[resource_type] += amount

    def check_nonnegative_resources(self):
        negative_resources = filter(lambda r: self.resources[r] < 0, self.resources)
        print("ERROR: Negative resources in inventory:\n{}".format('\n'.join(
            '{}: {}'.format(resource, self.resources[resource]) for resource in negative_resources)))
